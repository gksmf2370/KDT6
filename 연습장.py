class Bugger:

    def __init__(self, bread, patty, veg, kind):
        self.bread=bread
        self.patty=patty
        self.veg=veg
        self.kind=kind

    def printInfo(self):
        print(f'브랜드 : {self.kind}')
        print(f'빵종류 : {self.bread}')
        print(f'패 티: {self.patty}')
        print(f'야 채: {self.veg}')

Bugger1=Bugger('브리오슈', '불고기', '양상추 양파 토마토', '롯데리아')

Bugger2=Bugger('참깨빵', '불고기', '양상추 양파 토마토 치즈', '맥도날드')

Bugger1.printInfo()
Bugger2.printInfo()