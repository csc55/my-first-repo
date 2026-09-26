height = int(input("身高(cm):"))

weight = int(input("体重(kg):"))

bmi = weight * 10000 / height ** 2 

print("你的BMI是:", bmi)

if bmi < 18.5:
    
    print("偏瘦")
        
if 18.5 <= bmi < 24:
    
    print("正常")
        
if bmi >= 24:

    print("偏重")
