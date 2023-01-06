class Verification:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__lenPassword()

    def __lenPassword(self):
        if len(self.password) < 8:
            raise ValueError('shot paroltext')

    def save(self):
        with open('user', 'a') as r:
            r.write(f'{self.login, self.password}' + '\n')
            