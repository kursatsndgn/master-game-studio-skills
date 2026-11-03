# `rea` - Autonomous Studio Automation & Workspace Companion

`rea` is an autonomous local task runner and workspace automation helper for the Master Game Studio framework.

## Capabilities

1. **Workspace Health & Linting (`rea validate`):**
   - Scans narrative markdown files for dialogue lines exceeding the 120-character limit.
   - Audits Lore tier declarations (`[Established]`, `[Provisional]`, `[Under Review]`).
   - Verifies Blender Python scripts for headless execution compatibility.
   - Validates director quality gate checklists.

2. **Micro-Task Slicer (`rea slice <feature>`):**
   - Implements the `i-have-adhd` task decomposition model.
   - Automatically slices features into 3–5 minute executable chunks with binary done criteria.

3. **Gate Checking (`rea gate-check <gate_name>`):**
   - Evaluates prerequisites for `cd-narrative` and `ql-story-ready`.

## Quickstart

```bash
# Validate entire repository against studio standards
python global-tools/rea/rea_orchestrator.py validate

# Slice a feature into micro-tasks
python global-tools/rea/rea_orchestrator.py slice "Inventory System"

# Run a gate check
python global-tools/rea/rea_orchestrator.py gate-check cd-narrative
```
