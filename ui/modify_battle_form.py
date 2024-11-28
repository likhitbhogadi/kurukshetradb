def modify_battle_formation(cur, con):
    try:
        # Ask the user for the identifying keys: Day and Army ID
        day = int(input("Enter the Day of the formation you want to modify: ").strip())
        army_id = int(input("Enter the Army ID of the formation you want to modify: ").strip())

        # Ask the user for new values, if provided
        formation_name = input("Enter the new Formation Name (leave blank to keep current): ").strip()
        commander_id = input("Enter the new Commander ID (leave blank to keep current): ").strip()

        # Start constructing the SQL SET clause dynamically based on provided values
        set_clause = []
        params = []

        if formation_name:
            set_clause.append("FORMATION_NAME = %s")
            params.append(formation_name)
        if commander_id:
            set_clause.append("COMMANDER_ID = %s")
            params.append(int(commander_id))  # Convert commander_id to an integer

        # If no fields were provided to update, inform the user
        if not set_clause:
            print("No changes were made to the formation.")
            return

        # Prepare the SQL UPDATE query with dynamically built SET clause
        query = f"""
            UPDATE BATTLE_FORMATION
            SET {', '.join(set_clause)}
            WHERE DAY = %s AND ARMY_ID = %s
        """
        
        # Adding the day and army_id to the parameters for the WHERE clause
        params.extend([day, army_id])

        # Execute the query with the user-provided values
        cur.execute(query, tuple(params))
        
        # Commit the changes
        con.commit()

        print(f"Formation for Day {day} and Army ID {army_id} has been successfully updated.")
    
    except Exception as e:
        # Rollback the transaction in case of an error
        con.rollback()
        print(f"An error occurred: {e}")