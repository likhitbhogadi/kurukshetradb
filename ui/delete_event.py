def delete_event_and_related_data(cur, con):
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