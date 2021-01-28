import os 
import csv
from jinja2 import Template
from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
 
class IncludePlugin(BasePlugin):

    config_scheme = (
        ('src_path', config_options.Type(str, default="docs")),
    )
    page = None

    def includex(self, filename):
        # !!! TODO support git+, https and other uris
        # !!! TODO support BOF, EOF markers
        # !!! TODO support line range
        path = f'{self.config["src_path"]}/{filename}'
        suffix = os.path.splittext(path)[-1]
        if suffix == ".csv" :
            cmd_str = ''
            with open('test.csv')as f:
                f_csv = csv.reader(f)
                for row in f_csv:
                    cmd_str=cmd_str+row
                return cmd_str
        else:
            with open(path, 'r') as f:
                return f.read()

    def on_page_markdown(self, markdown, page, config, **kwargs):
        self.page = page
        md_template = Template(markdown)
        return md_template.render(includex=self.includex)
