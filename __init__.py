
'''
/*-------------------------------------------*\
Copyright (C) 2025 Brainless

This program is free software: 
you can redistribute it and/or modify it under 
the terms of the GNU General Public License...
\*-------------------------------------------*/
┌─────────────────────────────────────────────┐
│    ┌───\    ┌─────┐   ┌───\     ┌─────┐     │
│    │ ┌┐ │   │ ┌───┘   │ ┌\ \    └─┐ ┌─┘     │
│    │ ' /    | └───┐   │ │ \ \     │ │       │
│    │ . \    └───┐ │   │ │ / /     │ │       │
│    │ └┘ │   ┌───┘ │   │ └/ /      │ │       │
│    └───/    └─────┘   └───/       └─┘       │
└─────────────────────────────────────────────┘
/*-------------------------------------------*\
        Bootleg Scientific Data Toolkit        
      고삐리가 대충만든 데이터 툴킷 v.0.0.0  
\*-------------------------------------------*/
'''



try: 
    from . import FileManager
    from . import dirscanner
    from . import header
    from . import pack
    print('''
/*-------------------------------------------*\
Copyright (C) 2025 Brainless

This program is free software: 
you can redistribute it and/or modify it under 
the terms of the GNU General Public License...
\*-------------------------------------------*/
    ''')
    header.banner(False)
except ImportError: 
    print('[ImportError] Error Occured While Importing BSDT.')    
try: 
    import pandas
    import numpy
    import openpyxl

except ImportError:
    import sys
    import os
    print('[ImportError] Installing Required Packages Automatically...')
    print('[Not_Ice]     press Ctrl+C to inturrupt this process If this repeats repeatedly')
    pack.boot()
    os.execl(sys.executable, sys.executable, *sys.argv)
__version__ = 'v.0.0.0'
__author__ = 'Brainless'