
#if statement practise 1
'''
age = 18
detail = input('enter your age ')
if int(detail) > age:
    print('he is major')
else:
    print('he is youngerone')
'''
# if statement in boolean
'''
house = 5000000
is_good_credit = True
if is_good_credit:
    down_payment = 0.1 * 5000000
else:
    down_payment = 0.2 * 5000000
print(f"Down_payment:rs{down_payment}")

'''
#logical operator in if statement
"""
good_credit = True
high_salary = True
security_sign = False
criminal_record = False
if good_credit and high_salary:
    print('he is eligible for loan')

if good_credit or security_sign:
    print("and also he is eligible")

    if high_salary and not criminal_record:
        print("not eligible for the loan")

"""
# comparison operator in if statement
'''
enter_name = input("enter your name: ")
if len(enter_name) < 3:
    print("name must be atleast 3 characters")
elif len(enter_name) > 50:
    print("name can be maximum of 50 characters")
else:
    print("name looks good")
    
'''

