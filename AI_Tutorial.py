import pyttsx3
import datetime
import os
import wikipedia
import speech_recognition as sr
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning to all the Aspiring Engineers of the future !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon to all the Aspiring Engineers of the future !")

	else:
		speak("Good Evening to all the Aspiring Engineers of the future !")

	speak("Myself Friday I am AI assisstant developed as a tutorial presentation ! ")
	speak("Today With my help group A6 is  going to explain you all about vast modules of python and the different functions present in it !")

def takeCommand():

	r = sr.Recognizer()

	with sr.Microphone() as source:

		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		return "None"

	return query

if __name__ == '__main__':
	clear = lambda: os.system('cls')

	# This Function will clean any
	# command before execution of this python file
	clear()
	wishMe()

	while True:

		query = takeCommand().lower()

		if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 3)
			speak("According to Wikipedia")
			print(results)
			speak(results)

		elif 'search' in query or 'play' in query:

			query = query.replace("search", "")
			query = query.replace("play", "")
			webbrowser.open(query)


		elif 'build' in query:
			speak("I have build importing various python modules written by a vast community of GitHub and many Computer Science researcher The main imported module is pyttsx3 which is used for the conversion of text to speech in a program it works offline. and for the rest Ajay will definitely try to clear your doubts")
			webbrowser.open("google.com")

		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			speak(f"Sir, the time is {strTime}")

		elif 'exit' in query:
			speak("Thanks for giving me your time")
			exit()
