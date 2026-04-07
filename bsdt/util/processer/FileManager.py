import shutil
import pandas
import re
from pathlib import Path
from typing import Union
class Root: # 프로젝트 루트 클래스
    registry = {}
    def __init__(self):
        path =  
class Case: # 케이스 객체 클래스
    pass # TODO
class Obj: # 목적물 객체 클래스: 파일/디렉토리
    @classmethod
    def create(cls, path:Union[str, list, Path]): # Obj 자식 클래스 검출 및 할당. 
        path = Path(*path) if isinstance(path,list) else Path(path)
        if not path.exists(): raise FileNotFoundError
        match Path(path).suffix:
            case '.txt' : return text   (path)
            case '.csv' : return csv    (path)
            case '.xlsx': return excel  (path)
            case '.dat' : return forces (path)
            case _      : return Obj    (path)
    def __init__(self, path:Union[str, list, Path]):
        self.path = Path(*path) if isinstance(path,list) else Path(path)
        if not self.path.exists(): raise FileNotFoundError
        self.file = bool(self.path.is_file())
        self.dir  = bool(self.path.is_dir())
        self.name = self.path.name
        classname = self.__class__.__name__
        if not self.path.parent.name in Obj.registry: Obj.registry[self.path.parent.name] = {}
        if not classname in Obj.registry[self.path.parent.name]: Obj.registry[self.path.parent.name][classname] = []
        Obj.registry[self.path.parent.name][classname].append(self)
    def delete(self, target: list): # 파일/디렉토리 삭제 메서드. target은 self 기준 상대경로
        if target: target_path = self.path.joinpath(*target).resolve()
        else: raise ValueError('target Not Found')
        if target_path.is_file(): 
            target_path.unlink()
            print(f'[FILE Removal] Removed {target_path}')
        elif target_path.is_dir(): 
            shutil.rmtree(target_path)
            print(f'[FOLDER Removal] Removed {target_path}')
        else: print(f'[ERROR OCCURED] {target_path} seems to be something that must not exist here...')

    def update(self, target):
        source = Path('TODO', 'BSDT_control', self.parent.name, '__host__',self.name) #TODO
        if target: target_path = self.path.joinpath(*target).resolve()
        if source.is_file(): 
            shutil.copy2(source,target)
            print(f'[FILE Update] Updated {target}')
        elif source.is_dir(target):
            shutil.copytree(source,target)
            print(f'[FOLDER Update] Updated {target}')
        else: print(f'[ERROR OCCURED] {target} seems to be something that must not exist here...')

class text(Obj):
    def read(self,idx,idxinterval = 1):    # txt파일 읽기: 파일 형식은 \n(개행)으로 구분된 실수 리스트
        with open(self.path,'r') as f:
            try: value = [float(line.strip()) for line in f.readlines() if line.strip()]
            except ValueError: raise TypeError('target file must not include something is not number')
        return pandas.DataFrame({
            self.name   : value,
            idx: range(1,idxinterval*len(value)+1,idxinterval)
            })
class csv(Obj): # csv 파일 객체 클래스
    def read(self): return pandas.read_csv(self.path) # 출력 형식: pandas Dataframe
class excel(Obj): # 엑셀 파일 객체 클래스
    def read(self): return pandas.read_excel(self.path)
class forces(Obj): # forces.dat 파일 전용 객체 클래스
    def read(self):
        with open(self.path,'r') as f:
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


