from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException, NoSuchWindowException, NoSuchElementException
import os
import time
import sys
import json
import urllib.request
import shutil
import platform
import getpass
import string
loggedIn = False
oneQuiz = False
osSelected = False
noJSON = False
pageIDChoosen = False
bulletMaker = 0
osis = 0
# 0 = Mac, 1 = Windows, 2 = Linux
directory = os.getcwd()
platform = platform.system()
if (platform == "darwin"):
    osis = 0
if (platform == "win32"):
    osis = 1
if (platform == "linux" or platform == "linux32"):
    osis = 2
if not os.path.exists(directory+"/"+"info.json"):
    f= open("info.json","w+")
    f.close()
    noJSON = True
if noJSON == True:
    pageID = "ns"
    successes = 0
    failures = 0
    path = "ns"
    username = "ns"
    password = "ns"
    recover = {"pageID": "ns", "successes": 0, "failures": 0, "path": "ns", "username": "ns", "password": "ns"}
    with open ('info.json', 'r+') as myfile:
        recover=myfile.write(json.dumps(recover))
with open ('info.json', 'r') as myfile:
    info=json.loads(myfile.read())
def save(info, pageID1, successes1, failures1, path1, username1, password1):
    info["pageID"] = pageID1
    info["successes"] = successes1
    info["failures"] = failures1
    info["path"] = path1
    info["username"] = username1
    info["password"] = password1
    with open ('info.json', 'r+') as myfile:
        info=myfile.write(json.dumps(info))
pageID = info["pageID"]
successes = info["successes"]
failures = info["failures"]
path = info["path"]
username = info["username"]
password = info["password"]
checkedforchrome = False
if not os.path.exists(path):
    path = "ns"
    save(info, pageID, successes, failures, path, username, password)
def reset():
    os.remove("info.json")
    sys.exit()
def count_letters(word):
    return len(word) - word.count(' ')
if path == "ns":
    if (osis == 1):
        my_file = directory+"/"+"chromedriver.exe"
    else:
        my_file = directory+"/"+"chromedriver"
    if os.path.exists(my_file):
        path = my_file
        save(info, pageID, successes, failures, path, username, password)
if (path == "ns"):
    while (checkedforchrome == False):
        checkedforchrome = True
        chromecheck = input('Have you installed ChromeDriver (Y or N)? >>> ')
        if (chromecheck == "y" or chromecheck == "Y"):
            path = input("The path to chromedriver is: >>> ")
            if not os.path.exists(path):
                print("Invalid Path!")
                checkedforchrome = False
            else:
                save(info, pageID, successes, failures, path, username, password)
                print("Continuing...")

        if (not chromecheck == "Y" and not chromecheck == "y" and not chromecheck == "N" and not chromecheck == "n"):
            print("Invalid Option...Restarting...")
            checkedforchrome = False

        if (chromecheck == "n" or chromecheck == "N"):
            chromeinstalled = input("Would you like the script to install it for you (Y or N)? >>> ")
            if (chromeinstalled == "y" or chromeinstalled == "Y"):
                while (osSelected == False):
                    osSelected = True
                    useros = input("What OS are you on (W for Windows, M for Mac, L64 for 64 bit Linux, and L32 for 32 bit Linux)? >>> ")
                    print("Downloading...")
                    if (useros == "w" or useros == "W"):
                        downloadurl = "https://chromedriver.storage.googleapis.com/2.29/chromedriver_win32.zip"
                        file_name = "chromedriver_win32.zip"
                    if (useros == "m" or useros == "M"):
                        downloadurl = "https://chromedriver.storage.googleapis.com/2.29/chromedriver_mac64.zip"
                        file_name = "chromedriver_mac64.zip"
                    if (useros == "l64" or useros == "L64"):
                        downloadurl = "https://chromedriver.storage.googleapis.com/2.29/chromedriver_linux64.zip"
                        file_name = "chromedriver_linux64.zip"
                    if (useros == "l32" or useros == "L32"):
                        downloadurl = "https://chromedriver.storage.googleapis.com/2.29/chromedriver_linux32.zip"
                        file_name = "chromedriver_linux32.zip"
                    if (not useros == "w" and not useros == "W" and not useros == "m" and not useros == "M" and not useros == "l64" and not useros == "L64" and not useros == "l32" and not useros == "L32"):
                        print("Invalid Option. Restarting...")
                        time.sleep(0.5)
                        osSelected = False
                    with urllib.request.urlopen(downloadurl) as response, open(file_name, 'wb') as out_file:
                        shutil.copyfileobj(response, out_file)
                    print("Downloaded! Please unzip the file and restart the script.")
                    time.sleep(1)
                    sys.exit()
            if (chromeinstalled == "n" or chromeinstalled == "N"):
                    print("Goodbye!")
                    sys.exit()
if (username == "ns" and password == "ns"):
        reply = input('Would you like to have the script enter your username and password for you (Y or N)? >>> ')
        if (reply == "n" or reply == "N"):
            username = "dw"
            password = "dw"
        if (reply == "Y" or reply == "y"):
            print("None of this data is transmitted, it is just saved for ease of use on your local machine.")
            username = input("Email: >>> ")
            password = getpass.getpass("Password: >>> ")
        save(info, pageID, successes, failures, path, username, password)
        print("Thank you!")
print("INFO: Only close the browser, not the script or terminal")
runTypeSelected = False
while runTypeSelected == False:
    runTypeSelected = True
    passwordcount = count_letters(password)
    passwordhidden = "blank"
    while(not bulletMaker == passwordcount):
        if passwordhidden == "blank":
            passwordhidden = "•"
        else:
            passwordhidden = passwordhidden + "•"
        bulletMaker = bulletMaker + 1
    bulletMaker = 0
    print("Type in an option: Start, Settings, Read Data, Reset Data, Quit")
    time.sleep(0.1)
    runTypeInput = input("I choose: >>> ")
    time.sleep(0.1)
    runTypeInput = runTypeInput.upper()
    if runTypeInput == "START":
        chooseRunType = input("Would you like to do multiple quizes (Y or N)? >>> ")
        if (chooseRunType == "y" or chooseRunType == "Y"):
            if pageID == "ns":
                print("https://quizlet.com/0<---PageID/micromatch")
                while pageIDChoosen == False:
                    pageIDChoosen = True
                    pageID = input("What pageID would you like to start from (Please type in an integer)? >>> ")
                    try:
                        pageID = int(pageID)
                        save(info, pageID, successes, failures, path, username, password)
                    except ValueError:
                        pageIDChoosen = False
            oneQuiz = False
        if (chooseRunType == "n" or chooseRunType == "N"):
            if pageID == "ns":
                print("https://quizlet.com/0<---PageID/micromatch")
                pageIDChoosen = False
                while pageIDChoosen == False:
                    pageIDChoosen = True
                    pageID = input("What pageID would you like the bot to run on (Please type in an integer)? >>> ")
                    try:
                        pageID = int(pageID)
                        save(info, pageID, successes, failures, path, username, password)
                    except ValueError:
                        pageIDChoosen = False
                oneQuiz = True
    if runTypeInput == "SETTINGS":
        doneChanging = False
        while doneChanging == False:
            save(info, pageID, successes, failures, path, username, password)
            whattochange = input("Type P to change the PageID, Type PA to change the path to ChromeDriver, Type E to change the email, Type PAS to change the password, or type Q to exit. >>> ")
            whattochange = whattochange.upper()
            if whattochange == "P":
                if pageID == "ns":
                    print("PageID has not been set.")
                else:
                    print("PageID is set to:", pageID)
                pageIDChoosen = False
                while pageIDChoosen == False:
                    pageIDChoosen = True
                    pageID = input("What would you like to set the pageID to? >>> ")
                    try:
                        pageID = int(pageID)
                        save(info, pageID, successes, failures, path, username, password)
                    except ValueError:
                        pageIDChoosen = False
                doneChanging = False
            if whattochange == "PA":
                if path == "ns":
                    print("The path to ChromeDriver has not been set.")
                else:
                    print("The path to ChromeDriver is set to:", path)
                    checkedforchrome = False
                    while (checkedforchrome == False):
                            checkedforchrome = True
                            path = input("I would like to set the path to ChromeDriver to: >>> ")
                            if not os.path.exists(path):
                                print("Invalid Path!")
                                checkedforchrome = False
                    doneChanging = False
            if whattochange == "E":
                if username == "ns":
                    print("The email has not been set.")
                if username == "nw":
                    print("You have disabled automatic password and email entering.")
                if not username == "ns" and not username == "nw":
                    print("The email is set to:", username)
                if username == "nw":
                    enableemailandpassword = input("Would you like to enable email and password entering (Y or N)? >>> ")
                    enableemailandpassword = enableemailandpassword.upper()
                if not username == "nw":
                    enableemailandpassword = "Y"
                if enableemailandpassword == "Y" or not email == "dw":
                    email = input("I would like to set the email to: >>> ")
                doneChanging = False
            if whattochange == "PAS":
                print("The password currently is:", passwordhidden)
                verifypassword = getpass.getpass("Please enter your password to continue: >>> ")
                if verifypassword == password:
                    print("Correct!")
                    print("The password currently is:", password)
                    password = getpass.getpass("I would like to change my password to: >>> ")
                else:
                    print("Invalid Password!")
                doneChanging = False
            if whattochange == "Q":
                print("Leaving...")
                doneChanging = True
                runTypeSelected = False
            if not whattochange == "P" and not whattochange == "PA" and not whattochange == "E" and not whattochange == "PAS" and not whattochange == "Q":
                doneChanging = False
    if runTypeInput == "READ DATA":
        if pageID == "ns":
            print("PageID has not been set.")
        else:
            print("PageID is set to:",str(pageID))
        print("There have been:",str(failures),"failures.")
        print("There have been:",str(successes),"successes.")
        if path == "ns":
            print("The path to ChromeDriver is not set.")
        else:
            print("The path to ChromeDriver is set to:",path)
        if username == "ns":
            print("The email is not set.")
        if username == "dw" and password == "dw":
            print("You have disabled automatic password and email entering.")
        if not username == "ns" and not username == "dw" and not password == "ns" and not password == "dw":
            print("The email is set to:",username)
        if not username == "dw" and not password == "dw":
            print("The password is:", passwordhidden)
            passwordprotect = getpass.getpass("Enter the password to unhide the password: ")
            if (passwordprotect == password):
                sys.stdout.flush()
                print("The password is:", password)
            else:
                print("Incorrect!")
        if password == "ns":
            print("The password is not set.")
        runTypeSelected = False
    if runTypeInput == "RESET DATA":
        usersure = input("Are you sure (Y or N)? >>> ")
        if (usersure == "y" or usersure == "Y"):
            reset()
            runTypeSelected = False
        if (usersure == "n" or usersure == "N"):
            runTypeSelected = False
    if runTypeInput == "QUIT":
        print("Goodbye!")
        sys.exit()
    if not runTypeInput == "START" and not runTypeInput == "RESET DATA" and not runTypeInput == "QUIT" and not runTypeInput == "READ DATA" and not runTypeInput == "SETTINGS":
        runTypeSelected = False
chromedriver = path
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
browser.set_window_size(1600, 1000)
def click(id):
    try:
        browser.find_element_by_id("definition-"+id).click()
        browser.find_element_by_id("term-"+id).click()
    except:
        pass
def login():
    try:
        browser.find_element_by_xpath("//div[@class='TrophiesModal-loggedOutActions']/div/button").click()
    except:
        browser.find_element_by_xpath("//a[@href][2]").click()
    time.sleep(2)
    browser.find_element_by_xpath("//div[@class='UISocialButton']/a").click()
    try:
        browser.find_element_by_xpath("//input[@type='email']").send_keys(username+Keys.ENTER)
        time.sleep(1)
        browser.find_element_by_xpath("//input[@type='password']").send_keys(password+Keys.ENTER)
    except:
        pass

if oneQuiz == False:
    while True:
        save(info, pageID, successes, failures, path, username, password)
        try:
            browser.get("https://quizlet.com/"+str(pageID)+"/micromatch")
            browser.find_element_by_id("start").click()
            terms = browser.find_elements_by_xpath("//a[@data-type='term']")
            for term in terms:
                click(term.get_attribute("data-id"))
            successes = successes + 1
            if not loggedIn:
                time.sleep(1)
                login()
                loggedIn = True
            pageID = pageID + 1
            time.sleep(2)
        except NoSuchWindowException:
            sys.exit()
        except WebDriverException as e:
            failures = failures + 1
            pageID = pageID + 1
        except NoSuchElementException:
            failures = failures + 1
            pageID = pageID + 1
        except:
            pass
if oneQuiz == True:
    while True:
        save(info, pageID, successes, failures, path, username, password)
        try:
            browser.get("https://quizlet.com/"+str(pageID)+"/micromatch")
            browser.find_element_by_id("start").click()
            terms = browser.find_elements_by_xpath("//a[@data-type='term']")
            for term in terms:
                click(term.get_attribute("data-id"))
            successes = successes + 1
            if not loggedIn:
                login()
                loggedIn = True
            time.sleep(2)
        except NoSuchWindowException:
            sys.exit()
        except WebDriverException:
            sys.exit()
        except NoSuchElementException:
            failures = failures + 1
            pageID = pageID + 1
