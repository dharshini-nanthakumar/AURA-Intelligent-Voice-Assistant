import webbrowser
import datetime
import os

def speak(text):
    print(text)
    os.system(f'powershell -Command "Add-Type –AssemblyName System.Speech; '
              f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\');"')

# Greeting based on time
hour = datetime.datetime.now().hour

if hour < 12:
    greeting = "Good Morning"
elif hour < 18:
    greeting = "Good Afternoon"
else:
    greeting = "Good Evening"

print("=======================================")
print("     AURA - Intelligent Voice Assistant")
print("=======================================")

name = input("Please enter your name: ")
speak(f"{greeting}, {name}. Welcome to Aura.")
speak("I am your voice assistant created for Science Day Project.")

while True:
    print("\nAvailable Commands:")
    print("1. google")
    print("2. whatsapp")
    print("3. youtube")
    print("4. search")
    print("5. play")
    print("6. time")
    print("7. date")
    print("8. notepad")
    print("9. calculate")
    print("10. about")
    print("11. system")
    print("12. motivate")
    print("13. clear")
    print("14. exit")

    command = input("\nEnter command: ").lower()

    if command == "1" or command == "google":
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif command == "2" or command == "whatsapp":
        speak("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")

    elif command == "3" or command == "youtube":
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif command == "4" or command == "search":
        speak("What should I search?")
        query = input("Search: ")
        webbrowser.open("https://www.google.com/search?q=" + query)

    elif command == "5" or command == "play":
        speak("Which song should I play?")
        song = input("Song name: ")
        webbrowser.open("https://www.youtube.com/results?search_query=" + song)

    elif command == "6" or command == "time":
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")

    elif command == "7" or command == "date":
        today = datetime.date.today()
        speak(f"Today's date is {today}")

    elif command == "8" or command == "notepad":
        speak("Opening Notepad")
        os.system("notepad")

    elif command == "9" or command == "calculate":
        speak("Enter your calculation")
        expression = input("Example: 5+3 : ")
        try:
            result = eval(expression)
            speak(f"The result is {result}")
        except:
            speak("Invalid calculation")

    elif command == "10" or command == "about":
        speak("Aura is a command based intelligent voice assistant.")
        speak("It integrates web services, system automation,")
        speak("real time clock processing and user interaction.")
        speak("This project demonstrates automation using Python.")

    elif command == "11" or command == "system":
        speak("Fetching system information")
        os.system("systeminfo")

    elif command == "12" or command == "motivate":
        speak("Here is your motivation for today.")
        speak("Success is built on consistency and courage.")

    elif command == "13" or command == "clear":
        os.system("cls")

    elif command == "14" or command == "exit":
        speak(f"Thank you {name}. Have a great day.")
        break

    else:
        speak("Invalid command. Please try again.")
