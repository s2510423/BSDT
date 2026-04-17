import shutil
import pandas
import re
from pathlib import Path
from typing import Union
import header

class Root:
    "프로젝트 루트 클래스: 각각의 케이스를 담는 파라미터 스윕의 객체화" 
    '''
OOP 캡슐 구조로 한번에 여러 개의 스윕 관리 가능
(쓸모가 없어야 좋겠지만) 필요시 여러개의 과제 동시 실행도 가능
    '''
    registry = {} # 프로젝트 전체 레지스트리 생성
    regi_list = [] # Root 클래스로 선언된 객체 리스트를 이용한 호출 가능
    def __init__(self,path:Union[str,list,Path,type(None)]=None):
        match path: # self.path 지정. path 미입력 시 작업 영역을 기준으로 함.
            case None: self.path = Path.cwd()
            case _: self.path = Path(*path) if isinstance(path,list) else Path(path) # 리스트일 경우 경로 파싱 자동
        if not self.path.exists(): raise FileNotFoundError # 폴더 존재 여부 예외처리
        if not self.path.is_dir(): raise NotADirectoryError('Root is required to be Directory.')
        Root.registry[self] = {} # 레지스트리에 스스로를 추가.
        Root.regi_list.append(self)

class Case: 
    "Obj 객체를 담는 케이스 객체 클래스" 
    '''
하나의 파라미터 스윕 내의 여러 케이스, 하나의 케이스 내의 여러 Obj
말초까지 접근하지 않고도 OpenFOAM 실행 및 조건 수정 수행(개발 예정)
    '''
    regi_list=[] # Case 자식 객체 호출을 위한 리스트
    def __init__(self,path:Union[str, list, Path],parent:Root):
        self.path = Path(*path) if isinstance(path,list) else Path(path) # 리스트일 경우 자동 파싱
        if not self.path.exists(): raise FileNotFoundError # 폴더 존재 여부 핸들링
        if not self.path.is_dir(): raise NotADirectoryError('Case is required to be Directory.')
        self.parent = parent
        Root.registry[self.parent][self] = {"General": []} # 레지스트리에 부모 Root도 등록 -> 트리형 레지스트리 구조를 이용한 계층화 전략
        Case.regi_list.append(self) # 평면적 리스트 형식으로 인덱싱 최적화

    def foamRun(self):
        p = subprocess.Popen(["foamRun"], cwd = self.path)
        return p
    def decompose(self, np, solver):
        i=0
        while (self.path / 'log' / f'log.{solver}.{i}.bsdt').exists(): 
            i += 1
        log = self.path / log / f'log.{solver}.{i}.bsdt'
        log.parent.mkdir(parents=True, exist_ok=True)
        self.log = open(log, "w", encoding='utf-8')
        self.log.write(header.logo(1))
        subprocess.run(["decomposePar", "-force"], cwd=self.path)
        p = subprocess.Popen(["mpirun", "-np", np, solver, '-parallel'], cwd=self.path, stdout=self.log, stderr=self.log, text=True)
        return p
        
class Obj:
    "말단 객체 클래스: 파일/디렉토리"
    '''
파일 삭제, 업데이트(중앙 __host__ 디렉토리 이용) 지원
결과 파일 후처리 및 시각화 지원
    '''
    ''' [LEGACY]
    @classmethod
    def create(root:Root, case:Case, cls, path:Union[str, list, Path]): # Obj 자식 클래스 검출 및 할당. 
        path = Path(*path) if isinstance(path,list) else Path(path)
        if not path.exists(): raise FileNotFoundError
        match Path(path).suffix:
            case '.txt' : return text   (path)
            case '.csv' : return csv    (path)
            case '.xlsx': return excel  (path)
            case '.dat' : return forces (path)
            case _      : return Obj    (path)
    '''
    regi_list=[]
    def __init__(self, path:Union[str, list, Path], parent:Case ): # grandparent 정도는 대략 알아서 잘 이해해주시길
        self.path = Path(*path) if isinstance(path,list) else Path(path) # 리스트 자료형 자동 파싱
        if not self.path.exists(): raise FileNotFoundError # 폴더일 필요는 없어서 존재여부만 핸들링
        self.file = bool(self.path.is_file()) # 필요한 변수들 설정.
        self.dir  = bool(self.path.is_dir()) # 없는 것보다야 낫겠지
        self.name = self.path.name # 반박시 니말이 맞음
        self.classname = self.__class__.__name__ 
        self.parent = parent
        self.grandparent = self.parent.parent
        if not self.classname in Root.registry[self.grandparent][self.parent]: Root.registry[self.grandparent][parent][self.classname] = [] 
        # 파일 형식에 따른 레지스트리 내 분류
        Root.registry[self.grandparent][self.parent]["General"].append(self) # 통합 레지스트리 지원
        Root.registry[self.grandparent][self.parent][self.classname].append(self)
        Obj.regi_list.append(self)
    def delete(self): # 셀프 삭제 메서드
        if self.file: 
            self.path.unlink()
            print(f'[FILE Removal] Removed {self.path}')
        elif self.dir: 
            shutil.rmtree(self.path)
            print(f'[DIRECTORY Removal] Removed {self.path}')
        else: print(f'[ERROR OCCURED] {"{",self.path,"}"} seems to be something that must not exist here...')
        Root.registry[self.grandparent][self.parent]["General"].remove(self) 
        Root.registry[self.grandparent][self.parent][self.classname].remove(self)
        Obj.regi_list.remove(self)

    def copy(self, source: Obj): # Obj 간 복사 메서드
        if source.file != self.file or source.dir != self.dir: raise ValueError(f"[Type Mismatch] Between {source.path} and {self.path}. NEIN!!")
        if source.file: 
            shutil.copy2(source.path,self.path)
            print(f'[FILE Copy] Synced {source.path} into {self.path}')
        elif source.dir:
            shutil.copytree(source.path,self.path, dirs_exist_ok=True)
            print(f'[DIRECTORY Copy] Synced {source.path} into {self.path}')
        else: print(f'[ERROR OCCURED] {source.path} or {self.path} seems to be something that must not exist here...')

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


