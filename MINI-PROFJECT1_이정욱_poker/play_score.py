
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
    
    
    # print(num_casting_list)
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