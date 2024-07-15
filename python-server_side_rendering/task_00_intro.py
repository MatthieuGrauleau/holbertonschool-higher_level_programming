#!/usr/bin/python3

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Template should be a string")
        return
    if not isinstance(attendees, list):
        print("Attendees should be a list")
        return
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    for i, attende in enumerate(attendees, start=1):
        content = template
        for placeholder in ["name", "event_title", "event_date", "event_location"]:
                value = attende.get(placeholder, "N/A")
                content = content.replace(f"{{{placeholder}}}", value if value else "N/A")
        
        output_filename = f"output_{i}.txt"
        with open(output_filename, "w") as output_file:
            output_file.write(content)
        print(f"Generated {output_filename}")