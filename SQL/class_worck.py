from class_test import Verification
from tkinter import Tk, Button

class V2(Verification):

    def __init__(self, login, password, age):
        super().__init__(login, password)
        self.__save()
        self.age = age

    def __save(self):
        with open('user') as r:
            for i in r:
                if f'{self.login, self.password}' + '\n' == i:
                    raise ValueError('user is done')
        super().save()

    def show(self):
        return self.login, self.password

x = V2('jhff', '1239876513', 35)

# class My_app(Tk):
#
#     def __init__(self):
#         Tk.__init__(self)
#         self.geometry('400x400')
#         self.setUI()
#
#     def setUI(self):
#         Button(self, text='OK').pack()
#
# root = My_app()
# root.mainloop()


