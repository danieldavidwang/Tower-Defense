from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "generated" / "repo_metrics.json"
IGNORED_DIRS = {".git", ".venv", "venv", "__pycache__", "generated"}


def python_files():
    files = []

    for path in ROOT.rglob("*.py"):
        if any(part in IGNORED_DIRS for part in path.parts):
            continue
        files.append(path)

    return sorted(files)


def count_metrics(files):
    line_count = 0
    todo_count = 0

    for path in files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        line_count += len(text.splitlines())
        todo_count += text.count("TODO")
        todo_count += text.count("FIXME")

    return {
        "python_files": len(files),
        "python_lines": line_count,
        "todo_fixme_markers": todo_count,
    }


def main():
    files = python_files()
    metrics = count_metrics(files)

    OUTPUT.parent.mkdir(exist_ok=True)
    OUTPUT.write_text(
        json.dumps(metrics, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
