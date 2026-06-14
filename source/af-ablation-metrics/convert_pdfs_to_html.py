"""Convert PDF to AI-readable HTML: text as HTML text, charts/figures/tables
as embedded images. Uses PyMuPDF to extract the page layout (text blocks +
image blocks) and reconstruct in correct reading order."""

import fitz  # PyMuPDF
from pathlib import Path
import base64
import re

DPI = 200  # DPI for rendered images (charts, figures, tables)


def extract_image_block(pdf_doc, page, block, page_idx):
    """Extract an image embedded in the PDF and return base64 data URI."""
    try:
        # PyMuPDF image block has "image" key with the xref
        # First try direct extraction via xref
        xref = block.get("xref", None) if isinstance(block, dict) else None
        if xref is None and hasattr(block, "xref"):
            xref = block.xref

        if xref and xref > 0:
            # Extract image using xref
            img_info = pdf_doc.extract_image(xref)
            if img_info:
                img_bytes = img_info["image"]
                ext = img_info.get("ext", "png")
                mime = f"image/{ext}" if ext != "jpg" else "image/jpeg"
                if ext == "jpg":
                    mime = "image/jpeg"
                b64 = base64.b64encode(img_bytes).decode("ascii")
                return f"data:{mime};base64,{b64}"
    except Exception:
        pass

    # Fallback: render the image region as a pixmap
    try:
        bbox = block.get("bbox", None) if isinstance(block, dict) else getattr(block, "bbox", None)
        if bbox:
            clip = fitz.Rect(*bbox)
            mat = fitz.Matrix(DPI / 72, DPI / 72)
            pix = page.get_pixmap(clip=clip, matrix=mat, colorspace=fitz.csRGB)
            img_bytes = pix.tobytes("png")
            b64 = base64.b64encode(img_bytes).decode("ascii")
            return f"data:image/png;base64,{b64}"
    except Exception:
        pass

    return None


def render_region_as_image(page, bbox):
    """Render a specific region (e.g., table area) as a PNG image."""
    try:
        clip = fitz.Rect(*bbox)
        mat = fitz.Matrix(DPI / 72, DPI / 72)
        pix = page.get_pixmap(clip=clip, matrix=mat, colorspace=fitz.csRGB)
        img_bytes = pix.tobytes("png")
        b64 = base64.b64encode(img_bytes).decode("ascii")
        return f"data:image/png;base64,{b64}"
    except Exception:
        return None


def is_table_area(page, bbox):
    """Heuristic: detect if a block region likely contains a table.
    Checks for structured text layout with multiple columns/rows."""
    clip = fitz.Rect(*bbox)
    blocks = page.get_text("dict", clip=clip)["blocks"]
    text_blocks = [b for b in blocks if b["type"] == 0]
    if len(text_blocks) == 0:
        return False

    # If many small text blocks aligned in a grid pattern → likely a table
    if len(text_blocks) >= 3:
        # Count distinct x-positions (columns)
        x_positions = set()
        y_positions = set()
        for tb in text_blocks:
            b = tb["bbox"]
            x_positions.add(round(b[0], 1))
            y_positions.add(round(b[1], 1))
        # Table has multiple columns and rows
        if len(x_positions) >= 2 and len(y_positions) >= 2:
            return True

    return False


def sanitize_text(text):
    """Escape HTML entities and normalize whitespace."""
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = text.replace("\"", "&quot;")
    return text


def build_text_html(spans):
    """Build HTML string from a list of text spans, preserving bold/italic."""
    parts = []
    for span in spans:
        text = sanitize_text(span["text"])
        if not text.strip():
            parts.append(text)
            continue

        flags = span.get("flags", 0)
        font = span.get("font", "")
        size = span.get("size", 0)

        is_bold = bool(flags & 2) or "bold" in font.lower() or "heavy" in font.lower()
        is_italic = bool(flags & 1) or "italic" in font.lower() or "oblique" in font.lower()

        # Check for superscript/subscript via small font size relative to baseline
        # We'll skip this for simplicity; main focus is bold/italic

        if is_bold and is_italic:
            parts.append(f"<b><i>{text}</i></b>")
        elif is_bold:
            parts.append(f"<b>{text}</b>")
        elif is_italic:
            parts.append(f"<i>{text}</i>")
        else:
            parts.append(text)

    return "".join(parts)


def compute_average_font_size(page):
    """Compute the average body text font size from a page."""
    blocks = page.get_text("dict")["blocks"]
    sizes = []
    for b in blocks:
        if b["type"] == 0:
            for line in b.get("lines", []):
                for span in line.get("spans", []):
                    if span["text"].strip():
                        sizes.append(span["size"])
    if not sizes:
        return 10
    # Return the mode (most common font size)
    from collections import Counter
    count = Counter(round(s, 1) for s in sizes)
    return count.most_common(1)[0][0]


def pdf_to_html(pdf_path: Path) -> Path:
    out_path = pdf_path.with_suffix(".html")
    pdf_name = pdf_path.stem
    doc = fitz.open(str(pdf_path))
    total_pages = len(doc)

    html_parts = [
        "<!DOCTYPE html>",
        '<html lang="en">',
        "<head>",
        '<meta charset="utf-8">',
        f"<title>{pdf_name}</title>",
        "<style>",
        "  :root { color-scheme: light dark; }",
        "  body { font-family: Georgia, 'Times New Roman', Times, serif;",
        "         max-width: 850px; margin: 0 auto; padding: 20px 32px;",
        "         background: #fff; color: #1a1a1a; line-height: 1.6;",
        "         font-size: 17px; }",
        "  @media (prefers-color-scheme: dark) {",
        "    body { background: #1a1a1a; color: #e0e0e0; }",
        "  }",
        "  .page-break { border-top: 1px dashed #ccc; margin: 28px 0 8px;",
        "                position: relative; }",
        "  .page-label { font-size: 11px; color: #999; text-align: right;",
        "                margin: 2px 0 20px; }",
        "  .image-block { text-align: center; margin: 16px 0; }",
        "  .image-block img { max-width: 100%; height: auto; border: 1px solid #eee; }",
        "  .image-caption { font-size: 13px; color: #666; margin-top: 4px; }",
        "  .table-region { text-align: center; margin: 16px 0; }",
        "  .table-region img { max-width: 100%; height: auto; border: 1px solid #eee; }",
        "  .table-region .caption { font-size: 13px; color: #666; margin-top: 4px; }",
        "  h1, h2, h3 { margin-top: 24px; }",
        "  hr { border: 0; border-top: 1px solid #ddd; margin: 24px 0; }",
        "  /* Navigation toolbar */",
        "  #toolbar { position: sticky; top: 0; z-index: 100; background: #f5f5f5;",
        "             padding: 8px 16px; display: flex; align-items: center; gap: 12px;",
        "             border-bottom: 1px solid #ddd; font-size: 14px; }",
        "  @media (prefers-color-scheme: dark) {",
        "    #toolbar { background: #2a2a2a; border-color: #444; }",
        "  }",
        "  #toolbar span.title { font-weight: bold; margin-right: auto; }",
        "  #toolbar button, #toolbar input { padding: 4px 10px; border-radius: 4px;",
        "             border: 1px solid #ccc; background: #fff; cursor: pointer; font-size: 13px; }",
        "  @media (prefers-color-scheme: dark) {",
        "    #toolbar button, #toolbar input { background: #444; color: #eee; border-color: #555; }",
        "  }",
        "  #toolbar input { width: 48px; text-align: center; }",
        "</style>",
        "</head>",
        "<body>",
        f"<div id='toolbar'>",
        f"  <span class='title'>{pdf_name}</span>",
        "  <button onclick='prevPage()'>&larr; Prev</button>",
        f"  <input type='number' id='pageInput' value='1' min='1' max='{total_pages}' onchange='goToPage()'>",
        f"  <span>/ {total_pages}</span>",
        "  <button onclick='nextPage()'>Next &rarr;</button>",
        "  <button onclick='scrollToTop()'>Top</button>",
        "</div>",
    ]

    for page_idx in range(total_pages):
        page = doc[page_idx]
        page_num = page_idx + 1
        avg_font_size = compute_average_font_size(page)

        html_parts.append(f'<div class="page-break" id="page{page_num}"></div>')
        html_parts.append(f'<div class="page-label">Page {page_num} / {total_pages}</div>')

        # Get page content as dict (blocks: text + images)
        page_dict = page.get_text("dict")

        for block in page_dict["blocks"]:
            block_type = block["type"]

            if block_type == 1:  # Image block
                bbox = block["bbox"]
                # Check if it's a table area
                if is_table_area(page, bbox):
                    img_data = render_region_as_image(page, bbox)
                    if img_data:
                        html_parts.append(
                            f'<div class="table-region">'
                            f'<img src="{img_data}" alt="Table/Chart on page {page_num}" loading="lazy">'
                            f'</div>'
                        )
                else:
                    # Extract embedded image
                    img_data = extract_image_block(doc, page, block, page_idx)
                    if img_data:
                        html_parts.append(
                            f'<div class="image-block">'
                            f'<img src="{img_data}" alt="Figure on page {page_num}" loading="lazy">'
                            f'</div>'
                        )

            elif block_type == 0:  # Text block
                bbox = block["bbox"]
                # Check if this text block is in a table region
                if is_table_area(page, bbox):
                    # Render text-heavy table region as image for accuracy
                    img_data = render_region_as_image(page, bbox)
                    if img_data:
                        html_parts.append(
                            f'<div class="table-region">'
                            f'<img src="{img_data}" alt="Table on page {page_num}" loading="lazy">'
                            f'</div>'
                        )
                    continue

                lines = block.get("lines", [])
                if not lines:
                    continue

                # Determine if this block looks like a heading
                first_span = lines[0]["spans"][0] if lines and lines[0].get("spans") else None
                font_size = first_span["size"] if first_span else avg_font_size
                is_bold = False
                if first_span:
                    flags = first_span.get("flags", 0)
                    font = first_span.get("font", "")
                    is_bold = bool(flags & 2) or "bold" in font.lower() or "heavy" in font.lower()

                # Heuristic heading detection
                tag = "p"
                if font_size >= avg_font_size * 1.8 and is_bold:
                    tag = "h1"
                elif font_size >= avg_font_size * 1.4 and is_bold:
                    tag = "h2"
                elif font_size >= avg_font_size * 1.2 and is_bold:
                    tag = "h3"

                # Build paragraph content
                para_parts = []
                for line in lines:
                    line_text = build_text_html(line["spans"])
                    para_parts.append(line_text)

                para_html = "\n".join(para_parts)

                if tag == "p":
                    html_parts.append(f"<p>{para_html}</p>")
                else:
                    html_parts.append(f"<{tag}>{para_html}</{tag}>")

    # JavaScript navigation
    html_parts.append("<script>")
    html_parts.append("const TOTAL = " + str(total_pages) + ";")
    html_parts.append("function goToPage() {")
    html_parts.append("  let n = parseInt(document.getElementById('pageInput').value);")
    html_parts.append("  if (isNaN(n) || n<1) n=1; if (n>TOTAL) n=TOTAL;")
    html_parts.append("  document.getElementById('pageInput').value = n;")
    html_parts.append("  const el = document.getElementById('page' + n);")
    html_parts.append("  if (el) el.scrollIntoView({behavior:'smooth',block:'start'});")
    html_parts.append("}")
    html_parts.append("function nextPage() {")
    html_parts.append("  let n = parseInt(document.getElementById('pageInput').value);")
    html_parts.append("  if (n < TOTAL) {")
    html_parts.append("    document.getElementById('pageInput').value = n+1; goToPage();")
    html_parts.append("  }")
    html_parts.append("}")
    html_parts.append("function prevPage() {")
    html_parts.append("  let n = parseInt(document.getElementById('pageInput').value);")
    html_parts.append("  if (n > 1) {")
    html_parts.append("    document.getElementById('pageInput').value = n-1; goToPage();")
    html_parts.append("  }")
    html_parts.append("}")
    html_parts.append("function scrollToTop() { window.scrollTo({top:0,behavior:'smooth'}); }")
    html_parts.append("document.addEventListener('keydown',function(e){")
    html_parts.append("  if (e.key==='ArrowRight'||e.key==='PageDown') nextPage();")
    html_parts.append("  if (e.key==='ArrowLeft'||e.key==='PageUp') prevPage();")
    html_parts.append("});")
    html_parts.append("</script>")
    html_parts.append("</body></html>")

    out_path.write_text("\n".join(html_parts), encoding="utf-8")
    doc.close()
    return out_path


def main():
    here = Path(__file__).parent
    pdf_files = sorted(here.glob("*.pdf"))
    if not pdf_files:
        print("No PDF files found.")
        return

    print(f"Converting {len(pdf_files)} PDF(s) to AI-readable HTML (text as text, figures as images)...\n")
    for pdf in pdf_files:
        print(f"  {pdf.name} -> {pdf.stem}.html ...", end=" ", flush=True)
        try:
            out = pdf_to_html(pdf)
            size_mb = out.stat().st_size / (1024 * 1024)
            print(f"OK ({size_mb:.1f} MB)")
        except Exception as e:
            import traceback
            print(f"FAILED: {e}")
            traceback.print_exc()

    print("\nDone.")

if __name__ == "__main__":
    main()
