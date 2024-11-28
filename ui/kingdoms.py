def get_kingdoms_by_alliance(cur):
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