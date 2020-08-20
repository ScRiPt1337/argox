import subprocess
from sys import executable
from cprint import *

class analyzier:
    def __init__(self, url):
        self.url = url

    def run(self):
        try:
            result = subprocess.check_output( executable + " -m wad -f txt -q -u " + self.url, shell=True)
        except Exception as e:
            cprint.err(e)
        return result.decode().replace("Web application detection results for website","").replace(", found applications:","").replace(self.url+"/","").rstrip()