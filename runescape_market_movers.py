from bs4 import BeautifulSoup as bs
import requests



def main():
    websites = ['https://secure.runescape.com/m=itemdb_rs/top100?list=2&scale=0',
                'https://secure.runescape.com/m=itemdb_rs/top100?list=3&scale=0',
                'https://secure.runescape.com/m=itemdb_rs/top100?list=1&scale=0',
                'https://secure.runescape.com/m=itemdb_rs/top100?list=0k&scale=0']
    pages = {'3':'0k','2':'1','0':'2','1':'3'}
    user = input('Hello, Do you want the Top 100 Price Rises, Price Falls, Valuable Trades, or Most Traded?\n0 - Price Rises\n1 - Price Falls\n2 - Valuable Trades\n3 - Most Traded\n\t')
    while int(user) > 3 or int(user) < 0:
        print('sorry, please pick a number from the list')
        user = input('0 - Price Rises\n1 - Price Falls\n2 - Valuable Trades\n3 - Most Traded\n\t')
    
    get_top_100(pages[user])
    user = input('would you like another list? y/n ')
    if user == 'y':
        user = input('0 - Price Rises\n1 - Price Falls\n2 - Valuable Trades\n3 - Most Traded\n\t')
        while int(user) > 3 or int(user) < 0:
            print('sorry, please pick a number from the list')
            user = input('0 - Price Rises\n1 - Price Falls\n2 - Valuable Trades\n3 - Most Traded\n\t')
    else:
        input('Thank you for using this program, press anything to close')

def get_top_100(page):
    website = (f'https://secure.runescape.com/m=itemdb_rs/top100?list={page}&scale=0')
    test = requests.get(website).text
    soup = bs(test, 'lxml')
    Top100 = []
    #there is only one tbody in the website, that holds all the info we need
    tbody = soup.find('tbody')
    #each line is <tr> in the HTML code, we need all the lines
    tr = tbody.find_all('tr')
    #there are 6 boxes <td> on each line we need name, total rise, and Change
    for line in range(len(tr)):
        td = tr[line].find_all('td')
        item_name = ((td[0].text).strip())
        Top100.append({'name':((td[0].text).strip()),
                  'start price':(td[2].text),
                  'end price':(td[3].text),
                  'total rise':(td[4].text),
                  'change':(td[5].text)
                  })
    print('---------------------------------------------------------------------------')
    print(f'{"Name":<30}{"Start Price":<14}{"End Price":<12}{"Total Rise":<13}{"Change":<9}')
    for line in range(len(Top100)):
        print(f"{Top100[line]['name']:<30}{Top100[line]['start price']:<14}{Top100[line]['end price']:<12}{Top100[line]['total rise']:<13}{Top100[line]['change']:<9}")

if __name__ == '__main__':
    main()
