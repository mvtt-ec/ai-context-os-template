import json,tempfile,unittest,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/"scripts"))
from context_lib import parse_frontmatter
from build_context import allowed
class Tests(unittest.TestCase):
    def test_parse(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"x.md"; p.write_text("---\nid: x\ntype: project\nstatus: active\nsensitivity: internal\nshare: chatgpt,codex\nupdated: 2026-09-12\n---\n# X")
            m,b=parse_frontmatter(p); self.assertEqual(m["share"],["chatgpt","codex"])
    def test_policy(self):
        policy=json.loads((ROOT/"config/context-policy.json").read_text())
        self.assertFalse(allowed({"sensitivity":"restricted","share":["local"]},"local",policy))
        self.assertTrue(allowed({"sensitivity":"confidential","share":["local"]},"local",policy))
        self.assertFalse(allowed({"sensitivity":"confidential","share":["local"]},"chatgpt",policy))
if __name__=="__main__":unittest.main()
