from pathlib import Path
REQUIRED={"id","type","status","sensitivity","share","updated"}
def parse_frontmatter(path:Path):
    text=path.read_text(encoding="utf-8")
    if not text.startswith("---\n"): return {},text
    end=text.find("\n---\n",4)
    if end==-1:return {},text
    raw,body=text[4:end],text[end+5:]
    data={}
    for line in raw.splitlines():
        if not line.strip() or ":" not in line: continue
        k,v=line.split(":",1); k,v=k.strip(),v.strip()
        data[k]=[x.strip() for x in v.split(",") if x.strip()] if k=="share" else v
    return data,body
def context_records(root:Path):
    for p in (root/"context").rglob("*.md"):
        if "_template" in p.parts or p.name=="README.md": continue
        yield p
