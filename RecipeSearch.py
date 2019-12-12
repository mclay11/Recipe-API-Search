'''
INST326 Final Project
Recipe Puppy API Search
http://www.recipepuppy.com/about/api/
'''

#import libraries so there is no need to manually add query strings to URLs
import requests
import json

#create function to retrieve data from the api
def get(url):
    url = 'http://www.recipepuppy.com/api/' + url
    data = requests.get(url).json()
    return data['results']


#creates function which is run immediately as the program is executed
def main():


    print(' _____           _               _____                     _     ')
    print('|  __ \         (_)             / ____|                   | |    ')
    print('| |__) |___  ___ _ _ __   ___  | (___   ___  __ _ _ __ ___| |__  ')
    print('|  _  // _ \/ __| | \'_ \ / _ \  \___ \ / _ \/ _` | \'__/ __| \'_ \ ')
    print('| | \ \  __/ (__| | |_) |  __/  ____) |  __/ (_| | | | (__| | | |')
    print('|_|  \_\___|\___|_| .__/ \___| |_____/ \___|\__,_|_|  \___|_| |_|')
    print('                  | |                                            ')
    print('                  |_|                                            ')

    print(' ')
    print('Input ingredients here, type "done" when you are ready to search.')

    #allows user to input the ingredient(s) they want to search for
    ingredient_list = []
    while True:
        user_input = input()
        if user_input == 'done':
            break
        ingredient_list.append(user_input)

    print(' ')
    print('You searched for ' + ', '.join(ingredient_list))
    print(' ')

	#returns url that contains search results in json formatting
    ingredient_urls = []

    for ingredient in ingredient_list:
        ingredient_urls.append(ingredient + '%2C+')

    ingredient_urls = ''.join(ingredient_urls)

    #initiate a counter to keep track of number of results
    counter = 0

    #for each result, prints recipe title, ingredients, and url
    for response in get('?i='+ ingredient_urls + '&q='):
        counter += 1
        print('***********************************************************************************************************')
        print(' ')
        print('Recipe Name: ' , response['title'].strip())
        print('All Ingredients: ' , response['ingredients'])
        print('Link to Full Recipe: ' , response['href'])
        print(' ')
    print('***********************************************************************************************************')

    #if zero results were found, the program will state so
    if counter == 0:
        print('Sorry, no results were found')

    print(' ')
    input('Press ENTER to exit')


if __name__ == '__main__':
    main()
