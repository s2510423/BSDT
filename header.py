def logo():
    print(r'''

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


Bootleg Execution Starting...
    ''')
def license():
    print(r'''
/*-------------------------------------------*\

Copyright (C) 2025 s2510423

This program is free software: 
you can redistribute it and/or modify it under 
the terms of the GNU General Public License...

\*-------------------------------------------*/
    ''')
def header(license_bool):
    if license_bool==True:license()
    else:pass
    logo()