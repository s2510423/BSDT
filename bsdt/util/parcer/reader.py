import os

#엑셀파일
def excel(dir):
    # 예외처리
        # 1. 입력 데이터 형식: 리스트
    if not isinstance(dir,list): raise TypeError('input type is required to be List') 
        # 2. 내용물 형식: 문자열
    for path in dir:
        if not isinstance(path, str): raise TypeError('contents of input List are required to be String')
        # 3. 파일 확장자 확인
    if not dir[-1].endswith('.xlsx'): raise SyntaxError('target file must be .xlsx')
        # 4. 파일 존재여부 확인
    target =  os.path.join(dir)
    if not  os.path.isfile(target): raise FileNotFoundError('target file does not exist')