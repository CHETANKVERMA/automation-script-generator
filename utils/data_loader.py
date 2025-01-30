import os
import pandas as pd

DATA_FOLDER = "data"

def generate_sample_data():
    """Generates 10 independent CSV automation script files automatically."""
    
    # Define 10 distinct sets of automation tasks
    sample_data_1 = [
        ["Open webpage", "openWebPage(url)"],
        ["Parse HTML", "parseHTML(html)"],
        ["Extract data", "extractDataFromHTML(selector)"],
        ["Save data", "saveDataToCSV(fileName)"]
    ]

    sample_data_2 = [
        ["Send GET request", "sendGetRequest(url)"],
        ["Send POST request", "sendPostRequest(url, data)"],
        ["Validate response", "validateResponse(response)"]
    ]

    sample_data_3 = [
        ["Create file", "createFile(filePath)"],
        ["Write to file", "writeToFile(filePath, content)"],
        ["Read file", "readFile(filePath)"],
        ["Delete file", "deleteFile(filePath)"]
    ]

    sample_data_4 = [
        ["Click element", "clickElement(elementID)"],
        ["Enter text", "enterText(inputID, text)"],
        ["Submit form", "submitForm(formID)"]
    ]

    sample_data_5 = [
        ["Connect to database", "connectToDatabase(dbUrl)"],
        ["Query database", "queryDatabase(query)"],
        ["Store result", "storeQueryResult(fileName)"]
    ]

    sample_data_6 = [
        ["Capture screenshot", "captureScreenshot(filePath)"],
        ["Save screenshot", "saveScreenshot(filePath)"]
    ]

    sample_data_7 = [
        ["Login", "login(username, password)"],
        ["Navigate to dashboard", "navigateToDashboard()"],
        ["Logout", "logout()"]
    ]

    sample_data_8 = [
        ["Send email", "sendEmail(to, subject, body)"],
        ["Check inbox", "checkInbox()"],
        ["Delete email", "deleteEmail(emailID)"]
    ]

    sample_data_9 = [
        ["Generate report", "generateReport(data)"],
        ["Save report", "saveReport(fileName)"],
        ["Send report", "sendReport(recipient)"]
    ]

    sample_data_10 = [
        ["Download file", "downloadFile(url)"],
        ["Extract data", "extractDataFromZip(filePath)"],
        ["Process data", "processData(data)"]
    ]

    # Ensuring the "data" folder exists
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    # Create 10 distinct scripts with independent steps
    sample_data_list = [
        sample_data_1,
        sample_data_2,
        sample_data_3,
        sample_data_4,
        sample_data_5,
        sample_data_6,
        sample_data_7,
        sample_data_8,
        sample_data_9,
        sample_data_10
    ]

    for i, sample_data in enumerate(sample_data_list, 1):
        df = pd.DataFrame(sample_data, columns=["Step", "Function"])
        df.to_csv(f"{DATA_FOLDER}/script_{i}.csv", index=False)

def load_data():
    """Loads all CSV files into a single DataFrame."""
    all_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")]
    dataframes = [pd.read_csv(os.path.join(DATA_FOLDER, file)) for file in all_files]
    return pd.concat(dataframes, ignore_index=True)

if __name__ == "__main__":
    generate_sample_data()
    print("✅ Sample data generated.")
