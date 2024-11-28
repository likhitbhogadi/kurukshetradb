def get_formation_and_warrior_names(cur):   #IF WANT PRINT THE MULTIPLE NAMES OF THE COMMANDER
    try:
        # Ask the user for the kingdom name
        kingdom_name = input("Enter the kingdom name: ").strip()

        if not kingdom_name:
            print("You must provide a kingdom name. Please try again.")
            return

        # SQL query with the given condition
        query = """
            SELECT BF.FORMATION_NAME, W.WARRIOR_ID
            FROM WARRIOR AS W
            JOIN BATTLE_FORMATION AS BF ON W.WARRIOR_ID = BF.COMMANDER_ID
            JOIN KINGDOM AS K ON K.KINGDOM_ID = W.KINGDOM_ID
            WHERE K.NAME = %s;
        """
        
        # Executing the query with the user-provided kingdom name
        cur.execute(query, (kingdom_name,))
        
        # Fetching all rows from the result set
        results = cur.fetchall()

        # Checking if any results were returned
        if not results:
            print(f"No matching records found for kingdom: {kingdom_name}.")
        else:
            # Printing the result
            print("{:<20} {:<20}".format("FORMATION_NAME","COMMANDER_ID"))
            print("-" * 40)
            for row in results:
                print("{:<20} {:<20}".format(row["FORMATION_NAME"], row["WARRIOR_ID"]))

    except Exception as e:
        print(f"An error occurred: {e}")