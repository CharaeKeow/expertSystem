#production_rules.py
#Keep the production rules and functions
import output as op

#Start the expert system
def start():
    print("\n\nWhy you want to learn programming")
    print("1. For my kids.")
    print("2. I don't know. Just pick one for me.")
    print("3. To make money")
    print("4. Just for fun.")
    print("5. I'm interested.")
    print("6. I wanna to improve myself.")

    why = input("Why you wanna learn programming?:\nPick a number: ")

    if (why == '1'):
        #clear() should I include this?
        op.python()
    elif (why == '2'):
        op.python()
    elif (why == '3'):
        platform()
    elif (why == '4' or why=='5' or why=='6'):
        pref_to_learn()
    else:
        print("Seems like an invalid choice.")

#Auto or manual?
def car():
    print("\n\nAuto or Manual car?")
    print("1. Manual")
    print("2. Auto")

    car = input("\nChoose one: ")

    if(car=='1'):
        op.c()
    elif(car=='2'):
        op.java()

#Do you prefer to learn?
def pref_to_learn():
    print("\n\nI prefer to learn things")
    print("1. The easy way")
    print("2. The best way")
    print("3. The slightly harder way")    
    print("4. The really hard way")
    
    pref_to_learn = input("\nChoose one: ")

    if(pref_to_learn == '1'):
        op.python()
    elif(pref_to_learn == '2'):
        op.python()
    elif(pref_to_learn == '3'):
        car()
    elif(pref_to_learn == '4'):
        op.cpp()
    else:
        print("\nInvalid choice!")    

#Platform
def platform():
    print("\n\nHave any platform/field in mind?")
    print("1. Doesn't matter. I just want $$$")
    print("2. Mobile")
    print("3. Web")
    print("4. Google")
    print("5. Facebook")
    print("6. Microsoft")   
    print("7. Apple") 
    print("8. Enterprise")
    print("9. 3D/Gaming")
    
    platform = input("\nWhich platform/field?: ")
    
    if (platform == '1'):
        op.java()
    elif (platform == '2'):
        mobile()
    elif (platform == '3'):
        web()
    elif (platform == '4' or platform == '5'):
        op.python()
    elif (platform == '6'):
        op.c()
    elif (platform == '7'):
        op.objective_c()
    elif (platform == '8'):
        think_MS()
    elif (platform == '9'):
        op.cpp()
    else:
        print("\nInvalid choice!")
    return

#Think about Microsoft?
def think_MS():
    print("\n\nWhat do you think about Microsoft?")
    print("1. I'm a fan!")
    print("2. Not bad.")
    print("3. Suck")
    
    think_MS = input("\nChoose one: ")

    if (think_MS == '1'):
        op.csharp()
    elif (think_MS == '2' or think_MS == '3'):
        op.java()
    else:
        print('\nInvalid option')        

#Try something new - no
def no():
    print("\n\nWhich one is your favourite toy?")
    print("1. Lego")
    print("2. Play-doh")
    print("3. I have an old & ugly toy, but I love it so much!")
    
    no = input("\nChoose one?")
    if(no == '1'):
        op.python()
    elif(no == '2'):
        op.ruby()
    elif(no == '3'):
        op.php()
    else:
        print('\nInvalid option')

#Try something new?
def try_some_new():
    print("\n\nDo you like to try something new, with huge potential")
    print("but less mature?")
    print("1. Yes")    
    print("2. No")

    try_some_new = input("\nChoose one?: ")

    if (try_some_new == '1'):
        op.javascript()
    elif(try_some_new == '2'):
        no()
    else:
        print("\nInvalid option")

#Do you want to work for
def work_for():
    print("\n\nI want to work for... ")
    print("1. Corporate")
    print("2. Startup")

    work_for = input("\nChoose one: ")

    if (work_for == '1'):
        think_MS()
    elif (work_for == '2'):
        try_some_new()
    else:
        print("\nInvalid option")

#Web
def web():
    print("\n\nWhich end?")
    print("1. Front-end(web interface)")
    print('2. Back-end("brain" behind a website)"')
    web = input("\nChoose one: ")
    
    if (web =='1'):
        op.javascript()
    elif (web == '2'):
        work_for()
    else:
        print('\nInvalid option.')

#Mobile
def mobile():
    print("Which OS?")
    print("1. ioS")
    print("2. Android")
    mobile = input("\nChoose one: ")

    if (mobile == '1'):
        op.objective_c()
    elif (mobile == '2'):
        op.java()
    else: 
        print("\nUh-oh. Invalid choice")
