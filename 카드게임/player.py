# 자신이 가지고있는 카드 관리 (holding_card_list, open_card_list)
# 두 장의 동일한 카드를 제거하는 기능 (번호가 동일할경우 ,holding_card_list에서 open_card_list로 이동)
class Player:
    def __init__(self, name):
        self.name = name
        self.holding_card_list = list()
        self.open_card_list = list()

        
    def add_card_list(self, card_list):
        self.holding_card_list.extend(card_list) 

    def display_two_card_lists(self):
        print(f"[{self.name}] Open card list: {len(self.open_card_list)}")
        for card in self.open_card_list:
            print(card, end=' ')
        print()
        print()

        print(f"[{self.name}] Holding card list: {len(self.holding_card_list)}")
        for card in self.holding_card_list:
            print(card, end=' ')
        print()

    def check_one_pair_card(self):
        print('-'*80)
        print('-'*80)        
        print(f"[{self.name}: 숫자가 같은 한쌍의 카드 검사]")
        print('-'*80)
        print('-'*80)
        number_count = {}

        for card in self.holding_card_list:
            number = card.number
            if number in number_count:
                number_count[number].append(card)
            else:
                number_count[number] = [card]
        
        for number, cards in number_count.items():
            if len(cards) >=2: #원페어이상일때
                self.open_card_list.extend(cards[:2])
                for card in cards[:2]:
                    self.holding_card_list.remove(card)
                        

