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
    ''')
def log():
    print(r'''

/*-------------------------------------------*\
        Bootleg Scientific Data Toolkit        
      고삐리가 대충만든 데이터 툴킷 v.0.0.0  
\*-------------------------------------------*/


Bootleg Execution Starting...
    ''')

def banner(short_bull=True):
    if not short_bull: logo()
    else: pass
    log()


def menu(title,content_list,size=1): # 메뉴 출력 함수

    # 예외처리
        # 1. 제목과 내용 존재 확인
    if not (title and content_list):
        print('[Error Occured] Title or Content is not given') # 에러 메세지
        return None # None을 반환하고 함수 종료

        # 2. 제목과 내용의 자료형 확인
    if not type(title) == str:
        print('[Error Occured] Title needs to be string')
        return None
    if not type(content_list) == list:
        print('[Error Occured] Content needs to be list')
        return None

    width = size * 22 + 4 # 메뉴 너비 설정

        # 3. 제목의 메뉴 외부 침범 여부 확인
    if not len(title) <= width :
        print('[Error Occured] Title is longer than width of the menu.')
        return None

        # 4. 내용의 메뉴 외부 침범 여부 확인
    for content in content_list:
        if not len(str(content)) <= width - 15 :
            print(f'[Error Occured] Content is longer than width of the menu: {content}')
            return None

    # 실행 함수
    num = 0
    print('/*' + '-' * (width - 4) + '*\\')                         # /*-----------------------*\
    print(title.center(width))                                      #         menu title         
    print('|' + '-' * (width - 2) + '|')                            # |-------------------------|
    for content in content_list:                                    #     [  1  ]    content 1
        num += 1                                                    #     [  2  ]    content 2
        print(' ' * 4 + f'[{str(num).center(5)}]' + ' ' * 4 + content)   #     [  3  ]    content 3
    print('\\*' + '-' * (width - 4) + '*/')                         # \*-----------------------*/
    return input('[Select Your Choice]: ')                          # [Select Your Choice]: {input}
    