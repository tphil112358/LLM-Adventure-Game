import json
import time
import os
from abc import ABC, abstractmethod
import random
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from Combat import Player, Combat, Enemy, Item
from ollamacenter import handle_conversation,template

def run_round(context, player, prompt, choices):
    """
    Runs a single round of the game outside of combat.
    Parameters:
    prompt: a string describing to the player the situation relevant to their choices.
    choices: a list of strings between 2-4 objects large, which describes the course of action the player can react with.

    Returns a bool representing if the player has successfully escaped the dungeon. 
    """

    if not (2 <= len(choices) <= 4):
        raise ValueError("The choices list must contain between 2 and 4 items.")

    print("\n" + prompt)
    for i, choice in enumerate(choices, start=1):
        print(f"{i}: {choice}")

    choose = False
    while choose == False:
        try:
            player_choice = int(input("\nWhat do you choose? ").strip())
            if 1 <= player_choice <= len(choices):
                print(f"\nYou chose: {choices[player_choice - 1]}")
                choose = True
            else:
                print(f"Please enter a number between 1 and {len(choices)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        
    player_choice_dicta = choices[player_choice - 1]
    narr, consequences, context = handle_conversation(1, context, prompt, player_choice_dicta) # Narrative is a string, consequences is a formatted array.
    narrative, consequences, context = handle_conversation(narr, context, prompt, player_choice_dicta)
    print(narrative)

    if consequences[0] == "b": # Begin battle
        this_player = player
        this_enemy = Enemy(name=consequences[1], hp=consequences[2], attack_stat=consequences[3])
        this_combat = Combat(this_player, this_enemy)
        this_combat.engage_in_battle(this_combat)
    elif consequences[0] == "n": # No consequences
        pass
    elif consequences[0] == "c": # Standard Consequences
        """
        Standard consequences can include any number of effects, and each effect consists of three parts:
        [1] : a string, the formatting code
            "hl" : Health Loss
            "hg" : Health Gain
            "ii" : Item
            "di" : Defense Item
            "ai" : Attack Item
        [2] : a string, either a description of what happened for health loss and gain, or the name of the item
        [3] : an int, either the amount of health to be lost/gained, or the amount the defence or attack stat is being raised, for ii, leave a 0.
        
        The following loop repeats for the number of objects in the consequences array / 3 (Once for each effect)
        Example array:
        consequences = ["c", "hl", "You breathed some of the poison gas.", 10, "ai", "Elvish Sword", 15]
        (The player choose to take a risk by entering the poison gas cloud room to grab an sword they saw, losing 10 health but increasing attack stat by 15.)
        """
        looped = 0
        for c in consequences / 3:
            if consequences[1 + (3 * looped)] == "hl": # Consequence was the player loses health
                print(f"{consequences[2 + (3 * looped)]}. Lose {consequences[3 + (3 * looped)]} health")
                player.set_health(player.get_health() - consequences[3 + (3 * looped)])
            elif consequences[1 + (3 * looped)] == "hg": # Consequence was the player gains health
                print(f"{consequences[2 + (3 * looped)]}. Gain {consequences[3 + (3 * looped)]} health")
                player.set_health(player.get_health() + consequences[3 + (3 * looped)])
            elif consequences[1 + (3 * looped)] == "ii": # Consequence was an item was found, add it to inventory
                print(f"You find a {consequences[2 + (3 * looped)]}! Use it to heal 200 hit points")
                player.inventoryadditem(consequences[3 + (3 * looped)])
            elif consequences[1 + (3 * looped)] == "di": # Consequence was a defense item was found, raise defense-stat
                print(f"You find a {consequences[2 + (3 * looped)]}! Gain {consequences[3 + (3 * looped)]} defence.")
                player.raise_defense({consequences[3 + (3 * looped)]})
            elif consequences[1 + (3 * looped)] == "ai": # Consequence was a attack item was found, raise attack-stat
                print(f"You find a {consequences[2 + (3 * looped)]}! Gain {consequences[3 + (3 * looped)]} attack.")
                player.raise_attack({consequences[3 + (3 * looped)]})


def main():
    os.system("cls")
    model = OllamaLLM(model="llama2")
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    
    escaped = False
    numberOfRounds = 0
    print("Welcome to the dungeon escape game!")
    player_name = input("Enter your hero's name: ")
    player1 = Player(player_name, 100, 20, 10)
    print(f"Hello, {player1.get_name()}! Your adventure begins now!")
    context = "You are lying on a cold stone floor in a dark dungeon. You have no idea how you got here. You see a rusty sword on the ground next to you. You hear a growl in the distance.\n"
    narrative = "You chose to take the sword and stand up.\n"
    print(context)
    time.sleep(1)
    print(narrative)
    time.sleep(1)

    while (escaped == False):
        prompt, choices, context = handle_conversation(0, context, narrative)
        run_round(context, player1, prompt, choices)
        if player1.get_health() <= 0:
            print("\nYou were defeated...")
            time.sleep(1)
            print("Game Over.")
            os.close()
        numberOfRounds += 1
    print("\n You won!\n")
    print(f"\n You successfully escaped the dungeon with {player1.get_health()} health remaining after confronting {numberOfRounds} challenges.")
            

if __name__ == "__main__":
    main()
