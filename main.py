# Получение название ножа через json файл
from tkinter.messagebox import NO
from bs4 import BeautifulSoup
import requests
import json
from fake_useragent import UserAgent
ua = UserAgent()


# url = f'https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=40&isStore=true&limit=60&maxPrice=10000&minPrice=67.99838327043936&offset={offset}&type=2&withStack=true'
# r = requests.get(url)

result = []
def get_data(type_weapon = 2):
    operation = 0
    batch_size = 60
    offset = 0
    while True:    
        for i in range(offset,offset + batch_size , 60):
            print(f"Page/{operation}")
            url = f'https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=40&isStore=true&limit=60&maxPrice=10000&minPrice=67.99838327043936&offset={i}&type={type_weapon}&withStack=true'
            headers = {'User-Agent': ua.random}
            r = requests.get(url, headers=headers)
            data = r.json()
            count = data.get('items')
            offset += batch_size
            for a in count:
                if a.get('overprice') is not None and a.get('overprice') < -10:
                    name = a.get('fullName')
                    price = a.get('price')
                    overprice = a.get('overprice')
                    link = a.get('3d')
                    result.append({'name': name,
                    'price': price,
                    'overprice': overprice,
                    'link': link})
                else:
                    continue
            operation += 1
        if len(count)<60:
            break
    print(len(result))
    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)



def main():
    get_data()


if '__main__' == __name__:
    main()
    
    