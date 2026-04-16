__version__ = 'v.0.0.0'
__author__ = 'Brainless'
print(r'''
/*-------------------------------------------*\
Copyright (C) 2025 Brainless

This program is free software: 
you can redistribute it and/or modify it under 
the terms of the GNU General Public License...
\*-------------------------------------------*/
    ''')
from bsdt.apps.util import header
header.banner(False)
try: 
    import pandas
    import numpy
    import openpyxl
    import pyfoam

except ModuleNotFoundError:
    import sys
    import os
    import subprocess
    from pathlib import Path
    subprocess.run([sys.executable, '-m','pip','install','-r', str((Path(__file__).parent / 'requirements.txt').resolve())])
    print('[ModuleNotFoundError] Installing Required Packages Automatically...')
    print('[Not_Ice]     press Ctrl+C to inturrupt this process If this repeats repeatedly')
    pack.boot()
    if sys.argv == ['']:
        print('[NotIce] It seems that this process is running on python enterpreter.')
        print('[NotIce] just restart this process again, then it will work')
        sys.exit(0)
    else: os.execl(sys.executable, sys.executable, *sys.argv)
import bsdt.apps.util as util
import bsdt.apps as apps