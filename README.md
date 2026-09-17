# R3XA_REGISTRY

Canonical, shareable registry of reusable R3XA building blocks (settings, data_sources, data_sets).  
The goal is to version reference JSON fragments that can be reused across experiments and validated against the official R3XA schema.

## State
- Five reusable reference items are currently maintained under `registry/`.
- GitLab CI validates every JSON item against the R3XA_API schema and runs the test suite.
- The current validation contract is R3XA_API `v2.0.0rc3` with schema `2026.9.18`.

## Scope
- **Settings**: specimens, machines, environments, software configs.
- **Data sources**: cameras, sensors, load frames, acquisition pipelines.
- **Data sets**: raw / processed outputs linked to sources.

## Repository layout
```
registry/
  imaging/
    data_sources/
      camera/
      generic/
    data_sets/
      list/
  mechanical_testing/
    settings/
      specimen/
    data_sets/
      file/
scripts/
  validate_all.py
```

## Naming & IDs
- Filenames: lowercase, words separated by `_`.
- Inside each JSON, include a stable semantic `id` with the appropriate family prefix (`stg-`, `src-`, or `set-`) and a concise `title`/`description`.
- Keep metadata self-contained; avoid absolute paths. Use relative placeholders when paths are needed.

## Validation (with `r3xa-api`)
```bash
python -m pip install "r3xa-api @ git+https://gitlab.com/photomechanics/R3XA_API.git@v2.0.0rc3"
python - <<'PY'
from r3xa_api.registry import validate_item, load_item
item = load_item("registry/imaging/data_sources/camera/avt_dolphin_f145b.json")
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
1. Expand the validated item catalogue across imaging and mechanical-testing use cases.
2. Refine domains and naming conventions as reusable items are contributed.
3. Define and publish the first Registry release once the collection and governance are stable.

## License
GPL-2.0-or-later (aligns with R3XA_API). If a different license is desired for registry data, specify before publishing.
