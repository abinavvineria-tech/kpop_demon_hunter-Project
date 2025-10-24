def create_hunter_profile():
    """
    Creates a profile for a K-pop demon hunter by prompting the user for input.
    """
    print("Enter the details for the K-pop Demon Hunter:")

    # Get user input for the hunter's name
    while True:
        name = input("Enter the Huntrix's name: ").strip()
        if name:
            break
        else:
            print("Name cannot be empty. Please enter a valid name.")

    # Get user input for the hunter's age
    while True:
        try:
            age = int(input("Enter the Huntrix's age: "))
            if age > 0:
                break
            else:
                print("Please enter a positive number for age.")
        except ValueError:
            print("Invalid input. Please enter a number for the age.")

    # Get user input for the country of origin
    while True:
        country = input("Enter the Huntrix's country of origin: ").strip()
        if country:
            break
        else:
            print("Country cannot be empty. Please enter a valid country.")

    # Store the details in a dictionary
    hunter_profile = {
        "Name": name,
        "Age": age,
        "Country": country
    }

    # Display the created profile
    print("--- K-pop Demon Hunter Profile ---")
    print(f"Name: {hunter_profile['Name']}")
    print(f"Age: {hunter_profile['Age']}")
    print(f"Country: {hunter_profile['Country']}")
    print("--------------------------------")

    return hunter_profile


if __name__ == "__main__":
    create_hunter_profile()
