#각 클래스의 객체 생성 및 게임 진행
from card import Card
from player import Player
from gamedealer import GameDealer


def play_game():
    # 두명의 player 객체 생성
    player1 = Player("흥부")
    player2 = Player("놀부")

    dealer = GameDealer()    
    dealer.make_deck()
    dealer.print_deck()
    dealer.card_shuffle()
    
    players = [player1, player2]
    dealer.first_provide_cards(players)

    while True:
        player1.check_one_pair_card()
        player1.display_two_card_lists()

        player2.check_one_pair_card()
        player2.display_two_card_lists()

        if len(dealer.deck) == 0:
            print('[GameDealer] 딜러가 가진 카드 수: 0')
            break
        
        if len(player1.holding_card_list) == 0 or len(player2.holding_card_list) == 0:
            if len(player1.holding_card_list) ==0:
                print(f'{player1.name} 승리')
            if len(player2.holding_card_list) ==0:
                print(f'{player2.name} 승리')
            break

        dealer.four_provide_cards(players)

        if len(player1.holding_card_list) == 0 or len(player2.holding_card_list) == 0:
            if len(player1.holding_card_list) ==0:
                print(f'{player1.name} 승리')
            if len(player2.holding_card_list) ==0:
                print(f'{player2.name} 승리')
            break


if __name__ == '__main__':
    play_game()