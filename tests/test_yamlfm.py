import os
import unittest
from rucola import Rucola
from rucola_yamlfm import YamlFrontmatter


class Test(unittest.TestCase):

    def setUp(self):
        self.app = Rucola(os.path.dirname(__file__))

    def test_basic(self):

        self.app.use(
            YamlFrontmatter()
        )

        f = self.app.get('foo.md')
        self.assertEqual(1, f['a'])
        self.assertEqual('bar', f.content)

    def test_custom_limiter(self):

        self.app.use(
            YamlFrontmatter(limiter='===')
        )

        f = self.app.get('limiter.md')
        self.assertEqual('yes', f['test'])
        self.assertEqual('content', f.content)

    def test_no_content(self):

        self.app.use(
            YamlFrontmatter('nocontent.md')
        )

        f = self.app.get('nocontent.md')
        self.assertEqual('', f.content)
