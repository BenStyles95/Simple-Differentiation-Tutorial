# ------------------------------------------------------------------------------------------
# Differential Tutorial Program - Benjamin Styles
# ------------------------------------------------------------------------------------------
# Instructions for choices
# ------------------------------------------------------------------------------------------
# Choice 1
def choice_1():
    print("\n\t Hello and welcome to the Differentiation Tutorial Program." +
          "\n\tThis program aims to teach you how to differentiate " +          
          "\n\tfunctions. This program can be used by anyone who wishes " +         
          "\n\tto learn the differentiation topic or for people who want" +          
          "\n\tto sharpen their skills."
          "\n\n\tInstructions:" +
          "\n\n\t For any x with a power term, input x^ e.g. 2 x^ 3" +
          "\n\n\t Spaces are crucial for the program to work so when inputting" +
          "\n\tan equation for example "'-2x^2+5x-6'", type it out like this:"+
          "\n\t- 2 x^ 2 + 5 x - 6"+
          "\n\n\t I hope you enjoy using this program and master the differential"
          "\n\ttechniques!")

    input("\n\tPress the enter key to return to the menu.")
# ------------------------------------------------------------------------------------------
# Choice 2
def choice_2():
    print("\n\t///////////////////////////////////" +
          "\n\t//Introduction to Differentiation//" +
          "\n\t///////////////////////////////////")
    
    input()
    
    print("\n\t Differentiation is a topic which branches off the school of" +
          "\n\tcalculus. The differentiation technique allows us to find a" +
          "\n\tderivative of a function.")

    input()

    print("\n\t The derivative of a function is the rate of change of a dependent" +
          "\n\twhich is determined by the independent variable.")

    input()

    print("\n\t The definition may seem mind-boggling, but it is simpler than you" +
          "\n\tthink.")

    input()

    print("\n\t For exmple, if an experiment was set up to see how long (in seconds)" +
          "\n\tit takes for a given car to slow down from 80 metres per second to" +
          "\n\t30 metres per second, we could use differentiation to find the rate" +
          "\n\tof change at which the car slows down.")

    input()

    print("\n\t Our independent variable would be time because this variable is being" +
          "\n\tchanged e.g. 10s, 20s, 30s etc. Our dependent variable would be" +
          "\n\tthe speed at which the car is travelling, because the value of speed" +
          "\n\tis dependent on how many seconds have gone by.")

    input()

    print("\n\t Let's say that the equation of the function for the above scenario is" +
          "\n\ty = 2 x^ 4 + 5 x - 6. If you wanted to find the derivative of this" +
          "\n\tfunction, these are the rules that you should follow:")

    input()

    print("\n\n\t dy/dx(x^n) = n*x^(n-1)")

    input()

    print("\n\t What this rule is explaing is to find a derivative of a function, you" +
          "\n\twill need to take the x term's power and times it by the coefficient of" +
          "\n\tthe x term. Then you need to subtract one from the power.")

    input()

    print("\n\t So, for y = 2 x^ 2 + 5 x - 6, dy/dx = 8 x^ 3 + 5")

    input()

    print("\n\t You might be wondering where the - 6 went. There isn't any x term" +
          "\n\tassociated with the value. Therefore - 6 is simply reduced to 0.")

    input()

    loop = 0

    while loop != 1:

        ans = input("\n\n\t Try to differentiate y = 4 x^ 3 + 7 x + 3: dy/dx = ")

        if ans == "12 x^ 2 + 7":
            print("\n\t Well done, you are correct.")
            break

        elif ans != "12 x^ 2 + 7":
            print("\n\t That is incorrect, try again.")
            loop = 0

    while loop != 1:

        ans = input("\n\n\t Try to differentiate y = 8 x^ 4 + 12 x + 5: dy/dx = ")

        if ans == "32 x^ 3 + 12":
            print("\n\t Well done, you are correct.")
            break

        elif ans != "32 x^ 3 + 12":
            print("\n\t That is incorrect, try again.")
            loop = 0
            
    while loop != 1:

        ans = input("\n\n\t Try to differentiate y = - 4 x^ 4 + 26 x - 9: dy/dx = ")

        if ans == "- 16 x^ 3 + 26":
            print("\n\t Well done, you are correct.")
            break

        elif ans != "- 16 x^ 3 + 26":
            print("\n\t That is incorrect, try again.")
            loop = 0
        
    print("\n\t Now that you've got the hang of differentiation, try it some of the" +
          "\n\ttest your knowledge modes to help you practice.")

    input("\nPress enter to return to the menu.")
# ------------------------------------------------------------------------------------------
# Choice 3
def choice_3():
    import random

    print("\n\tTest Your Knowledge - Easy")
    print("\n\tPress enter when you're ready to start")

    tries = 0
    score = 0

    while tries != 10:
        
        co_1 = str(random.randint(1, 10))
        co_2 = str(random.randint(1, 5))

        ops = ["+","-"]

        op = ops[random.randint(0, 1)]

        answer = [co_1+" x",op,co_2]

        print("\n\ty = ",str(answer).translate({ord(","): "", ord("("): "", ord(")"): "",
                                               ord("["): "", ord("]"): "", ord("'"): ""}))
        
        # Differentiation of the equation

        answer_pt2 = []

        while answer != []:
            
            if "x^" in answer[0]:

                term = answer[0]
                
                # Position value of x^
                pos = term.index("x^")

                # Splitting the term up
                co,x,exp = term.split()
                [[pos-1],[pos],[pos+1]]
                
                #Changing strings into integers
                a = int(co)
                b = int(exp)
                
                # Differentiation
                new_co = a*b
                new_exp = b - 1

                # Combing the solved term
                solved = (new_co,x,new_exp)

                # Adding solved term to answer
                answer_pt2.append(solved)

                # Delete solved part of equation
                answer = answer[1::]

            elif "x" in answer[0]:

                term = answer[0]

                pos = term.index("x")

                co,x = term.split()
                [[pos-1],[pos]]

                answer_pt2.append(co)

                answer = answer[1::]

            elif "x^" not in answer[0] and "x" not in answer[0] and "+" not in answer[0] and "-" not in answer[0]:
                answer = answer[1::]
            else:
                answer_pt2.append(answer[0])
                answer = answer[1::]
            
        if "+" in answer_pt2[len(answer_pt2)-1] or "-" in answer_pt2[len(answer_pt2)-1]:
            answer_pt2 = answer_pt2[0:len(answer_pt2)-1]
        # Output        
        answer_pt2 = str(answer_pt2)

        answer_pt2 = answer_pt2.translate({ord(","): "", ord("("): "", ord(")"): "",
                                         ord("["): "", ord("]"): "", ord("'"): ""})

        correct = input("\n\tdy/dx = ?: ")

        if correct == answer_pt2:
            print("\n\tWell done that is correct.")
            tries += 1
            score += 1

        elif correct != answer_pt2:
            print("\n\tThat is incorrect.")
            tries += 1

        print("\n\tdy/dx = ",answer_pt2)

        print("\n\tNext Question!")

    print("\n\tYou managed to get a score of",score," out of 10!")
    input("\nPress the enter key to return to the menu.")
# ------------------------------------------------------------------------------------------
# Choice 4
def choice_4():
    import random

    print("\n\tTest Your Knowledge - Intermediate")
    print("\n\tPress enter when you're ready to start")

    tries = 0
    score = 0

    while tries != 10:

        co_1 = str(random.randint(1, 5))
        co_2 = str(random.randint(1, 5))
        co_3 = str(random.randint(1, 5))

        power_1 = str(random.randint(2, 3))

        ops = ["+","-"]

        op_1 = ops[random.randint(0, 1)]
        op_2 = ops[random.randint(0, 1)]

        answer = [co_1+" x^ "+power_1,op_1, co_2+" x",op_2,co_3]

        print("\n\ty = ",str(answer).translate({ord(","): "", ord("("): "", ord(")"): "",
                                               ord("["): "", ord("]"): "", ord("'"): ""}))
        
        # Differentiation of the equation

        answer_pt2 = []

        while answer != []:
            
            if "x^" in answer[0]:

                term = answer[0]
                
                # Position value of x^
                pos = term.index("x^")

                # Splitting the term up
                co,x,exp = term.split()
                [[pos-1],[pos],[pos+1]]
                
                #Changing strings into integers
                a = int(co)
                b = int(exp)
                
                # Differentiation
                new_co = a*b
                new_exp = b - 1

                # Combing the solved term
                solved = (new_co,x,new_exp)

                # Adding solved term to answer
                answer_pt2.append(solved)

                # Delete solved part of equation
                answer = answer[1::]

            elif "x" in answer[0]:

                term = answer[0]

                pos = term.index("x")

                co,x = term.split()
                [[pos-1],[pos]]

                answer_pt2.append(co)

                answer = answer[1::]

            elif "x^" not in answer[0] and "x" not in answer[0] and "+" not in answer[0] and "-" not in answer[0]:
                answer = answer[1::]
            else:
                answer_pt2.append(answer[0])
                answer = answer[1::]
            
        if "+" in answer_pt2[len(answer_pt2)-1] or "-" in answer_pt2[len(answer_pt2)-1]:
            answer_pt2 = answer_pt2[0:len(answer_pt2)-1]
        # Output        
        answer_pt2 = str(answer_pt2)

        answer_pt2 = answer_pt2.translate({ord(","): "", ord("("): "", ord(")"): "",
                                         ord("["): "", ord("]"): "", ord("'"): ""})

        correct = input("\n\tdy/dx = ?: ")

        if correct == answer_pt2:
            print("\n\tWell done that is correct.")
            tries += 1
            score += 1

        elif correct != answer_pt2:
            print("\n\tThat is incorrect.")
            tries += 1

        print("\n\tdy/dx = ",answer_pt2)

        print("\n\tNext Question!")

    print("\n\tYou managed to get a score of",score," out of 10!")
    input("\nPress the enter key to return to the menu.")  
# ------------------------------------------------------------------------------------------
# Choice 5
def choice_5():
    import random

    print("\n\tTest Your Knowledge - Hard")
    print("\n\tPress enter when you're ready to start")

    tries = 0
    score = 0

    while tries != 10:

        co_1 = str(random.randint(1, 20))
        co_2 = str(random.randint(1, 20))
        co_3 = str(random.randint(1, 20))
        co_4 = str(random.randint(1, 20))

        power_1 = str(random.randint(0, 10))
        power_2 = str(random.randint(0, 10))

        ops = ["+","-"]

        op_1 = ops[random.randint(0, 1)]
        op_2 = ops[random.randint(0, 1)]
        op_3 = ops[random.randint(0, 1)]

        answer = [co_1+" x^ "+power_1,op_1, co_2+" x^ "+power_2,op_2, co_3+" x ",op_3,co_4]

        print("\n\ty = ",str(answer).translate({ord(","): "", ord("("): "", ord(")"): "",
                                               ord("["): "", ord("]"): "", ord("'"): ""}))

        # Differentiation of the equation

        answer_pt2 = []

        while answer != []:
            
            if "x^" in answer[0]:

                term = answer[0]
                
                # Position value of x^
                pos = term.index("x^")

                # Splitting the term up
                co,x,exp = term.split()
                [[pos-1],[pos],[pos+1]]
                
                #Changing strings into integers
                a = int(co)
                b = int(exp)
                
                # Differentiation
                new_co = a*b
                new_exp = b - 1

                # Combing the solved term
                solved = (new_co,x,new_exp)

                # Adding solved term to answer
                answer_pt2.append(solved)

                # Delete solved part of equation
                answer = answer[1::]

            elif "x" in answer[0]:

                term = answer[0]

                pos = term.index("x")

                co,x = term.split()
                [[pos-1],[pos]]

                answer_pt2.append(co)

                answer = answer[1::]

            elif "x^" not in answer[0] and "x" not in answer[0] and "+" not in answer[0] and "-" not in answer[0]:
                answer = answer[1::]
            else:
                answer_pt2.append(answer[0])
                answer = answer[1::]
            
        if "+" in answer_pt2[len(answer_pt2)-1] or "-" in answer_pt2[len(answer_pt2)-1]:
            answer_pt2 = answer_pt2[0:len(answer_pt2)-1]
        # Output        
        answer_pt2 = str(answer_pt2)

        answer_pt2 = answer_pt2.translate({ord(","): "", ord("("): "", ord(")"): "",
                                         ord("["): "", ord("]"): "", ord("'"): ""})

        correct = input("\n\tdy/dx = ?: ")

        if correct == answer_pt2:
            print("\n\tWell done that is correct.")
            tries += 1
            score += 1

        elif correct != answer_pt2:
            print("\n\tThat is incorrect.")
            tries += 1

        print("\n\tdy/dx = ",answer_pt2)

        print("\n\tNext Question!")

    print("\n\tYou managed to get a score of",score," out of 10!")
    input("\nPress the enter key to return to the menu.")
# ------------------------------------------------------------------------------------------
# Choice 6
def choice_6():
    
# Where the user inputs their desired equation

    equation = input("\n\tWhat equation would you like to differentiate? y = ")

    # Where the equation is broken up into a list through a parsing tree

    answer = []

    # Detects if there is a minus at the front of the equation

    if "-" in equation[0]:

        answer.append(equation[0])
        equation = equation[2::]

    # Parsing tree (while loop)
    while equation != []: 

        # Identifying the operator

        # If "+" is or isn't in equation
        if "+" in equation:
            add_position = equation.index("+")

        elif "+" not in equation:
            add_position = 0

        # If "-" is or isn't in equation
        if "-" in equation:
            sub_position = equation.index("-")

        elif "-" not in equation:
            sub_position = 0
        
        # If '+' or '-' is not present in the equation
        if add_position == 0 and sub_position == 0:
            break

        # If index value of "+" is bigger than the index value of "-"
        elif add_position > sub_position:

            if sub_position == 0:

                operator = equation[add_position:add_position+2]
                chunk = equation[0:add_position]
                chunk2 = equation[add_position+2::]
                answer.append(chunk)     
                answer.append(operator)
                equation = chunk2
            
            elif sub_position > 0:

                operator = equation[sub_position:sub_position+2]
                chunk = equation[0:sub_position]
                chunk2 = equation[sub_position+2::]
                answer.append(chunk)        
                answer.append(operator)
                equation = chunk2
                
        # If index value of "+" is smaller than the index value of "-"        
        elif add_position < sub_position:

            if add_position == 0:

                operator = equation[sub_position:sub_position+2]
                chunk = equation[0:sub_position]            
                chunk2 = equation[sub_position+2::]
                answer.append(chunk)        
                answer.append(operator)
                equation = chunk2

            elif add_position > 0:

                operator = equation[add_position:add_position+2]
                chunk = equation[0:add_position]
                chunk2 = equation[add_position+2::]
                answer.append(chunk)
                answer.append(operator)
                equation = chunk2
                
    # Adds what's leftover from equation to answer converts the tuple into a list
    answer.append(equation)

    # Differentiation of the equation

    answer_pt2 = []

    while answer != []:
        
        if "x^" in answer[0]:

            term = answer[0]
            
            # Position value of x^
            pos = term.index("x^")

            # Splitting the term up
            co,x,power = term.split()
            [[pos-1],[pos],[pos+1]]
            
            #Changing strings into floating points
            a = float(co)
            b = float(power)
            
            # Differentiation
            new_co = a*b
            new_power = b - 1

            # Combing the solved term
            solved = (new_co,x,new_power)

            # Adding solved term to answer
            answer_pt2.append(solved)

            # Delete solved part of equation
            answer = answer[1::]

        elif "x" in answer[0]:

            term = answer[0]

            pos = term.index("x")

            co,x = term.split()
            [[pos-1],[pos]]

            answer_pt2.append(co)

            answer = answer[1::]

        elif "x^" not in answer[0] and "x" not in answer[0] and "+" not in answer[0] and "-" not in answer[0]:
            answer = answer[1::]
        else:
            answer_pt2.append(answer[0])
            answer = answer[1::]
    # This checks if the equation inputted was just a constant
    if len(answer_pt2) >= 1:    
        if "+" in answer_pt2[len(answer_pt2)-1] or "-" in answer_pt2[len(answer_pt2)-1]:
            answer_pt2 = answer_pt2[0:len(answer_pt2)-1]

    elif len(answer_pt2) < 1:
        answer_pt2 = 0
        
    # Output        
    answer_pt2 = str(answer_pt2)
    print("\n\tdy/dx = ",answer_pt2.translate({ord(","): "", ord("("): "", ord(")"): "",
                                           ord("["): "", ord("]"): "", ord("'"): ""}))

    input("\n\nPress the enter key to return to the menu.")
# ------------------------------------------------------------------------------------------
# Menu

print("\t//////////////////////////////////////////////////////////////")
print("\t//Hello and Welcome to the Differentiation Tutorial Program!//")
print("\t//////////////////////////////////////////////////////////////")
          

selection = None

while selection != "0":
    print(
    """
    \t\t[1] - How To Use This Program
    \t\t[2] - Introduction To Simple Differentiation
    \t\t[3] - Test Your Knowledge - Easy
    \t\t[4] - Test Your Knowledge - Intermediate
    \t\t[5] - Test Your Knowledge - Hard
    \t\t[6] - Derivative Calculator
    \t\t[0] - Exit Program
    """
    )

    selection = input("What would you like to choose?: ")

    # Choice 1
    if selection == "1":
        choice_1()

    # Choice 2
    elif selection == "2":
        choice_2()
        
    # Choice 3
    elif selection == "3":
        choice_3()
        
    # Choice 4
    elif selection == "4":
        choice_4()

    # Choice 5    
    elif selection == "5":
        choice_5()

    # Choice 6        
    elif selection == "6":
        choice_6()
        
    # Choice 0    
    elif selection == "0":
        break

input("\n\n\tGoodbye! - [Press the enter key to exit]")
