def search_warriors_by_name(cur):
    try:
        # Ask the user for a partial name
        partial_name = input("Enter a partial name to search for warriors: ").strip()

        # Validate input
        if not partial_name:
            print("You must provide a partial name. Please try again.")
            return

        # SQL query to join tables and search for a partial name match
        query = """
        SELECT wn.NAME AS WarriorName, w.DOB, w.RANK, w.BATTLE_STATUS, k.NAME
        FROM WARRIOR_NAME wn
        INNER JOIN WARRIOR w ON wn.WARRIOR_ID = w.WARRIOR_ID
        INNER JOIN KINGDOM k ON k.KINGDOM_ID = w.KINGDOM_ID
        WHERE wn.NAME LIKE %s;
        """

        # Use the LIKE operator with wildcards for partial matching
        cur.execute(query, (f"%{partial_name}%",))

        # Fetch the results
        results = cur.fetchall()

        # Check if results were found
        if not results:
            print(f"No warriors found matching the partial name '{partial_name}'.")
            return

        # Display results
        print("{:<20} {:<15} {:<15} {:<20} {:<10}".format(
            "WarriorName", "DOB", "RANK", "BATTLE_STATUS", "KINGDOM_NAME"))
        print("-" * 80)
        for row in results:
            print("{:<20} {:<15} {:<15} {:<20} {:<20}".format(
                row["WarriorName"], row["DOB"], row["RANK"], row["BATTLE_STATUS"], row["NAME"]))

    except Exception as e:
        print("Error retrieving warriors from the database:", e)