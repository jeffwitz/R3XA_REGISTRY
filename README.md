# R3XA_REGISTRY

Canonical, shareable registry of reusable R3XA building blocks (settings, data_sources, data_sets).  
The goal is to version reference JSON fragments that can be reused across experiments and validated against the official R3XA schema.

## State
- Structure + guidelines drafted
- CI: validation workflow ready (.github/workflows/validate.yml)
- Needs initial items (see “Next steps”)

## Scope
- **Settings**: specimens, machines, environments, software configs.
- **Data sources**: cameras, sensors, load frames, acquisition pipelines.
- **Data sets**: raw / processed outputs linked to sources.

## Repository layout (proposed)
```
registry/
  imaging/
    data_sources/
      camera/
    data_sets/
      dic/
  mechanical_testing/
    settings/
      specimen/
    machines/
  processes/
  conventions/
scripts/
  validate_all.py
```

## Naming & IDs
- Filenames: lowercase, words separated by `_`.
- Inside each JSON, include a stable `id` (24 lowercase letters) and a concise `title`/`description`.
- Keep metadata self-contained; avoid absolute paths. Use relative placeholders when paths are needed.

## Validation (with `r3xa-api`)
```bash
pip install r3xa-api
python - <<'PY'
from r3xa_api.registry import validate_item, load_item
item = load_item("registry/data_sources/camera/avt_dolphin_f145b.json")
validate_item(item)  # raises if invalid
print("ok")
PY
```

## Contribution checklist
- [ ] JSON is valid and minimal (no GUI deps, no binaries).
- [ ] `id` unique within the registry.
- [ ] Describes units and dimensions where applicable.
- [ ] `validate_item` passes against the bundled schema.
- [ ] Document provenance (manufacturer, source, link) in `description` or extra fields.

## Next steps
1. Populate initial items (camera AVT, specimen openhole, dataset DIC).
2. Refine domains if needed (imaging / mechanical_testing / processes / conventions).
3. Tag v0.1 once a minimal validated set is ready.

## License
GPL-2.0-or-later (aligns with R3XA_API). If a different license is desired for registry data, specify before publishing.
