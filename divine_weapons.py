from colorama import Fore, Back, Style, init
init(autoreset=True)  # Automatically reset styles after each print

def get_divine_weapons(cur):
    try:
        # Ask the user for invincibility status
        invincible_status = input("Is the weapon invincible? (Enter 'Yes', 'No', or leave blank to fetch all weapons): ").strip()

        # Check if the user provided invincibility status
        if invincible_status:
            # Query for weapons based on invincibility status
            query = """
            SELECT *
            FROM DIVINE_WEAPON
            WHERE Invincible = %s;
            """
            cur.execute(query, (invincible_status,))
        else:
            # Query to fetch all weapons
            query = """
            SELECT *
            FROM DIVINE_WEAPON;
            """
            cur.execute(query)

        # Fetch all rows from the result set
        results = cur.fetchall()

        # Check if there are any rows
        if not results:
            if invincible_status:
                print(f"No divine weapons found with invincibility status '{invincible_status}'.")
            else:
                print("No divine weapons found in the database.")
            return

        if invincible_status:
            # Print header row without the "INVINCIBLE" column
            print("{:<15} {:<20}".format("WEAPON_ID", "NAME"))
            print("-" * 40)

            # Display each record without "INVINCIBLE"
            for row in results:
                print("{:<15} {:<20}".format(row["WEAPON_ID"], row["NAME"]))
        else:
            # Print header row with the "INVINCIBLE" column
            print("{:<15} {:<20} {:<10}".format("WEAPON_ID", "NAME", "INVINCIBLE"))
            print("-" * 50)

            # Display each record with "INVINCIBLE"
            for row in results:
                print("{:<15} {:<20} {:<10}".format(row["WEAPON_ID"], row["NAME"], row["INVINCIBLE"]))

    except Exception as e:
        print("Error retrieving divine weapons from the database:", e)
