import random
import math


class player:
    Deck =[]
    user_hand = {}
    hand_size = 10
    count_play = 5
    count_discard = 5
    chosen_cards = []
    play_hand = []
    discardList = []
    def __init__(self, name, count_play, count_discard):
        self.name = name
        self.count_play = count_play
        self.count_discard = count_discard 
        generate_cards()    

    

def generate_cards():
    suits = ["D", "C", "H", "S"]  
    ranks = ["Ace"] + [f"{i:02}" for i in range(2, 11)] + ["Jack", "Queen", "King"]
    player.Deck = [f"{suit}.{rank}" for suit in suits for rank in ranks]
    
def game_start():
    print('카드를 뽑습니다.', end =' ')
    i = 0
    while len(player.user_hand) < player.hand_size:
        player.user_hand[i] = player.Deck.pop(random.randint(0,len(player.Deck)-1))
        i += 1
    print(f'남은 카드 {len(player.Deck)}장')
        
def replenish_card():
    print('카드를 보충합니다.', end =' ')
    i = 0
    while len(player.user_hand) < player.hand_size:
        if i not in player.user_hand.keys():
            player.user_hand[i] = player.Deck.pop(random.randint(0,len(player.Deck)-1))
        i += 1
    player.user_hand = dict(sorted(player.user_hand.items()))
    print(f'남은 카드 {len(player.Deck)}장')
    
hand_type = ['High Card', 'Pair', 'Two Pair', 'Three of a Kind', 'Straight', 'Flush', 'Full House','Four of a Kind', 'Straight Flush']
score =     [(5,1),(10,2),(30,3),(30,4),(35,4),(40,4),(60,7),(100,8)]


def check_hand_type(play_hand):
    suits = ["D", "C", "H", "S"]  
    ranks = [f"{i:02}" for i in range(1, 14)]
    calc_suits = {key:0 for key in suits}
    calc_ranks = {key:0 for key in ranks}
    calc_hand = []
    calc_hand_type = 0
    
    for i in play_hand:
        if 'Ace' in i:
            i = i.replace('Ace', '01')
        elif 'Jack' in i:
            i = i.replace('Jack', '11')
        elif 'Queen' in i:
            i = i.replace('Queen', '12')
        elif 'King' in i:
            i = i.replace('King', '13')
        calc_hand.append(i.split('.'))
    
    # for i in range(len(calc_hand)):
    #     if 'Ace' in i:
    #         i.replace('Ace', '01')
    #     elif 'Jack' in i:
    #         i.replace('Jack', '11')
    #     elif 'Queen' in i:
    #         i.replace('Queen', '12')
    #     elif 'King' in i:
    #         i.replace('King', '13')
            
    print(calc_hand, len(calc_hand),'계산용 핸드')
    print(calc_suits)
    print(calc_ranks)
    for i in calc_hand:
        calc_suits[i[0]] +=1
        calc_ranks[i[1]] +=1
     
     
    if len(calc_hand) == 5: 
        check_straight()
    #플러시체크
    elif 5 in calc_suits.values():
        if check_straight() == 'Straight':
            calc_hand_type = 'Straight Flush'
        else:
            calc_hand_type = 'Flush'
    print(calc_suits)
    print(calc_ranks)
    if 4 in calc_ranks:
        calc_hand_type = 'Four of a Kind'
    elif 3 in calc_ranks:
        if 2 in calc_ranks:
            calc_hand_type = 'Full House'    
        else:
            calc_hand_type = 'Three of a Kind'
    elif list(calc_ranks.values()).count(2) == 2:
        calc_hand_type = 'Twop Pair'
    elif list(calc_ranks.values()).count(2) == 1:
        calc_hand_type = 'Pair'
    else:
        calc_hand_type = 'High Card'
    return calc_hand, calc_hand_type
        
    #포커/트리플/페어체크
    
    #스트레이트체크 values로
def check_straight():
    check_straight =[]
    straight_count = 0
    for i in range(5):
        check_straight.append(calc_hand[i][1])
        check_straight.sort()
    for i in range(4,0,-1):
        if check_straight == ['01', '10', '11', '12', '13']:
            straight_count = 4
        elif check_straight[i] == check_straight[i-1]+1:
            straight_count += 1
    if straight_count == 4:
        calc_hand_type = 'Straight'
        return calc_hand_type
            
        
# 점수 계산
def calcScore(hand_type):
    
    return
def color_card_dict(dict):
    values1 = list(dict.values())
    keys1 = list(dict.keys())
    color_card(values1,keys1)
    
def color_card(*args):
    for i in range(len(args[0])):
        if len(args) == 2:
         print(f"\033[37;40m {args[1][i]}:\033[0m" ,end ='')
        if 'D' in args[0][i]:
            print(f"\033[37;45m {args[0][i][:2]}\033[0m",end ='')
        elif 'H' in args[0][i]:
            print(f"\033[37;41m {args[0][i][:2]}\033[0m",end ='')
        elif 'C' in args[0][i]:
            print(f"\033[37;44m {args[0][i][:2]}\033[0m",end ='')
        elif 'S' in args[0][i]:
            print(f"\033[30;47m {args[0][i][:2]}\033[0m",end ='')
        print(f"\033[37;40m {args[0][i][2:]} \033[0m", end =' ')
        if i == len(args[0]):
            print(',', end =' ')   
    print()        

# 카드 선택.
def card_choose():
    print('-'*20)
    # print(player.user_hand,'이거')
    color_card_dict(player.user_hand)
    print('-'*20)
    choose_cardNum = list(input('카드인덱스(최대5):').strip())
    for i in choose_cardNum:
        player.chosen_cards.append(player.user_hand[int(i)])
    exit_sign = 1
    while exit_sign:
        color_card(player.chosen_cards)
        # print(player.chosen_cards, '저거')
        selectPD = input("0: 플레이 / 1: 버리기 /2: 취소 ").strip()
        if not selectPD or selectPD not in '012':
            print('잘못된 입력입니다.')
        elif selectPD == '2':       #취소
            player.chosen_cards.clear()
            print('취소하셨습니다.')
            return card_choose()
        
        elif selectPD == '1':       #버리기
            if player.count_discard == 0:
                return card_choose()
            else:
                exit_sign = 0
                player.count_discard -= 1
                print(f"{player.chosen_cards}를 버렸습니다.")
                for i in choose_cardNum:
                    del player.user_hand[int(i)]
                player.chosen_cards.clear()
                replenish_card()
                return card_choose()
        
        elif selectPD == '0':       #플레이
            if player.count_play == 0:
                return card_choose()
            else:
                exit_sign = 0
                player.count_play -= 1
                print(check_hand_type(player.chosen_cards))
                
                for i in choose_cardNum:
                    del player.user_hand[int(i)]
                player.chosen_cards.clear()
                replenish_card()
                return card_choose()
            


exlist = ['H.Jack', 'C.07', 'H.10', 'S.King', 'H.07']

