__version__ = 'v.0.0.0'
def logo(style=0):
    match style:
        case 0:print(rf'''
┌────────────────────────────────────────────┐
│     ________ ________________ ________     │
│     ___  __ )__  ___/___  __ \___  __/     │
│     __  __  |_____ \ __  / / /__  /        │
│     _  /_/ / ____/ / _  /_/ / _  /         │
│     /_____/  /____/  /_____/  /_/          │
│      Bootleg Scientific  Data Toolkit      │
│                                            │
├────────────────────────────────────────────┤

    Bootleg-Made Toolkit by Brainless Kiddo  
    
├────────────────────────────────────────────┤

     고삐리가 대충만든 데이터 툴킷 {__version__}                                        
        Bootleg Execution Starting...
        
└────────────────────────────────────────────┘
''')
        case 1:print(rf'''
/*--------------------------------------------*\
 |     ________ ________________ ________     |
 |     ___  __ )__  ___/___  __ \___  __/     |
 |     __  __  |_____ \ __  / / /__  /        |
 |     _  /_/ / ____/ / _  /_/ / _  /         |
 |     /_____/  /____/  /_____/  /_/          |
 |      Bootleg Scientific Data Toolkit       |
\*--------------------------------------------*/
Bootleg-Made Toolkit by Brainless Kiddo 
version = {__version__}

Bootleg Execution Starting...
        ''')
def log():
    print(r'''

/*-------------------------------------------*\
        Bootleg Scientific Data Toolkit        
      고삐리가 대충만든 데이터 툴킷 {__version__}  
\*-------------------------------------------*/


Bootleg Execution Starting...
    ''')

def banner(short_bool=True,style=1):#style argument is only for logo setting
    if not short_bool: logo(style)
    else: log()

class Exit(Exception): pass
def menu(title,content_list,size=1): # 메뉴 출력 함수

    # 예외처리
        # 1. 제목과 내용 존재 확인
    if not (title and content_list): raise SyntaxError('Title or Content is not given')

        # 2. 제목과 내용의 자료형 확인
    if not isinstance(title, str): raise TypeError('Title needs to be string')
    if not isinstance(content_list, list): raise TypeError('Content needs to be list')

    width = size * 22 # 메뉴 너비 설정

        # 3. 제목의 메뉴 외부 침범 여부 확인
    if len(title) > width : raise ValueError('Title is longer than width of the menu.')

        # 4. 내용의 메뉴 외부 침범 여부 확인
    for content in content_list:
        margin = 4 + 7 + 4 # 공백 + 숫자박스 + 공백
        if len(str(content)) > width - margin : raise ValueError(f'Content is longer than width of the menu: {content}')

    # 실행 함수
    num = 0
    print('/*' + '-' * width + '*\\')                                   # /*-----------------------*\
    print(' |' + title.center(width) + '| ')                            #  |      menu title       | 
    print('\\*' + '-' * width + '*/')                                   # \*-----------------------*/
    for content in content_list:                                        #     [  1  ]    content 1
        num += 1                                                        #     [  2  ]    content 2
        print(' ' * 4 + f'[{str(num).center(5)}]' + ' ' * 2 + content)  #     [  3  ]    content 3
                                                                        #
    num += 1;print(f'\n    [{str(num).center(5)}]    exit')             #     [  4  ]    exit
    print('\\*' + '-' * (width - 4) + '*/' + '\n')                      # \*-----------------------*/
    while True:
        try: choice =  int(input('[Select Your Choice]: '))             # [Select Your Choice]: {input}
        # 예외처리
            # 1. 선택 항목 형식 확인
        except ValueError: 
            print('Choice is required to be integer')
            continue
            # 2. 선택 항목 존재 확인
        if not 0 < choice <= num: 
            print(f'Invalid Choice: {choice}')
            continue
        # 설마 이걸 뚫고 실수를 해내겠어...?
        elif choice == num: raise Exit('User Decided to Exit')
        else: return choice
