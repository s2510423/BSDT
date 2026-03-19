import os
import shutil
import pandas
import re
def validate(directory,ext):
        # 1. 입력 데이터 형식: 리스트
    if not isinstance(directory,list): 
        print('input type is required to be List') 
        return None
        # 2. 내용물 형식: 문자열
    for path in directory:
        if not isinstance(path, str): 
            print('contents of input List are required to be String')
            return None
        # 3. 파일 확장자 확인
    if not directory[-1].endswith(ext):
        print(f'target file is not .{ext}')
        return None
        # 4. 파일 존재여부 확인
    target =  os.path.join(*directory)
    if not  os.path.isfile(target): raise FileNotFoundError('target file does not exist')
    return True

Obj_list = list()
text_list = list()
csv_list = list()
excel_list = list()
forces_list = list()
def factory(path): # Obj 및 그 자식 클래스를 자동 검출 및 할당. 
    if not validate(directory,''): raise ValueError()
    path = os.path.join(*path)
    if self.name.endswith('.txt' ): return text      (path) # 확장자 검사 및 하위 클래스 자동 적용
    elif self.name.endswith('.xlsx'): return excel   (path)
    elif self.name.endswith('.csv' ): return csv     (path)
    elif self.name ==   'forces.dat': return forces  (path)
class Obj: # 목적물 객체 클래스: 파일/디렉토리
    def __init__(self,path):
        # path form: list
        self.path = os.path.join(*path) # OS에 맞는 경로 형식으로 변환
        self.name = str(path[-1])

        Obj_list.append(self)
    def delete(self): # 파일/디렉토리 삭제 메서드
        ok = True
        target_path = os.path.join(self.path)
        print(f'[CAUTION] You are attempting to delete {self.path}..')
        repeat = True
        while True:
            ans = input('ARE YOU SURE...?  [Y/N]: ').lower()
            if ans == 'y':break
            elif ans == 'n': 
                ok = False
                break
            else: print('[ERROR OCCURED] TYPE IT CORRECTLY!!!!')
        if ok == True:
            if os.path.isfile(target_path): 
                os.remove(target_path)
                print(f'[FILE Removal] Removed {target_path}')
            elif os.path.isdir(target_path): 
                shutil.rmtree(target_path)
                print(f'[FOLDER Removal] Removed {target_path}')
            else: print(f'[ERROR OCCURED] {target_path} seems to be something that must not exist here...')

    def update(self, name,  script_depth = 0):
        source = os.path.join('....', 'BSDT_control', name, '__host__',path)
        target = os.path.join(self.path)
        if os.path.isfile(target): 
            shutil.copy2(source,target)
            print(f'[FILE Update] Updated {target}')
        elif os.path.isdir(target):
            shutil.copytree(source,target)
            print(f'[FOLDER Update] Updated {target}')
        else: print(f'[ERROR OCCURED] {target} seems to be something that must not exist here...')

class text(Obj):
    def __init__(self,path): 
        validate(path,'.txt')
        text_list.append(self)
    def read(self,idx,idxinterval = 1):    # txt파일 읽기: 파일 형식은 \n(개행)으로 구분된 실수 리스트
        with open(self.path,'r') as f:
            try: value = [float(line.strip(' ')) for line in f.readlines() if line.strip(' ')]
            except ValueError: raise TypeError('target file must not include something is not number')
        return pandas.DataFrame({
            self.name   : value,
            idx: range(1,idxinterval*len(value)+1,idxinterval)
            })
class csv(Obj): # csv 파일 객체 클래스
    def __init__(self,path): 
        validate(path,'.csv')
        csv_list.append(self)
    def read(self): return pandas.read_csv(self.path) # 출력 형식: pandas Dataframe
class excel(Obj): # 엑셀 파일 객체 클래스
    def __init__(self,path): 
        validate(path,'.xlsx')
        excel_list.append(self)
    def read(self): return pandas.read_excel(self.path)
class forces(Obj): # forces.dat 파일 전용 객체 클래스
    def __init__(self,path): 
        validate(path,'forces.dat')
        forces_list.append(self)
    def read(self):
        with open(validate(self.path.split(os.sep),'dat'),'r') as f:
            content = f.readlines()
        if not content[2].startswith('# Time'):raise ValueError('Invalid Form')
        else: content = content[3:]
        output = { k : [] for k in ['Time']+[a+b for a in ['F','M'] for b in ['x','y','z']]}
        for line in content:
            temp = list(map(float,re.findall(r'[+-]?\d+(?:\.\d+)?(?:[Ee][+-]\d+)?',line)))
            output['Time'].append(temp[ 0]         )
            output[ 'Fx' ].append(temp[ 1]+temp[ 4])    # 자동화를
            output[ 'Fy' ].append(temp[ 2]+temp[ 5])    # 어떻게
            output[ 'Fz' ].append(temp[ 3]+temp[ 6])    # 해야
            output[ 'Mx' ].append(temp[ 7]+temp[10])    # 될지 
            output[ 'My' ].append(temp[ 8]+temp[11])    # 모르겠다
            output[ 'Mz' ].append(temp[ 9]+temp[12])    # 그래서 그냥 방치하기로 결정함
        return pandas.DataFrame(output)


