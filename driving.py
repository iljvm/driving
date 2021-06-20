country = input('請輸入國籍:')
age = input('請輸入年齡:')
age = int(age)
if country == '台灣':
    if age >= 18:
        print('可以開車')
    else:
        print('不能開車')
elif country =='美國':
    if age >= 16:
        print('可以開車')
    else:
        print('不能開車')
else:
    print('請遵守各國法律')