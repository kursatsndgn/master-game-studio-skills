#!/usr/bin/env python3
"""
validate_studio.py
Comprehensive Repository & Skills Linter for Master Game Studio Skills
"""

import sys
import re
from pathlib import Path

def run_suite():
    repo_root = Path(__file__).resolve().parent.parent
    print("=" * 70)
    print("  MASTER GAME STUDIO SKILLS (ANTIGRAVITY BUILD) - REPO AUDITOR")
    print("=" * 70)

    errors = []
    warnings = []
    checked_files = 0

    # 1. Check all expected files
    expected_files = [
        "README.md",
        ".cursorrules",
        ".gitignore",
        "LICENSE",
        "CONTRIBUTING.md",
        ".claude/memory-system.md",
        "global-tools/rea/README.md",
        "global-tools/rea/rea_orchestrator.py",
        "skills/01-architecture-&-core/studio-director.md",
        "skills/01-architecture-&-core/director-gates/cd-narrative.md",
        "skills/01-architecture-&-core/director-gates/ql-story-ready.md",
        "skills/02-narrative-&-world/narrative-rules.md",
        "skills/02-narrative-&-world/interactive-fiction.md",
        "skills/02-narrative-&-world/conlang-worldbuilding.md",
        "skills/02-narrative-&-world/character-dialogue.md",
        "skills/03-game-design/design-core.md",
        "skills/04-blender-3d-artist/3d-pipeline.md",
        "skills/04-blender-3d-artist/scripts/blender_prop_generator.py",
        "skills/05-game-engine-dev/vertical-slice.md",
        "skills/05-game-engine-dev/procedural-dungeon.md",
        "skills/06-ui-ux-graphics/hud-and-2d.md",
        "skills/07-audio-narrative/multimedia-pipeline.md",
        "skills/08-qa-security-audit/audit-pipeline.md",
    ]

    print("[1/3] Verifying core file registry...")
    for rel_path in expected_files:
        p = repo_root / rel_path
        if not p.is_file():
            errors.append(f"Missing core file: {rel_path}")
        else:
            checked_files += 1

    print(f"  [OK] Verified {checked_files}/{len(expected_files)} files present.")

    # 2. Check 120-character dialogue rule in narrative skills
    print("\n[2/3] Auditing 120-character dialogue ceiling...")
    narrative_dir = repo_root / "skills" / "02-narrative-&-world"
    dialogue_quotes = 0
    if narrative_dir.exists():
        for md_file in narrative_dir.glob("*.md"):
            with open(md_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
            for idx, line in enumerate(lines, 1):
                stripped = line.strip()
                # Check for in-dialogue examples in quotes
                if stripped.startswith("> *\"") or stripped.startswith("> \"") or stripped.startswith('"'):
                    # Skip if preceding line or current line marked as Bad or Counter-example
                    prev_line = lines[idx - 2] if idx >= 2 else ""
                    if "Bad" in prev_line or "Bad" in stripped or "❌" in prev_line:
                        continue
                    m = re.findall(r'"([^"]*)"', stripped)
                    for q in m:
                        dialogue_quotes += 1
                        if len(q) > 120:
                            warnings.append(f"Potential dialogue length violation ({len(q)} chars) at {md_file.name}:{idx}")

    print(f"  [OK] Audited {dialogue_quotes} dialogue strings.")

    # 3. Check Lore tier compliance
    print("\n[3/3] Checking Lore Tier definitions and references...")
    cursorrules_path = repo_root / ".cursorrules"
    if cursorrules_path.exists():
        content = cursorrules_path.read_text(encoding="utf-8")
        for tag in ["[Established]", "[Provisional]", "[Under Review]"]:
            if tag not in content:
                errors.append(f".cursorrules missing lore tag: {tag}")
            else:
                print(f"  [OK] Found rule tag {tag}")

    print("\n" + "=" * 70)
    if warnings:
        print(f"[*] Warnings ({len(warnings)}):")
        for w in warnings:
            print(f"    - {w}")

    if errors:
        print(f"[!] Validation FAILED with {len(errors)} error(s):")
        for e in errors:
            print(f"    - {e}")
        return 1
    else:
        print(f"[+] SUCCESS: All {checked_files} files passed validation. Repo is GitHub-ready!")
        return 0

if __name__ == "__main__":
    sys.exit(run_suite())
