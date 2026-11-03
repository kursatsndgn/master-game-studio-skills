# Master Game Studio Skills

Autonomous, multi-agent game development framework powered by the **`pamirtuna/gamestudio-subagents`** backbone and **`Claude-Code-Game-Studios`** production discipline.

---

## 🏛️ Directory Architecture

```text
master-game-studio-skills/
├── README.md                      # Repo documentation, commands, and workflow guide
├── .cursorrules                   # Global AI agent rules (120-char dialogue cap, Lore tiers, etc.)
├── global-tools/
│   └── rea                        # Autonomous workflow & environment automation assistant
├── .claude/
│   └── memory-system.md           # Long-term context & memory management via claude-mem
└── skills/
    ├── 01-architecture-&-core/    # Orchestrator core & /brainstorm engine
    │   ├── studio-director.md     # Executive Producer & Task Routing (i-have-adhd slicing)
    │   └── director-gates/        # Quality & gate approvals (cd-narrative, ql-story-ready)
    ├── 02-narrative-&-world/      # Worldbuilding, interactive fiction & dialogue
    │   ├── narrative-rules.md     # Dialogue constraints, Lore tiers (Established, Provisional, Under Review)
    │   ├── interactive-fiction.md # Branching narrative analysis & graph validation
    │   ├── conlang-worldbuilding.md # Constructed languages (conlang), theology & settlement maps
    │   └── character-dialogue.md  # Voice arcs, subtext analyzer & naming engine
    ├── 03-game-design/            # Mechanics, combat, level design & economy
    │   └── design-core.md         # Balance rules, graphify progression & modly asset integration
    ├── 04-blender-3d-artist/      # 3D pipeline & procedural modeling
    │   └── 3d-pipeline.md         # Blender Python MCP, retopology, PBR & modular assembly
    ├── 05-game-engine-dev/        # Engine implementation (Godot 4, Unity)
    │   ├── vertical-slice.md      # 15-minute playable prototype pipeline
    │   └── procedural-dungeon.md  # watabou procedural dungeon & city map generation
    ├── 06-ui-ux-graphics/         # Interface design, HUD & 2D visuals
    │   └── hud-and-2d.md          # ui-ux-pro-max-skill, taste-skill & mcptoon comic art
    ├── 07-audio-narrative/        # Audio cloning & cinematic rendering
    │   └── multimedia-pipeline.md # OpenVoice speech cloning & Remotion React cutscenes
    └── 08-qa-security-audit/      # Quality assurance & security
        └── audit-pipeline.md      # Strix security audit, no-ai-slop filter & skillspector
```

---

## 🛠️ Sub-Agent & Skill Integration Matrix

| Sub-Agent | Specialized Repos / Skills | Primary Domain |
|---|---|---|
| **@studio-director** | `i-have-adhd`, Director Gates | Task decomposition, milestone approvals, cross-department handoffs |
| **@game-writer / @narrative-director** | `jwynia/agent-skills/creative` | Branching narrative, conlangs, 120-char dialogue rules, lore audits |
| **@game-designer** | `graphify`, `modly` | Combat loops, progression math, economy balancing |
| **@3d-artist** | `PoBruno/mcp-blender-agent`, `blender-skills` | Python headless Blender modeling, retopology, PBR shaders |
| **@engine-developer** | `watabou`, `modly`, Godot 4 / Unity | Core controller, 15-min vertical slice, procedural generation |
| **@art-director / @ui-ux** | `ui-ux-pro-max-skill`, `taste-skill`, `mcptoon` | HUD layout, typography, 2D art & comic-style illustrations |
| **@audio-narrative-engineer** | `openvoice`, `remotion` | Neural voice generation, programmatic video cutscenes |
| **@qa-auditor** | `strix`, `no-ai-slop`, `skillspector` | Security vulnerability auditing, AI slop removal, code quality |
| **Global Tools** | `rea`, `claude-mem` | Autonomous local agent assistance & persistent project memory |

---

## 💡 The `/brainstorm` Protocol

When kicking off a new game concept or vertical slice, invoke `/brainstorm` to initiate the structured pre-production engine:

1. **5 Socratic Exploration Dimensions:**
   - **Gameplay & Core Loop:** The 5-second tactile satisfaction loop and target core emotion.
   - **Art Direction & Vibe:** Visual style (Stylized 3D, Low-Poly, Pixel, Dark Gothic) and camera projection.
   - **Narrative Scope:** Environmental storytelling vs. deeply branching dialogue tree.
   - **Tech & Platform:** Engine (Godot 4 / Unity), target specs (PC, Mobile), procedural vs. hand-crafted balance.
   - **Market References & USP:** Fusion of 2 benchmark titles + 3 Unique Selling Propositions.

2. **Market Validation & Dynamic Feature Tree:**
   - Genre saturation and competitor analysis.
   - Flexible modular feature mapping (`F00: Core Loop`, `F01: Narrative & Conlang`, `F02: 3D Assets`, etc.) tailored to project scale.

3. **Multi-Chat Execution Blueprint:**
   - Dedicated chat plan assigning specific sub-agents, context files, and initial prompts to each feature.
