class Abonent:
    records_number = 6
    def __init__(self, second_name: str ="", first_name: str='', third_name:str='',
                  organization_name: str='', work_number:str ='', personal_number:str =''):
        self.second_name = second_name
        self.first_name = first_name
        self.third_name = third_name
        self.organization_name = organization_name
        self.work_number = work_number
        self.personal_number = personal_number

    def write_in_txt(self, file_name):
        file = open(file_name, 'a')
        file.writelines([self.second_name, '\n',
                         self.first_name,'\n', self.third_name,'\n', 
                         self.organization_name, '\n',self.work_number,'\n', self.personal_number, '\n\n'])
        file.close()
    def __str__(self):
        return self.second_name  + '\n' + self.first_name + '\n' + self.third_name +'\n' + self.organization_name  +'\n' +  self.work_number + '\n' +self.personal_number + '\n\n' 
     