import pyttsx3  #pip install pyttsx3  Text to speech conversion
import datetime  #module
import speech_recognition as sr  # For speech recognition
import wikipedia   # To use Wikipedia module
import smtplib      # To user SMTP Simple Mail Tranfer Protocol
import webbrowser as wb     # to use chrome browser
import os  #inbuilt       # For OS functionalities
import pyautogui         # To access windows screen cursor usewd in SS
import psutil        # To access OS CPU amd Battery Usage
import pyjokes  # For Jokes
import requests, json  #inbuilt

engine = pyttsx3.init()
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume', 100)

#change voice
def voice_change(v):
    x = int(v)
    engine.setProperty('voice', voices[x].id)
    speak("done sir")


#speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#time function
def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)

OPENWEATHER_APP_ID = "6a57e4f50b3749937c1af2884106c66a"


def get_weather_report(city):
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"

#date function  
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return(ip_address["ip"])
    

def checktime(tt):
    hour = datetime.datetime.now().hour
    if ("morning" in tt):
        if (hour >= 6 and hour < 12):
            speak("Good morning sir")
        else:
            if (hour >= 12 and hour < 18):
                speak("it's Good afternoon sir")
            elif (hour >= 18 and hour < 24):
                speak("it's Good Evening sir")
            else:
                speak("it's Goodnight sir")
    elif ("afternoon" in tt):
        if (hour >= 12 and hour < 18):
            speak("it's Good afternoon sir")
        else:
            if (hour >= 6 and hour < 12):
                speak("Good morning sir")
            elif (hour >= 18 and hour < 24):
                speak("it's Good Evening sir")
            else:
                speak("it's Goodnight sir")
    else:
        speak("it's night sir!")


#welcome function
def wishme():
    speak("Welcome Back")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning sir!")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon sir")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening sir")
    else:
        speak("Goodnight sir")

    speak("Nebula at your service, Please tell me how can i help you?")


def wishme_end():
    speak("signing off")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening")
    else:
        speak("Goodnight.. Sweet dreams")
    quit()


#command by user function
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  #Translate audio to query  
        print(query)   ####
    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"

    return query


#sending email function
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()         # Availability of SMTP, Domain name of host client
    server.starttls()     # Secure Connection
    server.login("ujj.pandey297@gmail.com", "xwwujogmmccnndog")
    server.sendmail("ujj.pandey297@gmail.com", to, content)
    server.close()


#screenshot function
def screenshot():
    img = pyautogui.screenshot()
    img.save(
        "G:\\Sourabh\\Project\\Voice Assistance\\Nebula\\screenshots\\ss.png"
    )


#battery and cpu usage
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU usage is at ' + usage)
    print('CPU usage is at ' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    print("battery is at:" + str(battery.percent))


#joke function
def jokes():
    j = pyjokes.get_joke()
    print(j)
    speak(j)




def personal():
    speak(
        "I am Nebula, version 1.0, I am an AI assistent, I am developed by Sourabh on 11 November 2022 in INDIA"
    )
    speak("Now i hope you know me")


if __name__ == "__main__":
    wishme()
    while (True):
        query = takeCommand().lower()

        #time

        if ('time' in query):
            time()

#date

        elif ('date' in query):
            date()

#personal info
        elif ("tell me about yourself" in query):
            personal()
        elif ("about you" in query):
            personal()
        elif ("who are you" in query):
            personal()
        elif ("yourself" in query):
            personal()

        elif ("developer" in query or "tell me about your developer" in query
              or "father" in query or "who develop you" in query
              or "developer" in query):
            res = open("about.txt", 'r')
            speak("here is the details: " + res.read())

#searching on wikipedia

        elif ('wikipedia' in query or 'what' in query or 'who' in query
              or 'when' in query or 'where' in query):
            speak("searching...")
            query = query.replace("wikipedia", "")
            query = query.replace("search", "")
            query = query.replace("what", "")
            query = query.replace("when", "")
            query = query.replace("where", "")
            query = query.replace("who", "")
            query = query.replace("is", "")
            result = wikipedia.summary(query, sentences=2)
            print(query)
            print(result)
            speak(result)

#sending email
  
        elif ("email" in query):
            try:
                speak("What is the message for the email")
                content = takeCommand()
                to = 'sourabh6712@gmail.com'
                sendEmail(to, content)
                speak("Email has sent")
            except Exception as e:
                print(e)
                speak(
                    "Unable to send email check the address of the recipient")
        elif ("search on google" in query or "open website" in query):
            speak("What should i search or open?")
            chromepath = 'C:\Program Files\Google\Chrome\Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')

#sysytem logout/ shut down etc

        elif ("logout" in query):
            os.system("shutdown -1")
        elif ("restart" in query):
            os.system("shutdown /r /t 1")
        elif ("shut down" in query):
            os.system("shutdown /r /t 1")

#play songs

        elif ("play songs" in query):
            speak("Playing...")
            songs_dir = "C:\\Music";
            songs = os.listdir(songs_dir)   #List Directories
            os.startfile(os.path.join(songs_dir, songs[0]))  #It will play first song
            quit()

#reminder function

        elif ("create a reminder list" in query or "reminder" in query):
            speak("What is the reminder?")
            data = takeCommand()
            speak("You said to remember that" + data)
            reminder_file = open("data.txt", 'a')
            reminder_file.write('\n')
            reminder_file.write(data)
            reminder_file.close()

#reading reminder list

        elif ("do you know anything" in query or "remember" in query):
            reminder_file = open("data.txt", 'r')
            speak("You said me to remember that: " + reminder_file.read())

#screenshot
        elif ("screenshot" in query):
            screenshot()
            speak("Done!")

#cpu and battery usage
        elif ("cpu and battery" in query or "battery" in query
              or "cpu" in query):
            cpu()
        
#Find my IP
        elif("find my ip" in query):
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')


# Who is your Daddy
        
        elif 'nebula are you there' in query:
            speak("Yes Sir, at your service")
        elif 'nebula who made you' in query:
            speak("Yes Sir, my master build me in AI")

#location
        elif 'location' in query:
            speak('What is the location?')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            wb.get('chrome').open_new_tab(url)
            speak('Here is the location ' + location)

#jokes
        elif ("tell me a joke" in query or "joke" in query):
            jokes()

#weather
        elif ("weather" in query or "temperature" in query):
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

#nebula features
        elif ("tell me your powers" in query or "help" in query
              or "features" in query):
            features = ''' i can help to do lot many things like..
            i can tell you the current time and date,
            i can tell you the current weather,
            i can tell you battery and cpu usage,
            i can create the reminder list,
            i can take screenshots,
            i can send email to your boss or family or your friend,
            i can shut down or logout or hibernate your system,
            i can tell you non funny jokes,
            i can open any website,
            i can search the thing on wikipedia,
            i can change my voice from male to female and vice-versa
            And yes one more thing, My boss is working on this system to add more features...,
            tell me what can i do for you??
            '''
            print(features)
            speak(features)

        elif ("hii" in query or "hello" in query or "goodmorning" in query
              or "goodafternoon" in query or "goodnight" in query
              or "morning" in query or "noon" in query or "night" in query):
            query = query.replace("nebula", "")
            query = query.replace("hi", "")
            query = query.replace("hello", "")
            if ("morning" in query or "night" in query or "goodnight" in query
                    or "afternoon" in query or "noon" in query):
                checktime(query)
            else:
                speak("what can i do for you")

#changing voice
        elif ("voice" in query):
            speak("for female say female and, for male say male")
            q = takeCommand()
            if ("female" in q):
                voice_change(1)
            elif ("male" in q):
                voice_change(0)
        elif ("male" in query or "female" in query):
            if ("female" in query):
                voice_change(1)
            elif ("male" in query):
                voice_change(0)

#exit function

        elif ('i am done' in query or 'bye bye nebula' in query
              or 'go offline nebula' in query or 'bye' in query
              or 'nothing' in query):
            wishme_end()
