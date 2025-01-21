from langchain_ollama import OllamaLLM

model = OllamaLLM("llama2")

result = model.invoke(input="hello world")
print(result)