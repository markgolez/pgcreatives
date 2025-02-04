from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load DeepSeek Coder R1
# Change to "deepseek-coder-33b" for a larger model
model_name = "deepseek-ai/DeepSeek-R1-Distill-Llama-70B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name, torch_dtype=torch.float16, device_map="auto"
)

# Function to get AI-generated code suggestions


def generate_code(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    output = model.generate(**inputs, max_length=256)
    return tokenizer.decode(output[0], skip_special_tokens=True)


# Example usage
prompt = "Write a Python function to merge two sorted lists."
print(generate_code(prompt))
