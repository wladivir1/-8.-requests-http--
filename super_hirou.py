import requests
import json


 
def superhero_api():
    """Получает содержимое по API"""
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    hero_dict = json.loads(requests.get(url).content)
    
    return hero_dict

def max_hero_power(hero_dict):
    """Выводит максимальное значение силы героя"""
    heroes_list = ['Hulk', 'Captain America', 'Thanos']
    intelligence_dict = dict()
    
    for line in hero_dict:
        for name in heroes_list:
            if name == line['name']:               
                intelligence_dict[line['name']] = line['powerstats']['intelligence']

    max_key = max(intelligence_dict, key=intelligence_dict.get)             
    print(f'Самый умный: {max_key}')        

def main():
    max_hero_power(superhero_api())
    
        
if __name__ == '__main__':
    main()
       