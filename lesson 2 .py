import colorama
from colorama import Fore, Style
from textblob import TextBlob
colorama.init()
print(f"{Fore.CYAN}welcome to sentiment spy!{style.RESET_ALL}")
user_name=input(f"{Fore.Magenta}please enter your name:{style.RESET_ALL}").strip()
if not user_name:
    user_name="mystery agent"
conversation_history=[]
print(f"\n{Fore.CYAN}Hello,agent{user_name}!")
print(f"type a sentence and i will analyze your sentences with textblob and show you the sentiment.")
print(f"type{Fore.YELLOW}reset{Fore.CYAN},{Fore.YELLOW}history{Fore.CYAN},or exit to quit")
while True:
    user_input=input(f"{Fore.GREEN}>>{style.RESET_ALL}").strip()
    if not user_input:
            print("please enetr some text or a valid command.")
            Continue
    if user_input.lower()=="exit":
        print("exiting sentiment spy. farewell, agent !")
        break
    elif user_input.lower()=="reset":
        conservation_history.clear()
        print("all conservation history cleared !")
        Continue
    elif user_input.lower()=="history":
        if not conservation_history:
            print("no conservation history yet!")
        else:
            print("coservation history:")
            for idx,(text,polarity,sentiment_type) in enumerate(conservation_history,start=1):
                if sentiment_type=="positive":
                    color=Fore.GREEN
                elif sentiment_type=="negative":
                    color=Fore.RED
                else:
                    color=Fore.YELLOW
                print("{idx}.{color}{emoji}{text}"
                      f"polarity:{polarity:.2f},{sentiment_type}{style.RESET_ALL}")
        Continue
    polarity=TextBlob(user_input).sentiment.polarity
    if polarity>0.25:
        sentiment_type="positive"
    elif polarity<-0.25:
        sentiment_type="negative"
    else:
        sentiment_type="neutral"
    conversation_history.append((user_input,polarity,sentiment_type))
    print("sentiment detected!")