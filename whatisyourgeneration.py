#input으로 사용자의 나이를 입력받은 후, 다음 표의 어는 세대에 속하는지 출력하시요. 입출력 문구는 자유룹게 지으면 됩니다. 
# ------------------------------------------------------------------------------------------------------------
#      ~1924       |  가장 위대한 세대 (The Greatest Generation)
#  1925~1945	   |  침묵 세대(The Silent Generation)
#  1946~1964	   |  베이비붐 세대(baby boomer)
#  1965~1980	   |  X세대(Generation X)
#  1981~1996	   |  M세대(Millennial)
#  1997~2009	   |  Z세대(Generation Z)
#  2010~           |  알파세대(Generation Alpha)
# ------------------------------------------------------------------------------------------------------------


    
generations = {
              "가장위대한세대(The Greatest Generation)": range(1925),
              "침묵세대(The Silent Generation)": range(1925,1946),
              "베이비붐세대(baby boomer)": range(1946,1965),
              "X세대(Generation X))": range(1965,1981),
              "M세대(Millennial)": range(1981,1997),
              "Z세대(Generation Z)": range(1997,2010),
              "알파세대(Generation Alpha)": range(2010,2100)
              }

age = int(input("당신의 나이를 입력해주세요. \n"))

sGeneration = "아직 미분류된 세대"
for gen, agerange in generations.items():
    for agedata in  list(agerange):
        if (age == agedata):
            sGeneration = gen
            break
    
print("당신은 " + sGeneration + " 입니다.")