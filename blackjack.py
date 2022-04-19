import random

try:
    import tkinter
except ImportError:  # For python2 users
    import Tkinter as tkinter

mainWindow = tkinter.Tk()


def load_card(card_image):
    """Function to load the card images from the file to the GUI"""
    suits = ['heart', 'diamond', 'spade', 'club']
    face_card = ['king', 'queen', 'jack']

    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'
    # For each suite retrieve the image for the card
    for suit in suits:
        # First the number cards from 1 to 10
        for card in range(1, 11):
            name = f'cards/{str(card)}_{suit}.{extension}'
            image = tkinter.PhotoImage(file=name)
            card_image.append((card, image,))
        # Next the face cards
        for card in face_card:
            name = f'cards/{card}_{suit}.{extension}'
            image = tkinter.PhotoImage(file=name)
            card_image.append((10, image,))


# Setup the screen and frames for the game
mainWindow.title("--Black Jack--")
mainWindow.geometry('640x480')

# Setup the result text
result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text).grid(row=0, column=0, columnspan=3)

# Setup the card frame and the dealer and the player window

card_frame = tkinter.Frame(mainWindow, relief='sunken', borderwidth=1, background='green')
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text='Dealer', background='green', fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background='green', fg='white').grid(row=1, column=0)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text='Player', background='green', fg='white').grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background='green', fg='white').grid(row=3, column=0)

# Embedded frame to hold the card images
dealer_card_frame = tkinter.Frame(card_frame, background='green').grid(row=0, column=1, sticky='ew', rowspan=2)
player_card_frame = tkinter.Frame(card_frame, background='green').grid(row=2, column=1, sticky='ew', rowspan=4)

# Setup the button frame for the buttons to go in
button_frame = tkinter.Button(mainWindow)
button_frame.grid(row=3, column=0, sticky='w', columnspan=3)

dealer_button = tkinter.Button(button_frame, text='Dealer').grid(row=0, column=0)
player_button = tkinter.Button(button_frame, text='Player').grid(row=0, column=1)


# Load cards
cards = []
load_card(cards)
print(cards)

# Create a new deck of cards
deck = list(cards)
random.shuffle(deck)

# Create an list to store the dealers and players hand

dealer_hand = []
player_hand = []
mainWindow.mainloop()