import argparse


def create_hunter_profile(name, age, country):
    """
    Creates and returns a profile for a K-pop demon hunter.
    """
    hunter_profile = {
        "Name": name,
        "Age": age,
        "Country": country
    }
    return hunter_profile


def main():
    """
    Main function to parse arguments and create the profile.
    """
    # Initialize the parser with a description
    parser = argparse.ArgumentParser(
        description="A CLI tool to create profiles for K-pop Demon Hunters.")

    # Add the command-line arguments
    parser.add_argument("-n", "--name", type=str,
                        required=True, help="The name of the Huntrix.")
    parser.add_argument("-a", "--age", type=int,
                        required=True, help="The age of the Huntrix.")
    parser.add_argument("-c", "--country", type=str, required=True,
                        help="The country of origin for the Huntrix.")

    # Parse the arguments provided by the user
    args = parser.parse_args()

    # Create the profile using the parsed arguments
    profile = create_hunter_profile(args.name, args.age, args.country)

    # Display the created profile
    print("\
--- K-pop Demon Hunter Profile ---")
    print(f"Name:    {profile['Name']}")
    print(f"Age:     {profile['Age']}")
    print(f"Country: {profile['Country']}")
    print("--------------------------------")


if __name__ == "__main__":
    main()
