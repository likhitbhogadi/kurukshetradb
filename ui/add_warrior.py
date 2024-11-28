def Add_warrior(cur, con):
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