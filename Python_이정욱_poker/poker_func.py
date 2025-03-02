import random
import math
import play_score
from play_score import *

class player:
    Deck =[]
    user_hand = {}
    hand_size = 10
    count_play = 5
    count_discard = 5
    chosen_cards = []
    play_hand = []
    discardList = []
    calc_hand = []
    calc_hand_type = 0
    end_score = 0
    def __init__(self, name, count_play, count_discard):
        self.name = name
        self.count_play = count_play
        self.count_discard = count_discard 
        generate_cards()    

    

    
def game_start():        
    print('카드를 뽑습니다.', end =' ')
    i = 0
    while len(player.user_hand) < player.hand_size:
        player.user_hand[i] = player.Deck.pop(random.randint(0,len(player.Deck)-1))
        i += 1
    print(f'남은 카드 {len(player.Deck)}장')
        
def replenish_card():
    if len(player.Deck):
        print('카드를 보충합니다.', end =' ')
        i = 0
        while len(player.user_hand) < player.hand_size:
            if len(player.Deck):
                if i not in player.user_hand.keys():
                    player.user_hand[i] = player.Deck.pop(random.randint(0,len(player.Deck)-1))
                i += 1
            else: 
                print(f"남은 카드가 없습니다.")
                break
        player.user_hand = dict(sorted(player.user_hand.items()))
        print(f'남은 카드 {len(player.Deck)}장')
    else:
        print(f"남은 카드가 없습니다.")
    
def check_hand_type(play_hand):
    suits = ["D", "C", "H", "S"]  
    ranks = [f"{i:02}" for i in range(1, 14)]
    calc_suits = {key:0 for key in suits}
    calc_ranks = {key:0 for key in ranks}
    player.calc_hand = []
    player.calc_hand_type = 0
    # player.calc_hand_type = 0
    
    for i in play_hand:
        if 'Ace' in i:
            i = i.replace('Ace', '01')
        elif 'Jack' in i:
            i = i.replace('Jack', '11')
        elif 'Queen' in i:
            i = i.replace('Queen', '12')
        elif 'King' in i:
            i = i.replace('King', '13')
        player.calc_hand.append(i.split('.'))
        
    hand_type = ['High Card', 'Pair', 'Two Pair', 'Three of a Kind', 'Straight', 'Flush', 'Full House','Four of a Kind', 'Straight Flush']
    hand_score =     [(5,1),(10,2),(30,3),(30,4),(35,4),(40,4),(60,7),(100,8)]
    calcScore_dict = dict(zip(hand_type,hand_score))    
            
    # print(player.calc_hand, len(player.calc_hand),'계산용 핸드')
    # print(calc_suits)
    # print(calc_ranks)
    for i in player.calc_hand:
        calc_suits[i[0]] +=1
        calc_ranks[i[1]] +=1
     
    # print(calc_suits)
    # print(calc_ranks)
    # print(5 in calc_suits.values(), len(player.calc_hand) == 5)
    
    if check_straight():
        player.calc_hand_type = 'Straight'
    # print('이거')
    #플러시체크
    elif 5 in calc_suits.values():
        if check_straight():
            player.calc_hand_type = 'Straight Flush'
        else:
            player.calc_hand_type = 'Flush'
    elif 3 in calc_ranks.values() and 2 in calc_ranks.values():
        player.calc_hand_type = 'Full House' 
            
    elif 4 in calc_ranks.values():
        player.calc_hand_type = 'Four of a Kind'
    elif 3 in calc_ranks.values():
        # print('요거')
        if 2 in calc_ranks.values():
            player.calc_hand_type = 'Full House'    
        else:
            player.calc_hand_type = 'Three of a Kind'
    elif list(calc_ranks.values()).count(2) == 2:
        player.calc_hand_type = 'Twop Pair'
    elif list(calc_ranks.values()).count(2) == 1:
        player.calc_hand_type = 'Pair'
    else:
        player.calc_hand_type = 'High Card'
    # print(player.calc_hand_type)
    current_score = calc_score(calc_ranks, player.calc_hand_type)
    player.end_score += current_score
    # player.end_score += score  
    return player.calc_hand, player.calc_hand_type, current_score
        
    #포커/트리플/페어체크
    
    #스트레이트체크 values로
def check_straight():
    check_straight =[]
    straight_count = 0
    for i in range(5):
        check_straight.append(player.calc_hand[i][1])
        check_straight.sort()
    # print(check_straight)
    for i in range(len(check_straight)-1):
        if check_straight == ['01', '10', '11', '12', '13']:
            straight_count = 4
        elif int(check_straight[i]) == int(check_straight[i+1])-1:
            straight_count += 1
    if straight_count == 4:
        # player.calc_hand_type = 'Straight'
        return True        
    else:
        return False
        
            
        
# 점수 계산 player.calc_hand, player.calc_hand_type
# 족보의 숫자 5,4,3,2,1 순서에 따라 하나씩 처리
def calcScore(*args):


    # args[0] =  player.calc_hand
    # args[1] = player.calc_hand_type
    return

def end():
    print('끝났습니다.')
    print('최종점수 {0}점 입니다'.format(player.end_score))
    pass


# ♣️ ♠️ ♦️ ♥️
# 카드 선택.



exlist = ['H.Jack', 'C.07', 'H.10', 'S.King', 'H.07']
name = 'james'
james = player('james', 3,5)
# print(player.Deck)
game_start()

card_choose()

end()