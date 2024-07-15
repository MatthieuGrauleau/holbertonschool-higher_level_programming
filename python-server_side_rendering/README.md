0. Creating a Simple Templating Program
mandatory
In this task, you will create a Python function that generates personalized invitation files from a template with placeholders and a list of objects. Each output file should be named sequentially, starting from 1. You will also implement specific error handling for various edge cases.

Objective
Understand how to use string templating in Python.
Implement file operations for reading templates and writing output files.
Handle various edge cases and errors gracefully.
Instructions
Create the Template:

Use the provided template with placeholders for name, event_title, event_date, and event_location.
Define the Data:

Use the provided list of objects as your data source.
Write the Templating Function:

Define a function named generate_invitations that takes two parameters: template and attendees.
Check Input Types:

Verify that template is a string and attendees is a list of dictionaries.
If template is not a string or attendees is not a list of dictionaries, log an error message and terminate the function.
Handle Empty Inputs:

Check if the template is empty and log an error message if it is.
Check if the attendees list is empty and log an error message if it is.
Process Each Attendee:

Iterate over the list of attendees and replace the placeholders in the template with the corresponding values from each attendee’s dictionary.
If a value is missing, replace it with “N/A”.
Generate Output Files:

Write the processed template to output files named output_X.txt, where X is the index of the attendee starting from 1.
Specific Error Handling Behaviors:
Empty Template: If the template is empty, log an error message, “Template is empty, no output files generated.” and terminate without creating any files.
Empty List of Objects: If the list of objects is empty, log a message, “No data provided, no output files generated.” and terminate without creating any files.
Missing Data in Object: If an object is missing data for any of the placeholders, replace the missing data with the text “N/A” in the output file. For example, if event_date is missing, it should appear as “event_date: N/A” in the output.
Invalid Input Types: If the input template is not a string or the list is not a list of dictionaries, log an error message indicating the type of invalid input and terminate the function.