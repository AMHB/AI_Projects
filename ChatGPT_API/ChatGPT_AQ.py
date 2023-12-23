import openai

# My API key* Account amehrb@gmail.com
api_key = "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"
openai.api_key = api_key

# Define the conversation function
def chat_with_gpt(prompt_text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt_text},
        ],
    )
    return response.choices[0].message["content"]

# Start a conversation loop
print("You can start chatting. Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chat_with_gpt(user_input)
    print("ChatGPT:", response)
