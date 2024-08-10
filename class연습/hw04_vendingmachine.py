class VendingMachine:
    def __init__(self, input_dict):



        self.input_money = 0
        self.inventory = input_dict
    def run(self):
        
        self.input_money = int(input("동전을 투입하세요: "))
        self.refund = self.input_money
        if self.input_money <300:
            print(f'투입된 돈 ({self.input_money}이 300원보다 작습니다.)')
        else:
            while(True):
                self.show_menu()
                menu = input('메뉴를 선택하세요: ')

                if menu == 1:
                    self.check_inventory('black_cof')
                    self.update_inventory('black_cof')
                elif menu == 2:
                    self.check_inventory('cream_cof')
                    self.update_inventory('cream_cof')
                elif menu == 3:
                    self.check_inventory('sugar_cof')
                    self.update_inventory('sugar_cof')
                elif menu == 4:
                    self.print_inventory()
                elif menu == 5:
                    break

        self.refun()
        self.stop_machine()


    def show_menu(self):
            print('--------------------------------')
            print(f'  커피 자판기 (잔액:{self.input_money}원)')
            print('--------------------------------')
            print(f'1. 블랙 커피')       
            print(f'2. 프림 커피')
            print(f'3. 설탕 커피')
            print(f'4. 재료현황')
            print(f'5. 종료')


    def stop_machine(self):
        print('--------------------------------')
        print(f'  커피 자판기 동작을 종료합니다.')
        print('--------------------------------')

    def refun(self):
        print(f'{self.refund}원을 반환합니다.')         
    
    # 재료현황 업데이트
    def update_inventory(self, coffetype):
        coffe = {'black_cof' : {'coffe':30 ,'water': 100, 'cup':1},
                 'cream_cof' : {'coffe':15, 'cream':15, 'water': 100, 'cup':1},
                 'sugar_cof' : {'coffe': 10, 'cream':10, 'sugar':10, 'water':100, 'cup': 1}, 
                }
        need = coffe[coffetype]

        for item, amount in need.items():
            self.inventory[item] -= amount

    # 커피 제공 가능 확인 기능
    def check_inventory(self, coffetype):
        coffe = {'black_cof' : {'coffe':30 ,'water': 100, 'cup':1},
                 'cream_cof' : {'coffe':15, 'cream':15, 'water': 100, 'cup':1},
                 'sugar_cof' : {'coffe': 10, 'cream':10, 'sugar':10, 'water':100, 'cup': 1},
                }
        need = coffe[coffetype]

        for item, amount in need.items():
            if self.inventory[item] < amount:
                print(f'재료 부족: {item}이 부족합니다.')
    # 재료 현황 출력
    def print_inventory(self):
        print(f'재료 현황:',end=' ')
        for item, amount in self.inventory.items():
            print(f'{item}: {amount}', end=' ')


inventory_dict = {'coffe': 100, 'cream': 100, 'sugar': 100, 'water': 500, 'cup': 5, 'change': 0}
coffe_machine = VendingMachine(inventory_dict)
coffe_machine.run()
