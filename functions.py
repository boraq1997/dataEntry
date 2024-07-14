import importFiles as imf

def readJsonFile(filename):
    try:
        with open(filename, 'r') as f:
            data = imf.json.load(f)
            return data
    except FileNotFoundError:
        imf.messagebox.showinfo(title="ERROR", message=f"ERROR: file {filename} is not found.", icon="warning")
    
    except imf.json.JSONDecodeError:
        imf.messagebox.showinfo(title="ERROR", message=f"ERROR: file {filename} is not valid JSON", icon="warning")
    
def addLineToJsonFile(filename, newData):
    try:
        with open(filename, 'w') as f:
            imf.json.dump(newData, f, indent=4)
            imf.messagebox.showinfo(title="SUCCESS", message="add new user succesfuly.", icon="info")
    except PermissionError as e:
        imf.messagebox.showinfo(title="PERMISION ERROR", message="file permision error", icon="warning")
    except Exception as e:
        imf.messagebox.showinfo(title="ERROR", message=f"error: {e}", icon="error")
