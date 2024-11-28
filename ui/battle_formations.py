def get_battle_formations(cur):
    try:
        # Ask the user for the day
        day = input("Enter the day to get battle formations (leave blank to fetch all formations): ").strip()

        if day:
            # Validate input to ensure it's a number
            if not day.isdigit():
                print("Invalid day. Please enter a valid number.")
                return

            # Query for formations on a specific day
            query = """
            SELECT Formation_Name
            FROM BATTLE_FORMATION
            WHERE Day = %s;
            """
            cur.execute(query, (int(day),))
        else:
            # Query to fetch all formations
            query = """
            SELECT Formation_Name, Day
            FROM BATTLE_FORMATION;
            """
            cur.execute(query)

        # Fetch all rows from the result set
        results = cur.fetchall()

        # Check if there are any rows
        if not results:
            if day:
                print(f"No battle formations found for Day {day}.")
            else:
                print("No battle formations found in the database.")
            return

        if day:
            # Print header row
            print("{:<25}".format("FORMATION_NAME"))
            print("-" * 25)

            # Display each record
            for row in results:
                print("{:<25}".format(row["Formation_Name"]))
        else:
            # Print header row
            print("{:<25} {:<10}".format("FORMATION_NAME", "DAY"))
            print("-" * 35)

            # Display each record
            for row in results:
                print("{:<25} {:<10}".format(row["Formation_Name"], row["Day"]))

    except Exception as e:
        print("Error retrieving battle formations from the database:", e)