"""a module with an awesome game developed by flawless Ija Maharyta"""
import time

def slow_print(text, delay=0.03):
    """
    Just a func for printing text by letter so it looks nice.
    """
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(delay)
    print('')


def get_user_choice():
    """
    Function for getting inputed choice. 
    Returnes 'a','b' or 'c'.
    Always waits for user to input sth valid. 
    """
    while True:
        user_choice = input(">>> ")
        if user_choice in ("a", "b", "c", "q"):
            return user_choice
        print("Введіть коректну відповідь: 'a', 'b' або 'c' (будь ласка!)")


def get_lore_from_file(index):
    """
    Function for reading file and getting proper string from it.
    Returns description of situation and list of choices for user. 
    """
    next_scene = None
    with open("moves.txt", "r", encoding="utf-8") as file:
        for line in file:
            next_scene = line
            next_scene = next_scene.split("$")
            new_index = next_scene[0].split("&")
            if new_index[0]==index:
                break
    deep_descr = next_scene[1].split("#")
    deep_descr = [el.split("&") for el in deep_descr]
    main_descr = next_scene[0].split("&")
    return [main_descr, deep_descr]


def choice(list_of_choices):
    """
    Function for offering a user a list of choices.
    Returns index of next scene and points of respect.
    """
    slow_print("~~~", 0.8)
    letter = ord('a')
    for variant in list_of_choices:
        print(f'{chr(letter)}) {variant[0]}')
        letter+=1
    user_choice = get_user_choice()
    if user_choice == "q":
        return ["---", "q"]
    index_of_choice = ord(user_choice) - ord('a')
    next_m = list_of_choices[index_of_choice][1]
    points = int(list_of_choices[index_of_choice][2])
    return [next_m, points]


def get_ending(i):
    """
    Function for reading the file and returning the ending by index.
    """
    ending = get_lore_from_file(f'xx{i}')[1][0][0]
    text = ending.split('\\n')
    return text


def determine_ending(dynamic, counters, balance):
    """
    Function that determinates the ending which the user has reached.
    It gets list of numbers (dynamics), and number which repeats the most
    refers to the ending that the user will get. 
    Also, there are more prioritized endings then other ones, so function
    checks them according to their priority. Therefore, if the user gets
    the same amount of two or more diferent dynamics, the ending will be
    chosen by it's priority.
    Prints the ending's name, it's description and points of respect.
    """
    if dynamic.count('4') == max(counters):
        text = get_ending('4')
        for el in text:
            print(el)
    elif dynamic.count('2') == max(counters):
        text = get_ending('2')
        for el in text:
            print(el)
    elif dynamic.count('1') == max(counters):
        text = get_ending('1')
        for el in text:
            print(el)
    elif dynamic.count('3') == max(counters):
        text = get_ending('3')
        for el in text:
            print(el)
    print(f'Ви завершили гру з рівнем репутації {balance}!')


def main():
    """
    Actual functional game.
    It ends in two ways: either you lose all your reputation points, or you get
    enough choices to end the game.
    """
    balance = 15
    index = '000'
    dyn = []
    slow_print("Вітаю, студенте! Зараз грудень, надворі страшенний холод, \
а у вас скоро сесія.")
    slow_print("Настав час прокинутись та піти на кампус, аби вчитись!")
    slow_print("p.s. Натисність q для завершення гри в будь-який момент.")
    slow_print("p.s.2 Будь-які висловлення, які можуть вас зачепити, \
сприймайте не більше ніж жарт :)")
    while balance > 0:
        if index == 'fff':
            break
        descr, variants = get_lore_from_file(index)
        if len(descr)>1:
            text = descr[1].split('\\n')
            for el in text:
                slow_print(el)
        try:
            index, points = choice(variants)
            if points == "q":
                print("Дякую за гру! <3")
                return
        except (EOFError, KeyboardInterrupt):
            print("\nДякую за гру! <3")
            return
        dyn.append(index[0])
        balance += points
    if balance <=0:
        print('Ви втратили забагато очок репутації.',
'Дуже шкода, та ваші цінності не відповідають цінностям УКУ :(', sep='\n')
    else:
        counters = [dyn.count('1'), dyn.count('2'), dyn.count('3'), dyn.count('4')]
        determine_ending(dyn,counters,balance)

main()
