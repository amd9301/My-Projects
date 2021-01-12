# To make the code talk we are installing package pyttsx3

import pyttsx3
import  PyPDF2

print("Enter the book name you want to listen: ")
name = input()
book = open(name,'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages =  pdfReader.numPages

print('Number of pages',pages)
print('Enter the page number where you want to start: ')
start = int(input())

speaker = pyttsx3.init()
speaker.setProperty('rate',180)
speaker.setProperty('volume',0.7)

voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
# Use female voice
speaker.setProperty('voice', voice_id)

for num in range(start-1,pages):
    page = pdfReader.getPage(num)
    # After getting the page , extract the text
    text = page.extractText()
    speaker.say(text)
    # speaker.say('Hello World dot')
    speaker.runAndWait()
