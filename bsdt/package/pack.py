import subprocess
import sys
import os

def boot():
    pack_req = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'requirements.txt')
    subprocess.run([sys.executable, '-m','pip','install','-r',pack_req])

def imp():
    subprocess.run([sys.executable, '-m','pip','install','-r','requirements.txt'])

