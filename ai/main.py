from utils import *
from fastapi import FastAPI
from transformers import AutoModelForCausalLM, AutoTokenizer


import sys


app = FastAPI()

# Use a publicly available model
model_name = "EleutherAI/gpt-neo-2.7B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")


@app.post("/generate-code/")
async def generate_code(prompt: str, max_length: int = 128):
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(
        inputs["input_ids"], max_length=max_length, temperature=0.7)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"code": result}

# To run the API, use: uvicorn filename:app --reload


if __name__ == "__main__":
    if len(sys.argv) < 2:
        project_path = input("Enter the path to your project: ")
    else:
        project_path = sys.argv[1]

    assistant = AIAssistant(project_path)
    assistant.cli()
