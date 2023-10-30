import LeapYear
import unittest


class TestLeapYear(unittest.TestCase):
    def test_2020(self):
        r= LeapYear.is_leap_year(2020)
        self.assertEqual(r, True)
        
    def testT_2077(self):
        r = LeapYear.is_leap_year(2077)
        self.assertEqual(r, False) 
        
    def ttest_2400(self):
        r = LeapYear.is_leap_year(2400)
        self.assertEqual(r,True)
    def ttest_2100(self):
        r = LeapYear.is_leap_year(2100)
        self.assertEqual(r, 2100)
    
        

#if __name__ == "__main__":
#    unittest.main()

def bokri(money, interest, duration):
    return money * (1 + interest)**duration
    
    
def ri(interest,duration):
    return  (1 + interest)**duration


def bokri2(money, interest, duration):
    pri = money
    while duration >=0:
        if duration >= 1 :
            pri = pri*ri(interest,duration)
        duration -= 1
    return  pri


print(bokri(3600000,0.058,1.9))
print(bokri2(3600000,0.058,1.9)) 


joblist = [30, 40, 22, 10, 9, 13, 89, 21, 3]
total_jobtime = sum(joblist)
avg_time = total_jobtime / len(joblist)





