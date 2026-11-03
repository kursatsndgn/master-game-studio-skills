# Contributing to Master Game Studio Skills

Thank you for contributing to the Master Game Studio Skills framework! We follow strict engineering, narrative, and artistic standards derived from `pamirtuna/gamestudio-subagents` and `Claude-Code-Game-Studios`.

## Production Principles

1. **Dialogue Ceiling (120 Characters):**
   - Any in-game dialogue line or script must strictly be 120 characters or fewer.
   - Use subtext and sensory-grounded actions rather than exposition dumps.

2. **Lore Tiers:**
   - Every piece of world lore must specify its tier:
     - `[Established]`: Canon, immutable.
     - `[Provisional]`: Working draft, pending director validation.
     - `[Under Review]`: Flagged for contradiction or mechanical friction.

3. **No AI Slop:**
   - Avoid generic, bloated placeholder prose (e.g., "The ancient realm was filled with boundless mystery...").
   - Define exact gameplay formulas, physics metrics, engine hooks, and tactile art specifications.

4. **i-have-adhd Slicing:**
   - Decompose tasks into 3–7 minute atomic micro-steps with clear binary success definitions.

5. **Sub-Agent Boundaries:**
   - Keep roles cleanly separated: `@3d-artist` produces Blender assets and shaders, `@engine-developer` implements gameplay loops, `@game-writer` writes narrative graphs, and `@qa-auditor` reviews and enforces gates.

## Validation Before Commit
Run the built-in validator before submitting pull requests:
```bash
python tools/validate_studio.py
```
