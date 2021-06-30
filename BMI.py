#這是一個計算BMI的程式
height = input('請輸入身高(cm)：')
weight = input('請輸入體重(kg)：')
height = int(height)
weight = int(weight)
height = height / 100
BMI = weight / height / height
if BMI < 18.5:
	print('你的BMI為',BMI,'屬體重過輕')
elif BMI >= 18.5 and BMI < 24:
	print('你的BMI為',BMI,'屬體重正常')
elif BMI >= 24 and BMI < 27:
	print('你的BMI為',BMI,'屬體重過重')
elif BMI >= 27 and BMI < 30:
	print('你的BMI為',BMI,'屬輕度肥胖')
elif BMI >= 30 and BMI < 35:
	print('你的BMI為',BMI,'屬中度肥胖')
elif BMI < 35:
	print('你的BMI為',BMI,'屬重度肥胖')
