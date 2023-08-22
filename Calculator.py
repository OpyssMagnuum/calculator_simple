import PySimpleGUI as sg

layout = [
    [sg.T('Калькулятор', justification='center', expand_x=True, font=('Arial Bold', 20), key='-T-')],

    [sg.T('0', justification='right', expand_x=True, font=('Unispace', 20), key='Num', background_color='dark blue')],

    [sg.B('C', key='clear', font=('Arial', 14), expand_x=True),
     sg.B('<', key='delete', font=('Arial', 14), size=4),
     sg.B('/', key='divide', font=('Arial', 14), size=2)],

    [sg.B('7', key='7', font=('Unispace', 14), size=4),
     sg.B('8', key='8', font=('Unispace', 14), size=4),
     sg.B('9', key='9', font=('Unispace', 14), size=4),
     sg.B('x', key='multi', font=('Unispace', 14), expand_x=True)],

    [sg.B('4', key='4', font=('Unispace', 14), size=4),
     sg.B('5', key='5', font=('Unispace', 14), size=4),
     sg.B('6', key='6', font=('Unispace', 14), size=4),
     sg.B('-', key='subt', font=('Arial', 14), expand_x=True)],

    [sg.B('1', key='1', font=('Unispace', 14), size=4),
     sg.B('2', key='2', font=('Unispace', 14), size=4),
     sg.B('3', key='3', font=('Unispace', 14), size=4),
     sg.B('+', key='add', font=('Arial', 14), expand_x=True)],

    [sg.B('0', key='0', font=('Unispace', 14), expand_x=True),
     sg.B('.', key='dot', font=('Arial', 14), size=4),
     sg.B('=', key='equals', font=('Arial', 14), size=2)],

]


def addNum(arg, current_num):
    if current_num != '0' or '.' in current_num:
        ret_num = current_num + arg
        return ret_num
    else:
        return arg


def changeNum(current_num, prev_num, oper):
    if oper == '':
        return current_num
    switcher = {
        '+': current_num + prev_num,
        '-': prev_num - current_num,
        '*': prev_num * current_num,
        '/': prev_num / current_num,
    }
    res = switcher.get(oper, '')
    return int(res) if not('.' in str(res).strip('.')) or (str(res)[-1] == '0' and str(res)[-2] == '.') else res


last_oper = ''  # Последняя операция +-*/
previous_num = '0'
wait_till_num_pressed = False

print(int(1.0))

window = sg.Window('Калькулятор', layout)
while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    # Если нажата цифра (0-9)
    if event.isdigit():
        current_number = window['Num'].get()
        if wait_till_num_pressed:
            previous_num = current_number.strip('.')
            current_number = '0'
            wait_till_num_pressed = False
        print(window[f'{event}'].GetText())
        print(addNum(window[f'{event}'].GetText(), current_number))
        window['Num'].update(addNum(window[f'{event}'].GetText(), current_number))

    # Если нажата точка (.)
    if event == 'dot':
        window['Num'].update(window['Num'].get()+'.')

    # Если нажата кнопка '<' (убрать 1 элемент с конца)
    if event == 'delete':
        window['Num'].update(window['Num'].get()[:-1])
        if window['Num'].get() == '':
            window['Num'].update('0')
        wait_till_num_pressed = False

    # Если нажата кнопка 'c' (убирает все символы и забывает все операции)
    if event == 'clear':
        window['Num'].update('0')
        last_oper = ''
        wait_till_num_pressed = False

    # Если нажата кнопка '='
    if event == 'equals':
        changed = changeNum(float(window['Num'].get()), float(previous_num), last_oper)
        window['Num'].update(changed)
        wait_till_num_pressed = True
        last_oper = ''

    # Всевозможные операции
    if event == 'add' or event == 'subt' or event == 'multi' or event == 'divide':
        switcher = {
            'add': '+',
            'subt': '-',
            'multi': '*',
            'divide': '/',
        }
        last_oper = switcher.get(event, '')
        wait_till_num_pressed = True


window.close()
