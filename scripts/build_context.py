#!/usr/bin/env python3
import argparse,json
from pathlib import Path
from context_lib import parse_frontmatter,context_records
ROOT=Path(__file__).resolve().parents[1]
def allowed(meta,target,policy):
    s=meta.get("sensitivity")
    return s!="restricted" and target in meta.get("share",[]) and s in policy["targets"][target]["allow"]
def main():
    p=argparse.ArgumentParser(); p.add_argument("--target",required=True,choices=["chatgpt","claude","gemini","codex","local"]); a=p.parse_args()
    policy=json.loads((ROOT/"config/context-policy.json").read_text())
    parts=[]
    for n in ["00_MASTER_CONTEXT.md","01_ABOUT_ME.md","02_OPERATING_RULES.md","03_ACTIVE_INDEX.md"]:
        parts.append(f"\n\n<!-- SOURCE: {n} -->\n\n"+(ROOT/n).read_text().strip())
    count=0
    for path in sorted(context_records(ROOT)):
        meta,body=parse_frontmatter(path)
        if allowed(meta,a.target,policy):
            parts.append(f"\n\n<!-- SOURCE: {path.relative_to(ROOT)} -->\n\n"+body.strip()); count+=1
    out=ROOT/"generated"/a.target/"CONTEXT.md"; out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(f"# Generated Context Packet — {a.target}\n"+ "".join(parts)+"\n")
    print(f"Built {out.relative_to(ROOT)} with {count} records.")
if __name__=="__main__": main()
