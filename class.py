class  cars:
    madeYear = 0
    color = 'black'
    weight = 0
    width = 0
    height = 0
    tops = 0
    
    
    def getCarInfor(self) :
        infor = f"만든 연도: {self.madeYear} 년 \n색상: {self.color} \n무게: {self.weight} kg" + \
                f"\n가로: {self.width} cm \n세로: {self.height} cm \n높이: {self.tops} cm"
        return infor
    def __init__(self,madeYear=0, color= "black", weight=0, width=0, height=0, tops=0):
        self.madeYear = madeYear
        self.color = color
        self.weight = weight
        self.width = width
        self.height = height
        self.tops = tops

car = cars(madeYear=2014, tops=300, color='red')
print(car.getCarInfor())


class SportCar(cars) :
    maxSpeed = 0
    
    def setSpeed(self, maxSpeed=0):
        self.maxSpeed = maxSpeed 
    def getCarInfor(self):
        return "\n스포츠카 \n" + super().getCarInfor() + f"\n최대 속도: {self.maxSpeed} km/s"     
    def 운전(self) :
        print("스포츠가 운행 시작 싱싱~~~~")
        
    def ㄷㄱ2333():
        pass
            


car1 = SportCar(madeYear= 2016)
car1.setSpeed(250)
print(car1.getCarInfor())

car1.운전()


import fridge 

f = fridge.Fridge()
apple  = fridge.Food()
elephant = fridge.Food()


f.open()
f.put(apple)
f.put(elephant)
f.put(apple)
f.close()
print(f.__repr__())

print(f.foods)

