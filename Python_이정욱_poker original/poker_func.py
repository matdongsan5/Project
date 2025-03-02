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
            print(f"\033[97;40m {args[0][i][:2]}\033[0m",end ='')
        print(f"\033[30;47m {args[0][i][2:]} \033[0m", end =' ')
        if i == 4:
            print()
        if i == len(args[0]):
            print(',', end =' ')   
    print()        
# ♣️ ♠️ ♦️ ♥️
# 카드 선택.
def card_choose():
    
    print('-'*20)
    # print(player.user_hand,'이거')
    color_card_dict(player.user_hand)
    print('-'*20)
    sorted_type = input('정렬 타입(0:종류, 1:숫자, 2:넘어가기)):').strip()
    if sorted_type == 'quit':
        quit()
    if not sorted_type or sorted_type not in '012' or len(sorted_type) != 1:
        print('잘못된 입력입니다.')
        return card_choose()
    elif sorted_type == '0':
        player.user_hand=sorted_by_suit(player.user_hand)
        return card_choose()
    elif sorted_type == '1':
        player.user_hand=sorted_by_ranks(player.user_hand)
        return card_choose()
    else:
        choose_cardNum = list(input('카드인덱스(최대5):').strip())
        print('-'*20)
        if choose_cardNum == 'quit':
          quit()
        if not choose_cardNum or len(set(choose_cardNum)) != len(choose_cardNum):
                print('잘못된 입력입니다.')
                return card_choose()
        for i in choose_cardNum:
            player.chosen_cards.append(player.user_hand[int(i)])
        exit_sign = 1
        while exit_sign:
            color_card(player.chosen_cards)
            # print(player.chosen_cards, '저거')
            print('플레이 회수 [{0}] / 버리기 회수 [{1}]'.format(player.count_play, player.count_discard))
            selectPD = input("0: 플레이 / 1: 버리기 /2: 취소 ").strip()
            print('-'*20)
            if selectPD == 'quit':
                quit()
            if not selectPD or selectPD not in '012':
                print('잘못된 입력입니다.')
            elif selectPD == '2':       #취소
                player.chosen_cards.clear()
                print('취소하셨습니다.')
                return card_choose()
            
            elif selectPD == '1':       #버리기
                if player.count_discard == 0:
                    print('더 이상 버릴 수 없습니다.')
                    return card_choose()
                else:
                    exit_sign = 0
                    player.count_discard -= 1
                    print(f"선택된 카드를 버립니다.")
                    color_card(player.chosen_cards)
                    for i in choose_cardNum:
                        del player.user_hand[int(i)]
                    player.chosen_cards.clear()
                    replenish_card()
                    return card_choose()
            
            elif selectPD == '0':       #플레이
                
                    exit_sign = 0
                    player.count_play -= 1
                    
                    pht_pcc = check_hand_type(player.chosen_cards)
                    # print(pht_pcc, '점')
                    show_play = []
                    for i in pht_pcc[0]:
                        if i[1] == '01':
                            show_play.append(f"{i[0]}.{'Ace'}")
                        elif i[1] == '11':
                            show_play.append(f"{i[0]}.{'Jack'}")
                        elif i[1] == '12':
                            show_play.append(f"{i[0]}.{'Queen'}")
                        elif i[1] == '13':
                            show_play.append(f"{i[0]}.{'King'}")
                        else:
                            show_play.append(f"{i[0]}.{i[1]}")
                    color_card(show_play)
                    print('-'*20)
                    print("{0}, {1}점입니다.".format(pht_pcc[1],pht_pcc[2]))
                    print("총점 {} 입니다.".format(player.end_score))
                    print('-'*20)
                    for i in choose_cardNum:
                        del player.user_hand[int(i)]
                    player.chosen_cards.clear()
                    
                    if player.count_play == 0:
                        break
                
                    replenish_card()
                    return card_choose()


exlist = ['H.Jack', 'C.07', 'H.10', 'S.King', 'H.07']
name = 'james'
james = player('james', 3,5)
# print(player.Deck)
game_start()

card_choose()

end()