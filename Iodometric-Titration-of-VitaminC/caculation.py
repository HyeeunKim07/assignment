# 몰수 계산
x=float(input("용질의 질량을 입력해주세요:")) # 용질의 질량
y=float(input("용질의 몰 질량을 입력해주세요:")) # 몰 질량
print("몰수:",x/y)

# 평균 몰수 계산
x=float(input("IO3-의 몰수를 입력해주세요:")) # 몰수
y=float(input("소비된 IO3- 표준 용액의 부피를 입력해주세요:")) # 표준 용액의 부피
print("평균 몰수:",x*y)

# 아스코르브 질량 계산
x=float(input("IO3-의 평균 몰수를 입력해주세요:")) # 평균 몰수
y=float(input("비타민 c의 분자량을 입력해주세요:")) # 분자량
print("100ml에서의 아스코르브 질량:",50*x*y)
