import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Path to the local directory where you stored the Qwen-2.5:14B model files.
# Replace with your actual path.
model_path = "C:\Users\Mark\.ollama\models\manifests\registry.ollama.ai\library\qwen2.5"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.float16,  # Use FP16 for better memory efficiency.
    device_map="auto",          # Automatically map to GPU if available.
)

# Example usage: Generate text
input_text = "Hello, how are you?"
# Ensure inputs are on the same device as model.
inputs = tokenizer(input_text, return_tensors='pt').to("cuda")

# Context manager for disabling gradient calculation (for inference).
with torch.no_grad():
    output_sequences = model.generate(**inputs)

# Decode generated sequences
output_text = tokenizer.decode(output_sequences[0], skip_special_tokens=True)
print(f"Generated Text: {output_text}")


# ### Explanation

# 1. **Import Libraries**: Import the necessary libraries from `torch` and `transformers`.

# 2. **Define Model Path**: Set `model_path` to the directory containing your local model files.

# 3. **Load Tokenizer**: Use `AutoTokenizer.from_pretrained()` with the path to your tokenizer files.

# 4. **Load Model**: Use `AutoModelForCausalLM.from_pretrained()` with the same path and specify:
#    - `torch_dtype=torch.float16` for better memory efficiency on GPUs.
#    - `device_map="auto"` to automatically map model components across devices (including GPU).

# 5. **Generate Text**:
#    - Encode input text using the tokenizer.
#    - Pass encoded inputs to the model for generation.
#    - Decode and print the generated output.

# ### Running the Script
# Save this script as a `.py` file, e.g., `run_qwen.py`, then run it from your command line or terminal:

# ```bash
# python run_qwen.py
# ```

# This will load the local Qwen-2.5:14B model and generate output based on the input text provided.

# ### Troubleshooting Tips

# - **Check GPU Availability**: Make sure you have a compatible GPU with sufficient memory.
# - **Model Compatibility**: Ensure your local model files are correctly structured and can be loaded by
# `transformers`.
# - **Dependencies**: Verify that all necessary dependencies (like `torch`, `transformers`) are installed.
