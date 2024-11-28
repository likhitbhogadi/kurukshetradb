def add_new_formation(cur, conn):                  #didn't check this have to check this function
    try:
        # Prompt the user for formation details
        army_id = int(input("Enter the Army ID: ").strip())
        day = int(input("Enter the Day: ").strip())
        formation_name = input("Enter the Formation Name: ").strip()
        commander_id = int(input("Enter the Commander ID: ").strip())
        
        # SQL query to insert a new formation
        query = """
            INSERT INTO BATTLE_FORMATION (ARMY_ID, DAY, FORMATION_NAME, COMMANDER_ID)
            VALUES (%s, %s, %s, %s);
        """
        
        # Execute the query with user inputs
        cur.execute(query, (army_id, day, formation_name, commander_id))
        
        # Commit the transaction
        conn.commit()
        
        print(f"Formation '{formation_name}' added successfully for Army ID {army_id} on Day {day}.")
    
    except Exception as e:
        # Rollback the transaction in case of an error
        conn.rollback()
        print(f"An error occurred: {e}")