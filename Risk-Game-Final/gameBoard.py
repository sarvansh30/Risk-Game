import customtkinter as ctk
from PIL import Image, ImageTk
import random
import time
import mainGame

def close_current_window():
    app.destroy()  # Close the current window

def navigate_to_new_page(winner):
    close_current_window()  # Close the current window
    mainGame.gameWindow(winner)  # Call the gameWindow function with the winner parameter

def choose_territories():
    navigate_to_new_page(winner)  # Navigate to the gameWindow with the winner set to "Player"

def roll_dice():
    # Disable the button during dice rolling animation
    roll_button.configure(state=ctk.DISABLED)

    # Display rolling animation for 2 seconds
    for _ in range(20):
        dice_value_player.configure(text=str(random.randint(1, 6)))
        dice_value_ai.configure(text=str(random.randint(1, 6)))
        app.update()
        time.sleep(0.1)

    # Enable the button after dice rolling animation
    roll_button.configure(state=ctk.NORMAL)
    
    # Get the dice values
    player_dice = int(dice_value_player.cget("text"))
    ai_dice = int(dice_value_ai.cget("text"))

    # Determine the winner
    global winner 
    if player_dice > ai_dice:
        winner_label.configure(text="Player wins! It's their turn.")
        winner = "Player"
        # Change button text and command
        roll_button.configure(text="Choose Territories", command=choose_territories)
    elif player_dice < ai_dice:
        winner_label.configure(text="AI wins! It's AI's turn.")
        winner = "AI"
        # Change button text and command
        roll_button.configure(text="Choose Territories", command=choose_territories)
    else:
        winner_label.configure(text="It's a tie! Roll again.")
        winner = None  # Set winner to None in case of tie
        
        # Change button text and command
        roll_button.configure(text="Roll the dice", command=roll_dice)

app = ctk.CTk()
app.title("Risk Game")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
app.geometry("1600x800")

frame = ctk.CTkFrame(master=app, width=1600, height=800)
frame.pack(pady=0, padx=0, fill="both", expand=True)

# Create labels to indicate players
player_label = ctk.CTkLabel(frame, text="Player:", font=("Helvetica", 24))
player_label.place(relx=0.4, rely=0.3, anchor="center")

ai_label = ctk.CTkLabel(frame, text="AI:", font=("Helvetica", 24))
ai_label.place(relx=0.6, rely=0.3, anchor="center")

# Create widgets
dice_value_player = ctk.CTkLabel(frame, text="", font=("Helvetica", 48))
dice_value_player.place(relx=0.4, rely=0.4, anchor="center")

dice_value_ai = ctk.CTkLabel(frame, text="", font=("Helvetica", 48))
dice_value_ai.place(relx=0.6, rely=0.4, anchor="center")

roll_button = ctk.CTkButton(frame, text="Roll the dice", command=roll_dice)
roll_button.place(relx=0.5, rely=0.6, anchor="center")

winner_label = ctk.CTkLabel(frame, text="", font=("Helvetica", 24))
winner_label.place(relx=0.5, rely=0.7, anchor="center")

app.mainloop()
