
from models.codex.code_generation import generate_code

if __name__ == "__main__":
    prompt = "Write a Python function to calculate the factorial of a number."
    code = generate_code(prompt)
    print("Generated Code:\n", code)
