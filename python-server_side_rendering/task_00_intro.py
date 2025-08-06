"""

"""

def generate_invitations(template, attendees):
    # Check for empty inputs
    if not template:
        raise ValueError("Template is empty, no output files generated.")
    if not attendees:
        raise ValueError("No data provided, no output files generated.")

    # Check for input types
    if not isinstance(template, str):
        raise TypeError("Template is not str, it's a " + str(type(template)))

    if not isinstance(attendees, list):
        raise TypeError("Attendees is not a list, it's a " + str(type(attendees)))

    if not all(isinstance(attendee, dict) for attendee in attendees):
        raise TypeError("Not all elements in attendees are dicts")

    # Use a loop to map the dict values into the string
    for i, attendee in enumerate(attendees):
        invitation = template.format_map(attendee)
        try:
            with open(f"output_{i}.txt", "w") as f:
                f.write(invitation)
        except FileExistsError:
            print("Already Exists")