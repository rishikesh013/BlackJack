import random

try:
    import tkinter
except ImportError:  # For python2 users
    import Tkinter as tkinter


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


def deal_card(frame):
    """
    Function to deal with the cards from the deck
    :param frame: The card frame to be displayed on
    :return: The value of the top most card
    """
    # Pop the next card of the top of the deck
    next_card = deck.pop(0)
    deck.append(next_card)
    # Add the image to the label and display the image
    tkinter.Label(frame, image=next_card[1], relief='sunken').pack(side='left')
    # Return the cards face value
    return next_card


def score_hand(hand):
    """
    Function used to calculate the score of the player and the dealer
    :param hand: A list which returns the top face card value
    :return: The calculated score is returned
    """
    score = 0
    ace = False

    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value

        # If we bust check if there is an ace and subtract 10
        if score >= 21 and ace:
            score -= 10
            ace = False

    return score


def deal_dealer():
    """
    Function to deal with the dealer frame and to calculate the results for the dealer
    :return: None
    """
    global games_won_by_dealer
    global games_won_by_player
    global draw
    global dealer_won
    if not dealer_won:
        dealer_score = score_hand(dealer_hand)
        while 0 < dealer_score < 17:
            dealer_hand.append(deal_card(dealer_card_frame))
            dealer_score = score_hand(dealer_hand)
            dealer_score_label.set(dealer_score)

        player_score = score_hand(player_hand)
        if player_score > 21:
            result_text.set("Dealer Won!!")
            games_won_by_dealer += 1
            dealer_won_label.set(games_won_by_dealer)
            dealer_won = True
        elif dealer_score > 21 or dealer_score < player_score:
            result_text.set("Player Won!!")
            games_won_by_player += 1
            player_won_label.set(games_won_by_player)
            dealer_won = False
        elif dealer_score > player_score:
            result_text.set("Dealer Won!!")
            games_won_by_dealer += 1
            dealer_won_label.set(games_won_by_dealer)
            dealer_won = True
        else:
            result_text.set("Draw!")
            draw += 1
            draw_label.set(draw)
            dealer_won = False
    else:
        result_text.set("Dealer won!!. No further car dealt!")


def deal_player():
    """
    Function to deal with the player card frame and to calculate the score of the player
    :return: None
    """
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set('Dealer Won!!')


def new_game():
    """
    Function which clears all the frame and creates a new frame for the user
    :return: None
    """
    global dealer_card_frame
    global player_card_frame
    global dealer_won
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)
    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)
    dealer_hand.clear()
    player_hand.clear()
    initialize_game()
    result_text.set("")
    dealer_won = False


def shuffle():
    random.shuffle(deck)


def initialize_game():
    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def load_new_deck():
    global deck
    global number_of_deck_loaded
    number_of_deck_loaded += 1
    deck += list(cards)
    shuffle()


def play():
    initialize_game()
    mainWindow.mainloop()


mainWindow = tkinter.Tk()

# Setup the screen and frames for the game
mainWindow.title("--Black Jack--")
mainWindow.geometry('640x480')
mainWindow.configure(background='green')

# Result frame to display the result of the Game
result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text, background="green", fg="tan1")
result.grid(row=2, column=0, columnspan=3)

dealer_score_label = tkinter.IntVar()
player_score_label = tkinter.IntVar()

# Card frame to display the dealer and the player card
card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=3, column=0, sticky='ew', columnspan=3, rowspan=2)

tkinter.Label(card_frame, text="Dealer", background="green", fg="DarkGoldenrod1").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="DarkGoldenrod1").grid(row=1,
                                                                                                         column=0)
tkinter.Label(card_frame, text="Player", background="green", fg="goldenrod3").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="goldenrod3").grid(row=3, column=0)
# embedded frame to hold the Dealer card
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

# embedded frame to hold the Player Card
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

# Button frame to add the necessary buttons
button_frame = tkinter.Frame(mainWindow, background="green")
button_frame.grid(row=5, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(button_frame, text="Dealer", background="DarkGoldenrod1", command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player", background="goldenrod3", command=deal_player)
player_button.grid(row=0, column=1)

new_game_button = tkinter.Button(button_frame, text="New Game", background="tan1", command=new_game)
new_game_button.grid(row=0, column=2)

load_deck_button = tkinter.Button(button_frame, text="Load new deck", background="tan1", command=load_new_deck)
load_deck_button.grid(row=0, column=3)

shuffle_deck_button = tkinter.Button(button_frame, text="Shuffle deck", background="tan2", command=shuffle)
shuffle_deck_button.grid(row=0, column=4)

# Main result frame to display the total games won by the dealer, player and number of matches that went draw
result_frame = tkinter.Frame(mainWindow)
result_frame.grid(row=0, column=0, rowspan=2, columnspan=3, sticky='ew')
result_frame.configure(background="green")

dealer_won_label = tkinter.IntVar()
tkinter.Label(result_frame, text="Dealer won", background="green", fg="DarkGoldenrod1").grid(row=0, column=0)
tkinter.Label(result_frame, textvariable=dealer_won_label, background="green", fg="DarkGoldenrod1").grid(row=1,
                                                                                                         column=0)
player_won_label = tkinter.IntVar()
tkinter.Label(result_frame, text="Player won", background="green", fg="goldenrod3").grid(row=0, column=2)
tkinter.Label(result_frame, textvariable=player_won_label, background="green", fg="goldenrod3").grid(row=1, column=2)

draw_label = tkinter.IntVar()
tkinter.Label(result_frame, text="Draw", background="green", fg="tan1").grid(row=0, column=4)
tkinter.Label(result_frame, textvariable=draw_label, background="green", fg="tan1").grid(row=1, column=4)

# Load cards
cards = []
load_card(cards)


# Create a new deck of cards
deck = list(cards)
number_of_deck_loaded = 0
# random.shuffle(deck)
shuffle()
# Create an list to store the dealers and players hand
dealer_hand = []
player_hand = []
# initialize_game()

# Global scoreboard details
games_won_by_dealer = 0
games_won_by_player = 0
draw = 0
dealer_won = False

if __name__ == '__main__':
    play()
