from rich.console import Console
# from rich.panel import Panel
# from rich.layout import Layout
# from rich.table import Table
# from rich.prompt import Prompt
import subprocess as sp
import pymysql
import pymysql.cursors
from colorama import Fore, Back, Style, init
init(autoreset=True)  # Automatically reset styles after each print

from banner import print_banner
from divine_weapons import get_divine_weapons

# def print_banner():
#     """Prints a colorful banner."""
#     print(Fore.LIGHTCYAN_EX+ Style.BRIGHT)
#     print("=======================================================")
#     print("               WELCOME TO COMPANY DB TOOL              ")
#     print("=======================================================")
#     print(Style.RESET_ALL)

console = Console()

def print_menu():
    """Prints the main menu with colors."""
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "MAIN MENU:")
    print(Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX+ Style.BRIGHT + "1." + Style.RESET_ALL + " Get warrior details")
    print(Fore.LIGHTYELLOW_EX+ Style.BRIGHT + "2." + Style.RESET_ALL + " Get Details of Divine weapon ")
    print(Fore.LIGHTYELLOW_EX+ Style.BRIGHT + "3." + Style.RESET_ALL + " Get Battle Formation Details")
    print(Fore.LIGHTYELLOW_EX+ Style.BRIGHT + "4." + Style.RESET_ALL + " Get Kinngdom Details")
    print(Fore.LIGHTYELLOW_EX+ Style.BRIGHT + "5." + Style.RESET_ALL + " Get Total Strength of Anga_nama")
    print(Fore.LIGHTYELLOW_EX+ Style.BRIGHT + "6." + Style.RESET_ALL + " Get warrior Details on partial or full name")
    print(Fore.LIGHTYELLOW_EX+ Style.BRIGHT + "7." + Style.RESET_ALL + " Get list of divine weapon with warrior based on kingdom")
    print(Fore.LIGHTYELLOW_EX+ Style.BRIGHT + "8." + Style.RESET_ALL + " Get formation name and warrior Id based on kingdom name")
    print(Fore.LIGHTYELLOW_EX+ Style.BRIGHT + "9." + Style.RESET_ALL + " Add a new warrior")
    print(Fore.LIGHTYELLOW_EX+ Style.BRIGHT + "10." + Style.RESET_ALL + " Modify a Battle formation based on Day and army_id")
    print(Fore.LIGHTYELLOW_EX+ Style.BRIGHT + "11." + Style.RESET_ALL + " Delete Event from Yuddhahani")
    print(Fore.LIGHTYELLOW_EX+ Style.BRIGHT + "12." + Style.RESET_ALL + " Add a new Battle formation")
    print(Fore.LIGHTRED_EX+ Style.BRIGHT + "14." + Style.RESET_ALL + " Logout")
    print(Fore.LIGHTCYAN_EX+ Style.BRIGHT + "-" * 50 + Style.RESET_ALL)


def get_warriors_by_kingdom():   #create a helper function to make it small

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



def get_battle_formations():
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

def get_kingdoms_by_alliance():
    try:
        # Ask the user for the alliance
        alliance = input("Enter alliance (Kauravas or Pandavas) or press Enter to fetch all kingdoms: ").strip()

        if alliance:
            # Query for kingdoms with a specific alliance
            query = """
            SELECT Name, Capital, Ruler
            FROM KINGDOM
            WHERE Alliance = %s;
            """
            cur.execute(query, (alliance,))
        else:
            # Query to fetch all KINGDOMs
            query = """
            SELECT Name, Capital, Ruler, Alliance
            FROM KINGDOM;
            """
            cur.execute(query)

        # Fetch all rows from the result set
        results = cur.fetchall()

        # Check if there are any rows
        if not results:
            if alliance:
                print(f"No kingdoms found for the alliance '{alliance}'.")
            else:
                print("No kingdoms found in the database.")
            return

        if alliance:
            # Print header row
            print("{:<25} {:<25} {:<25}".format("NAME", "CAPITAL", "RULER"))
            print("-" * 75)

            # Display each record
            for row in results:
                print("{:<25} {:<25} {:<25}".format(row["Name"], row["Capital"], row["Ruler"]))
        else:
            # Print header row
            print("{:<25} {:<25} {:<25} {:<15}".format("NAME", "CAPITAL", "RULER", "ALLIANCE"))
            print("-" * 90)

            # Display each record
            for row in results:
                print("{:<25} {:<25} {:<25} {:<15}".format(row["Name"], row["Capital"], row["Ruler"], row["Alliance"]))

    except Exception as e:
        print("Error retrieving kingdoms from the database:", e)



def get_total_strength_by_anga():  # if want add the case where user doesn't provide any info of anganama   WHAT ABOUT PARTICULAR ARMY
    try:
        # Ask the user for the Anga_Nāma
        anga_nama = input("Enter Anga_Nāma (Padati, Ashva, Gaja, Ratha): ").strip()

        # Validate input
        if not anga_nama:
            print("You must specify an Anga_Nāma. Please try again.")
            return

        # Query to calculate total strength for the given Anga_Nāma
        query = """
        SELECT SUM(INITIAL_STRENGTH-CASUALTIES) AS TotalStrength
        FROM CHATURANGA
        WHERE ANGA_NAMA = %s;
        """
        cur.execute(query, (anga_nama,))

        # Fetch the result
        result = cur.fetchone()

        # Display the result
        if result["TotalStrength"] is not None:
            print(f"The total strength of '{anga_nama}' is: {result['TotalStrength']}")
        else:
            print(f"No records found for Anga_Nāma '{anga_nama}'.")

    except Exception as e:
        print("Error calculating total strength from the database:", e)


def search_warriors_by_name():
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

   


def list_divine_weapons_by_kingdom():
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



def Add_warrior():
    try:
        # Takes warrior details as input
        row = {}
        print("Enter new warrior's details: ")
        
        # Basic Warrior Information
        row["ID"] = int(input("Warrior ID: "))
        row["Bdate"] = input("Birth Date (YYYY-MM-DD): ")
        row["battle_status"] = input("Battle Status (alive/deceased): ")
        row["kingdom_id"] = int(input("Kingdom ID: "))
        
        # Ask for the warrior's name(s)
        names = []
        while True:
            name = input("Enter Warrior's Name (or type 'done' to finish): ")
            if name.lower() == 'done':
                break
            names.append(name)
        
        # Ask for the warrior's skills
        skills = []
        while True:
            skill = input("Enter Warrior's Skill (or type 'done' to finish): ")
            if skill.lower() == 'done':
                break
            skills.append(skill)
        
        # Insert warrior's basic information into WARRIOR table
        query = "INSERT INTO `WARRIOR` (`WARRIOR_ID`, `DOB`, `RANK`, `BATTLE_STATUS`, `KINGDOM_ID`) VALUES (%d, '%s', '%s', '%s', %d)" % (
            row["ID"], row["Bdate"], 'Unknown', row["battle_status"], row["kingdom_id"])
        
        print("Executing Query to insert into WARRIOR table: ", query)
        cur.execute(query)
        con.commit()

        # Insert warrior's name(s) into WARRIOR_NAME table
        for name in names:
            name_query = "INSERT INTO `WARRIOR_NAME` (`WARRIOR_ID`, `NAME`) VALUES (%d, '%s')" % (row["ID"], name)
            print("Executing Query to insert into WARRIOR_NAME table: ", name_query)
            cur.execute(name_query)
        
        # Insert warrior's skill(s) into WARRIOR_SKILLS table
        for skill in skills:
            skill_query = "INSERT INTO `WARRIOR_SKILLS` (`WARRIOR_ID`, `SKILLS`) VALUES (%d, '%s')" % (row["ID"], skill)
            print("Executing Query to insert into WARRIOR_SKILLS table: ", skill_query)
            cur.execute(skill_query)
        
        # Commit all the changes
        con.commit()
        print("Warrior details inserted into database successfully!")
        
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def delete_event_and_related_data():
    try:
        # Ask the user for the Event_ID to delete
        event_id = int(input("Enter the Event_ID for Yuddhahāni to delete: ").strip())

        # Delete related data from YUDDHAHANI_WARRIOR_ID table first
        delete_related_query = """
        DELETE FROM YUDDHAHANI_WARRIOR_ID
        WHERE EVENT_ID = %s;
        """
        cur.execute(delete_related_query, (event_id,))
        con.commit()

        # Check if any rows were affected in the YUDDHAHANI_WARRIOR_ID table
        if cur.rowcount > 0:
            print(f"Successfully deleted related data in YUDDHAHANI_WARRIOR_ID for Event_ID {event_id}.")
        else:
            print(f"No related data found in YUDDHAHANI_WARRIOR_ID for Event_ID {event_id}.")

        # Now, delete the event from the EVENTS table
        delete_event_query = """
        DELETE FROM YUDDHAHANI
        WHERE EVENT_ID = %s;
        """
        cur.execute(delete_event_query, (event_id,))
        con.commit()

        # Check if any rows were affected in the EVENTS table
        if cur.rowcount > 0:
            print(f"Successfully deleted the Event_ID {event_id}.")
        else:
            print(f"No event found with Event_ID {event_id} and name 'YUDDHAHANI'.")

    except Exception as e:
        con.rollback()  # Rollback the transaction in case of error
        print("Error while deleting data:", e)




def get_formation_and_warrior_names():   #IF WANT PRINT THE MULTIPLE NAMES OF THE COMMANDER
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


def add_new_formation():                  #didn't check this have to check this function
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


def modify_battle_formation():
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


def Delete_warrior():
    print("delet warrior")


def dispatch(ch):
    if ch == 1:
        get_warriors_by_kingdom()
    elif ch == 2:
        get_divine_weapons()
    elif ch == 3:
        get_battle_formations()
    elif ch == 4:
        get_kingdoms_by_alliance()
    elif ch == 5:
        get_total_strength_by_anga()
    elif ch == 6:
        search_warriors_by_name()
    elif ch == 7:
        list_divine_weapons_by_kingdom()
    elif ch == 8:
        get_formation_and_warrior_names()
    elif ch == 9:
        Add_warrior()
    elif ch == 10:
        modify_battle_formation()
    elif ch == 11:
        delete_event_and_related_data()
    elif ch == 12:
        add_new_formation()
        
    else:
        print(Fore.LIGHTRED_EX+ Style.BRIGHT + "Error: Invalid Option" + Style.RESET_ALL)


# Get database connection details from the user
# user = input("Enter the database username (default 'root'): ") or "root"
# password = input("Enter the database password: ")
# db = input("Enter the database name (default 'ldb'): ") or "ldb"
user = "root"
password = "pass@dna123A"
db = "pp4"

# Global
try:
    # Establish the database connection once
    con = pymysql.connect(
        host='localhost',
        port=3306,
        user=user,
        password=password,
        db=db,
        cursorclass=pymysql.cursors.DictCursor
    )
    
    sp.call('clear', shell=True)
    print_banner()

    if con.open:
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Connected to database!" + Style.RESET_ALL)
    else:
        print(Fore.LIGHTRED_EX + Style.BRIGHT + "Failed to connect to database." + Style.RESET_ALL)
        exit()

    input(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Press ENTER to continue..." + Style.RESET_ALL)

    with con.cursor() as cur:
        # Loop for user interaction
        while True:
            sp.call('clear', shell=True)
            print_banner()
            print_menu()
            ch = int(input(Fore.LIGHTCYAN_EX+ Style.BRIGHT + "Enter your choice: " + Style.RESET_ALL))
            sp.call('clear', shell=True)

            if ch == 14:
                print(Fore.LIGHTRED_EX+ Style.BRIGHT + "Goodbye!" + Style.RESET_ALL)
                break  # Exit the loop
            else:
                try:
                    dispatch(ch)
                except Exception as e:
                    print(Fore.LIGHTRED_EX+ Style.BRIGHT + "Error during operation: " + Style.RESET_ALL + str(e))
                input(Fore.LIGHTYELLOW_EX+ Style.BRIGHT + "Press ENTER to continue..." + Style.RESET_ALL)

except Exception as e:
    sp.call('clear', shell=True)
    print(Fore.LIGHTRED_EX+ Style.BRIGHT + "Failed to connect to the database: " + Style.RESET_ALL + str(e))

finally:
    if 'con' in locals() and con.open:
        con.close()
        print(Fore.LIGHTCYAN_EX+ Style.BRIGHT + "Database connection closed." + Style.RESET_ALL)
