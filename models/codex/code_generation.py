
from transformers import pipeline

def generate_code(prompt):
    generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')
    response = generator(prompt, max_length=150, do_sample=True, temperature=0.7)
    return response[0]['generated_text']

if __name__ == "__main__":
    prompt = "Write a Python function to calculate the factorial of a number."
    code = generate_code(prompt)
    print("Generated Code:\n", code)
