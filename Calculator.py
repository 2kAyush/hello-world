def stack_validator(line):
    stack = []
    for i in line:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                return 0
            else:
                x = stack.pop()
                if i == '(' and x != ')':
                    return 0

    if not stack:
        return 1
    else:

        return 0


def rp_notation(infix):
    postfix = []
    stack = []
    global dic
    infix.insert(0, '(')
    infix.append(')')
    operator_list = ['^', '/', '*', '+', '-']
    priority = {'^': 3, '/': 2, '*': 2, '+': 1, '-': 1, '(': 0}
    for s in infix:
        if s.isalnum():
            if s not in dic and not s.isdigit():
                print('Invalid variable')
                return 0
            postfix.append(s)
        elif s == '(':
            stack.append(s)
        elif s == ')':
            while True:
                x = stack.pop()
                if x == '(':
                    break
                else:
                    postfix.append(x)

        elif s in operator_list:
            while True:
                if priority[stack[-1]] >= priority[s]:
                    x = stack.pop()
                    postfix.append(x)
                else:
                    break
            stack.append(s)
    return postfix


def stack_solver(post):
    stack = []
    global dic
    operator_list = ['^', '/', '*', '+', '-']
    for i in range(len(post)):
        if post[i] not in operator_list:
            stack.append(post[i])
        else:
            second = stack.pop()
            first = stack.pop()
            if first.isdigit():
                first = int(first)
            elif first.startswith('-'):
                first = int(first)
            else:
                first = dic[first]

            if second.isdigit():
                second = int(second)
            elif second.startswith('-'):
                second = int(second)
            else:
                second = dic[second]
            if post[i] == '+':
                stack.append(str(first + second))
            elif post[i] == '-':
                stack.append(str(first - second))
            elif post[i] == '*':
                stack.append(str(first * second))
            elif post[i] == '/':
                stack.append(str(int(first / second)))
            elif post[i] == '^':
                stack.append(str(first ** second))
    return int(stack.pop())


def sign_decider(si):
    re = 1
    for k in si:
        if k == '-':
            re *= -1
        elif k == '+':
            re *= 1
    if re == -1:
        return '-'
    elif re == 1:
        return '+'


def signer(line):
    main_lis = []
    eq_num = ''
    eq_sig = ''
    eq_bracket = ''
    bracket_list = ['(', '[', '{']
    bracket_rev_list = [')', ']', '}']
    operator_list = ['*', '/', '^']
    all_operator_list = ['*', '/', '^', '+', '-']
    for i in range(len(line)):
        if line[i] == '+' or line[i] == '-':
            eq_sig += line[i]
            if eq_num:
                main_lis.append(eq_num)
                eq_num = ''
            elif eq_bracket:
                main_lis.append(eq_bracket)
                eq_bracket = ''
        elif line[i].isalnum():
            if eq_sig:
                sign = sign_decider(eq_sig)
                main_lis.append(sign)
                eq_sig = ''
            eq_num += line[i]

        elif line[i] in bracket_list or line[i] in bracket_rev_list:
            if eq_sig:
                sign = sign_decider(eq_sig)
                main_lis.append(sign)
                eq_sig = ''
            elif eq_num:
                main_lis.append(eq_num)
                eq_num = ''
            main_lis.append(line[i])
        elif line[i] in operator_list and line[i + 1] not in all_operator_list:
            if eq_sig:
                sign = sign_decider(eq_sig)
                main_lis.append(sign)
                eq_sig = ''
            elif eq_num:
                main_lis.append(eq_num)
                eq_num = ''
            main_lis.append(line[i])

    if eq_num:
        main_lis.append(eq_num)
    if eq_sig:
        main_lis.append(eq_sig)
    return main_lis


def equal(line):
    line = line.split("=")
    var_l = line[0].strip(' ')
    var_r = line[1].strip(' ')
    for i in var_l:
        if i.isdigit():
            print('Invalid identifier')
            return 'Invalid', 0
    d = var_r[0].isdigit()
    for i in range(1, len(var_r)):
        if var_r[i].isdigit() != d:
            print('Invalid assignment')
            return 'Invalid', 0
    global dic
    if var_r.isdigit():
        return var_l, var_r
    else:
        if var_r in dic:
            var_r = dic[var_r]
            return var_l, var_r

        elif var_r not in dic:
            print('Unknown variable')
            return 'Unknown', 0


dic = {}
while True:
    ch = input()
    if ch == '/exit':
        print("Bye!")
        break
    elif ch == '/help':
        print("""The program calculates the sum of numbers
        and variable assignment is also possible
        """)
        continue
    elif ch.startswith('/'):
        print("Unknown command")
    elif ch.endswith('+') or ch.endswith('-') or ch.endswith('*') or ch.endswith('/') or ch.endswith('^'):
        print("Invalid expression")
    elif ch == '':
        continue
    elif ch.startswith('-'):
        print(ch)
    else:
        if '=' in ch:
            if ch.count('=') > 1:
                print('Invalid assignment')
                continue
            tp = equal(ch)
            if tp[0] == 'Unknown':
                continue
            elif tp[0] == 'Invalid':
                continue
            dic[tp[0]] = int(tp[1])
        elif '+' in ch or '-' in ch or '*' in ch or '/' in ch or '^' in ch:
            y = signer(ch)
            res = stack_validator(y)
            if res == 0:
                print('Invalid expression')
            else:
                lis = rp_notation(y)
                if lis == 0:
                    continue
                result = stack_solver(lis)
                if result == 'x':
                    continue
                print(result)

        else:
            if ch in dic:
                print(dic[ch])
            elif ch.isdigit():
                print(ch)
            else:
                print('Unknown Variable')
