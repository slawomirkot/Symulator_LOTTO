from random import randint


def user_choice():
    '''
    Get 6 different numbers between 1 and 49 from user and try until user give proper number.
    '''
    user_number_list = []
    while True:
        try:
            if len(user_number_list) >= 6:
                break
            user_number = input("Podaj 6 liczb pojedyńczo z zakresu 1-49!\nZatwierdz liczbę używająć klawisza ENTER:")
            user_number = int(user_number)
            if user_number < 1 or user_number > 49:
                print("Podaj liczbę z zakresu 1-49!")
                continue
            if user_number not in user_number_list:
                user_number_list.append(user_number)
            else:
                print("Podana liczba już występuje!")
                continue
        except ValueError:
            print("Wprowadzono nie poprawnie liczby, spróbuj ponownie!")
    return sorted(user_number_list)


def lotto():
    '''
    Chose 6 random numbers.
    '''
    lotto_number_list = []
    for i in range(6):
        while len(lotto_number_list) < 6:
            lotto_number = randint(1, 50)
            if lotto_number not in lotto_number_list:
                lotto_number_list.append(lotto_number)
            else:
                continue
    return lotto_number_list


def lotto_win():
    '''
    Main function with our program.
    '''
    user = user_choice()
    computer = lotto()
    winner_number = set(user) & set(computer)
    while True:
        if len(winner_number) == 0:
            print("Niestety brak trafionych liczb!")
            break
        elif len(winner_number) == 1:
            print("Trafiłeś tylko 1 liczbę!")
            break
        elif len(winner_number) == 2:
            print("Trafiłeś tylko 2 liczby!")
            break
        elif len(winner_number) == 3:
            print("Trafiłeś 3 liczby! Wygrałeś!")
            break
        elif len(winner_number) == 4:
            print("Trafiłeś 4 liczby! Wygrałeś!")
            break
        elif len(winner_number) == 5:
            print("Trafiłeś 5 liczb! Wygrałeś!")
            break
        elif len(winner_number) == 6:
            print("Trafiłeś 6 liczb! Wygrałeś!")
            break
    print(f"{user}\n{computer}")


lotto_win()
