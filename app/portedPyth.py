#! usr/bin/env python3
from datetime import date
import requests

'Initial declaration of the current date, along with a friendly greeting'

currentDate = date.today()
textDate = currentDate.strftime("%B %d, %Y")
print("Well Hello There!\nThe current date is " + textDate)



'Having the user enter their name'

print("Enter your name:")
def userName():
    return input()
usrNm = userName()
print("The user's name is " + usrNm)



'Having the user enter their name'

print("Enter your age:")
def declareAge():
    return int(input())
ageFunc = declareAge()
print("Your age is: " + str(ageFunc))


'Rewarding the user for a job well done'

def shibeImage():
    print("Thanks for cooperating, would you like a shibe? Please \nrespond with Yes or No, I'm not advanced enough to understand other phrases :^(")
    shibeInput = input()
    'supposed to parse input and match it to either Yes or No'

    if shibeInput == "Yes": 
        
        '''supposed to simply call on shibe.online and get a url link to an image, with
        exceptions for a failed request'''
        
        try:
            imageGet = requests.get("http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true", timeout=10)
            ethaJson = imageGet.json() if imageGet.status_code == 200 else None
            print("Here you go! :^)\n" + str(ethaJson))
        except requests.exceptions.RequestException:
            print("Ooohh.... sorry... no shibe today :/")
    
    'if user originally answered no, no picture and program immediately ceases'
    
    if shibeInput == "No":
        print("Why,.. not..,.? ',:)")
shibeImage()
