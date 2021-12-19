def guess_the_number():
    """Function with game."""
    print("Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w  max. 10 próbach.")
    print("Wciśnij enter by kontunuować")
    input()
    minimun = 0
    maximum = 1000
    user_answer = ""
    while user_answer != "wygrałeś":
        guess = ((maximum - minimun) // 2) + minimun
        print(f"Zgaduję {guess}")
        user_answer = input("Wprowadź odpowiedź (za dużo, za mało, wygrałeś): ")
        if user_answer == "za dużo":
            maximum = guess
        elif user_answer == "za mało":
            minimun = guess
        elif user_answer == "wygrałeś":
            break
        else:
            input("Wprowadź jeszcze raz odpowiedź (za dużo, za mało, wygrałeś): ")

    print("Wygrałem!")


if __name__ == '__main__': guess_the_number()
