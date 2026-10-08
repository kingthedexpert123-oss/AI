import re, random
from colorama import Fore,init
init(autoreset=True)
destinitions={
    "beaches":["bali","maldives","phuket"],
    "mountains":["swiss alps","rocky mountains","himalayas"],
    "cities":["tokyo","paris","new york"]
}
joke=[
    "why dont programmers like mature ? too many bugs!",
    "why did the computer go to the doctoe ? because it had a virus!",
    "why do travellers always feel warm? because of all their hot spots!"
]
def normalize_input(text):
    return re.sub(r"\s+"," ",text.strip().lower())
def recommend():
    print("travelBot:beaches,mountains, or cities ?")
    preferences=input("you:")
    preference=normalize_input(preference)
    if preference in destinations:
        suggestion=random.choice(destination[preference])
        print("travelBot: how about {suggestion} ?")
        print("travelBot: do you like it ? (yes/no)")
        answer=input("you:").lower()
        if answer=="yes":
            print("travelBot : awesome! enjoy {suggestion} !")
        elif answer=="no":
            print("travelBot: lets try another.")
            recommend()
        else:
            print("travelBot: i will suggest again.")
    else:
        print("travelBot: sorry , i dont have that type of destination.")
        recommend()
def packing_tips():
    print("tarvelBot: where to ?")
    locatiuon=normalize_input(input("you:"))
    print("travelBot: how many days ?")
    days=input("you:")
    print("travelBot: packing tips for {days} days in {location}:")
    print("pack versatile clothes.")
    print("bring cahrgers/adapters.")
    print("check the weather forecast.")
def tell_joke():
    print("travelBot: {random.choice(jokes)}")
def show_help():
    print("\nI can:")
    print("suggest travel spots (say'recommendation')")
    print("offer packing tips(say'packing)")
    print("tell a joke (say'joke')")
    print("type 'exit' or 'bye' to end.\n")
def chat():
    print("hello! im travelBot")
    name=input("your name ?")
    print("nive to meet you,{name}!")
    show_help()
    while True:
        user_input=input(Fore.YELLOW+f"{name}:")
        user_input=normalize_input(user_input)
        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print("travelBot: safe travels! goodbye")
            break
        else:
            print("travelBot: could you rephrase ?")
if __name__=="__main__":
    chat()

