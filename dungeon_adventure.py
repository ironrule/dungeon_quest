import random

def main():
    def setup_player():
        """
        Prompts the user to create their player profile.

        Returns:
            dict: A dictionary containing player stats with the following keys:
                - "name" (str): Player's name (entered by user)
                - "health" (int): Starting health, set to 10
                - "inventory" (list): Starts as an empty list
        Example:
            >>> setup_player()
            Enter your name: Ailene
            {'name': 'Ailene', 'health': 10, 'inventory': []}
        """
        # Ask the user for their name using input()
        print("Hello Adventurer! What is your name?")
        name = input("Enter your name: ")

        # Initialize a dictionary with keys: "name", "health", and "inventory"
        player_info = {
            "name": name,
            "health": 10,
            "inventory": []
        }
        # Return the dictionary
        return player_info

    def create_treasures():
        """
        Creates a dictionary of treasures, where each treasure has a value.

        Returns:
            dict: Example:
                {
                    "gold coin": 5,
                    "ruby": 10,
                    "ancient scroll": 7,
                    "emerald": 9,
                    "silver ring": 4
                }
        Tip:
            You can customize treasures or randomize the values using random.randint(3, 12).
        """
        # Create a dictionary of treasure names and integer values
        treasures = {
            "platinum bar": random.randint(8, 12),
            "agate": random.randint(3, 5),
            "silver ring": random.randint(5, 8),
            "gold monacle": random.randint(7, 10),
            "mysterious vial": random.randint(4, 6)
        }
        # Return the dictionary
        return treasures


    def display_options(room_number):
        """
        Displays available options for the player in the current room.

        Args:
            room_number (int): The current room number.

        Output Example:
            You are in room 3.
            What would you like to do?
            1. Search for treasure
            2. Move to next room
            3. Check health and inventory
            4. Quit the game
        """
        # Print the room number and the 4 menu options listed above
        print(f"You are in room {room_number}\nWhat would you like to do?")
        print("1. Search for treasure \n2. Move to next room \n3. Check health and inventory \n4. Quit the game")



    def search_room(player, treasures):
        """
        Simulates searching the current room.

        If the outcome is 'treasure', the player gains an item from treasures.
        If the outcome is 'trap', the player loses 2 health points.

        Args:
            player (dict): The player's current stats.
            treasures (dict): Dictionary of available treasures.

        Behavior:
            - Randomly choose outcome = "treasure" or "trap"
            - If treasure: choose a random treasure, add to player's inventory,
              and print what was found.
            - If trap: subtract 2 from player's health and print a warning.
        """
        # Randomly assign outcome = random.choice(["treasure", "trap"])
        # Write an if/else to handle treasure vs trap outcomes
        # Update player dictionary accordingly
        # Print messages describing what happened
        outcome = random.choice(["treasure", "trap"])
        if outcome == "treasure":
            random_treasure = random.choice(list(treasures.keys()))
            player["inventory"].append(random_treasure)
            print(f"You found a {random_treasure}!")
        else:
            player["health"] -= 2
            print("You set off a trap! You were injured and lost 2 health points.")

    def check_status(player):
        """
        Displays the player’s current health and inventory.

        Args:
            player (dict): Player stats including health and inventory.

        Example Output:
            Health: 8
            Inventory: ruby, gold coin
        or:
            Health: 10
            Inventory: You have no items yet.
        """
        # Print player health
        # If the inventory list is not empty, print items joined by commas
        # Otherwise print “You have no items yet.”
        print(f"Health: {player['health']}")
        if player["inventory"]:
            print("Inventory: " + ", ".join(player["inventory"]))
        else:
            print("Inventory: You have no items yet.")

    def end_game(player, treasures):
        """
        Ends the game and displays a summary.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary for item value lookup.

        Output:
            Prints player’s final health, inventory contents, and total score value.
        """
        # Calculate total score by summing the value of collected treasures
        # Print final health, items, and total value
        # End with a message like "Game Over! Thanks for playing."
        total_value = 0
        for item in player["inventory"]:
            total_value += treasures[item]
        print(f"Final Health: {player['health']}")
        if player["inventory"] == []:
            print("Inventory: You have no items.")
        else:
            print("Inventory: " + ", ".join(player["inventory"]))
        print(f"Total Score Value: {total_value}")
        print("Game Over! Thanks for playing.")
        
    def run_game_loop(player, treasures):
        """
        Main game loop that manages the rooms and player decisions.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary.

        Flow:
            - There are 5 rooms (use for loop range(1, 6))
            - Inside each room, use a while loop for player actions:
                1. Search room
                2. Move to next room
                3. Check status
                4. Quit
            - Health below 1 ends the game early.
        """
        # Loop through 5 rooms (1–5)
        # Inside each room, prompt player choice using input()
        # Use if/elif to handle each choice (1–4)
        # Break or return appropriately when player quits or dies
        # Call end_game() after all rooms are explored
        for room in range(1, 6):
            while True:
                display_options(str(room))
                choice = input("Enter your choice (1-4): ")
                if choice == "1":
                    search_room(player, treasures)
                    if player["health"] < 1:
                        print("You have died!")
                        end_game(player, treasures)
                        return
                elif choice == "2":
                    if room == 5:
                        print("You have escaped the dungeon!")
                        end_game(player, treasures)
                    else:
                        print("Moving to the next room...")
                    break
                elif choice == "3":
                    check_status(player)
                elif choice == "4":
                    print("Quitting the game...")
                    end_game(player, treasures)
                    return
                else:
                    print("Invalid choice. Please select a valid option.")

    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    run_game_loop(player, treasures)

if __name__ == "__main__":
    main()
