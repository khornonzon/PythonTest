from PhoneBook import PhoneBook

def print_menu():
    print('1. Print from txt\n2. Add new abonent\n3. Redact by FIO\n4. Find by FIO\n5. Exit\n')


pb = PhoneBook()

while (True):
    print_menu()
    decision = input()
    if decision=='1':
        file_name = input('Input the file name: ')
        pb.read_from_txt(file_name)
        pb.print_book()
    if decision=='2':
        file_name = input('Input the file name: ')
        pb.add_abonent(file_name)
    if decision=='3':
        file_name = input('Input the file name: ')
        second_name = input('Input the second name: ')
        first_name = input('Input the first name: ')
        third_name = input('Input the third name: ')
        pb.redact(file_name, second_name, first_name, third_name)
    if decision=='4':
        second_name = input('Input the second name: ')
        first_name = input('Input the first name: ')
        third_name = input('Input the third name: ')
        abonent = pb.find_by_FIO(second_name, first_name, third_name)
        if abonent:
            print(abonent)
        else: print('There is no such abonents\n')
        
    if decision=='5':
        break
    