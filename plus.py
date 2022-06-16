def podkl(self):
    a = input('Login pls:')
    b = input('Porol pls:')
    if a == self.l and b == self.p:
        return self.hello()

    else:
        while a != self.l and b != self.p:
            return print(f'ne pravilno povtarite \n{self.podkl()}')
