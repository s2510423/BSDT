import os
import shutil

#엑셀파일
def excel(dir):
    # 예외처리
        # 1. 입력 데이터 형식: 리스트
    if not isinstance(dir,list): 
        print('[Error Occured] input type is required to be List')
        return None
        # 2. 입력 데이터 리스트 내용물 형식: 문자열
    for path in dir:
        if not type(path) == str:
            print('[Error Occured] contents of input List are required to be String')
            return None
        # 3. 파일 확장자 확인
    if not dir[-1].endswith('.xlsx'):
        print('[Error Occured] target file must be .xlsx')
        return None
        # 4. 파일 존재여부 확인
    target =  os.path.join(dir)
    if not  os.path.isfile(target):
        print('[Error Occured] target file does not exist')
        return None
