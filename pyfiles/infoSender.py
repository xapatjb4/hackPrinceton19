from dotenv import load_dotenv
load_dotenv()
from geopy.geocoders import Nominatim
import geocoder
import os
from lib import lib
lib = lib(token = os.getenv("token"))

#params string path, 
#list contactList which is an array of tuples containing name and number both strings
def makeContactList(path, contactList):
    file1 = open("contacts.txt","w")#write mode
    for contact in contactList:
        name, number = contact
        file1.write("{},{}\n".format(name,number))
    print("Contact list made")

# def getContactList(path):




#paramas string path,
#int opt to determine 
#whether to send message saying batterie is low keep an eye out
#whether to send location if battery below 10 %
def messageContactList(path, opt):
    if opt <= 50:
        pass
    pass

def batbel50(user):
    print("why no send?")
    name,email = user
    subject = "Good vibrations battery life"
    text = "Hey {}, please be aware that your good vibration batteries are at or below 50%. Consider charging soon".format(name)
    print(text)
    sendEmail(email,subject,text)

def batbel25(users):
    tempUsers = users.copy()
    name, email = tempUsers[0]
    tempUsers.pop(0)
    subject = "Notifying emergency contacts"
    text = "Hey {}, you're batteries are at or below 25%, we've notified these contacts about the situation: ".format(name)
    for user in tempUsers[:-1]:
        contName,contEmail = user
        #send the email out to user
        contSubject = "Good vibration battery notifications"
        contText = "Hello {}, it look like {}'s glass batteries are running below 25%! We'll let you know if they're close to dying".format(contName,name)
        sendEmail(contEmail,contSubject,contText)
        print(contName)
        text+=contName+", "
    contName,contEmail = tempUsers[-1]
    #send the email out to user
    contSubject = "Good vibration battery notifications"
    contText = "Hello {}, it look like {}'s glass batteries are running below 25%! We'll let you know if they're close to dying".format(contName,name)
    sendEmail(contEmail,contSubject,contText)
    print(contName)
    text+=contName+". "
    print(text)
    sendEmail(email,subject,text) 
    pass

def batbel10(users):
    tempUsers = users.copy()
    #Send information about geolocation
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    g = geocoder.ip('me')
    location = geolocator.reverse(g.latlng)
    print(location.address)
    name, email = tempUsers[0]
    tempUsers.pop(0)
    print(name)
    subject = "Sharing location with emergency contacts"
    text = "Hey {}, you're batteries are at or below 10%, we've sent your location to the following contacts: ".format(name)
    for user in tempUsers[:-1]:
        contName,contEmail = user
        #send the email out to user
        contSubject = "Good vibration battery notifications"
        contText = "Hello {}, it look like {}'s glass batteries are running below 10%! Since he may get lost without his glasses, here is his location: {}".format(contName,name,location.address)
        sendEmail(contEmail,contSubject,contText)
        print(contName)
        text+=contName+", "
    contName,contEmail = tempUsers[-1]
    #send the email out to user
    contSubject = "Good vibration battery notifications"
    contText = "Hello {}, it look like {}'s glass batteries are running below 10%! Since he may get lost without his glasses, here is his location: {}".format(contName,name,location.address)
    sendEmail(contEmail,contSubject,contText)
    print(contName)
    text+=contName+". "
    print(text)
    sendEmail(email,subject,text) 


def notifyWearer():
    email = '7743121987@txt.att.net'
    subject = 'What\'s up'
    text = 'Thaaaat\'s a bitch'
    sendEmail(email,subject,text)
    pass

def sendEmail(email,subject,text):
    lib.waduphaitian.batnotif["@dev"].email(email = email, subject = subject,text = text)

arr = [("Xavier","5089816164@txt.att.net"),("Andy","7743121987@txt.att.net"),("Brother","7034014577@messaging.sprintpcs.com")]#,("Nouki","5168081284@tmomail.net"),
makeContactList("output.txt",arr)

while True:
    option = input("Enter scenario: ")
    print(type(option))

    try:
        #result = lib.waduphaitian.batnotif["@dev"](name='Dolores Abernathy')
        #notifyWearer()
        #batbel50(arr[0])
        if(option == '1'):
            print("got to 1")
            batbel50(arr[0])
        elif(option == '2'):
            batbel25(arr)
        elif(option == '3'):
            batbel10(arr)

    except RuntimeError as err:
        # handle error
        print(err)
#print(result)

