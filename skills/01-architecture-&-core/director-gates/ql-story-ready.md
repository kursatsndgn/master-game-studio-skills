# Quality Gate: Quest & Level Story Ready (`ql-story-ready.md`)
# Gate ID: GATE-02-QL-STORY-READY

## 1. Purpose
The `ql-story-ready` gate acts as the technical and design handover boundary between narrative writing and spatial/systems realization. A quest or level narrative CANNOT enter 3D modeling or engine scripting until this gate is cleared.

---

## 2. Hard Gate Requirements (Pass/Fail)

| Check ID | Requirement | Validation Method | Criteria |
|---|---|---|---|
| **QL-S01** | Branching Graph Integrity | Graph validation tool | Zero orphan nodes; all dialogue/quest branches terminate in valid state |
| **QL-S02** | Spatial Anchor Mapping | Level designer review | Every narrative beat has an identified geometric zone or trigger volume |
| **QL-S03** | Environmental Prop Manifest | 3D artist asset audit | Required environmental storytelling props itemized with mesh budgets |
| **QL-S04** | Pacing & Beat Budget | Combat & level design audit | Maximum traversal time between narrative beats does not exceed 90 seconds |
| **QL-S05** | Fallback & Fail-Safe State | Engine dev check | Failure states (player leaves area, NPC dies) defined and scripted |

---

## 3. Checklist for Sub-Agents (`@level-designer` / `@engine-developer` / `@3d-artist`)

- [ ] Quest state machine diagram attached (idle -> active -> objective_met -> resolved).
- [ ] List of interactive props mapped to modular asset IDs (`MOD_PROP_01`, etc.).
- [ ] NPC patrol routes, idle animation requirements, and voice trigger zones clearly marked in 3D coordinates.
- [ ] `cd-narrative` gate cleared prior to requesting `ql-story-ready` evaluation.

---

## 4. Gate Sign-Off Protocol
```markdown
### Gate Clearance Record
- **Date:** YYYY-MM-DD
- **Target Quest / Zone:** Z01: The Sunken Foundry
- **Auditors:** @level-designer & @engine-developer
- **Status:** [PASSED / REJECTED]
- **Handoff:** Ready for Blender kitbash assembly and Godot scene tree generation.
```
