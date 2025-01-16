import random
import json
from datetime import datetime as dt

print(f"--------------------------------------------Welcome to the University of Poppleton.------------------------------------------------")

# Function to get and process the user's name
def for_username():
    username = input("Please enter your name:")
    username = username.capitalize() #Changes the first letter to capital letter
    print(f"Hello,{username}! Welcome to the Chatbot of University of Poppleton.")
    return username

# Function to randomly assign an agent name
def for_agents(username):
    agents_name=["Alice", "Ethan", "Fiona", "Jack", "Jacob", "Sansa"]
    name_agent= random.choice(agents_name)
    print(f"I am agent {name_agent}, How can I assist you today?")
    return name_agent

# Function to load keywords and responses from a JSON file
def load_data_json():
    with open("key_words.json", "r") as file:
        get_data = json.load(file)
    return get_data
 
# Function to handle keyword-based responses   
def for_responses (check_key_word, get_data):
    check_key_word= check_key_word.lower() #conerts keywords to lowercase to handle case sensitiity

    # Iterate through the keys and values in the JSON data
    for key_word, values in get_data["keys_responses"].items(): #iteration over each keys and their values.
        if key_word in check_key_word: # Check if any keyword is present in the user's input
            return values # Return the corresponding response

    return random.choice(get_data["other_responses"]) #gives random responses from other_responses


def main():
    with open("conversation.txt", "a") as file:  # Open file once in append mode
        # Add a separator (optional) before each new conversation
        file.write("\n--- New Conversation ---\n")

        username = for_username()
        name_agent = for_agents(username)
        get_data = load_data_json()

        # Write the present date and time when conversation starts
        present_time = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        # Write initial message indicating the start of the conversation
        file.write(f"Conversation started at {present_time} with {username} and agent {name_agent}\n")

        while True:
            # Take user input
            check_key_word = input(f"{username}: ")

            # Check for exit conditions
            if check_key_word == "" or check_key_word.lower() in ["bye", "exit", "quit"]:
                print(f"Thank you. Have a great day {username}")
                file.write(f"{username}: {check_key_word}\n")
                file.write(f"Thank you. Have a great day {username}\n")
                break

            # Generate a response based on user input
            response = for_responses(check_key_word, get_data)
            print(f"{name_agent}: {response}")

            # log the conversation of user and agent to file 
            file.write(f"{username}: {check_key_word}\n")
            file.write(f"{name_agent}: {response}\n")



        
       
if __name__=="__main__":
    main()


