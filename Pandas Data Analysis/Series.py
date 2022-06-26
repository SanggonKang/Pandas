# pandas 불러오기
import pandas as pd

# Dictionary 만들고, 변수 dict 에 저장하기
dict = {'a':1, 'b':2, 'c':3}

# pandas Series() 함수로 Dictionary 를 Series 로 변환하고, 변수 sr 에 저장하기
sr = pd.Series(dict)

# 변수 sr 의 data type 출력하기
print(type(sr))
print('\n')

# 변수 sr 출력하기 (Series 객체 출력)
print(sr)