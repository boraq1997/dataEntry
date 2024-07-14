import importFiles as imf

def add():
    AcceptCheck = accBtn.get()
    if AcceptCheck == 1:
        firstName = firstNameEntry.get()
        LastName = lastNameEntry.get()
        title = userTitleCombobox.get()
        age = userAgeSpinbox.get()
        country = userContryCombobox.get()
        registrationStatus = regStat.get()
        natinality = natinalityComboBox.get()
        
        oldData = imf.func.readJsonFile('json/users.json')
        oldData['users'][firstName.upper()] = {
            "FirstName": firstName,
            "LastName": LastName,
            "Title": title,
            "Age": age,
            "Nationality": country,
            "Registration_Status": registrationStatus,
            "Nationalitys": natinality,
            "TermsAndConditions": AcceptCheck
        }
        imf.func.addLineToJsonFile('json/users.json', oldData)
    else:
        imf.messagebox.showwarning(title="ERROR", message="terms conditional most be checked to send data")

    # imf.func.addLineToJsonFile('json', oldData)
    # return 'SUCCESS'

root = imf.tk.Tk()
root.title("Data Entry Project")
root.option_add("*tearOff", False)
root.resizable(False, False)

style = imf.ttk.Style(root)
root.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")

mainFrame = imf.ttk.Frame(root)
mainFrame.pack()

regStat = imf.tk.IntVar()
accBtn =imf.tk.IntVar()

#====[USER INFORMATION]==
UserInfoFrame = imf.ttk.LabelFrame(mainFrame, text="User Information", padding=(5, 5, 5, 5))
UserInfoFrame.grid(row=0, column=0, padx=20, pady=20)

firstNameLabel = imf.ttk.Label(UserInfoFrame, text="First Name")
firstNameLabel.grid(row=0, column=0)
firstNameEntry = imf.ttk.Entry(UserInfoFrame)
firstNameEntry.grid(row=1, column=0)

lastNameLabel = imf.ttk.Label(UserInfoFrame, text="Last Name")
lastNameLabel.grid(row=0, column=1)
lastNameEntry = imf.ttk.Entry(UserInfoFrame)
lastNameEntry.grid(row=1, column=1)

userTitleLabel = imf.tk.Label(UserInfoFrame, text="Title")
userTitleLabel.grid(row=0, column=2)
userTitleCombobox = imf.ttk.Combobox(UserInfoFrame, values=["", "Mr.", "Ms.", "Dr.", "Eng."])
userTitleCombobox.grid(row=1, column=2)

userAgeLabel = imf.ttk.Label(UserInfoFrame, text="Age")
userAgeLabel.grid(row=2, column=0)
userAgeSpinbox = imf.ttk.Spinbox(UserInfoFrame, from_=10, to=80)
userAgeSpinbox.grid(row=3, column=0)

userCountryLabel = imf.ttk.Label(UserInfoFrame, text="Nationality")
userCountryLabel.grid(row=2, column=1)
userContryCombobox = imf.ttk.Combobox(UserInfoFrame, values=['', 'IRAQ-IQ', "UNITED STATE-US"])
userContryCombobox.grid(row=3, column=1)

for widget in UserInfoFrame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#====[USER SKILLS]==
userSkillsFrame = imf.ttk.LabelFrame(mainFrame, padding=(5, 5, 5, 5))
userSkillsFrame.grid(row=1, column=0, padx=20, pady=20, sticky="news")

registrationStatusLabel = imf.ttk.Label(userSkillsFrame, text="Registration Status")
registrationStatusLabel.grid(row=0, column=0)
registrationStatusCheckBtn = imf.ttk.Checkbutton(userSkillsFrame, text="Currently Registered", variable=regStat)
registrationStatusCheckBtn.grid(row=1, column=0)

natinalityLabel = imf.ttk.Label(userSkillsFrame, text="Nationality")
natinalityLabel.grid(row=0, column=1)
natinalityComboBox = imf.ttk.Spinbox(userSkillsFrame, from_=0, to="infinity")
natinalityComboBox.grid(row=1, column=1)

for widget in userSkillsFrame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#====[USER TERMS]==
UserTermsFrame = imf.ttk.LabelFrame(mainFrame, text="Terms & Conditions")
UserTermsFrame.grid(row=2, column=0, padx=20, pady=20, sticky="news")

AcceptCheckBtn = imf.ttk.Checkbutton(UserTermsFrame, text="I accept the Terms and conditions", variable=accBtn)
AcceptCheckBtn.grid(row=0, column=0)

submitButton = imf.ttk.Button(mainFrame, text="Enter Data", command=add)
submitButton.grid(row=3, column=0, padx=5, pady=5, sticky="news")

root.mainloop()