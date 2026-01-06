import subprocess
import sys
import os
from . import header

def boot():
    header.banner()
    pack_req = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'requirements.txt')
    subprocess.run([sys.executable, '-m','pip','install','-r',pack_req])

def imp():
    header.banner()
    subprocess.run([sys.executable, '-m','pip','install','-r','requirements.txt'])

