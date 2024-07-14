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


# firstName = "Borsbsbfaq"
# lastName = "Nezar"
# title = "Mr."
# age = 27
# nation = "Iraq-IQ"
# regStat = True
# national = "OK1"
# terms = False

# oldData = readJsonFile('json/users.json')

# oldData['users'][firstName.upper()] = {
#     "FirstName": firstName,
#     "LastName": lastName,
#     "Title": title,
#     "Age": age,
#     "Nationality": nation,
#     "Registration_Status": regStat,
#     "Nationalitys": national,
#     "TermsAndConditions": terms
#     }

# addLineToJsonFile('json/users.json', oldData)
# after = readJsonFile('json/users.json')
# print(after)