import json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class OpenClawContract(unittest.TestCase):
 def test_isolated_profile_and_readonly_probe(self):
  readme=(ROOT/"README.md").read_text()
  self.assertIn('openclaw --profile weavz-example',readme)
  self.assertIn('--transport streamable-http',readme)
  self.assertIn('mcp doctor weavz --probe',readme)
 def test_template_contains_no_credentials(self):
  text=(ROOT/"openclaw.config.example.json5").read_text()
  self.assertIn('transport: "streamable-http"',text)
  self.assertIn('auth: "oauth"',text)
  self.assertNotIn('Authorization',text); self.assertNotIn('token',text.lower())
if __name__=='__main__': unittest.main()
