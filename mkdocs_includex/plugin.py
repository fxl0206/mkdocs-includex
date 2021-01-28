import os 
import csv
import sys

from jinja2 import Template
from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
 
TPLX='\
|    | animal_1   | animal_2   |\n\
|---:|:-----------|:-----------|\n\
|  0 | elk        | dog        |\n\
|  1 | pig        | quetzal    |'

def parseCsv(path):
    cmd_str = ''
    with open(path,encoding= 'gbk')as f:
        f_csv = csv.reader(f)
        line = 0
        for row in f_csv :
            curRow='|'
            for col in row:
                curRow=curRow+col+"|"
            if line == 0 :
                hsp='|'
                for col in row:
                    hsp=hsp+":---"+"|"
                curRow=curRow+"\n"+hsp
            cmd_str=cmd_str+"\n"+curRow
            line=line+1
        return cmd_str

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
        suffix = os.path.splitext(path)[1]
        if suffix == ".csv" :
            return parseCsv(path)
        else:
            with open(path, 'r') as f:
                return f.read()

    def on_page_markdown(self, markdown, page, config, **kwargs):
        self.page = page
        md_template = Template(markdown)
        return md_template.render(includex=self.includex)

def main(argv):
    path=os.path.splitext("1.txt")[-1]
    print(path)
    print(parseCsv("../test/hosts-info.csv"))


if __name__ == "__main__":
   main(sys.argv[1:])