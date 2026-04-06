from pathlib import Path

obj_list=[]

class obj:
    def __init__(self,name):
        obj_list.append(name)

def scan(name):
    
    try: 
        obj_list.clear()
        with open(Path('BSDT_control',name,'target.bsdt'), 'r') as f:
            lines = f.readlines() 
            for line in lines:obj(line)

    except FileNotFoundError: print(f"[FileNotFoundError] It seems that {os.path.join('BSDT_control',name,'target.bsdt')} doesn't exist.")

def write_targetlist(name,targetlist):
    
    if os.path.exists(os.path.join(,'BSDT_control',name)): pass
    else: os.makedirs(os.path.join(,'BSDT_control',name))
    with open(os.path.join('BSDT_control',name,'target.bsdt'), 'w') as f:
        for target in targetlist:
            f.write(f'{target}\n')

def starting(head,name):
    
    target = []
    for i in os.listdir('.'):
        j = i.strip()
        if j.startswith(head): 
            target.append(j)
            print(f'Found {j}')
    write_targetlist(name,target)

def ending(foot,name):
    
    target = []
    for i in os.listdir('.'):
        j = i.strip()
        if j.endswith(foot):
            target.append(j)
            print(f'Found {j}')
    write_targetlist(name,target)