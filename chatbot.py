def chatbot():
    print("🤖 Welcome to CodeAlpha Chatbot!")
    print("Type 'bye' to exit.\n")

    while True:
        try:
            user = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye! (input closed)")
            break

        user = user.lower().strip()

        if user == "hello":
            print("Bot: Hi! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I'm doing great. How about you?")

        elif user == "what is your name":
            print("Bot: I am a simple Python chatbot.")

        elif user == "thank you":
            print("Bot: You're welcome!")

        elif user == "bye":
            print("Bot: Goodbye! Have a great day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()