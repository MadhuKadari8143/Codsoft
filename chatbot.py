import random

# Define some sample responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!", "Hi! How can I help you?"],
    "how are you": ["I'm just a bot, but I'm doing great!", "All good! How about you?"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "name": ["I'm a simple chatbot made with Python.", "You can call me PyBot!"],
    "default": ["Sorry, I didn't understand that.", "Can you rephrase that?", "I'm not sure what you mean."]
}

# Lowercase and check keywords
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

# Chat loop
def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print("Chatbot:", random.choice(responses["bye"]))
            break
        response = get_response(user_input)
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    chat()
