from cmath import e

phone_numbers = [{'name': 'amal', 'number': 1111111111}, {'name': 'Mohammed', 'number': 2222222222},
                 {'name': 'Khadijah', 'number': 3333333333}, {'name': 'Abdullah', 'number': 4444444444},
                 {'name': 'Rawan', 'number': 5555555555}, {'name': 'Faisal', 'number': 6666666666},
                 {'name': 'Layla', 'number': 7777777777}]


def search_num():
    num_input = input('Enter the number:')
    if len(num_input) != 10:
        print('this is invalid number')
    else:
        found = False
    for ph in phone_numbers:
        if num_input == str(ph['number']):
            found = True
            print(ph['name'])


    if found == False:
        print('sorry ,the number is not found')


def search_by_name():
    name_input = input('wwho want to call')
    for n in phone_numbers:
        if name_input == n['name']:
            print(n['number'])

def add_contact():
    new_name= input('enter new name')
    new_number= input('enter new number')
    phone_numbers.append({'name': new_name, 'number': new_number})


search_num()
search_by_name()
add_contact()
print(phone_numbers)
