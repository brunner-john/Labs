"""
This program receives input from the user and determines if the user is able to regiseter
to vote.

Author: John Brunner 
"""
import sys

valid_states = [
    "ak", "al", "ar", "as", "az", "ca", "co", "ct", "dc", "de",
    "fl", "ga", "gu", "hi", "ia", "id", "il", "in", "ks", "ky",
    "la", "ma", "md", "me", "mi", "mn", "mo", "mp", "ms", "mt",
    "nc", "nd", "ne", "nh", "nj", "nm", "nv", "ny", "oh", "ok",
    "or", "pa", "pr", "ri", "sc", "sd", "tn", "tx", "um", "ut",
    "va", "vi", "vt", "wa", "wi", "wv", "wy"
]
voter_info = {
    "first_name": "",
    "last_name": "",
    "age": 0,
    "citizenship": "",
    "state": "",
    "zip_code": ""
}

def continue_registration():
    """
    Function for giving the user the opportunity to exit
    the program without performing a keyboard interrupt

    """
    while True:
        user_input = input("Do you want to continue with Voter Registration? Yes or No\n")
        if user_input.lower() not in ("yes", "no"):
            print("Please enter yes or no.")
        elif user_input.lower() == "no":
            sys.exit()
        else:
            return

def get_user_information():
    """
    Function for getting voter information and 
    assigning it to a Voter object. 

    """

    def get_user_age():
        while True:
            try:
                age = int(input("What is your age?\n"))
                if age < 0 or age > 110:
                    print("Please enter a valid positive age.")
                elif age < 18:
                    print("Sorry, you are not old enough for voter registration")
                    sys.exit()
                else:
                    return age
            except ValueError:
                print("Invalid input. Please enter a valid integer age.")

    def get_citizenship():
        while True:
            citizenship = input("Are you a U.S. Citizen? (yes or no)\n")
            if citizenship.lower() in ("yes", "no"):
                return citizenship
            print("Please enter yes or no")

    def get_state():
        while True:
            state = input("What state do you live? (Abbreviated version e.g. MD)\n")
            if state.lower() in valid_states:
                return state
            print("please enter a valid state.\n")
    voter_info['first_name'] = input("What is your first name?\n")
    continue_registration()
    voter_info['last_name'] = input("What is your last name?\n")
    continue_registration()
    voter_info['age'] = get_user_age()
    continue_registration()
    voter_info['citizenship'] = get_citizenship()
    continue_registration()
    voter_info['state'] = get_state()
    continue_registration()
    voter_info['zip_code'] = input("What is your zipcode?\n")

def print_concluding_message():
    """
    Function for printing out all voter information in 
    the specified format and thanking the user for using the
    application.

    """
    print("Thanks for registering to vote. Here is the information we received:\n"
          f"Name (first last): {voter_info['first_name']} {voter_info['last_name']}\n"
          f"Age: {voter_info['age']}\n"
          f"U.S. Citizen: {voter_info['citizenship']}\n"
          f"State: {voter_info['state'].upper()}\n"
          f"Zipcode: {voter_info['zip_code']}\n"
          f"Thanks for trying the Voter Registration Application.\n"
          f"Your voter registration card should be shipped within 3 weeks")

def main():
    """
    Main function for program

    """
    print("Welcome to the Python Voter Registration Application.\n")
    continue_registration()

    get_user_information()

    print_concluding_message()

if __name__ == '__main__':
    main()
