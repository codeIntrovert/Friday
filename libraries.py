import os
from speak import takeCommand
from main import *
from selenium import webdriver  # to control browser operations
from selenium.webdriver.common.keys import Keys
#to search, will ask search query at the time of execution




def music():
    print("Now Playing... My Ordinary Life")
    led = "C:\\Users\\Hasan Imam\\Music\\My Ordinary Life-The Living Tombstone-9Zj0JOHJR-s.m4a"
    os.startfile(led)
    return


def open_application(query):
    if "Edge" in query:
        speak("Opening Microsoft Edge")
        os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
        return
   # elif "firefox" in query or "mozilla" in query:
       # speak("Opening Mozilla Firefox")
        #os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe')
        #return
    elif "word" in query:
        speak("Opening Microsoft Word")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2013.lnk')
        return
    elif "excel" in query:
        speak("Opening Microsoft Excel")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk')
        return

    elif "code" in query:
        speak("Opening Visual Studio")
        os.startfile('"C:\\Users\\Hasan Imam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"')
        return
    elif "spotify" in query:
        speak("Spotify")
        os.startfile("C:\\Users\\Hasan Imam\\Desktop\\Spotify.lnk")
        return


    else:
        speak("Application not available")
        return



def search_web(query):
    driver = webdriver.Edge('"D:\\webDriver\\edgedriver_win64\\msedgedriver.exe"')
    driver.implicitly_wait(1)
    driver.maximize_window()
    if 'youtube' in query.lower():
        speak("Opening in youtube")
        indx = query.lower().split().index('youtube')
        query = query.split()[indx+1:]
        driver.get("http://www.youtube.com/results?search_query=" + '+'.join(query))
        return
    else:
        if 'google' in query:
            indx = query.lower().split().index('google')
            query = query.split()[indx + 1:]
            driver.get("https://www.google.com/search?q=" + '+'.join(query))
        elif 'search' in query:
            indx = query.lower().split().index('google')
            query = query.split()[indx + 1:]
            driver.get("https://www.google.com/search?q=" + '+'.join(query))
        else:
            driver.get("https://www.google.com/search?q=" + '+'.join(query.split()))
        return

