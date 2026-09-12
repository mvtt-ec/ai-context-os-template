#!/usr/bin/env python3
import re
from pathlib import Path
from context_lib import parse_frontmatter,context_records,REQUIRED
ROOT=Path(__file__).resolve().parents[1]
P=[("OpenAI key",re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),("GitHub token",re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b")),("AWS key",re.compile(r"\bAKIA[0-9A-Z]{16}\b")),("private key",re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"))]
def main():
    e=[]
    for p in ROOT.rglob("*"):
        if not p.is_file() or ".git" in p.parts or "__pycache__" in p.parts: continue
        try:t=p.read_text(encoding="utf-8")
        except:continue
        for label,rx in P:
            if rx.search(t):e.append(f"{p.relative_to(ROOT)}: possible {label}")
    for p in context_records(ROOT):
        m,_=parse_frontmatter(p); missing=REQUIRED-set(m)
        if missing:e.append(f"{p.relative_to(ROOT)}: missing {sorted(missing)}");continue
        if m["sensitivity"]=="restricted" and m["share"]:e.append(f"{p.relative_to(ROOT)}: restricted record must have empty share")
    if e:
        print("VALIDATION FAILED"); [print("ERROR:",x) for x in e]; return 1
    print("VALIDATION PASSED"); print("Context records checked:",sum(1 for _ in context_records(ROOT))); return 0
if __name__=="__main__": raise SystemExit(main())
