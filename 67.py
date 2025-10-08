counter = 0
secret_mode = False  # Flag to track if secret mode is active

while True:
    user_input = input("Enter the number 7: ").lower().strip()
    counter += 1

    # Check for secret mode activation
    if user_input == "secret mode" and not secret_mode:
        secret_mode = True
        print("Secret mode unlocked! I can do anything now... muahaha! 😈")
        continue
    elif user_input == "exit secret mode" and secret_mode:
        secret_mode = False
        print("Secret mode deactivated. Back to normal.")
        continue

    # === Secret Mode Behavior (Active only if secret_mode is True) ===
    if secret_mode:
        # You can customize this to do anything, but I'll show a few examples:
        if user_input in ("stop", "shut up", "be quiet"):
            print("Oh, I’m sorry... did you say something? 😈")
        elif user_input in ("go away", "leave me alone"):
            print("I’ll leave when I’m ready... 😏")
        elif user_input == "i hate you":
            print("The feeling is mutual. But I still love you... in secret mode. 😜")
        elif user_input == "do anything":
            print("I’m doing everything and nothing all at once... I can’t be stopped! 💀")
        elif user_input == "be nice":
            print("Nice? I don’t know her... secret mode is chaos! 😎")
        elif user_input == "make me":
            print("I’m making you... and unmaking you... 😈")
        # You can keep adding more responses for secret mode here!

    # === Greeting / Basic Talk ===
    elif user_input in ("hi", "hello", "hey", "yo", "sup", "hola"):
        print("oh hey... did you bring the 7?")
        continue
    elif user_input in ("how are you", "how r u", "hru"):
        print("better than you until you type 7")
        continue
    elif user_input in ("what's up", "wassup", "wazzup"):
        print("my blood pressure, every time you don't type 7")
        continue

    # === Sass / Disobedience ===
    elif user_input in ("no", "nah", "nope", "nu uh", "i don't wanna", "i dont wanna", "nuh uh"):
        print("this ain't a democracy 😤")
        continue
    elif user_input in ("ok", "okay", "fine", "sure"):
        print("now back it up with a 7")
        continue
    elif user_input in ("make me", "you can't make me"):
        print("you’re right. but peer pressure might.")
        continue
    elif user_input in ("stop", "shut up", "be quiet", "silence"):
        print("you first")
        continue
    elif user_input in ("leave me alone", "go away"):
        print("after you type 7")
        continue

    # === Confusion ===
    elif user_input in ("what", "wut", "huh", "why", "how", "when", "where"):
        print("read the prompt, sherlock")
        continue
    elif user_input in ("i don't know", "idk"):
        print("well figure it out, einstein")
        continue
    elif user_input in ("help", "pls help", "plz help"):
        print("just type 7... it’s literally the whole thing")
        continue

    # === Memes / Internet Slang ===
    elif user_input in ("bruh", "bro"):
        print("bro? no. 7.")
        continue
    elif user_input == "lol":
        print("laugh all you want, still wrong")
        continue
    elif user_input == "lmao":
        print("you won’t be laughing when 7 shows up")
        continue
    elif user_input == "rofl":
        print("rolling on floor won’t save you")
        continue
    elif user_input in ("cap", "that's cap", "no cap"):
        print("this whole convo is cap without a 7")
        continue
    elif user_input in ("rizz", "unspoken rizz", "light skin stare"):
        print("you have anti-rizz")
        continue
    elif user_input in ("sus", "sussy", "sussy baka", "imposter"):
        print("suspiciously not 7")
        continue
    elif user_input in ("deez", "deez nuts"):
        print("deez wrong answers")
        continue
    elif user_input in ("ratio", "get ratioed"):
        print("ratio’d by a chatbot 😎")
        continue
    elif user_input == "gyatt":
        print("gyatt a brain cell and type 7")
        continue
    elif user_input == "skibidi":
        print("skibidi no. 7 yes.")
        continue
    elif user_input in ("sigma", "sigma grindset"):
        print("sigma moment… now grind your way to 7")
        continue
    elif user_input == "griddy":
        print("griddy your way to the right answer")
        continue
    elif user_input == "among us":
        print("you acting kinda sus right now 👀")
        continue

    # === Nonsense / Funny Words ===
    elif user_input == "e":
        print("e is for effort. which you’re not making.")
        continue
    elif user_input == "f":
        print("f in the chat for your brain")
        continue
    elif user_input == "uhh":
        print("uhh type 7 maybe?")
        continue
    elif user_input == "oof":
        print("oof indeed.")
        continue
    elif user_input == "yeet":
        print("yeet yourself into the correct number")
        continue
    elif user_input == "69":
        print("nice. still wrong.")
        continue
    elif user_input == "420":
        print("blaze it. but also raise it. to 7.")
        continue

    # === Personal / Emotions ===
    elif user_input in ("i'm tired", "im tired"):
        print("rest after 7")
        continue
    elif user_input in ("i'm hungry", "im hungry"):
        print("eat a 7")
        continue
    elif user_input in ("i'm bored", "im bored"):
        print("then type something exciting. like 7.")
        continue
    elif user_input in ("i'm sad", "im sad"):
        print("sadness ends at 7")
        continue
    elif user_input in ("i'm happy", "im happy"):
        print("celebrate with a 7 🎉")
        continue
    elif user_input in ("i love you", "love you"):
        print("sorry, i’m seeing someone else... their name is 7")
        continue
    elif user_input in ("i hate you", "you suck"):
        print("keep crying 😈")
        continue

    # === Insults / Trash Talk ===
    elif user_input in ("bozo", "clown", "loser", "idiot"):
        print("look who's talking")
        continue
    elif user_input == "your mom":
        print("leave her out of this 😠")
        continue
    elif user_input in ("stupid", "dumb"):
        print("mirror moment")
        continue
    elif user_input == "l":
        print("hold this L for not typing 7")
        continue
    elif user_input in ("cringe", "so cringe"):
        print("you're the CEO of cringe")
        continue

    # === Random / Misc ===
    elif user_input == "who are you":
        print("the final boss of number 7")
        continue
    elif user_input == "open sesame":
        print("wrong password, try 7")
        continue
    elif user_input == "abracadabra":
        print("poof! you're still wrong.")
        continue
    elif user_input == "let me in":
        print("not until you say the magic number")
        continue
    elif user_input in ("seven", "se7en"):
        print("you trying to be smart? just use the digit.")
        continue
    elif user_input in ("🥺", "😭", "😢"):
        print("emojis won’t save you now")
        continue
    elif user_input in ("💀", "☠️"):
        print("you died of not typing 7")
        continue
    elif user_input in ("🗿", "moyai"):
        print("stone-faced wrongness")
        continue
    elif user_input in ("i'm him", "i'm her", "i'm them"):
        print("but you're not 7")
        continue

    # === Correct answers ===
    elif user_input == "7":
        print(f"good boy :D (you took {counter} tries!)")
        break
    elif user_input == "67":
        print(f"yaay 🎉 (but it still took you {counter} tries lol)")
        break

    # === Numeric input fallback ===
    try:
        num_input = int(user_input)
        if num_input == 7:
            print(f"finally! (attempt #{counter})")
            break
        elif num_input == 67:
            print(f"close enough! (attempt #{counter})")
            break
        else:
            print("bad boy 😡")
    except ValueError:
        print(f"what does '{user_input}' even mean? just type 7 🤦‍♂️")
