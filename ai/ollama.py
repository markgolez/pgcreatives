from ollama import Ollama

# Initialize with specific configuration
model = Ollama(
    model_name="gpt2",
    device_type="cuda",  # or 'cuda' for GPU
    precision="fp16"   # or 'int8'
)

response = model.generate("Explain quantum computing in simple terms.")
print(response)


# 4. **Text Generation**
# ollama can generate text based on a given prompt:


model = Ollama()

# Generate text with specified parameters
response = model.generate(
    "Write a short story about an adventure.",
    max_tokens=500,
    temperature=0.7
)

print(response)


# 5. **Question Answering**
# You can also use ollama for question answering by providing context and a question:


model = Ollama()

# Question answering
context = "The Eiffel Tower is located in Paris, France."
question = "Where is the Eiffel Tower?"

response = model.answer(question, context)
print(response)


# 6. **Custom Models**
# If you want to use a custom model with ollama, you can specify the model path:


model = Ollama(model_path=r"C:\Users\Mark\.ollama\models")

response = model.generate("What is your name?")
print(response)


# 7. **Batch Processing**
# You can process multiple requests in a batch:


model = Ollama()

prompts = [
    "What is the capital of France?",
    "Who discovered penicillin?",
    "When was the Titanic built?"
]

responses = model.generate(prompts)
for i, response in enumerate(responses):
    print(f"Prompt {i+1}: {response}")


# 8. **Stream Responses**
# If you want to stream the responses as they are generated, you can use the `stream` method:


model = Ollama()

for token in model.stream("Tell me a joke."):
    print(token, end="")
print()


# 9. **Error Handling**
# Handle errors gracefully by catching exceptions:


model = Ollama()

try:
    response = model.generate(
        "Generate a 1000 token response.", max_tokens=1000)
    print(response)
except Exception as e:
    print(f"An error occurred: {e}")


# 10. **Advanced Features**
# For more advanced usage, you can explore fine-tuning the model, using different tokenizer types, or integrating
# with other libraries.


# Example Project
# Here’s a simple project idea to get started:

# **Task:** Create a text generation tool that generates creative writing prompts.


model = Ollama()

# Generate a list of creative writing prompts
prompts = model.generate(
    "Generate 5 creative writing prompts for children.",
    max_tokens=200,
    temperature=0.8
)

print("Creative Writing Prompts:")
for i, prompt in enumerate(prompts.split('\n'), 1):
    print(f"{i}. {prompt.strip()}")
