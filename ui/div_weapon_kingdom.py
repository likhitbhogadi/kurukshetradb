def list_divine_weapons_by_kingdom(cur):
    try:
        # Ask the user for the kingdom name
        kingdom_name = input("Enter the name of the kingdom (default: Hastinapura): ").strip()
        if not kingdom_name:
            kingdom_name = "Hastinapura"

        # SQL query to join WARRIOR, WARRIOR_NAME, and DIVINE_WEAPON tables
        query = f"""
        SELECT 
            GROUP_CONCAT(wn.NAME SEPARATOR ', ') AS WarriorNames, 
            w.RANK, 
            w.BATTLE_STATUS, 
            dw.NAME AS DivineWeapon
        FROM WARRIOR w
        INNER JOIN WARRIOR_NAME wn ON w.WARRIOR_ID = wn.WARRIOR_ID
        INNER JOIN DIVINE_WEAPON dw ON w.WARRIOR_ID = dw.WARRIOR_ID
        WHERE w.KINGDOM_ID IN (
            SELECT KINGDOM_ID FROM KINGDOM WHERE NAME = %s
        )
        GROUP BY w.WARRIOR_ID, w.RANK, w.BATTLE_STATUS, dw.NAME;
        """

        # Execute the query with the user-provided kingdom name
        cur.execute(query, (kingdom_name,))
        results = cur.fetchall()

        # Check if results are available
        if not results:
            print(f"No divine weapons found for warriors of {kingdom_name}.")
            return

        # Display the results in tabular format
        print(f"\nDivine Weapons with Warriors of {kingdom_name}")
        print("{:<40} {:<15} {:<15} {:<20}".format(
            "Warrior Names", "Rank", "Battle Status", "Divine Weapon"))
        print("-" * 90)
        for row in results:
            print("{:<40} {:<15} {:<15} {:<20}".format(
                row["WarriorNames"], row["RANK"], row["BATTLE_STATUS"], row["DivineWeapon"]))

    except Exception as e:
        print("Error retrieving data:", e)