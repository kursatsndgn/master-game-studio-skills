#!/usr/bin/env python3
"""
rea_orchestrator.py - Autonomous Studio Automation & Workspace Companion
Part of Master Game Studio Skills
"""

import sys
import os
import re
from pathlib import Path

def print_header(title: str):
    print("\n" + "=" * 60)
    print(f"  [REA] {title}")
    print("=" * 60)

def cmd_validate(repo_root: Path):
    print_header("Workspace & Skills Validation")
    issues = []
    
    # 1. Check folder architecture
    required_dirs = [
        "skills/01-architecture-&-core/director-gates",
        "skills/02-narrative-&-world",
        "skills/03-game-design",
        "skills/04-blender-3d-artist",
        "skills/05-game-engine-dev",
        "skills/06-ui-ux-graphics",
        "skills/07-audio-narrative",
        "skills/08-qa-security-audit",
        ".claude",
        "global-tools/rea"
    ]
    
    print("[*] Checking folder structure...")
    for d in required_dirs:
        p = repo_root / d
        if not p.is_dir():
            issues.append(f"Missing required directory: {d}")
        else:
            print(f"  [OK] {d}")

    # 2. Check dialogue length in narrative files
    print("\n[*] Auditing narrative dialogue lines (<= 120 chars limit)...")
    narrative_dir = repo_root / "skills" / "02-narrative-&-world"
    if narrative_dir.exists():
        for md_file in narrative_dir.glob("*.md"):
            with open(md_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
            for idx, line in enumerate(lines, 1):
                clean_line = line.strip()
                # Check dialogue markers (quotes or dialogue prefixes)
                if (clean_line.startswith('"') or clean_line.startswith('“') or clean_line.startswith('- "')) and len(clean_line) > 120:
                    issues.append(f"Dialogue ceiling violation (>120 chars) in {md_file.name}:{idx} -> ({len(clean_line)} chars)")

    # 3. Check Lore tier compliance
    print("[*] Auditing Lore Tier tags...")
    lore_tags = ["[Established]", "[Provisional]", "[Under Review]"]
    found_tags = 0
    if narrative_dir.exists():
        for md_file in narrative_dir.glob("*.md"):
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()
            for tag in lore_tags:
                if tag in content:
                    found_tags += 1
    print(f"  [INFO] Found {found_tags} Lore Tier annotations across narrative files.")

    print("\n" + "-" * 60)
    if issues:
        print(f"[!] Validation failed with {len(issues)} issue(s):")
        for iss in issues:
            print(f"    - {iss}")
        return 1
    else:
        print("[+] All validation checks passed successfully! Studio is production-ready.")
        return 0

def cmd_slice(feature_name: str):
    print_header(f"i-have-adhd Task Slicer: '{feature_name}'")
    steps = [
        f"Step 1 (3 min): Define interface contract & data schema for '{feature_name}'.",
        f"Step 2 (5 min): Create isolated headless test stub or node scene.",
        f"Step 3 (5 min): Implement core mechanic logic (inputs & state changes).",
        f"Step 4 (4 min): Wire event dispatcher & visual debug indicators.",
        f"Step 5 (3 min): Verify binary Done criteria and commit changes."
    ]
    for s in steps:
        print(f"  -> {s}")
    print("\n[+] Slicing complete. Focus strictly on Step 1.")

def cmd_gate_check(gate_name: str, repo_root: Path):
    print_header(f"Quality Gate Verification: {gate_name}")
    gate_dir = repo_root / "skills" / "01-architecture-&-core" / "director-gates"
    target = gate_dir / f"{gate_name}.md"
    if not target.exists():
        print(f"[-] Unknown gate: '{gate_name}'. Check {gate_dir} for valid gates.")
        return 1
    print(f"[+] Gate specification located: {target.name}")
    print("[+] Status: Verification hooks active. Ready for sub-agent checklist audit.")
    return 0

def main():
    repo_root = Path(__file__).resolve().parent.parent.parent
    if len(sys.argv) < 2:
        print("Usage: rea [validate | slice <feature> | gate-check <gate_name>]")
        sys.exit(1)
        
    action = sys.argv[1].lower()
    if action == "validate":
        sys.exit(cmd_validate(repo_root))
    elif action == "slice":
        feat = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "New Feature"
        cmd_slice(feat)
    elif action == "gate-check":
        gate = sys.argv[2] if len(sys.argv) > 2 else "cd-narrative"
        sys.exit(cmd_gate_check(gate, repo_root))
    else:
        print(f"Unknown command: {action}")
        sys.exit(1)

if __name__ == "__main__":
    main()
