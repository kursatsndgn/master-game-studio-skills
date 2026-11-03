# Interactive Fiction & Branching Narrative Diagnostics (`interactive-fiction.md`)
# Integration: jwynia/agent-skills/creative & Branching Graph Engine

## 1. Overview
This skill governs the structural architecture of choice systems, branching dialogue trees, and systemic quest structures. It provides analytical diagnostics to identify fake agency, narrative bottlenecks, and dead-end orphan nodes.

---

## 2. Narrative Branching Typologies

```text
1. The Diamond (Branch & Merge):
   (Root Node) --> [Choice A / Choice B] --> (Shared Consequence Hub)
   - Good for: Cost-effective production, consistent story milestones.

2. The Stateful Tree (Memory-Weighted):
   (Root Node) --> Sets Variable {reputation_thieves += 1} --> Unlocks late-game shortcut.
   - Good for: Deep player agency without exponential branch explosion.

3. The Open Constellation:
   Hub node with non-linear objective nodes resolved in any order.
```

---

## 3. Branching Health Diagnostics (Automated Checks)

Every dialogue and quest graph must be evaluated against the following mathematical metrics:

| Metric | Target Range | Description |
|---|---|---|
| **Agency Ratio (AR)** | `>= 0.40` | Ratio of divergent player choices with distinct game outcomes vs cosmetic branches. |
| **Dead-End Index** | `0` | Any branch that ends without a state trigger, quest resolution, or clean return loop is illegal. |
| **Max Linear Run** | `<= 3 nodes` | Maximum sequential dialogue nodes without a player interaction or choice prompt. |

---

## 4. Standard Dialogue Node Schema (JSON / GDScript Compatible)

```json
{
  "node_id": "DLG_KHOR_04",
  "speaker": "Kaelen",
  "lore_tier": "[Established]",
  "dialogue_text": "The gate mechanism requires fresh oil. Don't touch the brass lever.",
  "character_count": 67,
  "conditions": [
    {"variable": "player_knows_oil_source", "equals": true}
  ],
  "choices": [
    {
      "choice_text": "Where is the reservoir?",
      "character_count": 25,
      "next_node": "DLG_KHOR_05A",
      "effects": [{"variable": "sought_guidance", "increment": 1}]
    },
    {
      "choice_text": "I will force it open.",
      "character_count": 21,
      "next_node": "DLG_KHOR_05B",
      "effects": [{"variable": "brass_lever_strained", "set": true}]
    }
  ]
}
```
