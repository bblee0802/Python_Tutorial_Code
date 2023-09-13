#윤년 판별하기 
#윤년규칙 
# 1. 4의배수년은 윤년이다.
# 2. 4,100으로 나누어 떨어지면 평년이다.
# 3. 4,100,400으로 나누어 떨어지면  윤년이다. 

iYear = int(input("입력한 연도가 윤년인지 판별해줍니다. \n연도를 입력해주세요. (-9999 을 입력하면 종료합니다.) : "))

while  iYear != -9999:
    if iYear % 4 == 0:
        bGregorian = True
        if iYear % 100 == 0 :
            if iYear % 400 == 0:
                bGregorian = True
            else :
                bGregorian = False
    else:
        bGregorian = False
    
    if bGregorian == True:
        print(iYear, "년도는 윤년입니다. \n\n") 
    else: 
        print(iYear, "년도는 평년입니다. \n\n") 
    
    iYear = int(input( "연도를 입력하세요.(-9999을 입력하면 종료합니다.) : "))       
                    
    
