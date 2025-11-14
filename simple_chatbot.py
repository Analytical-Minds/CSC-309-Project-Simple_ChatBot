# Simple AI Chatbot
# Lab: Building a Basic Chatbot

# Import the datetime module
import datetime

def run_simple_chatbot():
    # Step 1: Ask for the user's name
    print(f"Welcome to Simple Chatbot by Analytical Minds\n")
    print(f"For best user experience, kindly respond with single format responses.\nFor example "
          f"What is your name?\nRes: Joseph or Joseph Inaku")
    name = input("Hello! What's your name? ")

    # Step 2: Generate a personalized greeting
    print(f"Nice to meet you, {name}!")

    # Step 3: Get and display the current date
    today = datetime.date.today()
    formatted_date = today.strftime("%B %d, %Y")  # e.g., "November 14, 2024"

    # Step 4: Display friendly message with date
    print(f"Today's date is {formatted_date}. Hope you’re having a great day, {name}!")

    # Step 5: Optional AI touch
    response = input("Would you like to hear a fun fact? (yes/no): ")

    if response.lower() == "yes":
        print("Did you know? Python was named after the comedy show 'Monty Python' — not the snake!")
    else:
        print("Alright! Have a wonderful day ahead, {0}!".format(name))


if __name__ == "__main__":
    run_simple_chatbot()