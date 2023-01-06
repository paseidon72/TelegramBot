
class Purse:

    def __init__(self, valuta, name='Unknown'):
        if valuta not in ('USD', 'EURO'):
            raise ValueError
        self.__money = 0.00
        self.valuta = valuta
        self.name = name

    def top_up_balance(self, howmany):
        self.__money = self.__money + howmany
        return howmany

    def top_doun_balance(self, howmany):
        if self.__money - howmany <= 0:
            print('no money is check')
            raise ValueError('no money is check')
        self.__money = self.__money - howmany
        return howmany

    def info(self):
        print(self.__money)

    def __del__(self):
        print('wallet is delete')


x = Purse('USD')
y = Purse('USD', 'Bill')
y.top_up_balance(200)
x.top_up_balance(y.top_doun_balance(25))
x.info()
y.info()



















