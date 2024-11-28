from colorama import Fore, Style, init
init(autoreset=True)

def get_warriors_by_kingdom(cur):   #create a helper function to make it small

    try:
        # Ask the user for the kingdom name
        kingdom_name = input("Enter the name of the kingdom (leave blank to fetch all warriors): ").strip()

        print(Fore.LIGHTCYAN_EX+ Style.BRIGHT + "Fetching warrior details..." + Style.RESET_ALL)

        # Check if the user provided a kingdom name
        if kingdom_name:
            # Query for warriors from the specified kingdom
            query = """
            SELECT WARRIOR.WARRIOR_ID, WARRIOR.DOB, WARRIOR.RANK, WARRIOR.BATTLE_STATUS, WARRIOR.KINGDOM_ID, KINGDOM.NAME AS KINGDOM_NAME
            FROM WARRIOR
            JOIN KINGDOM ON WARRIOR.KINGDOM_ID = KINGDOM.KINGDOM_ID
            WHERE KINGDOM.NAME = %s;
            """
            cur.execute(query, (kingdom_name,))
        else:
            # Query to fetch all warriors
            query = """
            SELECT WARRIOR.WARRIOR_ID, WARRIOR.DOB, WARRIOR.RANK, WARRIOR.BATTLE_STATUS, WARRIOR.KINGDOM_ID, KINGDOM.NAME AS KINGDOM_NAME
            FROM WARRIOR
            JOIN KINGDOM ON WARRIOR.KINGDOM_ID = KINGDOM.KINGDOM_ID;
            """
            cur.execute(query)

        # Fetch all rows from the result set
        results = cur.fetchall()

        # Check if there are any rows
        if not results:
            if kingdom_name:
                print(f"No warriors found from the kingdom '{kingdom_name}'.")
            else:
                print("No warriors found in the database.")
            return

        # Print a header row
        if kingdom_name:
            print("{:<15} {:<15} {:<20} {:<20}".format(
                "WARRIOR_ID", "DOB", "RANK", "BATTLE_STATUS"))
            print("-" * 85)

            # Iterate through the rows and display each record
            for row in results:
                warrior_id = row["WARRIOR_ID"]
                print("{:<15} {:<15} {:<20} {:<20}".format(
                    row["WARRIOR_ID"], row["DOB"], row["RANK"], row["BATTLE_STATUS"]))
            
                name_query = "SELECT NAME FROM WARRIOR_NAME WHERE WARRIOR_ID = %d;" % warrior_id
                cur.execute(name_query)
                names = cur.fetchall()

                # Print warrior names
                name_list = [name["NAME"] for name in names]
                print("    Names: ", ", ".join(name_list))

                # Query to fetch warrior skills from the WARRIOR_SKILLS table
                skill_query = "SELECT SKILLS FROM WARRIOR_SKILLS WHERE WARRIOR_ID = %d;" % warrior_id
                cur.execute(skill_query)
                skills = cur.fetchall()

                # Print warrior skills
                skill_list = [skill["SKILLS"] for skill in skills]
                print("    Skills: ", ", ".join(skill_list))
                print("-" * 80)

            
        else:
            print("{:<15} {:<15} {:<20} {:<20} {:<15}".format(
                "WARRIOR_ID", "DOB", "RANK", "BATTLE_STATUS", "KINGDOM_NAME"))
            print("-" * 85)

            # Iterate through the rows and display each record
            for row in results:
                warrior_id = row["WARRIOR_ID"]
                print("{:<15} {:<15} {:<20} {:<20} {:<15}".format(
                    row["WARRIOR_ID"], row["DOB"], row["RANK"], row["BATTLE_STATUS"], row["KINGDOM_NAME"]))


                name_query = "SELECT NAME FROM WARRIOR_NAME WHERE WARRIOR_ID = %d;" % warrior_id
                cur.execute(name_query)
                names = cur.fetchall()

                # Print warrior names
                name_list = [name["NAME"] for name in names]
                print("    Names: ", ", ".join(name_list))

                # Query to fetch warrior skills from the WARRIOR_SKILLS table
                skill_query = "SELECT SKILLS FROM WARRIOR_SKILLS WHERE WARRIOR_ID = %d;" % warrior_id
                cur.execute(skill_query)
                skills = cur.fetchall()

                # Print warrior skills
                skill_list = [skill["SKILLS"] for skill in skills]
                print("    Skills: ", ", ".join(skill_list))
                print("-" * 80)


    except Exception as e:
        print("Error retrieving warriors from the database:", e)