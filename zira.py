import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    
    else:
        speak("Good Evening Sir!")            

    speak("I am Zira Sir. Please tell me how may I help you")    

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"   
    return query      

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('addy2061998@gmail.com', 'your-password-here') # you can write actual password here or can access file here were you have written password. 
    server.sendmail('addy2061998@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
   wishMe()
   while True:
   
        query = takeCommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results) 

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com") 

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")       

        elif 'play music' in query:
            music_dir = 'H:\\My Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play video' in query:
            video_dir = 'H:\\Hollywood Songs'
            video = os.listdir(video_dir)
            print(video)
            os.startfile(os.path.join(video_dir, video[0]))   

        elif 'open images' in query:
            image_dir = 'H:\\PHOTOS'
            image = os.listdir(image_dir)
            print(image)
            os.startfile(os.path.join(image_dir, image[0]))

        elif 'open books' in query:
            books_dir = 'G:\\BOOKS'
            books = os.listdir(books_dir)
            print(books)
            os.startfile(os.path.join(books_dir, books[0])) 

        elif 'open movie' in query:
            movie_dir = 'F:\\HOLLYWOOD MOVIES\\A BEAUTIFUL MIND (2001)'
            movie = os.listdir(movie_dir)
            print(movie)
            os.startfile(os.path.join(movie_dir, movie[0]))             

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, The Time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\Adarsh kumar\\AppData\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'email to addy' in query:
            #we can make dictionary for more people
            try:
                speak("What should I Say?")
                content = takeCommand()
                to = "adarsh2061998@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry my friend Adarsh. I am not able to send this email")    

        elif 'quit' in query:
            exit()        