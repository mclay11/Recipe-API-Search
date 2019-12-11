'''
INST326 Final Project
Recipe Puppy API
http://www.recipepuppy.com/about/api/

'''
import requests
import json

def get(url):
    url = 'http://www.recipepuppy.com/api/' + url
    data = requests.get(url).json()
    return data['results']

def main():

    print('******** WELCOME TO RECIPE SEARCH ********')

    print('Input ingredients here, type "done" when you are ready to search.')
    ingredient_list = []
    while True:
        user_input = input()
        if user_input == 'done':
            break
        ingredient_list.append(user_input)

    print('You searched for ' + str(ingredient_list))

    ingredient_urls = []

    for ingredient in ingredient_list:
        ingredient_urls.append(ingredient + '%2C+')

    ingredient_urls = ''.join(ingredient_urls)

    for response in get('?i='+ ingredient_urls + '&q='):
        print('Recipe Name: ' , response['title'])
        print('All Ingredients: ' , response['ingredients'])
        print('Link to Full Recipe: ' , response['href'])
        print('**************************************************************************************************')

    input('Press ENTER to exit')

if __name__ == '__main__':
    main()
