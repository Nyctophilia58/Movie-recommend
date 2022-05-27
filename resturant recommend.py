import data
import time

restaurant_types = data.types
restaurant_data = data.restaurant_data


def welcome():
    print("*" * 61 + "\n****** WELCOME TO OUR RESTAURANT RECOMMENDATION SYSTEM ******\n" + "*" * 61)


def menu():
    welcome()
    choice_error = True
    while choice_error:
        choice = input("""\nChoose an option: 
        \r1. Recommend a restaurant
        \r2. Exit
        \nYour choice: """)
        if choice == "1":
            food_type()
        elif choice == "2":
            exit_message()
        else:
            input("Sorry, invalid input. Press ENTER to try again. ")


def food_type():
    choice_error = True
    while choice_error:
        choice = input(f"\nWhat type of food would you like to eat? "
                       f"\nOptions are: {restaurant_types}\n"
                       f"\nYour choice: ").lower()
        if choice in restaurant_types:
            recommend_restaurant(choice)
            get_user_preferences()
            choice_error = False
        else:
            input("Sorry, invalid input. Press ENTER to try again. ")


def recommend_restaurant(choice):
    print(f"\nHere are the restaurants we recommend for {choice.title()} food: ")
    for i in range(len(restaurant_data)):
        if restaurant_data[i][0] == choice:
            print(f"""\nRestaurant name: {restaurant_data[i][1]}
            \rRestaurant price: {restaurant_data[i][2]}/5
            \rRestaurant rating: {restaurant_data[i][3]}/5
            \rRestaurant location: {restaurant_data[i][4]}""")
    time.sleep(1.5)


def get_user_preferences():
    choice = input("\nAny restaurant you like? (y/n) ")
    if choice.lower() == "y":
        exit_message()
    else:
        user_choice = input("\nWould you like us to recommend some other restaurants? ").lower()
        if user_choice == "y":
            food_type()
        else:
            exit_message()


def exit_message():
    print("Thanks for using our system. Have a good day then! BYE. ")
    time.sleep(1.5)
    exit()


if __name__ == "__main__":
    menu()
