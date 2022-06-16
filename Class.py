from plus import podkl
class Vkbot:
    bot_name = 'vkbot'
    def __init__(self, login, porol):
        self.l = login
        self.p = porol
class Vkbot1(Vkbot):
    def hello(self):
        print(f'''Hello!
Eto {self.bot_name} i my prodaem telefoni''')
        return self.info()
    def pod(self):
        return podkl(self)

    def info(self):
        print('''1) Iphone 
2) Samsung
3) Redmi''')
        q = input('Viberi odno:')
        if q == '1':
            return self.iphone()
        elif q == '2':
            return self.samsung()
        elif q == '3':
            return self.redmi()
    def iphone(self):
        print('''1)Iphone 11 --- 300000tg
2)Iphone 12 --- 360000tg
3)Iphone 13 --- 450000tg
esli hotite nazad napishite 0''')
        iphon = input('CHto hotite priobresti?\n-')
        if iphon == '1':
            print('Otlichno s vas 300000')
            p = input('hotite chtoto eshe?')
            if p == 'da' or 'Da':
                return self.iphone()
            elif p == 'net':
                print('Poka')
        elif iphon == '2':
            print('kruto s vas 360000')
            p = input('hotite chtoto eshe?')
            if p == 'da' or 'Da':
                return self.iphone()
            elif p == 'net':
                print('Poka')
            else:
                print('nee znay chto skazat')
                return self.iphone()
        elif iphon == '3':
            print('horosho s vas 450000')
            p = input('hotite chtoto eshe?')
            if p == 'da' or 'Da':
                return self.iphone()
            elif p == 'net':
                print('Poka')
            else:
                print('nee znay chto skazat')
                return self.iphone()
        elif iphon == '0':
            return self.info()

    def samsung(self):
        print('''1) SAmsung s20 --- 280000
2)samsung s21 --- 370000
3)samsung s21 ultra --- 450000
esli hotite nazad napishite 0''')
        r = input('Chto hotite priobresti?\n- ')
        if r == '1':
            print('s vas 280000')
            p = input('hotite chtoto eshe?')
            if p == 'da' or 'Da':
                return self.iphone()
            elif p == 'net':
                print('Poka')
            else:
                print('nee znay chto skazat')
                return self.iphone()
        elif r == '2':
            print('s vas 370000 telephone horoshi')
            p = input('hotite chtoto eshe?')
            if p == 'da' or 'Da':
                return self.iphone()
            elif p == 'net':
                print('Poka')
            else:
                print('nee znay chto skazat')
                return self.iphone()
        elif r == '3':
            print('s vas 450000 telephone otlichny')
            p = input('hotite chtoto eshe?')
            if p == 'da' or 'Da':
                return self.iphone()
            elif p == 'net':
                print('Poka')
            else:
                print('nee znay chto skazat')
                return self.iphone()
        elif r == '0':
            return self.info()

    def redmi(self):
        print('''1) Redmi note 9 --- 90000
2)redmi note 10 --- 110000
3)redmi note 11 --- 140000
esli hotite nazad napishite 0''')
        d = input('CHTO HOTITE PRIOBRESTI?\n- ')
        if d == '1':
            print('TELEPHONE horoshi s vas 90000tg')
            p = input('hotite chtoto eshe?')
            if p == 'da' or 'Da':
                return self.iphone()
            elif p == 'net':
                print('Poka')
            else:
                print('nee znay chto skazat')
                return self.iphone()
        if d == '2':
            print('telephone otlichni s vas 110000tg')
            p = input('hotite chtoto eshe?')
            if p == 'da' or 'Da':
                return self.iphone()
            elif p == 'net':
                print('Poka')
            else:
                print('nee znay chto skazat')
                return self.iphone()
        if d == '3':
            print('Horosho s vas 140000tg')
            p = input('hotite chtoto eshe?')
            if p == 'da' or 'Da':
                return self.iphone()
            elif p == 'net':
                print('Poka')
            else:
                print(f'nee znay chto skazat {self.redmi}')

        if d == '0':
            return self.info()
s = Vkbot1('mahmud2007','mahmud07')
s.pod()


