def is_one_digit(v):
    return v.is_integer() and -10 < v < 10


def check(v1, v2, v3):
    msg = ""
    msg_6 = " ... lazy"
    msg_7 = " ... very lazy"
    msg_8 = " ... very, very lazy"
    msg_9 = "You are"
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 == '-' or v3 == '+' or v3 == '*'):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"


memory = 0
result = 0
while True:
    data = input(msg_0)
    a, op, b = data.split(" ")
    if a == 'M':
        a = memory
    if b == 'M':
        b = memory
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print(msg_1)
        continue
    if op not in ['+', '-', '*', '/']:
        print(msg_2)
        continue
    check(a, b, op)
    if op == '+':
        result = (a + b)
    elif op == '-':
        result = (a - b)
    elif op == '*':
        result = (a * b)
    elif op == '/':
        if b == 0:
            print(msg_3)
            continue
        result = (a / b)
    print(result)
    m = input(msg_4)
    if m == 'y':
        if is_one_digit(result):
            m = input(msg_10)
            if m == 'y':
                m = input(msg_11)
                if m == 'y':
                    m = input(msg_12)
                    if m == 'y':
                        memory = result
        else:
            memory = result
    m = input(msg_5)
    if m == 'y':
        continue
    else:
        break
