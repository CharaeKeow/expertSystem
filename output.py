from os import system, name

#clear command for a sleekier interface
def clear():
    
    #for windows
    if name == 'nt':
        _ = system('cls')
    else: 
        _ = system('clear')


def answer():
    print("\nYou are suggested to learn:")

def python():
    clear()
    answer()
    print("\n\t\tPython")
    print()
    print("\tDifficulty: Easy")
    print()
    print("Widely regarded as the best programming \nlanguage for beginners.")
    print()
    print("Easiest to learn")
    print()
    print("Widely used in scientific, technical & academic field, ")
    print("i.e. Artificial Intelligence")
    print()
    print("You can build website using Django, a popular")
    print("Python web framework.")
    print()
    print("\t\tUsed to build:")
    print("Youtube, Instagram, Spotify")

def java():
    clear()
    answer()
    print("\n\t\tJava")
    print()
    print("\tDiffifculty: Medium")
    print()
    print("Very popular on all platform, OS, and ")
    print("devices due to its portability.")
    print()
    print("One of the most in demand & highest")
    print("paying programming languages.")
    print()
    print("Slogan: write once, work everywhere.")
    print()
    print("\t\tUse to build:")
    print("Gmail, Minecraft, Most Android Apps, ")
    print("Enterprise applications")

def c():
    clear()
    answer()
    print("\n\t\tC")
    print()
    print("\tDifficulty: Medium")
    print("\nLingua franca of programming language")
    print("\nOne of the oldest and most widely used")
    print("language in the world.")
    print("\nPopular language for system and hardware")
    print("programming")   
    print("\nA subset of C++ except for the little details")
    print("\n\t\tUse to build:")
    print("Operating systems and hardware")

def cpp():
    clear()
    answer()
    print("\n\t\tC++")
    print("\n\tDifficulty: Hard")
    print("\nComplex version of C with a lot more features")
    print("\nWidely used for developing games, industrial and")
    print("performing-critical applications")
    print("\nLearning C++ is like learning how to manufacture, ")
    print("assemble, and drive a car")
    print("\nRecommended only if you have a mentor to guide you")
    print("\n\t\tUse to build:")
    print("Operating systems, hardware, and browser")

def javascript():
    clear()
    answer()
    print("\n\t\tJavascript")
    print("\n\tDifficulty: Fairly Easy")
    print('\n"Java and Javascript are similar like Car and Carpet"')
    print(" - Greg Hegwill")
    print("\nMost popular clients-side web scripting language")
    print("\nA must learn for front-end web developer (HTML and")
    print("CSS as well)")
    print("\nOne of the hottest programming language now, due to")
    print("its increasing popularity as server-side language(Node.js)")
    print("\n\t\tUse to build:")
    print("Paypal, front-end of majority of websites")

def csharp():
    clear()
    answer()
    print("\n\t\tC#")
    print("\n\tDifficulty: Medium")
    print("\nA popular choice for enterprise to create website and")
    print("Windows application using .NET framework")
    print("\nCan be used to build website with ASP.NET, a web")
    print("framework from Microsoft")
    print("\nSimilar to Java in basic syntax and some features")
    print("\n\t\tUsed to build:")
    print("Enterprise and Windows applications")

def ruby():
    clear()
    answer()
    print("\n\t\tRuby")
    print("\n\tDifficulty: Fairly easy")
    print("\nMostly known for its popular web framework, Ruby on Rails")
    print("\nFocuses on getting things done")
    print("\nDesigned for fun and productive coding")
    print("\nBest for fun and personal projects, startups, and rapid")
    print("development")
    print("\n\t\tUsed to build:")
    print("Hulu, Groupon, Slideshare")

def php():
    clear()
    answer()
    print("\n\t\tPHP")
    print("\n\tDifficulty: Fairly easy")
    print("\nSuitable for building small and simple sites within a")
    print("short-time frame")
    print("\nSupported by almost every web hosting services with")
    print("lower price")
    print("\nKnown as being a big headache to developers who manage")
    print("the codes")
    print("\n\t\tUsed to build:")
    print("Wordpress, Wikipedia, Flickr")

def objective_c():
    clear()
    answer()
    print("\n\t\tObjective-C")
    print("\n\tPrimary language used by Apple for Mac OS X & iOS")
    print("\nChoose this if you want to focus on developing iOS")
    print("or OS X apps only")
    print("\nConsider to learn Swift(newly introduced by Apple in")
    print("2014) as your next language")
    print("\n\tUsed to build:")
    print("Most iOS Apps and part of Mac OS X")