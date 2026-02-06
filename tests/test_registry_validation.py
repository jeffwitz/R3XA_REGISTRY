import json
from pathlib import Path

import pytest

from r3xa_api.registry import load_item, validate_item


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_DIR = ROOT / "registry"


def iter_json_files():
    return sorted(REGISTRY_DIR.rglob("*.json"))


@pytest.mark.parametrize("path", iter_json_files())
def test_registry_item_is_valid(path: Path):
    item = load_item(path)
    validate_item(item)

