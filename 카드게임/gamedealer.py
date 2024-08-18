# 1벌의 카드(deck) 생성 기능: 리스트로 구현
# 각 player들에게 카드를 나누어 주는 기능 => 자신이 가진 deck에서 제거하여 다른 선수들에게 제공

from card import Card
import random
from player import Player

class GameDealer:

    def __init__(self):
        self.deck = list()
        self.suit_number = 13

    def make_deck(self):
        print('[GameDealer] 초기 카드 생성')
        card_suits = ["♠","♥","♣","◆"]
        card_numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for suit in card_suits:
            for number in card_numbers:
                self.deck.append(Card(suit, number)) # card 객체 생성
    
    def print_deck(self):
        print(f'-'*80)
        print(f'[GameDealer] 딜러가 가진 카드 수: {len(self.deck)}')
        for i, card in enumerate(self.deck):
            print(card, end=' ')
            if (i + 1) % 13 == 0:  # 13개 카드를 출력한 후에 줄바꿈
                print()
        print()

    def card_shuffle(self):
        print('[GameDealer] 카드 랜덤하게 섞기')
        random.shuffle(self.deck)
        self.print_deck()

    def first_provide_cards(self, players):
        for player in players:
            dealt_cards = [self.deck.pop() for _ in range(10)]  # 각 플레이어에게 10장씩 나눠줌
            player.add_card_list(dealt_cards)
    
    def four_provide_cards(self, players):
        print(f'-'*80)
        print('카드 나누어 주기: 4장')
        for player in players:
            dealt_cards = [self.deck.pop() for _ in range(4)]  # 각 플레이어에게 4장씩 나눠줌
            player.add_card_list(dealt_cards)
        self.print_deck()

# if __name__ == '__main__':
#     dealer = GameDealer()
#     dealer.make_deck()
#     dealer.print_deck()
#     dealer.card_shuffle()

#     player1 = Player('흥부')
#     player2 = Player('놀부')

#     players = [player1, player2]
#     dealer.first_provide_cards(players)
#     player1.display_two_card_lists()
#     player2.display_two_card_lists()    

#     while True:

#         player1.check_one_pair_card()
#         player1.display_two_card_lists()

#         player2.check_one_pair_card()
#         player2.display_two_card_lists()

#         if len(dealer.deck) == 0:
#             print('[GameDealer] 딜러가 가진 카드 수: 0')
#             break
        
#         if len(player1.holding_card_list) == 0 or len(player2.holding_card_list) == 0:
#             if len(player1.holding_card_list) ==0:
#                 print(f'{player1.name} 승리')
#             if len(player2.holding_card_list) ==0:
#                 print(f'{player2.name} 승리')
#             break
#         dealer.four_provide_cards(players)
