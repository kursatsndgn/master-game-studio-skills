# Claude Long-Term Memory System (`memory-system.md`)
# Integration: claude-mem & Cross-Session Context Engine

## 1. Overview
The Master Game Studio framework maintains cross-session memory across complex multi-chat feature pipelines. When developers and sub-agents switch contexts (e.g. from 3D modeling in Blender to writing GDScript in Godot), the memory system prevents hallucinations, preserves established lore, and tracks active stage-gate states.

---

## 2. Memory Schema

```json
{
  "project_metadata": {
    "title": "Project Codename",
    "genre": "Action RPG / Immersive Sim",
    "engine": "Godot 4.3 .NET / Unity 6",
    "target_platform": "PC / Steam Deck"
  },
  "established_lore": {
    "world_name": "string",
    "immutable_canon": [
      "Rule 1: Magic requires physical thermodynamic cost.",
      "Rule 2: The Sun-Shatter event occurred 300 years ago."
    ],
    "conlang_roots": {
      "khor": "stone / fortress",
      "vel": "flow / liquid light"
    }
  },
  "active_features": {
    "F00": {"name": "Vertical Slice Core Loop", "status": "COMPLETED"},
    "F01": {"name": "Procedural Dungeon Generator", "status": "IN_PROGRESS", "owner": "@engine-developer"},
    "F02": {"name": "Hero Character Rig & Textures", "status": "PENDING_GATE_QL", "owner": "@3d-artist"}
  },
  "director_gates": {
    "cd-narrative": "PASSED",
    "ql-story-ready": "IN_REVIEW"
  }
}
```

---

## 3. Session Compaction & Handoff Protocol

1. **Episodic Summary Generation:**
   At the conclusion of each feature chat, the active sub-agent produces a 3-bullet summary:
   - What was built and verified.
   - What decisions were committed to `[Established]` lore.
   - What blockers or next steps are handed off to the next sub-agent.

2. **Compaction Strategy:**
   - Raw dialogue drafts are compressed into accepted script lines (<= 120 chars) and stored in `skills/02-narrative-&-world/`.
   - Blender asset metadata (vertex count, material names, bone hierarchies) are committed to `skills/04-blender-3d-artist/3d-pipeline.md`.

3. **Restoration Hook:**
   When opening a new chat window, prefix your message with:
   > `@studio-director: Load memory-system.md and report active feature state.`
