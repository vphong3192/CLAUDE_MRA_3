"""Shared loader for the harness test-suite.

Zero dependencies (stdlib only), no network, no LLM — the same constraints the
scripts under test obey. Each script lives beside its own skill rather than in a
package, so it is loaded by explicit path instead of by import name; that keeps
the tests runnable from any working directory.
"""
import pathlib
import sys
import types

# Never let a stale .pyc stand in for the source. A cached bytecode file from an earlier
# run once served default=0.1 while the source on disk said 0.4, so the suite was green
# against code that was not the code under test — a rigged inspection (R5). Everything
# below compiles from the source text on every run; nothing is written to __pycache__.
sys.dont_write_bytecode = True

REPO = pathlib.Path(__file__).resolve().parents[2]
CLAUDE = REPO / ".claude"
SKILLS = CLAUDE / "skills"
AGENTS = CLAUDE / "agents"


def load(relpath, name=None):
    """Compile a script under .claude/skills/ from source and return it as a module.

    Deliberately does NOT use importlib's file loader: that path consults __pycache__,
    and a stale .pyc can make the suite test something other than what is on disk.
    """
    path = SKILLS / relpath
    if not path.exists():                       # a moved script must fail loudly
        raise FileNotFoundError(path)
    name = name or f"harness_{path.stem}"
    mod = types.ModuleType(name)
    mod.__file__ = str(path)
    sys.modules[name] = mod
    exec(compile(path.read_text(encoding="utf-8"), str(path), "exec"), mod.__dict__)
    return mod


def categories(findings):
    """Findings are (line, category, detail) triples — pull out the category set."""
    return {cat for _, cat, _ in findings}
