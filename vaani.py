import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyautogui 
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from vaaniUi import Ui_vaaniUi
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
 engine.say(audio)
 engine.runAndWait()


def wishME():
 hour = int(datetime.datetime.now().hour) 
 if hour>=0 and hour<12:
     speak("Good Morning!")

 elif hour>+12 and hour<18:
     speak("Good Afternoon!")

 else :
     speak("Good Evening!")   

 speak ("Hii I am Vanni. How may I help you")  

 
class MainThread(QThread):
   def __init__(self):
      super(MainThread, self).__init__()


   def run(self):
      self.TaskExecution ()   
      
      
   def TaskExecution(self):
      wishME()
      while True:    
                 self.query = self.takeCommand().lower()

                #logic for executing tasks
                 if 'search' in self.query:
                            speak('Searching Wikipedia.....')
                            self.query = self.query.replace("wikipedia","")
                            results = wikipedia.summary(self.query, sentences=2)
                            speak("According to wikipedia")
                            print(results)
                            speak(results)

                 elif 'open youtube' in self.query:
                            webbrowser.open("youtube.com")

                 elif 'open google' in self.query:
                            webbrowser.open("google.com")

                 elif 'open amazon' in self.query:
                            webbrowser.open("amazon.in")

                 elif 'open stack over flow' in  self.query:
                            webbrowser.open("stackoverflow.com")
                 
                 elif 'news' in self.query:
                     speak("Finding today's top headlines")
                     webbrowser.open("google.com/news")         


                 elif 'play music' in self.query:
                            speak("Playing Music")
                            music_dir = 'E:\\songs'
                            songs = os.listdir(music_dir)
                            print(songs)
                            os.startfile(os.path.join(music_dir, songs[0]))
                            

                            
                 elif 'the time' in self.query:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        print(strTime)
                        speak(f"The time is {strTime}")

                 elif 'open code' in self.query:
                    codePath ="C:\\Users\\Rohit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)

                 elif 'volume up' in self.query:
                    pyautogui.press("volumeup")

                 elif'volume down' in self.query:
                    pyautogui.press("volumedown")

                 elif'mute' in self.query:
                    pyautogui.press("volumemute")

                 elif "unmute" in self.query:
                    pyautogui.press("volumeunmute")

   def takeCommand(self):
                    #it takes microphone input form the user and returns string output
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        print("Listening....")
                        r.pause_threshold = 1 
                        audio = r.listen(source)

                    try:
                        print("Recognizing...")
                        query = r.recognize_google(audio, language='en-in')
                        print(f"User said:{query}\n")  


                    except Exception as e:
                        #print(e)
                        print("Say that again please......")
                        return "None"        
                    return query
startExecution = MainThread()
                 
class Main(QMainWindow):
    def  __init__(self):
        super().__init__()   
        self.ui = Ui_vaaniUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close) 

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:/python/anime1.gif") 
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()  
        timer =QTimer(self)
        timer.timeout.connect(self.showTime) 
        timer.start(1000)  
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)  
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)



app = QApplication(sys.argv)
vaani = Main()
vaani.show()
exit (app.exec()) 
        

