__version__ = 'v.0.0.0'
__author__ = 'Brainless'

try: 
    from .util.parcer import  dirscanner, reader
    from .util.processer import FileManager
    from .package import pack
    print(r'''
/*-------------------------------------------*\
Copyright (C) 2025 Brainless

This program is free software: 
you can redistribute it and/or modify it under 
the terms of the GNU General Public License...
\*-------------------------------------------*/
    ''')
    header.banner(False)
except ImportError:
    import sys   
    print('[ImportError] Error Occured While Importing BSDT.')
    sys.exit(0)
try: 
    import pandas
    import numpy
    import openpyxl

except ImportError:
    from . import pack
    import sys
    import os
    print('[ImportError] Installing Required Packages Automatically...')
    print('[Not_Ice]     press Ctrl+C to inturrupt this process If this repeats repeatedly')
    pack.boot()
    if sys.argv == ['']:
        print('[NotIce] It seems that this process is running on python enterpreter.')
        print('[NotIce] just restart this process again, then it will work')
        sys.exit(0)
    else: os.execl(sys.executable, sys.executable, *sys.argv)