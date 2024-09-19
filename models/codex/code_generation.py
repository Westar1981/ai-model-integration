
import openai

def generate_code(prompt):
    openai.api_key = "YOUR_OPENAI_API_KEY"
    response = openai.completions.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    prompt = "Write a Python function to calculate the factorial of a number."
    code = generate_code(prompt)
    print("Generated Code:\n", code)
