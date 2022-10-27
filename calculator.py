# Author: Tejas Pai
# Date: 27/10/2022
# Description: Python interactive calculator program

def check(v1, v2, v3):
    msg = ""
    global msg_6
    global msg_7 
    global msg_8 
    global msg_9 

    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg += msg_7
    if v1 == 0 or v2 == 0 and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg += msg_8 
    if msg != "":
        msg = msg_9 + msg
        print(msg)


def is_one_digit(number):
    return number > -10 and number < 10 and number.is_integer()
        

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

messages = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]

memory = float(0)

while True:
    print(msg_0)
    calc = input().rstrip()
    x, oper, y = calc.split()

    if x == "M":
        x = memory
    if y == "M":
        y = memory
    
    try:
        x = float(x)
        y = float(y)

        if oper in "+-*/":
            check(x, y, oper)
            if oper == '+':
                result = x + y
            elif oper == '-':
                result = x - y
            elif oper == '*':
                result = x * y
            elif oper == '/':
                result = x / y
            else:
                pass
        else:
            print(msg_2)

        print(result)

        while True:
            print(msg_4)
            answer = input().strip()
        
            if answer.lower() == 'y':              
                if is_one_digit(result):
                    msg_index = 10
                    while True:
                        print(messages[msg_index])
                        answer = input().strip()
                        if answer.lower() == 'y' and msg_index < 12:
                            msg_index += 1
                        elif answer.lower() == 'y' and msg_index >= 12:
                            memory = result
                            break
                        elif answer.lower() == 'n':
                            break 
                        else:
                            continue
                    break
                else:
                    memory = result
                    break
            else:
                if answer.lower() != 'n':
                    continue
                else:
                    break

        while True:
            print(msg_5)
            answer = input().strip()

            if answer.lower() == 'y':
                break
            elif answer.lower() == 'n':
                exit()
            else:
                continue
        
    except TypeError:
        print(msg_1)
    
    except ValueError:
        print(msg_1)

    except ZeroDivisionError:
        print(msg_3)
