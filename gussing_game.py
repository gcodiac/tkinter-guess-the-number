import random
import tkinter as tk

correct_guess = random.randint(1, 100)
guess_count = 0
my_font = ('Camberia', 19, 'bold')


def shuffle():
    global correct_guess
    global guess_count
    guess_count = 0
    correct_guess = random.randint(1, 100)
    result.config(text="Start Gussing! ", foreground="#FFF")
    print(correct_guess)


def guess_func():
    # name.configure(state="disabled")
    # name.destroy()

    global guess_count
    global correct_guess
    guess_count += 1
    if int(guess.get()) < correct_guess:
        result.config(
            text="Ops! You need to guess higher. What is your guess?: ",  foreground="#9A9ACD")
    elif int(guess.get()) > correct_guess:
        result.config(
            text="Ops! You need to guess lower. What is your guess?: ", foreground="BlanchedAlmond")
    elif int(guess.get()) == correct_guess:
        result.config(
            text=f" Congrats! The right answer was {correct_guess}. It took you {guess_count} guesses")
        #btn.config(text="Play Again!")
    else:
        result.config(
            text="Wrong entry - plaese only enter numbers ", foreground="#FFFF72")


win = tk.Tk()
win.geometry("700x150")
win.title('Gussing Game')

tk.Label(win, font=my_font, bg="red", text="Welcome to the gussing game. Please guess a number between 1 and 100").grid(
    row=0, columnspan=3, pady=(10, 0), padx=2)

#name = tk.Entry(win)
#name.grid(row=1, column=0)
#name.insert(0, "Pelase Enter Your Name: ")

guess = tk.Entry(win, width=20)
guess.grid(row=1, columnspan=2, pady=20, sticky="E")


btn = tk.Button(win, text="Guess!", command=guess_func)
btn.grid(row=1, column=1, sticky="E")

shuffle_btn = tk.Button(win, text="Shuffle!", command=shuffle)
shuffle_btn.grid(row=1, column=2, sticky="W")

result = tk.Label(win, font=my_font, text="Start Gussing!")
result.grid(row=2, columnspan=3, sticky="WE")

win.mainloop()
