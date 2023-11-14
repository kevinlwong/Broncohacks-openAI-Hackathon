import os
import openai
openai.api_key = "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"
print("Ask the chatbot any question and enter 'quit' when you want to finish!")
conversation_history = []

answer = "y"

while answer != "n":
    question = input("You: ")
    conversation_history.append({"role": "user", "content": question})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "You are a helpful assistant, skilled in explaining complex programming concepts with creative flair."},
        *conversation_history
    ]
    )
    response = completion.choices[0].message.content

    print(f"AI: {response}")
    print("Would you like to continue? y|n")
    answer = input()
