import customtkinter as ctk
from PIL import Image, ImageTk
from Territory import Territory
from Continents import Continent
from Player import Player
from AIPlayer import AIPlayer
# Create continents
north_america = Continent("North America", 5)
south_america = Continent("South America", 2)
europe = Continent("Europe", 5)
africa = Continent("Africa", 3)
asia = Continent("Asia", 7)
australia = Continent("Australia", 2)

# Create territories
alaska = Territory("Alaska", north_america)

# Add territories to their respective continents
north_america.add_territory(alaska)


player = Player("Player")
ai = AIPlayer("AI")

# Create territories
territories2 = {
    "Alaska": Territory("Alaska", north_america),
    "N. W. Territory": Territory("N. W. Territory", north_america),
    "Alberta": Territory("Alberta", north_america),
    "Ontario": Territory("Ontario", north_america),
    "Quebec": Territory("Quebec", north_america),
    "Greenland": Territory("Greenland", north_america),
    "W. U.S.": Territory("W. U.S.", north_america),
    "E. U.S.": Territory("E. U.S.", north_america),
    "C. America": Territory("C. America", north_america),
    "Venezuela": Territory("Venezuela", south_america),
    "Brazil": Territory("Brazil", south_america),
    "Peru": Territory("Peru", south_america),
    "Argentina": Territory("Argentina", south_america),
    "Iceland": Territory("Iceland", europe),
    "G. Britain": Territory("G. Britain", europe),
    "N. Europe": Territory("N. Europe", europe),
    "Scandinavia": Territory("Scandinavia", europe),
    "Ukraine": Territory("Ukraine", europe),
    "S. Europe": Territory("S. Europe", europe),
    "N. Africa": Territory("N. Africa", africa),
    "Egypt": Territory("Egypt", africa),
    "E. Africa": Territory("E. Africa", africa),
    "Congo": Territory("Congo", africa),
    "S. Africa": Territory("S. Africa", africa),
    "Siberia": Territory("Siberia", asia),
    "Ural": Territory("Ural", asia),
    "Afghanistan": Territory("Afghanistan", asia),
    "M. East": Territory("M. East", asia),
    "India": Territory("India", asia),
    "China": Territory("China", asia),
    "Mongolia": Territory("Mongolia", asia),
    "Japan": Territory("Japan", asia),
    "Kamchatka": Territory("Kamchatka", asia),
    "Indonesia": Territory("Indonesia", australia),
    "W. Australia": Territory("W. Australia", australia),
    "E. Australia": Territory("E. Australia", australia),
    "New Guinea": Territory("New Guinea", australia)
}

# Add adjacent territories for each territory object
territories2["Alaska"].add_adjacent_territory(territories2["N. W. Territory"])
territories2["Alaska"].add_adjacent_territory(territories2["Alberta"])


# Example for one territory
territories2["N. W. Territory"].add_adjacent_territory(territories2["Alaska"])
territories2["N. W. Territory"].add_adjacent_territory(territories2["Alberta"])
territories2["N. W. Territory"].add_adjacent_territory(territories2["Ontario"])
territories2["N. W. Territory"].add_adjacent_territory(territories2["Greenland"])

# --- NORTH AMERICA ---
territories2["Alaska"].add_adjacent_territory(territories2["N. W. Territory"])
territories2["Alaska"].add_adjacent_territory(territories2["Alberta"])
territories2["Alaska"].add_adjacent_territory(territories2["Kamchatka"])

territories2["N. W. Territory"].add_adjacent_territory(territories2["Alaska"])
territories2["N. W. Territory"].add_adjacent_territory(territories2["Alberta"])
territories2["N. W. Territory"].add_adjacent_territory(territories2["Ontario"])
territories2["N. W. Territory"].add_adjacent_territory(territories2["Greenland"])

territories2["Greenland"].add_adjacent_territory(territories2["N. W. Territory"])
territories2["Greenland"].add_adjacent_territory(territories2["Ontario"])
territories2["Greenland"].add_adjacent_territory(territories2["Quebec"])
territories2["Greenland"].add_adjacent_territory(territories2["Iceland"])

territories2["Alberta"].add_adjacent_territory(territories2["Alaska"])
territories2["Alberta"].add_adjacent_territory(territories2["N. W. Territory"])
territories2["Alberta"].add_adjacent_territory(territories2["Ontario"])
territories2["Alberta"].add_adjacent_territory(territories2["W. U.S."])

territories2["Ontario"].add_adjacent_territory(territories2["N. W. Territory"])
territories2["Ontario"].add_adjacent_territory(territories2["Greenland"])
territories2["Ontario"].add_adjacent_territory(territories2["Quebec"])
territories2["Ontario"].add_adjacent_territory(territories2["E. U.S."])
territories2["Ontario"].add_adjacent_territory(territories2["W. U.S."])
territories2["Ontario"].add_adjacent_territory(territories2["Alberta"])

territories2["Quebec"].add_adjacent_territory(territories2["Greenland"])
territories2["Quebec"].add_adjacent_territory(territories2["Ontario"])
territories2["Quebec"].add_adjacent_territory(territories2["E. U.S."])

territories2["W. U.S."].add_adjacent_territory(territories2["Alberta"])
territories2["W. U.S."].add_adjacent_territory(territories2["Ontario"])
territories2["W. U.S."].add_adjacent_territory(territories2["E. U.S."])
territories2["W. U.S."].add_adjacent_territory(territories2["C. America"])

territories2["E. U.S."].add_adjacent_territory(territories2["Quebec"])
territories2["E. U.S."].add_adjacent_territory(territories2["Ontario"])
territories2["E. U.S."].add_adjacent_territory(territories2["W. U.S."])
territories2["E. U.S."].add_adjacent_territory(territories2["C. America"])

territories2["C. America"].add_adjacent_territory(territories2["W. U.S."])
territories2["C. America"].add_adjacent_territory(territories2["E. U.S."])
territories2["C. America"].add_adjacent_territory(territories2["Venezuela"])

# --- SOUTH AMERICA ---
territories2["Venezuela"].add_adjacent_territory(territories2["C. America"])
territories2["Venezuela"].add_adjacent_territory(territories2["Brazil"])
territories2["Venezuela"].add_adjacent_territory(territories2["Peru"])

territories2["Brazil"].add_adjacent_territory(territories2["Venezuela"])
territories2["Brazil"].add_adjacent_territory(territories2["Peru"])
territories2["Brazil"].add_adjacent_territory(territories2["Argentina"])
territories2["Brazil"].add_adjacent_territory(territories2["N. Africa"])

territories2["Peru"].add_adjacent_territory(territories2["Venezuela"])
territories2["Peru"].add_adjacent_territory(territories2["Brazil"])
territories2["Peru"].add_adjacent_territory(territories2["Argentina"])

territories2["Argentina"].add_adjacent_territory(territories2["Peru"])
territories2["Argentina"].add_adjacent_territory(territories2["Brazil"])

# --- EUROPE ---
territories2["Iceland"].add_adjacent_territory(territories2["Greenland"])
territories2["Iceland"].add_adjacent_territory(territories2["G. Britain"])
territories2["Iceland"].add_adjacent_territory(territories2["Scandinavia"])

territories2["Scandinavia"].add_adjacent_territory(territories2["Iceland"])
territories2["Scandinavia"].add_adjacent_territory(territories2["G. Britain"])
territories2["Scandinavia"].add_adjacent_territory(territories2["N. Europe"])
territories2["Scandinavia"].add_adjacent_territory(territories2["Ukraine"])

territories2["G. Britain"].add_adjacent_territory(territories2["Iceland"])
territories2["G. Britain"].add_adjacent_territory(territories2["Scandinavia"])
territories2["G. Britain"].add_adjacent_territory(territories2["N. Europe"])

territories2["N. Europe"].add_adjacent_territory(territories2["G. Britain"])
territories2["N. Europe"].add_adjacent_territory(territories2["Scandinavia"])
territories2["N. Europe"].add_adjacent_territory(territories2["Ukraine"])
territories2["N. Europe"].add_adjacent_territory(territories2["S. Europe"])

territories2["S. Europe"].add_adjacent_territory(territories2["N. Europe"])
territories2["S. Europe"].add_adjacent_territory(territories2["Ukraine"])
territories2["S. Europe"].add_adjacent_territory(territories2["M. East"])
territories2["S. Europe"].add_adjacent_territory(territories2["Egypt"])
territories2["S. Europe"].add_adjacent_territory(territories2["N. Africa"])

territories2["Ukraine"].add_adjacent_territory(territories2["Scandinavia"])
territories2["Ukraine"].add_adjacent_territory(territories2["N. Europe"])
territories2["Ukraine"].add_adjacent_territory(territories2["S. Europe"])
territories2["Ukraine"].add_adjacent_territory(territories2["M. East"])
territories2["Ukraine"].add_adjacent_territory(territories2["Afghanistan"])
territories2["Ukraine"].add_adjacent_territory(territories2["Ural"])

# --- AFRICA ---
territories2["N. Africa"].add_adjacent_territory(territories2["Brazil"])
territories2["N. Africa"].add_adjacent_territory(territories2["S. Europe"])
territories2["N. Africa"].add_adjacent_territory(territories2["Egypt"])
territories2["N. Africa"].add_adjacent_territory(territories2["E. Africa"])
territories2["N. Africa"].add_adjacent_territory(territories2["Congo"])

territories2["Egypt"].add_adjacent_territory(territories2["N. Africa"])
territories2["Egypt"].add_adjacent_territory(territories2["S. Europe"])
territories2["Egypt"].add_adjacent_territory(territories2["M. East"])
territories2["Egypt"].add_adjacent_territory(territories2["E. Africa"])

territories2["E. Africa"].add_adjacent_territory(territories2["Egypt"])
territories2["E. Africa"].add_adjacent_territory(territories2["M. East"])
territories2["E. Africa"].add_adjacent_territory(territories2["N. Africa"])
territories2["E. Africa"].add_adjacent_territory(territories2["Congo"])
territories2["E. Africa"].add_adjacent_territory(territories2["S. Africa"])

territories2["Congo"].add_adjacent_territory(territories2["N. Africa"])
territories2["Congo"].add_adjacent_territory(territories2["E. Africa"])
territories2["Congo"].add_adjacent_territory(territories2["S. Africa"])

territories2["S. Africa"].add_adjacent_territory(territories2["Congo"])
territories2["S. Africa"].add_adjacent_territory(territories2["E. Africa"])

# --- ASIA ---
territories2["Ural"].add_adjacent_territory(territories2["Ukraine"])
territories2["Ural"].add_adjacent_territory(territories2["Afghanistan"])
territories2["Ural"].add_adjacent_territory(territories2["China"])
territories2["Ural"].add_adjacent_territory(territories2["Siberia"])

territories2["Siberia"].add_adjacent_territory(territories2["Ural"])
territories2["Siberia"].add_adjacent_territory(territories2["China"])
territories2["Siberia"].add_adjacent_territory(territories2["Mongolia"])

territories2["Kamchatka"].add_adjacent_territory(territories2["Mongolia"])
territories2["Kamchatka"].add_adjacent_territory(territories2["Japan"])
territories2["Kamchatka"].add_adjacent_territory(territories2["Alaska"])

territories2["Afghanistan"].add_adjacent_territory(territories2["Ukraine"])
territories2["Afghanistan"].add_adjacent_territory(territories2["Ural"])
territories2["Afghanistan"].add_adjacent_territory(territories2["China"])
territories2["Afghanistan"].add_adjacent_territory(territories2["India"])
territories2["Afghanistan"].add_adjacent_territory(territories2["M. East"])

territories2["China"].add_adjacent_territory(territories2["Afghanistan"])
territories2["China"].add_adjacent_territory(territories2["Ural"])
territories2["China"].add_adjacent_territory(territories2["Siberia"])
territories2["China"].add_adjacent_territory(territories2["Mongolia"])
territories2["China"].add_adjacent_territory(territories2["India"])

territories2["Mongolia"].add_adjacent_territory(territories2["Siberia"])
territories2["Mongolia"].add_adjacent_territory(territories2["Kamchatka"])
territories2["Mongolia"].add_adjacent_territory(territories2["Japan"])
territories2["Mongolia"].add_adjacent_territory(territories2["China"])

territories2["Japan"].add_adjacent_territory(territories2["Kamchatka"])
territories2["Japan"].add_adjacent_territory(territories2["Mongolia"])

territories2["M. East"].add_adjacent_territory(territories2["S. Europe"])
territories2["M. East"].add_adjacent_territory(territories2["Ukraine"])
territories2["M. East"].add_adjacent_territory(territories2["Afghanistan"])
territories2["M. East"].add_adjacent_territory(territories2["India"])
territories2["M. East"].add_adjacent_territory(territories2["Egypt"])
territories2["M. East"].add_adjacent_territory(territories2["E. Africa"])

territories2["India"].add_adjacent_territory(territories2["M. East"])
territories2["India"].add_adjacent_territory(territories2["Afghanistan"])
territories2["India"].add_adjacent_territory(territories2["China"])

# --- AUSTRALIA ---
territories2["Indonesia"].add_adjacent_territory(territories2["New Guinea"])
territories2["Indonesia"].add_adjacent_territory(territories2["W. Australia"])

territories2["New Guinea"].add_adjacent_territory(territories2["Indonesia"])
territories2["New Guinea"].add_adjacent_territory(territories2["W. Australia"])
territories2["New Guinea"].add_adjacent_territory(territories2["E. Australia"])

territories2["W. Australia"].add_adjacent_territory(territories2["Indonesia"])
territories2["W. Australia"].add_adjacent_territory(territories2["New Guinea"])
territories2["W. Australia"].add_adjacent_territory(territories2["E. Australia"])

territories2["E. Australia"].add_adjacent_territory(territories2["New Guinea"])
territories2["E. Australia"].add_adjacent_territory(territories2["W. Australia"])
# Note: The above code is an example. You'll need to add the actual adjacent territories based on the game rules and the image provided.

import customtkinter as ctk
from PIL import Image, ImageTk
import random

# Global variables
game_instance = None
root_window = None
territory_buttons = None
current_player = None
current_player_label = None
attack_button = None
place_troop_button = None
move_troops_button = None
small_section = None

def create_territory_buttons(canvas, current_player):
    global territories2, player, ai
    # Define the coordinates and shapes of the territories
    territories = {
        "Alaska": [(10, 50), (100, 50), (100, 150), (10, 150)],
        "N. W. Territory": [(70, 70), (240, 70), (240, 195), (70, 195)],
        "Alberta": [(100, 100), (200, 100), (200, 225), (100, 225)],
        "Ontario": [(170, 80), (295, 80), (295, 280), (170, 280)],
        "Quebec": [(255, 150), (380, 150), (380, 300), (255, 300)],
        "Greenland": [(350, 50), (475, 50), (475, 150), (350, 150)],
        "W. U.S.": [(100, 175), (250, 175), (250, 300), (100, 300)],
        "E. U.S.": [(220, 230), (370, 230), (370, 330), (220, 330)],
        "C. America": [(150, 300), (225, 300), (225, 400), (150, 400)],
        "Venezuela": [(250, 400), (350, 400), (350, 500), (250, 500)],
        "Brazil": [(300, 450), (450, 450), (450, 550), (300, 550)],
        "Peru": [(220, 500), (320, 500), (320, 600), (220, 600)],
        "Argentina": [(200, 620), (350, 620), (350, 720), (200, 720)],
        "Iceland": [(470, 100), (570, 100), (570, 175), (470, 175)],
        "G. Britain": [(420, 170), (520, 170), (520, 270), (420, 270)],
        "N. Europe": [(550, 190), (650, 190), (650, 290), (550, 290)],
        "Scandinavia": [(550, 50), (650, 50), (650, 150), (550, 150)],
        "Ukraine": [(640, 190), (740, 190), (740, 265), (640, 265)],
        "S. Europe": [(520, 300), (620, 300), (620, 400), (520, 400)],
        "N. Africa": [(500, 450), (600, 450), (600, 500), (500, 500)],
        "Egypt": [(550, 400), (650, 400), (650, 500), (550, 500)],
        "E. Africa": [(650, 470), (680, 470), (680, 570), (650, 570)],
        "Congo": [(620, 580), (650, 580), (650, 680), (620, 680)],
        "S. Africa": [(620, 630), (650, 630), (650, 730), (620, 730)],
        "Siberia": [(840, 100), (940, 100), (940, 200), (840, 200)],
        "Ural": [(770, 150), (870, 150), (870, 250), (770, 250)],
        "Afghanistan": [(750, 270), (850, 270), (850, 370), (750, 370)],
        "M. East": [(670, 370), (770, 370), (770, 470), (670, 470)],
        "India": [(800, 390), (900, 390), (900, 490), (800, 490)],
        "China": [(870, 330), (970, 330), (970, 430), (870, 430)],
        "Mongolia": [(910, 288), (1010, 288), (1010, 388), (910, 388)],
        "Japan": [(1050, 270), (1150, 270), (1150, 370), (1050, 370)],
        "Kamchatka": [(1050, 110), (1150, 110), (1150, 210), (1050, 210)],
        "Indonesia": [(950, 500), (1050, 500), (1050, 600), (950, 600)],
        "W. Australia": [(970, 630), (1070, 630), (1070, 730), (970, 730)],
        "E. Australia": [(1090, 670), (1190, 670), (1190, 770), (1090, 770)],
        "New Guinea": [(1050, 480), (1150, 480), (1150, 580), (1050, 580)]
    }

    # Create the territory buttons
    territory_buttons = {}
    for name, coords in territories.items():
        x1, y1 = coords[0]
        x2, y2 = coords[2]
        button_x = (x1 + x2) // 2
        button_y = (y1 + y2) // 2
        territory = territories2[name]
        button_color = "gray"
        if territory.owner is not None:
            button_color = "green" if territory.owner == player else "red"
        
        button = ctk.CTkButton(canvas, text=str(territory.armies), width=20, height=20, corner_radius=10,
                   fg_color=button_color, hover_color="light gray", text_color="black")
        button.place(x=button_x - 10, y=button_y - 10)
        button.bind("<Button-1>", lambda event, territory=territory: claim_territory(territory, territory_buttons))
        button.territory = territory
        territory_buttons[name] = button

    return territory_buttons


def update_territory_buttons(territory_buttons, territory):
    button = territory_buttons[territory.name]
    button.configure(text=str(territory.armies),
                     fg_color="gray" if territory.owner is None else ("green" if territory.owner == player else "red"))


def switch_player():
    global current_player, player, ai, territories2, root_window, territory_buttons
    
    # Check if all territories are owned by the same player
    all_territories_owned = all(territory.owner == current_player for territory in territories2.values())
    
    if all_territories_owned:
        # Display a small window announcing the winner
        winner_window = ctk.CTkToplevel()
        winner_window.title("Game Over")
        winner_window.geometry("300x100")
        winner_label = ctk.CTkLabel(winner_window, text=f"Winner: {current_player.name}")
        winner_label.pack(pady=20)
        return
    
    # Switch to the next player's turn
    if current_player == player:
        current_player = ai
        current_player_label.configure(text=f"{ai.name}'s Turn")
        # Disable buttons during AI turn
        disable_action_buttons()
        # Schedule AI move after a short delay
        root_window.after(1000, execute_ai_turn)
    else:
        current_player = player
        current_player_label.configure(text=f"{player.name}'s Turn")
        # Enable buttons for player turn
        enable_action_buttons()


def disable_action_buttons():
    """Disable all action buttons during AI turn"""
    attack_button.configure(state="disabled")
    place_troop_button.configure(state="disabled")
    move_troops_button.configure(state="disabled")


def enable_action_buttons():
    """Enable all action buttons for player turn"""
    attack_button.configure(state="normal")
    place_troop_button.configure(state="normal")
    move_troops_button.configure(state="normal")


def execute_ai_turn():
    """Execute the AI's turn automatically"""
    global current_player, ai, player, territory_buttons, game_instance
    
    # Create a status label to show what AI is doing
    status_label = ctk.CTkLabel(small_section, text="AI is thinking...", font=("Helvetica", 14))
    status_label.pack(pady=10)
    root_window.update()
    
    # AI chooses territory if needed (during initial phase)
    unclaimed_territories = [t for t in territories2.values() if t.owner is None]
    if unclaimed_territories:
        # AI claims a random territory
        territory = random.choice(unclaimed_territories)
        territory.set_owner(ai)
        ai.add_territory(territory)
        update_territory_buttons(territory_buttons, territory)
        status_label.configure(text=f"AI claimed {territory.name}")
        root_window.update()
        root_window.after(1500, lambda: status_label.destroy())
        root_window.after(1500, switch_player)
        return
    
    # AI makes a move using minimax algorithm
    if game_instance:
        try:
            status_label.configure(text="AI is calculating best move...")
            root_window.update()
            
            # Get AI's best move
            move = ai.choose_and_apply_move(game_instance, player)
            
            # Update GUI based on move
            if move:
                action = move.get('action', '')
                status_label.configure(text=f"AI performed {action} action")
                
                # Update all affected territory buttons
                if 'from_territory' in move:
                    from_terr = move['from_territory']
                    if hasattr(from_terr, 'name'):
                        update_territory_buttons(territory_buttons, from_terr)
                
                if 'to_territory' in move:
                    to_terr = move['to_territory']
                    if hasattr(to_terr, 'name'):
                        update_territory_buttons(territory_buttons, to_terr)
                
                root_window.update()
        except Exception as e:
            print(f"AI move error: {e}")
            status_label.configure(text="AI skipped turn")
    
    # Clean up and switch back to player
    root_window.after(2000, lambda: status_label.destroy())
    root_window.after(2000, switch_player)


def claim_territory(territory, territory_buttons):
    global current_player, player, ai
    
    # Only allow claiming during player's turn
    if current_player != player:
        return
    
    if territory.owner is None:
        territory.set_owner(current_player)
        current_player.add_territory(territory)
        update_territory_buttons(territory_buttons, territory)
        switch_player()
    else:
        print(f"{territory.name} is already owned by {territory.owner.name}")


def place_troops(territory_buttons, small_section, root, current_player):
    # Only allow placing troops during player's turn
    if current_player != player:
        return
        
    # Display a label asking the player to choose a territory
    choose_territory_label = ctk.CTkLabel(small_section, text="Choose a territory to place troops")
    choose_territory_label.pack(pady=10)

    def select_territory(territory):
        nonlocal choose_territory_label

        if territory.owner is not None and territory.owner.name == current_player.name:
            choose_territory_label.pack_forget()

            troops_window = ctk.CTkToplevel(root)
            troops_window.attributes("-topmost", True)
            troops_window.title("Place Troops")

            troops_label = ctk.CTkLabel(troops_window, text="Enter the number of troops (1-3):")
            troops_label.pack(pady=10)

            troops_entry = ctk.CTkEntry(troops_window)
            troops_entry.pack(pady=10)

            def place_troops_callback():
                nonlocal troops_window

                troops_count = troops_entry.get()

                try:
                    troops_count = int(troops_count)
                    if 1 <= troops_count <= 3:
                        territory.armies += troops_count
                        update_territory_buttons(territory_buttons, territory)
                        troops_window.destroy()
                        switch_player()
                    else:
                        ctk.CTkLabel(troops_window, text="Invalid input. Please enter a number between 1 and 3.").pack(pady=10)
                except ValueError:
                    ctk.CTkLabel(troops_window, text="Invalid input. Please enter a number.").pack(pady=10)

            confirm_button = ctk.CTkButton(troops_window, text="Place Troops", command=place_troops_callback)
            confirm_button.pack(pady=10)

        else:
            ctk.CTkLabel(small_section, text=f"{territory.name} is not owned by {current_player.name}").pack(pady=10)

    def handle_button_click(event, territory):
        select_territory(territory)

    for button in territory_buttons.values():
        button.bind("<Button-1>", lambda event, territory=button.territory: handle_button_click(event, territory))


def move_troops(territory_buttons, small_section, root, current_player):
    global territories2

    # Only allow moving troops during player's turn
    if current_player != player:
        return

    choose_territory_label = ctk.CTkLabel(small_section, text="Choose a territory to move troops from")
    choose_territory_label.pack(pady=10)

    def select_from_territory(territory):
        nonlocal choose_territory_label

        if territory.owner is not None and territory.owner.name == current_player.name:
            choose_territory_label.pack_forget()

            choose_territory_label = ctk.CTkLabel(small_section, text="Choose a territory to move troops to")
            choose_territory_label.pack(pady=10)

            def select_to_territory(to_territory):
                nonlocal choose_territory_label

                if (to_territory in territory.adjacent_territories and 
                    to_territory.owner is not None and 
                    to_territory.owner.name == current_player.name):
                    
                    choose_territory_label.pack_forget()

                    troops_window = ctk.CTkToplevel(root)
                    troops_window.title("Move Troops")
                    troops_window.attributes("-topmost", True)

                    troops_label = ctk.CTkLabel(troops_window, text=f"Number of troops in {territory.name}: {territory.armies}")
                    troops_label.pack(pady=10)

                    troops_entry = ctk.CTkEntry(troops_window)
                    troops_entry.pack(pady=10)

                    def move_troops_callback():
                        nonlocal troops_window

                        troops_count = troops_entry.get()

                        try:
                            troops_count = int(troops_count)
                            if 1 <= troops_count < territory.armies:
                                territory.armies -= troops_count
                                to_territory.armies += troops_count
                                update_territory_buttons(territory_buttons, territory)
                                update_territory_buttons(territory_buttons, to_territory)
                                troops_window.destroy()
                                switch_player()
                            else:
                                ctk.CTkLabel(troops_window, text="Invalid input. Please enter a number between 1 and one less than the total troops.").pack(pady=10)
                        except ValueError:
                            ctk.CTkLabel(troops_window, text="Invalid input. Please enter a number.").pack(pady=10)

                    confirm_button = ctk.CTkButton(troops_window, text="Move Troops", command=move_troops_callback)
                    confirm_button.pack(pady=10)

                else:
                    if to_territory not in territory.adjacent_territories:
                        ctk.CTkLabel(small_section, text=f"{to_territory.name} is not adjacent to {territory.name}").pack(pady=10)
                    elif to_territory.owner is None or to_territory.owner.name != current_player.name:
                        ctk.CTkLabel(small_section, text=f"{to_territory.name} is not owned by {current_player.name}").pack(pady=10)

            for button in territory_buttons.values():
                button.bind("<Button-1>", lambda event, territory=button.territory: select_to_territory(territory))

        else:
            ctk.CTkLabel(small_section, text=f"{territory.name} is not owned by {current_player.name}").pack(pady=10)

    for button in territory_buttons.values():
        button.bind("<Button-1>", lambda event, territory=button.territory: select_from_territory(territory))


def attack_territory(territory_buttons, small_section, root, current_player):
    global territories2

    # Only allow attacking during player's turn
    if current_player != player:
        return

    choose_territory_label = ctk.CTkLabel(small_section, text="Choose a territory to attack from")
    choose_territory_label.pack(pady=10)

    def select_from_territory(territory):
        nonlocal choose_territory_label

        if territory.owner == current_player and territory.armies > 1:
            choose_territory_label.pack_forget()

            choose_territory_label = ctk.CTkLabel(small_section, text="Choose a territory to attack")
            choose_territory_label.pack(pady=10)

            def select_to_territory(to_territory):
                nonlocal choose_territory_label

                if to_territory.owner != current_player:
                    choose_territory_label.pack_forget()

                    attack_window = ctk.CTkToplevel(root)
                    attack_window.title("Attack")
                    attack_window.attributes("-topmost", True)

                    troops_label = ctk.CTkLabel(attack_window, text=f"Number of troops in {territory.name}: {territory.armies}")
                    troops_label.pack(pady=10)

                    troops_entry = ctk.CTkEntry(attack_window)
                    troops_entry.pack(pady=10)

                    def perform_attack():
                        nonlocal attack_window

                        troops_count = troops_entry.get()

                        try:
                            troops_count = int(troops_count)
                            if 1 <= troops_count < territory.armies:
                                territory.armies -= troops_count
                                update_territory_buttons(territory_buttons, territory)

                                attack_result = resolve_attack(territory, to_territory, troops_count)

                                if attack_result:
                                    to_territory.set_owner(current_player)
                                    to_territory.armies = troops_count
                                    update_territory_buttons(territory_buttons, to_territory)
                                else:
                                    territory.armies = 1

                                attack_window.destroy()
                                switch_player()
                            else:
                                ctk.CTkLabel(attack_window, text="Invalid input. Please enter a number between 1 and one less than the total troops.").pack(pady=10)
                        except ValueError:
                            ctk.CTkLabel(attack_window, text="Invalid input. Please enter a number.").pack(pady=10)

                    confirm_button = ctk.CTkButton(attack_window, text="Attack", command=perform_attack)
                    confirm_button.pack(pady=10)

                else:
                    ctk.CTkLabel(small_section, text=f"{to_territory.name} is owned by {current_player.name}").pack(pady=10)

            for button in territory_buttons.values():
                button.bind("<Button-1>", lambda event, territory=button.territory: select_to_territory(territory))

        else:
            if territory.owner != current_player:
                ctk.CTkLabel(small_section, text=f"{territory.name} is not owned by {current_player.name}").pack(pady=10)
            else:
                ctk.CTkLabel(small_section, text=f"{territory.name} has only 1 troop").pack(pady=10)

    for button in territory_buttons.values():
        button.bind("<Button-1>", lambda event, territory=button.territory: select_from_territory(territory))


def resolve_attack(from_territory, to_territory, troops_count):
    attacker_dice = roll_dice(min(troops_count, 3))
    defender_dice = roll_dice(min(to_territory.armies, 2))
    attacker_wins = compare_dice_rolls(attacker_dice, defender_dice)

    result_window = ctk.CTkToplevel()
    result_window.title("Attack Result")

    attacker_label = ctk.CTkLabel(result_window, text=f"{from_territory.owner.name}'s Dice Rolls: {', '.join(map(str, attacker_dice))}")
    attacker_label.pack(pady=5)

    defender_label = ctk.CTkLabel(result_window, text=f"{to_territory.owner.name}'s Dice Rolls: {', '.join(map(str, defender_dice))}")
    defender_label.pack(pady=5)

    if attacker_wins:
        result_label = ctk.CTkLabel(result_window, text=f"{from_territory.owner.name} wins the attack!")
    else:
        result_label = ctk.CTkLabel(result_window, text=f"{to_territory.owner.name} wins the attack!")
    result_label.pack(pady=10)

    return attacker_wins


def roll_dice(num_dice):
    return sorted([random.randint(1, 6) for _ in range(num_dice)], reverse=True)


def compare_dice_rolls(attacker_rolls, defender_rolls):
    for attacker_roll, defender_roll in zip(attacker_rolls, defender_rolls):
        if attacker_roll > defender_roll:
            return True
        elif attacker_roll < defender_roll:
            return False
    return len(attacker_rolls) > len(defender_rolls)


def gameWindow(winner):
    global current_player_label, current_player, root_window, territory_buttons
    global attack_button, place_troop_button, move_troops_button, small_section
    global game_instance, player, ai, territories2
    
    # Import the Game class (make sure Game.py is in the same directory)
    from Game import Game
    
    # Create continents list if not already created
    continents_list = [north_america, europe, asia, africa, australia, south_america]
    
    # Initialize the game instance
    game_instance = Game(player, ai, territories2, continents_list)
    
    root_window = ctk.CTk()
    root_window.title("RiskGame")
    root_window.geometry("1600x800")

    frame = ctk.CTkFrame(master=root_window, width=1600, height=800)
    frame.pack(pady=0, padx=0, fill="both", expand=True)

    large_section = ctk.CTkCanvas(master=frame, width=1200, height=800, highlightthickness=0)
    large_section.place(x=0, y=0)

    map_image = Image.open("map.png")
    section_width = 1200
    section_height = 800
    image_width, image_height = map_image.size
    zoom_factor = section_width / image_width

    resized_image = map_image.resize((int(image_width * zoom_factor), int(image_height * zoom_factor)), Image.Resampling.LANCZOS)
    map_photo = ImageTk.PhotoImage(resized_image)

    large_section.create_image(0, 0, anchor="nw", image=map_photo)
    large_section.image = map_photo

    global current_player
    if winner.lower() == player.name.lower():
        current_player = player
    else:
        current_player = ai

    territory_buttons = create_territory_buttons(large_section, current_player)

    small_section = ctk.CTkFrame(master=frame, width=400, height=800)
    small_section.place(x=1200, y=0)

    current_player_label = ctk.CTkLabel(small_section, text=f"{current_player.name}'s Turn", width=380)
    current_player_label.pack(pady=10, fill="x")

    attack_button = ctk.CTkButton(small_section, text="Attack", width=380, 
                                   command=lambda: attack_territory(territory_buttons, small_section, root_window, current_player))
    attack_button.pack(pady=10, fill="x")

    place_troop_button = ctk.CTkButton(small_section, text="Place Troop", width=380, 
                                        command=lambda: place_troops(territory_buttons, small_section, root_window, current_player))
    place_troop_button.pack(pady=10, fill="x")

    move_troops_button = ctk.CTkButton(small_section, text="End Turn", width=380, 
                                        command=lambda: switch_player())
    move_troops_button.pack(pady=10, fill="x")

    # If AI goes first, trigger its turn
    if current_player == ai:
        disable_action_buttons()
        root_window.after(1000, execute_ai_turn)

    root_window.mainloop()

# gameWindow("AI")

