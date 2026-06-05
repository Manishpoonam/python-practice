import datetime

def get_date():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to log food or exercise
def log_activity(client_name, activity_type):
    if activity_type == 1:
        #logging for food
        item = input(f"\nWhat food did {client_name} eat? ")
        filename = f"{client_name}_food.txt"
        with open (filename, "a") as file:
            file.write((f"[{get_date()}] {item}\n"))
        print(f"✅ Successfully logged food for {client_name}.")

    elif activity_type == 2:
        # Logging Exercise
        item = input(f"\nWhat exercise did {client_name} do? ")
        filename = f"{client_name}_exercise.txt"
        with open(filename, "a") as file:
            file.write(f"[{get_time()}] {item}\n")
        print(f"✅ Successfully logged exercise for {client_name}.")
        
    else:
        print("❌ Invalid choice! Please select 1 or 2.")


# --- Main Program Execution ---

print("--- Welcome to the Health Management System ---")

# 1. Take 3 inputs from the user as names
client={}
for i in range(1, 4):
    name = input(f"Enter the name for User {i}: ")
    client[i] = name
    
print("\n" + "-"*30)

while True:
    print("\n" + "-"*30)
    print("Select a user to log data for:")
    for key, value in client.items():
        print(f"{key}. {value}")
    print("4. Exit the program")

    try:
        user_choice = int(input("Enter user number (1-4):"))

        if user_choice == 4:
            print("Exiting the program. Goodbye!")
            break

        elif user_choice in client:
            selected_name = client[user_choice]
            print(f"\nWhatdo you want to log for {selected_name}?")
            print("1. Food")
            print("2. Exercise")

            activity_choice = int(input("Enter your choice (1 or 2): "))

            # Call the function to handle the file writing
            log_activity(selected_name, activity_choice)

        else:
            print("❌ Invalid user number. Please select 1, 2, 3, or 4.")

    except ValueError:
        print("❌ Please enter a valid number.")


