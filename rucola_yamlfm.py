import os
import re
import yaml


class YamlFrontmatter:

    def __init__(self, pattern='**/*.md', limiter='---'):
        self.pattern = pattern
        self.limiter = limiter


    def __call__(self, app):

        reg = re.compile(r'^{}$'.format(self.limiter), re.MULTILINE)

        for f in app.find(self.pattern):

            try:
                _, fm, content = reg.split(f.content, 2)
            except ValueError:
                continue

            content = content.replace(os.linesep, '', 1)

            metadata = yaml.load(fm)
            f.update(metadata)
            f.content = content
