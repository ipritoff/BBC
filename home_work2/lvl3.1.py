print("Напишите строку:")

text = input()
print('Выбирите метод: Разделить строку по символу (split),\nПрисоединить строку или вставить между символами символ (join).')
method = input()

def level_three(method:str) -> str: #функция для операций split, join
    global text
    if method == 'split':
        print('Введите символ (разделитель)')
        letter_split = str(input())
        return text.split(letter_split)
    elif method == 'join':
        print('Что хотите сделать?:\nВставить символ между символами строки (paste),\nПрисоединить строку (join_str).')
        operation = str(input())
        if operation == 'paste':
            print("Напишите символ")
            letter_paste = str(input())
            return letter_paste.join(text)
        elif operation == 'join_str':
            print("Напишите строку, которую хотите присоединить к уже написанной")
            letter_join= str(input())
            return text.join(letter_join)
    elif method == 'count':
        print('Введите символ, который хотите посчитать')
        count_letter = str(input())
        return text.count(count_letter)
print(level_three(method))