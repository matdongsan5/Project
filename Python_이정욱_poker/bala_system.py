import random
import math
import bala_player

class System:
    
    def generate_cards(self, Player):
        suits = ["D", "C", "H", "S"]  
        ranks = ["Ace"] + [f"{i:02}" for i in range(2, 11)] + ["Jack", "Queen", "King"]
        Player.Deck = [f"{suit}.{rank}" for suit in suits for rank in ranks]
    
    def check_hand_type(self, Player):
        suits = ["D", "C", "H", "S"]  
        ranks = [f"{i:02}" for i in range(1, 14)]
        calc_suits = {key:0 for key in suits}
        calc_ranks = {key:0 for key in ranks}
        Player.calc_hand = []
        Player.calc_hand_type = 0
        # Player.calc_hand_type = 0
        
        for i in Player.play_hand:
            if 'Ace' in i:
                i = i.replace('Ace', '01')
            elif 'Jack' in i:
                i = i.replace('Jack', '11')
            elif 'Queen' in i:
                i = i.replace('Queen', '12')
            elif 'King' in i:
                i = i.replace('King', '13')
            Player.calc_hand.append(i.split('.'))
            
        hand_type = ['High Card', 'Pair', 'Two Pair', 'Three of a Kind', 'Straight', 'Flush', 'Full House','Four of a Kind', 'Straight Flush']
        hand_score =     [(5,1),(10,2),(30,3),(30,4),(35,4),(40,4),(60,7),(100,8)]
        calcScore_dict = dict(zip(hand_type,hand_score))    
                
        # print(Player.calc_hand, len(Player.calc_hand),'계산용 핸드')
        # print(calc_suits)
        # print(calc_ranks)
        for i in Player.calc_hand:
            calc_suits[i[0]] +=1
            calc_ranks[i[1]] +=1
        
        # print(calc_suits)
        # print(calc_ranks)
        # print(5 in calc_suits.values(), len(Player.calc_hand) == 5)
        
        if check_straight():
            Player.calc_hand_type = 'Straight'
        # print('이거')
        #플러시체크
        elif 5 in calc_suits.values():
            if check_straight():
                Player.calc_hand_type = 'Straight Flush'
            else:
                Player.calc_hand_type = 'Flush'
        elif 3 in calc_ranks.values() and 2 in calc_ranks.values():
            Player.calc_hand_type = 'Full House' 
                
        elif 4 in calc_ranks.values():
            Player.calc_hand_type = 'Four of a Kind'
        elif 3 in calc_ranks.values():
            # print('요거')
            if 2 in calc_ranks.values():
                Player.calc_hand_type = 'Full House'    
            else:
                Player.calc_hand_type = 'Three of a Kind'
        elif list(calc_ranks.values()).count(2) == 2:
            Player.calc_hand_type = 'Twop Pair'
        elif list(calc_ranks.values()).count(2) == 1:
            Player.calc_hand_type = 'Pair'
        else:
            Player.calc_hand_type = 'High Card'
        # print(Player.calc_hand_type)
        current_score = calc_score(calc_ranks, Player.calc_hand_type)
        Player.end_score += current_score
        # Player.end_score += score  
        return Player.calc_hand, Player.calc_hand_type, current_score
            
        #포커/트리플/페어체크
        
        #스트레이트체크 values로
    def check_straight():
        check_straight =[]
        straight_count = 0
        for i in range(5):
            check_straight.append(Player.calc_hand[i][1])
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
    def calc_score(calc_ranks,calc_hand_type):
        chips = 0
        score = 0
        if calc_hand_type == 'Pair':

        #pair

            key = {key for key, value in calc_ranks.items() if value == 2}
            key = list(key)
            if key[0] in 'AceJackQueenKing':
                chips = int(key[0])*10
            else:
                chips = int(key[0])*calc_ranks[key[0]]
            score = (chips+10)*2
            

    #two pair
        if calc_hand_type == 'Twop Pair':
            key = {key for key, value in calc_ranks.items() if value == 2}
            key = list(key)
            for i in range(2):        
                if key[i] in 'AceJackQueenKing':
                    chips += (10*calc_ranks[key[i]])
                else:
                    chips += (int(key[i])*calc_ranks[key[i]])
            score = (chips+20)*2
            

        #triple
        if calc_hand_type == 'Three of a Kind' :
            key = {key for key, value in calc_ranks.items() if value == 3}
            key = list(key)
                
            if key[0] in 'AceJackQueenKing':
                chips += 10*calc_ranks[key[0]]
            else:
                chips += int(key[0])*calc_ranks[key[0]]
            score = (chips+30)*3
            

        #fullhouse
        if calc_hand_type == 'Full House' :
            key = {key for key, value in calc_ranks.items() if value in [3, 2]}
            key = list(key)
            for i in range(2):        
                if key[i] in 'AceJackQueenKing':
                    chips += 10*calc_ranks[key[i]]
                else:
                    chips += int(key[i])*calc_ranks[key[i]]
            score = (chips+40)*4



        #four
        if calc_hand_type == 'Four of a Kind':
            key = {key for key, value in calc_ranks.items() if value == 4}
            key = list(key)
            if key[0] in 'AceJackQueenKing':
                    chips += 10*calc_ranks[key[0]]
            else:
                    chips += int(key[0])*calc_ranks[key[0]]
            score = (chips+60)*7  
        

        #straight
        if calc_hand_type == 'Straight':
            key = {key for key, value in calc_ranks.items()}
            key = list(key)
            for i in range(5):        
                if key[i] in 'AceJackQueenKing':
                    chips += 10
                else:
                    chips += int(key[i])
                
                    
            score = (chips+30)*4

        #flush
        if calc_hand_type == 'Flush':
            key = {key for key, value in calc_ranks.items()}
            key = list(key)
            for i in range(5):        
                if key[i] in 'AceJackQueenKing':
                    chips += 10
                else:
                    chips += int(key[i])
            score = (chips+35)*4
            

        #stf
        if calc_hand_type == 'Straight Flush':
            key = {key for key, value in calc_ranks.items()}
            key = list(key)
            for i in range(5):        
                if key[i] in 'AceJackQueenKing':
                    chips += 10
                else:
                    chips += int(key[i])
            score = (chips+100)*8
            

        return score


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