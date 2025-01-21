import requests
import json
import time
import os
from abc import ABC, abstractmethod
import random



def OllamaParser(message): # Dale's Domain
    # Set up the base URL for the local Ollama API
    pass

def run_round(prompt, choices):
    """
    Runs a single round of the game outside of combat.
    Parameters:
    prompt: a string describing to the player the situation relevant to their choices.
    choices: a list of strings between 2-4 objects large, which describes the course of action the player can react with.

    Returns nothing.
    """
def question(prompt, choices):
    """
    Runs a single round of the game outside of combat.

    Parameters:
    - prompt (str): A string describing the situation relevant to the player's choices.
    - choices (list of str): A list of strings (2-4 items) describing the available actions.

    Returns:
    - None
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

# Example usage
prompt = "You find yourself in a dark forest. There's a path ahead and a cave to your right. What do you do?"
choices = ["Take the path", "Enter the cave"]

escaped = False
def main():
    while (escaped == False):
        run_round(prompt, choices)
    


main()
