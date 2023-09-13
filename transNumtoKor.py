#숫자를 입력하면 한글로 변환해주는 프로그램 

number = int(input("숫자는 입력해주세요. \n"))

iStep = iDigiNumber = 0
sDigiNumber = '영'
sKorNumber = ''
table =  {0:'',
          1:'일',
          2:'이',
          3:'삼',
          4:'사',
          5:'오',
          6:'육',
          7:'칠',
          8:'팔',
          9:'구'}

if number == 0 :
    sKorNumber = table.get(0)

while number > 0 :
    iDigiNumber = number%10
    sDigiNumber = table.get(iDigiNumber)
    number = number//10
    
    if iDigiNumber == 0:
        if iStep ==4:
            sDigiNumber = sDigiNumber + '만 '
        elif iStep == 8:
            sDigiNumber = sDigiNumber + '억 '
        elif iStep == 12:
            sDigiNumber = sDigiNumber + '조 '
        elif iStep == 16:
            sDigiNumber = sDigiNumber + '경 '   
      
        sKorNumber = sDigiNumber + sKorNumber
        iStep += 1
        continue
   
    if iStep % 4 == 1:
        sDigiNumber = sDigiNumber + '십'
    elif iStep % 4 == 2 :
        sDigiNumber = sDigiNumber + '백'
    elif iStep % 4 == 3 :
        sDigiNumber = sDigiNumber + '천'
    elif iStep == 4:
        sDigiNumber = sDigiNumber + '만 '
    elif iStep == 8:
        sDigiNumber = sDigiNumber + '억 '
    elif iStep == 12:
        sDigiNumber = sDigiNumber + '조 '
    elif iStep == 16:
        sDigiNumber = sDigiNumber + '경 '
    else: 
        sDigiNumber = table.get(iDigiNumber)
    
    sKorNumber = sDigiNumber + sKorNumber
    iStep += 1

print(sKorNumber) 
    
