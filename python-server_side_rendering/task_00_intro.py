"""

"""

def generate_invitations(template, attendees):
    # Check for empty inputs
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Check for input types
    if not isinstance(template, str):
        print("Error: Template is not str, it's a " + str(type(template)))
        return

    if not isinstance(attendees, list):
        print("Error: Attendees is not a list, it's a " + str(type(attendees)))
        return

    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Not all elements in attendees are dicts")
        return

    # Use a loop to map the dict values into the string
    for i, attendee in enumerate(attendees, 1):
        # Format each attendee
        cleaned_attendee = {}
        for key, value in attendee.items():
            if value is None:
                cleaned_attendee[key] = f"{key}:N/A"
            else:
                cleaned_attendee[key] = value

        # Use edited attendee to format the invitation
        invitation = template.format_map(cleaned_attendee)
        with open(f"output_{i}.txt", "w") as f:
            f.write(invitation)