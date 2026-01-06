from . import header
import os
import shutil


class Folder:
    def __init__(self,name):
        # path form: dir1/dir2/file
        # !!!!!!Without space!!!!!!
        self.path = os.path.join(*name.split('/'))
        self.name = name.split('/')[-1]

    def delete(self, path):
        ok = True
        target_path = os.path.join(self.path,*path.split('/'))
        if target_path.strip() == '' or target_path == '.' : 
            print(f'[CAUTION] You are attempting to delete {self.path}..')
            repeat = True
            while repeat == True:
                ans = input('ARE YOU SURE...?  [Y/N]: ').lower()
                if ans == 'y': 
                    ok = True
                    repeat = False
                elif ans == 'n': 
                    ok = False
                    repeat = False
                else: 
                    print('[ERROR OCCURED] TYPE IT CORRECTLY!!!!')
                    repeat = True
        if ok == True:
            if os.path.isfile(target_path): 
                os.remove(target_path)
                print(f'[FILE Removal] Removed {target_path}')
            elif os.path.isdir(target_path): 
                shutil.rmtree(target_path)
                print(f'[FOLDER Removal] Removed {target_path}')
            else: print(f'[ERROR OCCURED] {target_path} seems to be something that must not exist here...')

    def update(self, raw_path, name,  script_depth = 0):
        depth = ['..'] * script_depth
        path = os.path.join(*raw_path.split('/'))
        source = os.path.join(*depth, 'BSDT_control', name, '__host__',path)
        target = os.path.join(self.path,path)
        if os.path.isfile(target):
            shutil.copy2(source,target)
            print(f'[FILE Update] Update {target}')
        elif os.path.isdir(target):
            shutil.copytree(source,target)
            print(f'[FOLDER Update] Update {target}')
        else: print(f'[ERROR OCCURED] {target} seems to be something that must not exist here...')