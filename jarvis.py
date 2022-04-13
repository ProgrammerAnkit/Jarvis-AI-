
from ast import operator
from audioop import add, mul
from re import sub
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import operator

engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[0].id) 

def speak(audio):
    
        engine.say(audio) 
        engine.runAndWait() #Without this command, speech will not be audible to us.
        
def wishme():
    
        hour = int(datetime.datetime.now().hour)
        speak("I am jarvis sir. how can i help you")
  
def takeCommand():
        #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
                
if __name__=="__main__" :
    wishme()
    while True:
        # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
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
        
        elif 'do some calculations' in query or 'can you calculate' in query:
          try:   
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("say what you want to calculate, example :3 plus 3")
                    print("Listening...")
                    r.adjust_for_ambient_noise(source)
                    r.pause_threshold = 1
                    audio1 = r.listen(source)
                my_string = r.recognize_google(audio1)
                print(my_string)
                def get_operator_fn(op):
                    return {
                        '+' : operator.add, #plus
                        '-' : operator.sub, #minus
                        'x' : operator.mul, #multiplied by 
                        'divided' : operator.__truediv__, #divided            
                    }[op]
                def eval_binary_expr(op1 , oper, op2): # 5 plus 8
                    op1,op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                speak("your result is")
                speak(eval_binary_expr(*(my_string.split())))
          except Exception as e:
                # print(e)    
                print("Say that again please...")   #Say that again will be printed in case of improper voice 
                speak("Say that again please...")


        