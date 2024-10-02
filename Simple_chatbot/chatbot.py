def chatbot(user_question):
    user_question = user_question.lower()
    # def user_question():
    if user_question == "What is your name?": 
        return "Chatbot: My name is Sehrish Shafiq!."
    elif user_question == "how are you?": 
        return "Chatbot: I'm doing well, thank you!."
    elif user_question == "how old are you?": 
        return "Chatbot: I'd prefer not to say!."
    elif user_question == "where are you from?": 
        return "chatbot: I'm from karachi!."
    elif user_question == "what are your qualifications?": 
        return "Chatbot: I've completed a Bachelor's degree in Computer Science!."
    else:
        return "Chatbot: Sorry, I don't understand that. Try asking something else!"
def main():
    print("welcome to my chatbot! type 'exit' when you are finished with your conversation.")
    while True:
        user_question = input("you: ")  
        if user_question.lower() == "exit":
            print("Goodbye! Have a nice day.")
            break
        response = chatbot(user_question)
        print(response)
if __name__ == "__main__":
    main()
