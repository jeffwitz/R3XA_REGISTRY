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


@pytest.mark.parametrize("path", iter_json_files())
def test_registry_item_id_uses_kind_prefix(path: Path):
    item = load_item(path)
    section, kind_name = item["kind"].split("/", 1)
    prefix = {"settings": "stg", "data_sources": "src", "data_sets": "set"}[section]

    assert item["id"].startswith(f"{prefix}-{kind_name}-")


def test_registry_item_ids_and_titles_are_unique():
    seen_ids: dict[str, Path] = {}
    seen_titles: dict[str, Path] = {}

    for path in iter_json_files():
        item = load_item(path).to_dict()
        item_id = item["id"]
        title = item.get("title")
        assert item_id not in seen_ids, (
            f"duplicate registry id {item_id!r}: {path} and {seen_ids[item_id]}"
        )
        seen_ids[item_id] = path
        if title:
            assert title not in seen_titles, (
                f"duplicate registry title {title!r}: {path} and {seen_titles[title]}"
            )
            seen_titles[title] = path
