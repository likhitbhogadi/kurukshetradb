def get_total_strength_by_anga(cur):  # if want add the case where user doesn't provide any info of anganama   WHAT ABOUT PARTICULAR ARMY
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