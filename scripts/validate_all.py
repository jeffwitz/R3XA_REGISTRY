import json
import sys
from pathlib import Path

from r3xa_api.registry import validate_item, load_item


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_DIR = ROOT / "registry"


def iter_json_files(root: Path):
    for path in root.rglob("*.json"):
        yield path


def main() -> int:
    errors = []
    for path in iter_json_files(REGISTRY_DIR):
        try:
            item = load_item(path)
            validate_item(item)
        except Exception as exc:  # noqa: BLE001
            errors.append((path, exc))

    if errors:
        print("Validation failed for:")
        for path, exc in errors:
            print(f" - {path}: {exc}")
        return 1

    print("All registry items valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
