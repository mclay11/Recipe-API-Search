'''
INST326 Final Project
Recipe Puppy API
http://www.recipepuppy.com/about/api/

'''
import requests
import json

def get(url):
    headers = {'X-API-KEY' : ''}
    url = 'http://www.recipepuppy.com/api/' + url
    data = requests.get(url, headers = headers).json()
    return data['results']

print('Input ingredients here')
ingredient_list = []
while True:
    user_input = input()
    if user_input == 'done':
        break
    ingredient_list.append(user_input)

print(ingredient_list)

ingredient_urls = []

for ingredient in ingredient_list:
    ingredient_urls.append(ingredient + '%2C+')

ingredient_urls = ''.join(ingredient_urls)

for response in get('?i='+ ingredient_urls + '&q='):
    print(response['title'])
    print(response['ingredients'])
    print(response['href'])
