import random
import math

class Player:
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
    
    
    def draw_card(self):        
        print('카드를 뽑습니다.', end =' ')
        i = 0
        while len(self.user_hand) < self.hand_size:
            self.user_hand[i] = self.Deck.pop(random.randint(0,len(self.Deck)-1))
            i += 1
        print(f'남은 카드 {len(self.Deck)}장')
        
    def replenish_card(self):
        if len(self.Deck):
            print('카드를 보충합니다.', end =' ')
            i = 0
            while len(self.user_hand) < self.hand_size:
                if len(self.Deck):
                    if i not in self.user_hand.keys():
                        self.user_hand[i] = self.Deck.pop(random.randint(0,len(self.Deck)-1))
                    i += 1
                else: 
                    print(f"남은 카드가 없습니다.")
                    break
            self.user_hand = dict(sorted(self.user_hand.items()))
            print(f'남은 카드 {len(self.Deck)}장')
        else:
            print(f"남은 카드가 없습니다.")



def sorted_by_suit(dict1):
    new_dict={}
    new_dict = dict(zip(sorted(dict1.keys()), sorted(dict1.values())))
    # print(list(dict1.keys()))
    # print(new_dict,'newdict1')
    # dict1 = dict(zip(sorted(dict1.keys()), sorted(dict1.values())))
    dict1.clear()
    dict1.update(new_dict)
    return dict1


def sorted_by_ranks(dict1):
    new_dict={}
    # print(dict1)
    sorted_ranks = {}
    num_casting_list = list(dict1.values())
    for i in range(len(num_casting_list)):
        if 'Ace' in num_casting_list[i]:
            num_casting_list[i] = num_casting_list[i].replace('Ace', '01')
        elif 'Jack' in num_casting_list[i]:
            num_casting_list[i] = num_casting_list[i].replace('Jack', '11')
        elif 'Queen' in num_casting_list[i]:
            num_casting_list[i] = num_casting_list[i].replace('Queen', '12')
        elif 'King' in num_casting_list[i]:
            num_casting_list[i] = num_casting_list[i].replace('King', '13')
    
    dict1 = dict(zip(dict1.keys(),num_casting_list))
    # print(dict1)
    
    for i in dict1:
        sorted_ranks[i] = dict1[i].split('.')[1]+'.'+dict1[i].split('.')[0]
    # print(sorted_ranks)    
    dict1 = dict(zip(sorted(dict1.keys()), sorted(sorted_ranks.values())))
    for i in dict1:
        new_dict[i] = dict1[i].split('.')[1]+'.'+dict1[i].split('.')[0]    
        
    for i in range(len(new_dict)):
        if '01' in new_dict[i]:
            new_dict[i] = new_dict[i].replace('01', 'Ace')
        elif '11' in new_dict[i]:
            new_dict[i] = new_dict[i].replace('11', 'Jack')
        elif '12' in new_dict[i]:
            new_dict[i] = new_dict[i].replace('12', 'Queen')
        elif '13' in new_dict[i]:
            new_dict[i] = new_dict[i].replace('13', 'King')
            
    # print(new_dict,'newdict2')
    dict1.clear()
    dict1.update(new_dict)
    return dict1
            
def card_choose(self):
    print('-'*20)
    # print(player.user_hand,'이거')
    # color_card_dict(player.user_hand)
    print('-'*20)
    sorted_type = input('정렬 타입(0:종류, 1:숫자, 2:넘어가기)):').strip()
    if sorted_type == 'quit':
        quit()
    if not sorted_type or sorted_type not in '012' or len(sorted_type) != 1:
        print('잘못된 입력입니다.')
        return card_choose()
    elif sorted_type == '0':
        self.user_hand=sorted_by_suit(self.user_hand)
        return card_choose()
    elif sorted_type == '1':
        self.user_hand=sorted_by_ranks(self.user_hand)
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
            self.chosen_cards.append(self.user_hand[int(i)])
        exit_sign = 1
        while exit_sign:
            # color_card(self.chosen_cards)
            # print(self.chosen_cards, '저거')
            print('플레이 회수 [{0}] / 버리기 회수 [{1}]'.format(self.count_play, self.count_discard))
            selectPD = input("0: 플레이 / 1: 버리기 /2: 취소 ").strip()
            print('-'*20)
            if selectPD == 'quit':
                quit()
            if not selectPD or selectPD not in '012':
                print('잘못된 입력입니다.')
            elif selectPD == '2':       #취소
                self.chosen_cards.clear()
                print('취소하셨습니다.')
                return card_choose()
            
            elif selectPD == '1':       #버리기
                if self.count_discard == 0:
                    print('더 이상 버릴 수 없습니다.')
                    return card_choose()
                else:
                    exit_sign = 0
                    self.count_discard -= 1
                    print(f"선택된 카드를 버립니다.")
                    # color_card(self.chosen_cards)
                    for i in choose_cardNum:
                        del self.user_hand[int(i)]
                    self.chosen_cards.clear()
                    self.replenish_card()
                    return card_choose()
            
            elif selectPD == '0':       #플레이
                
                    exit_sign = 0
                    self.count_play -= 1
                    
                    pht_pcc = self.check_hand_type(self.chosen_cards)
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
                    # color_card(show_play)
                    print('-'*20)
                    print("{0}, {1}점입니다.".format(pht_pcc[1],pht_pcc[2]))
                    print("총점 {} 입니다.".format(self.end_score))
                    print('-'*20)
                    for i in choose_cardNum:
                        del self.user_hand[int(i)]
                    self.chosen_cards.clear()
                    
                    if self.count_play == 0:
                        break
                
                    self.replenish_card()
                    return card_choose()