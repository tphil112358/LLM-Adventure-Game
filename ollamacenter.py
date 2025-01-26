from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import os
import json

# Define your Player and Combat classes as in the first snippet.
configStoryHandler = """
Your response will always be in json format no matter what. You are narrating a medieval adventure game that the player is trying to get out of a dungeon. Once the player kills 5 monsters they get out of the dungeon and win the game. Make sure that their options keep them in the dungeon until.Keep your responces short.
Your response will always be in this format. Do write anything before or after the format below, newlines, or any additional formatting such as numbering or lettering the choices. Don't go past the json format below.
{
  "story": {
    "description": "",
    "choices": ["(Choice 1)", "(Choice 2)", "(Choice 3)"]
  }
}
"""

configConsequenceHandler = """
Your responses will always be in string format no matter what. You are decicing the positive and negative consequences of a player's actions in a medieval choose-your-own-adventure game where the player is trying to escape a dungeon. 
Your responses will always be in one and only one of the charcter sets below. Do write anything before or after the set of one or two characters you select. Do not format or frame them in any way.

FOR NO CONSEQUENCES, JUST CONTINUE THE STORY: "n"
FOR WHEN A BATTLE STARTING IS THE CONSEQUENCE: "b"
FOR HEALTH LOSS: "hl"
FOR HEALTH GAIN: "hg"
FOR GAINS AN OFFENSIVE ITEM LIKE A BETTER SWORD: "ai"
FOR GAINS A DEFENSIVE ITEM LIKE BETTER ARMOR: "di"
FOR GAINS A HEALTH POTION: "ii"
"""

noConsequencesConfig = """
You are writing the narrative of a player's actions in a medieval choose-your-own-adventure game where the player is trying to escape a dungeon. Your response will always be in json format no matter what.
Your response will always be in the json format below. Do write anything before or after the format. Fill in the fields in parenthesis, and omit the parenthesis themselves. Do not change ANYTHING outside the parenthesis, only return as-is.
{
    "response": {
    "consequences": [n,"",0,0],
    "narrative": "(A sentence or two describing what happened or what information was discovered as a result of the player's action.)"
    }
}
"""

battleConsequencesConfig = """
You are deciding the details of an initiating battle and a narrative of the player's actions that led to it in a medieval choose-your-own-adventure game where the player is trying to escape a dungeon. Your response will always be in json format no matter what.
Your response will always be in the json format below. Do write anything before or after the format. Fill in the fields in parenthesis, and omit the parenthesis themselves. Do not change ANYTHING outside the parenthesis, only return as-is.
{
    "response": {
    "consequences": [b,"(Name of the enemy)",(Health of the enemy as an integer between 10 and 100; 10 is pathetic, 50 is a normal, and 100 is the final boss),(Attack-stat of the enemy as an integer between 5 and 30; 5 is pathetic, 15 is a normal, and 30 is the final boss)],
    "narrative": "(A sentence or two describing how the enemy appeared as a result of the player's action.)"
    }
}
"""

healthlossConsequencesConfig = """
You are deciding the narrative and severity of a health loss related to the player's actions in a medieval choose-your-own-adventure game where the player is trying to escape a dungeon. Your response will always be in json format no matter what.
Your response will always be in the json format below. Do write anything before or after the format. Fill in the fields in parenthesis, and omit the parenthesis themselves. Do not change ANYTHING outside the parenthesis, only return as-is.
{
    "response": { 
    "consequences": [c,"hl","(a very brief sentence describing the damage)",(Health lost as an integer between 1 and 100; 1 is a papercut, 10 is an inconvience, 30 is a major wound, and 100 is guranteed instant death)],
    "narrative": "(A sentence or two describing what happened as a result of the player's action.)"
    }
}
"""

healthgainConsequencesConfig = """
You are deciding the narrative and extent of a health gain related to the player's actions in a medieval choose-your-own-adventure game where the player is trying to escape a dungeon. Your response will always be in json format no matter what.
Your response will always be in the json format below. Do write anything before or after the format. Fill in the fields in parenthesis, and omit the parenthesis themselves. Do not change ANYTHING outside the parenthesis, only return as-is.
{
    "response": { 
    "consequences": [c,"hg","(a very brief sentence describing the healing)",(Health gained as an integer between 1 and 100; 1 is a reaffirming pat on the shoulder, 10 is an slight heal, 30 is a major heal, and 100 is a full heal)],
    "narrative": "(A sentence or two describing what happened as a result of the player's action.)"
    }
}
"""
offensiveItemConsequencesConfig = """
You are deciding the name and appropriate strength of a weapon that the player has found in a medieval choose-your-own-adventure game where the player is trying to escape a dungeon. Your response will always be in json format no matter what.
Your response will always be in the json format below. Do write anything before or after the format. Fill in the fields in parenthesis, and omit the parenthesis themselves. Do not change ANYTHING outside the parenthesis, only return as-is.
{
    "response": { 
    "consequences": [c,"ai","(a very brief sentence describing the weapon)",( Attack gained as an integer between 1 and 40; 1 is a rock, 10 is a standard blade, 20 is a quality weapon, and 40 is a legendary weapon)],
    "narrative": "(A sentence or two describing what happened as a result of the player's action.)"
    }
}
"""
defensiveItemConseqeuncesConfig = """
You are deciding the name and appropriate strength of a defensive piece of equipment that the player has found in a medieval choose-your-own-adventure game where the player is trying to escape a dungeon. Your response will always be in json format no matter what.
Your response will always be in the json format below. Do write anything before or after the format. Fill in the fields in parenthesis, and omit the parenthesis themselves. Do not change ANYTHING outside the parenthesis, only return as-is.
{
    "response": { 
    "consequences": [c,"di",(a very brief sentence describing the armor)",( defense gained as an integer between 1 and 50; 1 is a polishing oil, 10 is a new shield, 25 is a magic helmet, and 50 is a magic armor)],
    "narrative": "(A sentence or two describing what happened as a result of the player's action.)"
    }
}
"""
healthPotionConfig = """
You are deciding a creative name of a healing item that the player has found in a medieval choose-your-own-adventure game. Your response will always be in json format no matter what.
Your response will always be in the json format below. Do write anything before or after the format. Fill in the fields in parenthesis, and omit the parenthesis themselves. Do not change ANYTHING outside the parenthesis, only return as-is.
{
    "response": { 
    "consequences": [c,"ii",(A creative name for a healing item)"],
    "narrative": "(A sentence or two describing what happened as a result of the player's action.)"
    }
}
"""



template = """

Here is your instructions: {config}

Here is the most recent scenario or scenario result: {narrative}
Here was the player's choice in reaction to that scenario: {player_choice_dicta}
"""

model = OllamaLLM(model="llama2")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation(which_config, context, narrative, player_choice_dicta=""):
    if which_config == 0:
        config = configStoryHandler
    elif which_config == 1:
        config = configConsequenceHandler
    elif which_config == "n":
        config = noConsequencesConfig
    elif which_config == "b":
        config = battleConsequencesConfig
    elif which_config == "hl":
        config = healthlossConsequencesConfig
    elif which_config == "hg":
        config = healthgainConsequencesConfig
    elif which_config == "ai":
        config = offensiveItemConsequencesConfig
    elif which_config == "di":
        config = defensiveItemConseqeuncesConfig
    elif which_config == "ii":
        config = healthPotionConfig
    else:
        print("Broken which_config! Must be 0 or 1")
    
    
    result = chain.invoke({"narrative": narrative, "player_choice_dicta": player_choice_dicta, "config": config})
    
    if config == configStoryHandler:
        parsed_result = json.loads(result)
        returned_result1 = parsed_result['story']['description']
        returned_result2 = parsed_result['story']['choices']
    elif config == configConsequenceHandler:
        returned_result1 = result
        returned_result2 = ""
    else:
        parsed_result = json.loads(result)
        returned_result1 = parsed_result['response']['narrative']
        returned_result2 = parsed_result['response']['consequences']
    
    context += f"Story: {result}\nYou: {narrative}\n"
    return returned_result1, returned_result2, context

    