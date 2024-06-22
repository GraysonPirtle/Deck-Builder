from tkinter import *

main_window = Tk()
main_window.title("Deck Builder Probability")

#Labels
Label(main_window, text="How large is the deck?:",fg="black",bg="cyan",width=40,height=1).grid(row= 0, column= 0)
Label(main_window, text="How many cards are you drawing?:",fg="black",bg="cyan",width=40,height=1).grid(row= 1, column= 0)
Label(main_window, text="How many needed cards are left in deck?:",fg="black",bg="cyan",width=40,height=1).grid(row= 2, column= 0)
Label(main_window, text="How many of those cards do you need?:",fg="black",bg="cyan",width=40,height=1).grid(row= 3, column= 0)
Label(main_window, text="Do you need exactly that amount?(enter 1 or 0):",fg="black",bg="cyan",width=40,height=1).grid(row= 4, column= 0)
Label(main_window, text="",fg="black",bg="cyan",width=40,height=2).grid(row=5,column=0)

#Text Input
deck_size = Entry(main_window, width = 2, borderwidth = 1)
deck_size.grid(row= 0, column= 1)

cards_drawn = Entry(main_window, width = 2, borderwidth = 1)
cards_drawn.grid(row= 1, column= 1)

needed_left = Entry(main_window, width = 2, borderwidth = 1)
needed_left.grid(row= 2, column= 1)

needed_amount = Entry(main_window, width = 2, borderwidth = 1)
needed_amount.grid(row= 3, column= 1)

exact = Entry(main_window, width = 2, borderwidth = 1)
exact.grid(row= 4, column= 1)

def on_enter():
    n = int(deck_size.get())
    r = int(cards_drawn.get())
    c = int(needed_left.get())
    m = int(needed_amount.get())
    e = int(exact.get())

    def factorial(x):
        if x==0:
            return 1;
        else:
            numTimes = x-1
            while (numTimes >= 1):
                x = x*numTimes
                numTimes = numTimes - 1
            return x;

    def nCr(n,r):
        numer = factorial(n)
        denom = factorial(r)*factorial(n-r)
        return numer/denom;

    def deck(n,r,c,m,e):
        denom = nCr(n,r)
        if e == 0:
            if m == 1:
                numer = (nCr((n-c),(r)))
                odds = 1 - float(numer)/(denom)
                return odds*100
            else:
                numerator = []
                while (m <= r):
                    numer = (nCr(c,m))*(nCr((n-c),(r-m)))
                    numerator.append(numer)
                    m = m+1
                    total = sum(numerator)
                return float((total)/(denom)*100)
        else:
            numer = (nCr(c,m))*(nCr((n-c),(r-m)))
            return float((numer)/denom)*100

    print(f"You have a {deck(n,r,c,m,e)}% chance of drawing what you need, given the provided parameters.")



#Buttons
Button(main_window, text="Enter", command= on_enter).grid(row=5, column = 1)

main_window.mainloop()
#n is deck size, r is cards drawn, c is amount of needed cards left in deck,
#m is how many needed cards you need, and e is if you need exactly that amount or not
