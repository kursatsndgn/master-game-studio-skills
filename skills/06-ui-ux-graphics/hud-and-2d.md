# UI/UX Graphics, HUD & 2D Art Pipeline (`hud-and-2d.md`)
# Integrations: ui-ux-pro-max-skill, taste-skill, awesome-design-md, mcptoon
# Sub-Agent Domain: @art-director / @ui-ux-designer

## 1. Design Philosophy & Taste System
In accordance with `taste-skill` and `ui-ux-pro-max-skill`, game user interfaces must avoid the generic flat blue sci-fi or bevelled brown fantasy tropes. Every UI element must possess:
- **Materiality:** Reflect the physical world lore (e.g. etched brass, oxidized copper, weathered vellum).
- **Radical Contrast:** Minimum WCAG AAA equivalent contrast for in-game HUD indicators against high-luminance game backgrounds.
- **Micro-Interactions:** 100ms haptic and visual confirmation on button presses, hover states, and focus rings.

---

## 2. HUD Architecture & Spatial Anchors

```text
+-------------------------------------------------------------+
| [Top-Left: Compass / Current Quest Tracker]                 |
| [Player Status: Health / Stamina - Minimalist Gauge]        |
|                                                             |
|                          (Crosshair / Focus)                |
|                                                             |
| [Subtitle Box: Centered Bottom, <= 120 chars, Dark Backing] |
| [Bottom-Left: Quick Slots]        [Bottom-Right: Ammo/Gear] |
+-------------------------------------------------------------+
```

---

## 3. Typography & Sizing Standards
- **Header Font:** Expressive, custom display serif or geometric sans matching universe conlang aesthetics.
- **Body & Subtitle Font:** Highly legible humanist sans-serif (e.g. Inter, Roboto Condensed) with a minimum point size of 18pt at 1080p resolution.
- **Letter Spacing:** `0.02em` on body; `0.08em` on uppercase headers.

---

## 4. `mcptoon` Comic & 2D Illustration Pipeline
For storyboards, dialogue portraits, and 2D animated cutscenes:
1. **Line Weight Hierarchy:** Bold 3px outer silhouette lines; fine 1px interior contour lines.
2. **Halftone Texturing:** Ben-Day dots or coarse line screening on shadow planes.
3. **Palette Restriction:** Strict 5-color palette per faction/zone to maintain immediate visual identity.
