#FizzBuzz

def  fizzBuzz(iStart, iEnd) :
    for i in range(iStart,iEnd):
        match (i%3, i%5):
            case (0,0) :
                print("FizzBuzz")
            case(0, _) :
                print("Fizz")
            case(_,0) :
                print("Buzz")
            case _:
                print(i)    
    else:
        print("게임 종료")
               
        
fizzBuzz(1,400)

