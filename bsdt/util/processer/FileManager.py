import os
import shutil


class Obj: # 목적물 객체 클래스: 파일/디렉토리
    def __init__(self,name):
        # path form: dir1/dir2/file
        # !!!!!!Without space!!!!!!
        # 
        self.path = os.path.join(*name.split('/')) # OS에 맞는 경로 형식으로 변환
        if str(name.split('/')[-1]).endswith('.xlsx'): name = text(name) # 확장자 검사 및 하위 클래스 자동 적용
        if str(name.split('/')[-1]).endswith('.xlsx'): name = excel(name)
    def delete(self, path): # 파일/디렉토리 삭제 메서드
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
        path = os.path.join(*raw_path.split('/'))
        source = os.path.join('....', 'BSDT_control', name, '__host__',path)
        target = os.path.join(self.path,path)
        if os.path.isfile(target):
            shutil.copy2(source,target)
            print(f'[FILE Update] Update {target}')
        elif os.path.isdir(target):
            shutil.copytree(source,target)
            print(f'[FOLDER Update] Update {target}')
        else: print(f'[ERROR OCCURED] {target} seems to be something that must not exist here...')

class text(Obj): # 텍스트 파일 객체 클래스
    def read(): pass
class excel(Obj): # 엑셀 파일 객체 클래스
    def read(): pass


