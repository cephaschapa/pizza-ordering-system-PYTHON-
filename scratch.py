#PIZZA APPLICATION VERSION 1
from random import randint
import sys
import datetime
timeNow = datetime.datetime.now()

# some ity bitty functions Lee please do some research on them
def choice():
    #print(topping())
    choice = int(input('>>> Choose Topping: '))
    if choice == 1:
        top = 'Toppings: Cheese'
        print(top)
    elif choice == 2:
        top = 'Toppings: Extra Sauce'
        print(top)
    elif choice == 3:
        top = 'Toppings: Garlic'
        print(top)
    elif choice == 4:
        top = 'Toppings: Grated Pepper'
        print(top)
    elif choice == 5:
        top = 'Chilli Sauce'
        print(top)
    else:
        print('invalid Option')

def optionA(value3, name):


    print(topping())
    print('+--------------------------------------+')
    print('+                Your Oder             +')
    print('+--------------------------------------+')
    print(choice())

    pizza_specs = ['Pizza Name: Pepperoni and Cheese', 'Thickness: 2.5cm dough', 'Price: K115.00']
    for specs in pizza_specs:
        print(specs)

    print('Customer Name', customer_name)
    order_Num = randint(200, 600)
    print('Order Number:', order_Num)
    print('Cashier Name: ', cashierName)
    print('Time / Date ordered: ', timeNow)



def optionB(value3, name):


    print(topping())
    print('+--------------------------------------+')
    print('+                Your Oder             +')
    print('+--------------------------------------+')
    print(choice())

    pizza_specs = ['Pizza Name: Hum and Olives', 'Extras: Onion toppings', 'Thickness: 2.5cm dough', 'Price: K115.00']
    for specs in pizza_specs:
        print(specs)

    print('Customer Name', customer_name)
    order_Num = randint(200, 600)
    print('Order Number:', order_Num);
    print('Cashier Name: ', cashierName)
    print('Time / Date ordered: ', timeNow)

def optionC(value4, name):


    print(topping())
    print('+--------------------------------------+')
    print('+                Your Oder             +')
    print('+--------------------------------------+')
    print(choice())

    pizza_specs = ['Pizza Name: Creamy Chicken', 'Thickness: 3cm dough', 'Price: K120.00']
    for specs in pizza_specs:
        print(specs)

    order_Num = randint(200, 600)
    print('Customer Name', customer_name)
    print('Order Number:', order_Num)
    print('Cashier Name: ', cashierName)
    print('Time / Date ordered: ', timeNow)

def optionD(value5,name):



    print(topping())
    print('+--------------------------------------+')
    print('+                Your Oder             +')
    print('+--------------------------------------+')
    print(choice())
    pizza_specs = ['Pizza Name: Mushroom and Chicken', 'Thickness: 3cm dough', 'Price: K108.00']
    for specs in pizza_specs:
        print(specs)
    order_Num = randint(200,600)
    print('Order Number:', order_Num);
    print('Customer Name: ', customer_name)
    print('Cashier Name: ', cashierName)
    print('Time / Date ordered: ', timeNow)


#logical code block
def logicBlock(value,value2, value3):
    if menu_option == 1:

        print(optionA(customer_name,cashierName))
        print('------------------------------------------')
    elif menu_option == 2:
        print('------------- Specifications -------------')
        print(optionB(customer_name, cashierName))
        print('------------------------------------------')
    elif menu_option == 3:
        print('------------- Specifications -------------')
        print(optionC(customer_name, cashierName))
        print('------------------------------------------')
    elif menu_option == 4:
        print('------------- Specifications -------------')
        print(optionD(customer_name, cashierName))
        print('------------------------------------------')
    else:
        print('invalid Option')

def menu():
    print('')
    print('+--------------------------+')
    print('+        Pizza Menu        +')
    print('+--------------------------+')
    print('1. Pepperoni and Cheese')
    print('2. Hum and Olives')
    print('3. Creamy Chicken')
    print('4. Mushroom and Chicken')
    print('')

def topping():
    print('+--------------------------+')
    print('+        Toppings          +')
    print('+--------------------------+')
    topnarry = ['1. Cheese', '2. Extra Sauce', '3. Garlic', '4. Grated Pepper', '5. Chili Sauce']
    for x in topnarry:
        print(x)


#Welcome message
print('+--------------------------------------------------------------------+')
print('+                Hello! Welcome to Liwanaires Pizza                  +')
print('+--------------------------------------------------------------------+')



#input variable
customer_name = input('Enter your name: ')
cashierName = 'John Doe'
#Menu options
print('Howdy!', customer_name)
print('Liswanaires pizza is the best in town. Choose your order!')
menu()

menu_option = int(input('>>> Enter your option number here: '))


#choose toppings
print('(0_0) MMMMMM good choice', customer_name,)
toppings = input('Would you live some toppings? [y/n]')
if toppings == 'y':
    print('')
    print('Please Enter your Choice')
    print('')


elif toppings == 'n':
    print('OK!')
else:
    print('Invalid Option')

logicBlock(menu_option,customer_name,cashierName)

print('+--------------------------------------------------------------------+')
print('+              Thank you ', '>>' ,customer_name, '<<', '! Come back again')
print('+--------------------------------------------------------------------+')

exit = input('Press enter to exit')
sys.exit()

#End of Program

