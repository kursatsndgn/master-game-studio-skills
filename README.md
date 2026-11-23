# Master Game Studio Skills

Autonomous, multi-agent game development framework powered by the **`pamirtuna/gamestudio-subagents`** backbone and **`Claude-Code-Game-Studios`** production discipline.

---

## 🏛️ Directory Architecture

```text
master-game-studio-skills/
├── README.md                      # Repo documentation, commands, and workflow guide
├── CODEX.md                       # OpenAI Codex & GitHub Copilot root instructions
├── AGENTS.md                      # Multi-agent coordination hierarchy & JSON contracts
├── mcp.json                       # Universal Model Context Protocol configuration
├── .cursor/                       # Cursor Editor configuration & MCP registry
│   └── mcp.json                   # Cursor native MCP connector bindings
├── .cursorrules                   # Global AI agent rules (120-char dialogue cap, Lore tiers, etc.)
├── mcp-connectors/                # Live Engine & DCC tool MCP bridges
│   ├── blender-mcp/               # Blender 4.x JSON-RPC stdio bridge (Port 9876)
│   ├── godot-mcp/                 # Godot 4 EditorPlugin TCP/WebSocket bridge (Port 9080)
│   ├── unity-mcp/                 # MCP for Unity: CoplayDev/unity-mcp submodule (stdio)
│   ├── unreal-mcp/                # Unreal Engine 5 Web Remote Control bridge (Port 30010)
│   └── qgis-mcp/                  # QGIS MCP: jjsantos01/qgis_mcp submodule (plugin port 9876)
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
    │   ├── 3d-pipeline.md         # Blender Python MCP, retopology, PBR & modular assembly
    │   └── qgis-terrain-pipeline.md # QGIS DEM elevation, 16-bit heightmaps & Blender-GIS
    ├── 05-game-engine-dev/        # Engine implementation (Godot 4, Unity)
    │   ├── vertical-slice.md      # 15-minute playable prototype pipeline
    │   └── procedural-dungeon.md  # watabou procedural dungeon & city map generation
    ├── 06-ui-ux-graphics/         # Interface design, HUD & 2D visuals
    │   └── hud-and-2d.md          # ui-ux-pro-max-skill, taste-skill & mcptoon comic art
    ├── 07-audio-narrative/        # Audio cloning & cinematic rendering
    │   └── multimedia-pipeline.md # OpenVoice speech cloning & Remotion React cutscenes
    ├── 08-qa-security-audit/      # Quality assurance & security
    │   └── audit-pipeline.md      # Strix security audit, no-ai-slop filter & skillspector
    └── 09-playtest-&-feedback/    # FINAL STEP: human-like playtest & feature handoff
        └── playtester.md          # Open-Godot-MCP deterministic play, playtest-lab bots/personas, fun/friction report
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
| **@playtester** | `Open-Godot-MCP`, `playtest-lab`, `claude-game-playtest-skills` | Final gate: plays the build like a human, finds fun & friction, hands fixes to features |
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

---

## 🛡️ Live Editor Transparency & Human Intervention (Golden Rule)

Every automated action and asset generation step performed by AI sub-agents must strictly uphold developer autonomy:

- **100% Hierarchy Visibility:** Every spawned object, mesh, light, trigger volume, or camera MUST be visible in the editor's hierarchy/outliner dock (Godot SceneTree, Unity Hierarchy, Blender Outliner, Unreal World Outliner). No ghost nodes or memory-only placeholders.
- **Explicit Owner Assignment (Godot 4):** All dynamically instantiated nodes must explicitly execute `node.owner = EditorInterface.get_edited_scene_root()` so they appear in the editor scene tree.
- **Direct Developer Intervention:** The developer can select, tweak properties, transform, or delete any generated node directly in the 2D/3D viewport and inspector dock at any time.
- **Physical Disk Persistence:** All assets are serialized to disk (`.tscn`, `.prefab`, `.gltf`, `.blend`, `.tres`) to ensure instant FileSystem inspection.
- **Native Undo/Redo Compliance:** Every engine modification registers with the editor undo system for full Ctrl+Z reversibility.

---

## 🎮 Final Step: Human-Like Playtest (`@playtester`)

The last stage of every feature cycle. After QA passes, `@playtester` plays the build from the start like a real player and
decides whether it is *fun*, not just whether it works.

1. **Deterministic play** via [Open-Godot-MCP](https://github.com/masteryee-labs/Open-Godot-MCP): freeze the clock, decide, step
   exact milliseconds with inputs, screenshot, verify state. Co-op tested with host/client instances, latency and sync checks.
2. **Bot sweep** via [playtest-lab](https://github.com/miandbits/playtest-lab): many seeds for crashes, softlocks, skill gradient, dominant strategy.
3. **Personas**: first-timer, speedrunner, explorer, rule-breaker, co-op.
4. **Measured signals**: dead time, inputs per task, input→feedback latency, missing feedback, repeated deaths, FPS.
5. **Report + work cards** (`playtest/YYYY-MM-DD-<section>.md`) routed to the owning feature (F00..Fn). Nothing is fixed
   or dispatched without the developer's approval; fixes are re-played to close each finding.
6. **Optional channel**: the developer's narrated recording reviewed with
   [claude-game-playtest-skills](https://github.com/jrejaud/claude-game-playtest-skills).

Setup:
```bash
git clone https://github.com/masteryee-labs/Open-Godot-MCP && cd Open-Godot-MCP && uv tool install .
claude mcp add -s user open-godot-mcp -- open-godot-mcp
git clone https://github.com/miandbits/playtest-lab ~/.claude/skills/playtest-lab
claude plugin marketplace add https://github.com/jrejaud/claude-game-playtest-skills
claude plugin install game-playtest-skills@game-playtest
```
Requires Godot 4.5+ (the addon goes in `addons/open_godot_mcp` and must be enabled in Project Settings → Plugins), Python 3.11+, uv, Node 20+.
