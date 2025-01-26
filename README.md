# LLM-Adventure-Game

# Overview

Implements a language-learning-trained model into a “choose your own adventure” game framework. The game’s basic framework is implemented in Python, which accepts the user’s input with other relevant context and query the LLM to create content in the adventure. The purpose in making it was to deepen knowledge and understanding of tokens, AI infrastructure, and explore natively-run models rather than paid software-as-a-service tools.

# Development Environment
https://ollama.com/download
Ollama is a free program that runs pre-trained and publicly avaiable models. You could use any one, I chose the most versatile aand lightweight, ollama2, since cutting-edge weights and mesh complexity weren't key to understanding the fundamentals of AI implementation, and significantly sped up troubleshooting. The program runs in python and has just one dependency, which you can install using the following (once Ollama is installed)

python -m venv llmadventure
.\llmadventure\Scripts\Activate.ps1 
pip install langchain langchain-ollama ollama 

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Ollama]https://ollama.com/
* [Informative LLM Documentation]https://www.cloudflare.com/learning/ai/what-is-large-language-model/

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Implement additional LLM queries to improve performance and realism (itemized queries)
* Experiment with newer LLMs to improve functionality
* Introduce a walked character arc, granting a skeleton to the sometimes amorphous AI-generated story (which would itself be AI-generated)

