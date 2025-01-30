def generate_script_from_steps(user_steps):
    # Predefined steps mapped to their corresponding function names
    functions = {
        "Open webpage": "openWebPage()",
        "Parse HTML": "parseHTML()",
        "Extract data": "extractData()",
        "Save data to CSV": "saveDataToCSV()",
        "Login": "login(username, password)",
        "Click button": "clickButton(buttonName)",
        "Fill form": "fillForm(formData)",
        "Submit form": "submitForm()",
        "Verify message": "verifyMessage(expectedMessage)",
        "Logout": "logout()"
    }

    # Initialize the content of the generated script
    script_content = "# Generated Automation Script\n\n"

    # Iterate through user input steps
    for step in user_steps:
        # Check if the step is in the predefined functions
        if step in functions:
            script_content += f"def {functions[step]}:\n    print('{step}...')\n\n"
        else:
            script_content += f"# {step} is not defined\n\n"

    # Return the complete script content as a string
    return script_content
