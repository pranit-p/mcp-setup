from openai import OpenAI

client = OpenAI(api_key="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")

# Set your OpenAI API key

def chat_with_gpt(prompt, model="gpt-3.5-turbo"):
    try:
        response = client.chat.completions.create(model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500)
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error: {str(e)}"

# Interactive chat loop
print("ChatGPT CLI (type 'exit' to quit)")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ['exit', 'quit']:
        break

    reply = chat_with_gpt(user_input)
    print("ChatGPT:", reply)