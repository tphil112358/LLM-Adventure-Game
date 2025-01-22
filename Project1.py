import requests
import json
import time
import os
from abc import ABC, abstractmethod
import random
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from combat import Player, Combat

def OllamaParser(message): # Dale's Domain
    # Set up the base URL for the local Ollama API
    pass

def run_round(prompt, choices):
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

    OllamaParser(context,player_choice)
    narrative, consequences = (f"The player made choice #{player_choice}.") # Narrative is a string, consequences is a formatted array.
    print(narrative)
    if consequences[0] == "b": # Begin battle
        start_combat(consequences[1],consequences[2])
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
                player.sethealth(player.gethealth() - consequences[3 + (3 * looped)])
            elif consequences[1 + (3 * looped)] == "hg": # Consequence was the player gains health
                print(f"{consequences[2 + (3 * looped)]}. Gain {consequences[3 + (3 * looped)]} health")
                player.sethealth(player.gethealth() + consequences[3 + (3 * looped)])
            elif consequences[1 + (3 * looped)] == "ii": # Consequence was an item was found, add it to inventory
                print(f"You find a {consequences[2 + (3 * looped)]}! Use it to {item.description(consequences[2 + (3 * looped)])}")
                player.inventoryadditem(consequences[3 + (3 * looped)])
            elif consequences[1 + (3 * looped)] == "di": # Consequence was a defense item was found, raise defense-stat
                print(f"You find a {consequences[2 + (3 * looped)]}! Gain {consequences[3 + (3 * looped)]} defence.")
                player.raiseDefense({consequences[3 + (3 * looped)]})
            elif consequences[1 + (3 * looped)] == "ai": # Consequence was a attack item was found, raise attack-stat
                print(f"You find a {consequences[2 + (3 * looped)]}! Gain {consequences[3 + (3 * looped)]} attack.")
                player.raiseAttack({consequences[3 + (3 * looped)]})
            
def handle_ai_interaction(context, user_input):
    result = chain.invoke({"context": context, "answer": user_input})
    return result

def main():
    model = OllamaLLM(model="llama2")
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    escaped = False
    numberOfRounds = 0
    print("Welcome to the dungeon escape game!")
    player_name = input("Enter your hero's name: ")
    player = Player(player_name)
    print(f"Hello, {player.get_name()}! Your adventure begins now!")
    time.sleep(1)

    while (escaped == False):
        prompt, choices = queryAI(narrative, context, choice, config)
        run_round(prompt, choices)
        if Player.getHealth() <= 0:
            print("\nYou were defeated...")
            time.sleep(1)
            print("Game Over.")
        numberOfRounds += 1
    print("\n You won!\n")
    print(f"\n You succesfully escaped the dungeon with {player.gethealth()} health remaining after confronting {numberOfRounds} challanges.")
            

if __name__ == "__main__":
    main()
