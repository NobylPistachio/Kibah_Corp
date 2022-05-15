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

    
## test_items:

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
list_test.append(item_1)
list_test.append(item_2)
list_test.append(item_3)
list_test.append(item_4)
list_test.append(item_5)
list_test.append(item_6)
list_test.append(item_7)
list_test.append(item_8)
list_test.append(item_9)
list_test.append(item_10)

for n in range(len(list_test)):
    for stat in list_test[n].stats:
        DATA_TYPES[stat] += list_test[n].stats[stat]
print(DATA_TYPES)




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
    
#items[id][description]
#items[id][gold]
#items[id][tags]
#items[id][stats]

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
    pass
