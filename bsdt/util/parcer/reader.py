import os
import pandas
import re
# Input
def validate(directory,ext):
        # 1. 입력 데이터 형식: 리스트
    if not isinstance(directory,list): raise TypeError('input type is required to be List') 
        # 2. 내용물 형식: 문자열
    for path in directory:
        if not isinstance(path, str): raise TypeError('contents of input List are required to be String')
        # 3. 파일 확장자 확인
    if not directory[-1].endswith('.'+ext): raise ValueError(f'target file must be .{ext}')
        # 4. 파일 존재여부 확인
    target =  os.path.join(*directory)
    if not  os.path.isfile(target): raise FileNotFoundError('target file does not exist')
    return target
def read_excel(directory):    # 엑셀파일 읽기
    return pandas.read_excel(validate(directory,'xlsx')) # 출력 형식: pandas Dataframe
def read_csv  (directory):    # CSV 파일 읽기 
    return pandas.read_csv  (validate(directory,'csv' ))  # 출력형식은 위와 동일
def read_forces  (directory):    # forces.dat 파일 읽기: OpenFOAM 데이터 출력 파일.
    with open(validate(directory,'dat'),'r') as f:
        content = f.readlines()
    if not content[2].startswith('# Time'):raise ValueError('Invalid Form')
    else: content = content[3:]
    output = { k : [] for k in ['Time']+[a+b for a in ['F','M'] for b in ['x','y','z']]}
    for line in content:
        temp = list(map(float,re.findall(r'[+-]?\d+(?:\.\d+)?(?:[Ee][+-]\d+)?',line)))
        output['Time'].append(temp[ 0]         )    # tlqkf
        output[ 'Fx' ].append(temp[ 1]+temp[ 4])    # 자동화를
        output[ 'Fy' ].append(temp[ 2]+temp[ 5])    # 어떻게
        output[ 'Fz' ].append(temp[ 3]+temp[ 6])    # 해야
        output[ 'Mx' ].append(temp[ 7]+temp[10])    # 될지 
        output[ 'My' ].append(temp[ 8]+temp[11])    # 모르겠다
        output[ 'Mz' ].append(temp[ 9]+temp[12])    # 그래서 그냥 방치하기로 결정함
    return pandas.DataFrame(output)
def read_txt  (directory,title,idx,idxinterval = 1):    # txt파일 읽기: 파일 형식은 \n(개행)으로 구분된 정수/실수 리스트
    with open(validate(directory,'txt'),'r') as f:
        try: value = [float(line.strip(' ')) for line in f.readlines() if line.strip(' ')]
        except ValueError: raise TypeError('target file must not include something is not number')
    return pandas.DataFrame({
        title: value,
        idx: range(1,idxinterval*len(value)+1,idxinterval)
        })
