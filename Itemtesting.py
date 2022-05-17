import json
file = open('items.json')
data = json.load(file)
items = data['data']
##print(data.keys())
TAGS = []
LEAGUE_ITEMS = {}

##im thinking of making 1 central dictionary but maybe it should be a dictionary comprehension of the json file
counter = 0

##for a in items:
##    print(len(items[a]))




def item_search():
    user = input('What Item ID do you want to look at? If you need the keys type keys\npress ENTER to exit ')
    while user != '':
        if user in items.keys():
            present(user)
        elif user == 'keys':
            #be able to present them with a name of the item
            for a in items:
                print(a+' - '+items[a]['name'])
            print()                
            #print(items.keys())
        else:
            print('\terror: bad item key')
        user = input('What Item ID do you want to look at? If you need the keys type keys\npress ENTER to exit ')
def present(num):
    item_id = num
    print(f"{'id':<12}{item_id}")
    for category in items[item_id]:
            print(f"\t{category:<12}{type(items[item_id][category])}\n\t\t{items[item_id][category]}")

class Item:
    """This is supposed to replace the json file so
       it would be easier to access"""
    
    def __init__(self,name,ID,description,gold,tags,stats):
        self.name = name
        self.id = ID
        self.description = description
        self.gold = gold
        self.tags = tags
        self.stats = stats


#Data_counter
DATA_TYPES = {}            
for a in items:
    for b in range(len(items[a]['stats'])):
        for c in items[a]['stats']:           
            if c not in DATA_TYPES:
                DATA_TYPES[c] = 0     
#print(DATA_TYPES)

##def items_maker():
##    for ID in items:
##         = Item(items[ID]['name'],
##                    ID,
##                    items[ID]['description'],
##                    items[ID]['gold'],
##                    items[ID]['tags'],
##                    items[ID]['stats'])
##        LEAGUE_ITEMS[item.name] = item
##    print(LEAGUE_ITEMS)


    
def test_items():

    item_1 = Item(items['3748']['name'],
                  3748,
                  items['3748']['description'],
                  items['3748']['gold'],
                  items['3748']['tags'],
                  items['3748']['stats'])
    item_2 = Item(items['6632']['name'],
                  6632,
                  items['6632']['description'],
                  items['6632']['gold'],
                  items['6632']['tags'],
                  items['6632']['stats'])
    item_3 = Item(items['3047']['name'],
                  3047,
                  items['3047']['description'],
                  items['3047']['gold'],
                  items['3047']['tags'],
                  items['3047']['stats'])
    item_4 = Item(items['3742']['name'],
                  3742,
                  items['3742']['description'],
                  items['3742']['gold'],
                  items['3742']['tags'],
                  items['3742']['stats'])
    item_5 = Item(items['4401']['name'],
                  4401,
                  items['4401']['description'],
                  items['4401']['gold'],
                  items['4401']['tags'],
                  items['4401']['stats'])
    item_6 = Item(items['3075']['name'],
                  3075,
                  items['3075']['description'],
                  items['3075']['gold'],
                  items['3075']['tags'],
                  items['3075']['stats'])
    item_7 = Item(items['3143']['name'],
                  3143,
                  items['3143']['description'],
                  items['3143']['gold'],
                  items['3143']['tags'],
                  items['3143']['stats'])
    item_8 = Item(items['3026']['name'],
                  3026,
                  items['3026']['description'],
                  items['3026']['gold'],
                  items['3026']['tags'],
                  items['3026']['stats'])
    item_9 = Item(items['1039']['name'],
                  1039,
                  items['1039']['description'],
                  items['1039']['gold'],
                  items['1039']['tags'],
                  items['1039']['stats'])
    item_10 = Item(items['3089']['name'],
                  3089,
                  items['3089']['description'],
                  items['3089']['gold'],
                  items['3089']['tags'],
                  items['3089']['stats'])
    #--------------------------------------------

    #adding test_items objects to a list
    list_test = []
    add = list_test.append
    list_test.append(item_1.id)
    list_test.append(item_2.id)
    list_test.append(item_3.id)
    list_test.append(item_4.id)
    list_test.append(item_5.id)
    list_test.append(item_6.id)
    list_test.append(item_7.id)
    list_test.append(item_8.id)
    list_test.append(item_9.id)
    list_test.append(item_10.id)


#summing up the stats
##for n in range(len(list_test)):
##    for stat in list_test[n].stats:
##        DATA_TYPES[stat] += list_test[n].stats[stat]
    #part 2

def Stat_Sum(list_of_items):
    #Stat_Sum() should be given a list of item ids,

    #taken from above, dont know if I need to reset the list every time I use Stat_Sum()
    for data in DATA_TYPES:
        DATA_TYPES[data] = 0

    #if given a list of ids this will add them up
    for ID in list_of_items:
        item = items[str(ID)]
        for stat in item['stats']:
            DATA_TYPES[stat] += item['stats'][stat]
            
    #gives back a dict like this
##            {'FlatMovementSpeedMod': 0,
##            'FlatHPPoolMod': 0,
##            'FlatCritChanceMod': 0,
##            'FlatMagicDamageMod': 0,
##            'FlatMPPoolMod': 0,
##            'FlatArmorMod': 0,
##            'FlatSpellBlockMod': 0,
##            'FlatPhysicalDamageMod': 0,
##            'PercentAttackSpeedMod': 0,
##            'PercentLifeStealMod': 0,
##            'FlatHPRegenMod': 0,
##            'PercentMovementSpeedMod': 0.1}
            
    return DATA_TYPES
        
    
    
    
    
    
    



        #a way to present my test items
##print(f'''{item_1.name:^25}\t{type(item_1.stats)}\n{item_1.stats}\n
##{item_2.name:^25}\n{item_2.stats}\n
##{item_3.name:^25}\n{item_3.stats}\n
##{item_4.name:^25}\n{item_4.stats}\n
##{item_5.name:^25}\n{item_5.stats}\n
##{item_6.name:^25}\n{item_6.stats}\n
##{item_7.name:^25}\n{item_7.stats}\n
##{item_8.name:^25}\n{item_8.stats}\n
##{item_9.name:^25}\n{item_9.stats}\n
##{item_10.name:^25}\n{item_10.stats}\n
##          ''')
        #how to break down the items 
#items[id][description]
#items[id][gold]
#items[id][tags]
#items[id][stats]
        #another way to break down items
 #items[####][
##for a in items:
##    for b in items[a]:
##        if counter < 10:
##            print(type(items[a][b]))
##            print(items[a][b])
##            counter += 1
        

        #makes the TAGS list
##for a in items:
##    for b in range(len(items[a]['tags'])):
##        if items[a]['tags'][b] not in TAGS:
##            TAGS.append(items[a]['tags'][b])


                
##        print(items[a]['stats'])
##        print()


            #this gives an item
#print(items['1001'])

if __name__ == '__main__':
    list_test = [3748,6632,3047,3742,4401,3075,3143,3026,1039,3089]
    print(Stat_Sum(list_test))
    
