class Person():
    def __init__(self, full_name='', birthyear=''):
        self.full_name = full_name
        # try:
        self.birthyear = int(birthyear)
        # except int(birthyear) > 2019 or int(birthyear) < 1900 :
        #     raise ''

    def name_only(self):
        probel_index = self.full_name.find(' ')
        return self.full_name[:probel_index]
    def lastname_only(self):
        probel_index = self.full_name.find(' ')
        return self.full_name[probel_index+1:]
    def age_in(self,year=2019):
        return year - self.birthyear
    def __str__(self):
        return"{} {}".format(self.__class__, self.full_name)


if __name__ == '__main__':
    Igor = Person('Igor Kalynovskyi', 1987)
    print(Igor.name_only())
    print(Igor.lastname_only())
    print(Igor.age_in(2050))
    print(Igor.age_in())
    print(Igor)
