from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
from datasets import load_dataset

# Load dataset
dataset = load_dataset("bigcode/the-stack", split="data")

# Tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Tokenize data


def tokenize_data(example):
    return tokenizer(example["text"], truncation=True, padding="max_length", max_length=512)


tokenized_dataset = dataset.map(tokenize_data, batched=True)

# Training arguments
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="steps",
    save_steps=500,
    eval_steps=500,
    logging_dir="./logs",
    per_device_train_batch_size=4,
    num_train_epochs=3,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
)

trainer.train()
