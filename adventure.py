start = '''
You work at Trump Co.
'''




print(start)




print("Type 'Male' or 'Female'")
user_input = input()
if user_input == "Male":
    print("You're a new employee, and you just received a pay raise!") # finished the story by writing what happens
    print("Do you take your girlfriend out for dinner? Or do you go out with your bois for a boys' night?")
    print("Type 'GF' to take your girlfriend out or 'Ma Boys' to go out for a boys' night")
    user_input = input()
    if user_input == "GF":
        print("You got lucky tonight! ;P but oh no! Your GF is pregnant! Leave her or ask for a paternity leave?")
        print("Type 'leave' to leave her, or 'paternity leave' to ask your boss.")
        user_input = input()
        if user_input == "leave":
            print("Enjoy your single life, man! You are now sexy, free, and single, and ready to mingle! End of Story")
        elif user_input == "paternity leave":
            print("Your boss gives you one month of paid parternity leave with personal support from him.")
            print("Yay! You get to live happily ever after with your new family!")
        else:
            print("Incorrect input. Try again.")
    elif user_input == "Ma Boys":
        print("You partied hard with your bois and there were strippers! End of Story")
    else:
        print("Incorrect input. Try again.")
elif user_input == "Female":
    print("You've been an employee for five years, but a new employee just got a pay raise.") # finished the story writing what happens
    print("Do you confront your boss? Or do you stay quiet?")
    print("Type 'confront' or 'say nothing'")
    user_input = input()
    if user_input == "confront":
        print("Your boss decided that you should be fired for asking.")
        print("Sorry, dude. Tough luck. Now you're unemployed and have to beg on the streets.")
        print("But wait! There's a job opportunity to be a stripper! But then a grumpy rich carmudgeon offers to be your sugar daddy.")
        print("Type 'take ma clothes off' to be a stripper, or 'gimme that moolah' to be a sugar baby.")
        user_input = input()
        if user_input == "take ma clothes off":
            print("LET'S GOOO!! I can't wait to swing around a pole and devalue myself!")
            print("But what about the baby? Do you put them up for adoption or do you bare that baby bump?")
            print("Type 'adoption' or 'bare that belly' to decide the fate of your child.")
            user_input = input()
            if user_input == "adoption":
                print("The local firemen are very kind and offer a place for you as well as the unborn baby. They offer you support and a way to avoid a life as a stripper.")
                print("You end up marrying one of the nice firemen and live happily ever after. End of Story")
            elif user_input == "bare that belly":
                print("You end up physically hurting yourself as a stripper and hurt your baby. You are rushed to the hospital, but the baby doesn't survive.")
                print("Sorry. Maybe next time you should just keep quiet about your salary and inequality in the workplace. End of Story.")
        elif user_input == "gimme that moolah":
            print("Sweet! You just got yourself a sugar daddy for you AND your unborn child!")
            print("Do you put the child up for adoption? Or do you keep the baby and raise them under your sugar daddy?")
            print("Type 'adoption' or 'keep and raise'")
            user_input = input()
            if user_input == "adoption":
                print("The local firemen are very kind and offer a place for you as well as the unborn baby. They offer you support and a way to avoid a life as a stripper.")
                print("You end up marrying one of the nice firemen and live happily ever after. End of Story")
            elif user_input == "keep and raise":
                print("Yay! Your sugar daddy is now a sugar grandad (is that even a thing?)! You live somewhat happily ever after as an underappreciated woman. End of Story")
            else:
                print("Incorrect input. Try again.")
        else:
            print("Incorrect input. Try again.")
    elif user_input == "say nothing":
        print("You now have the same pay for the next five years.")
        print("In these next five years, you have gotten married, and now are pregnant")
        print("You ask for a maternity leave, but your boss only gives you two options: two weeks of paid leave, or one full month, unpaid.")
        print("Type 'two weeks' for a short, paid leave, or 'one month' for one full month, but unpaid.")
        user_input = input()
        if user_input == "two weeks":
             print("You suffer through post-partum depression, but don't get the proper treatment or time to heal.")
             print("Hope you feel better!")
             print("Good luck in the future as a female in the industry. End of Story")
        elif user_input == "one month":
             print("Your post-partum depression now has time to heal, but you are in a financial crisis. Your husband has to work overtime for the family, and you are left alone with the responsibility of caring for your child.")
             print("Good luck in the future as a female in the industry. End of Story")
        else:
             print("Incorrect input. Try again.")
    else:
        print("Incorrect input. Try again.")
else:
    print("Incorrect input. Try again.")
