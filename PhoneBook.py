from Abonent import Abonent

class PhoneBook:
    def __init__(self):
        self.abonents: list[Abonent] = []

    def read_from_txt(self, file_name: str):
        file = open(file_name, 'r')
        file_content = file.readlines()
        for i in range(0, len(file_content), Abonent.records_number+1):
            second_name = file_content[i][:len(file_content[i])-1]
            first_name = file_content[i+1][:len(file_content[i+1])-1]
            third_name = file_content[i+2][:len(file_content[i+2])-1]
            organization_name = file_content[i+3][:len(file_content[i+3])-1]
            work_number = file_content[i+4][:len(file_content[i+4])-1]
            personal_number = file_content[i+5][:len(file_content[i+5])-1]
            delimiter = file_content[i+6]
            abonent = Abonent(second_name, first_name, third_name, organization_name, work_number, personal_number)
            self.abonents.append(abonent)
        file.close()
            
    def print_book(self):
        for a in self.abonents:
            print(a)

    def add_abonent(self, file_name:str):
            second_name = input('Input the second name: ')
            first_name = input('Input the first name: ')
            third_name = input('Input the third name: ')
            organization_name = input('Input organization name: ')
            work_number = input('Input work number: ')
            personal_number = input('Input personal number: ')
            abonent = Abonent(second_name, first_name, third_name, organization_name, work_number, personal_number)
            self.abonents.append(abonent)
            abonent.write_in_txt(file_name)

    def find_by_FIO(self, second_name:str, first_name:str, third_name:str)->Abonent:
         for a in self.abonents:
              if a.second_name == second_name and a.first_name == first_name and a.third_name == third_name:
                   return a
         return None

    def redact(self, file_name:str, second_name: str, first_name: str, third_name: str):
         founded = False
         for a in self.abonents:
            if a.second_name == second_name and a.first_name == first_name and a.third_name == third_name:
                founded = True
                second_name = input('Input the second name: ')
                first_name = input('Input the first name: ')
                third_name = input('Input the third name: ')
                organization_name = input('Input organization name: ')
                work_number = input('Input work number: ')
                personal_number = input('Input personal number: ')
                a.second_name = second_name
                a.first_name = first_name
                a.third_name = third_name
                a.organization_name = organization_name
                a.work_number = work_number
                a.personal_number = personal_number
                file = open(file_name, 'w')
                for a in self.abonents:
                     a.write_in_txt(file_name)
                file.close()
         if not founded:
            print('There is no such abonents.')
        
         

pb = PhoneBook()
pb.read_from_txt('input.txt')
print(pb.find_by_FIO('Kolesnikova', 'Anastasia', 'Igorevna'))
pb.redact('input.txt', 'Kolesnikova', 'Anastasia', 'Igorevna')
pb.print_book()
pb.read_from_txt('input.txt')


