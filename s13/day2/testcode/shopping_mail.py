#!/usr/bin/env python
# -*- codind:utf-8 -*-
#Author:ljb
salary = input('input your salary:')
if salary.isdigit():
    salary = int(salary)
else:
    exit('invalid data type')

welcome_msg = "Welcome to My Shoping mail".center(50,'-')
print(welcome_msg)


exit_flags = True

product_list = [
    ('iphone',5000),
    ('MAC',8000),
    ('Xiaomi',500),
    ('Coffee',30),
    ('bike',700),
    ('food',20)
]
shop_car = []
while exit_flags is not False:
    for item in enumerate(product_list):
        index = item[0]
        p_product = item[1][0]
        p_price = item[1][1]
        print(index,'.',p_product,p_price)
    choice_input = input('[q=quit,c=check]What do you want to buy?:')
    if choice_input.isdigit():
        choice_input = int(choice_input)
        if choice_input < len(product_list):
            p_item = product_list[choice_input]
            if p_item[1] <= salary:
                shop_car.append(p_item)
                salary -= salary
                print('Add %s into shop car ,you current balance is %s' %(p_item,salary))
            else:
                print('you current balance is %s,you can not afford' %salary)
        else:
            if choice_input == 'q' or choice_input == 'quit':
                print('you purchased products as blow'.center(40,'*'))
                for item in shop_car:
                    print(item)
                print('END'.center(40,'*'))
                print('your balance is %s'% salary)
                print('BYE')
                exit_flags = False
            elif choice_input == 'c' or choice_input == 'check':
                print('you purchased products as blow'.center(40,'*'))
                for item in shop_car:
                    print(item)
                print('END'.center(40,'*'))
                print('your balance is %s'% salary)




