from smsmodule import *

print("MENU:\n", "=>> CREATE.\n", "=>> SEARCH.\n",
      "=>> VIEW ALL STUDENT.\n", "=>> VIEW EACH STUDENT.\n", "=>> EDIT.\n", "=>> DELETE.\n")
menu = input("=>> WHAT DO YOU WANT TO DO?: ")
data = menu.strip().title()
if data in ["Search", "Create", "View All Student", "View Each Student", "Edit", "Delete"]:
    match data:
        case "Create":
            print("CREATE RECORD:\n", "=>> 1. Personal Data.\n", "=>> 2. Acedemic Performance.\n", "=>> 3. Behavioural Skills.\n",
                  "=>> 4. Psychomotor.\n", "=>> 5. Performance Analysis.\n", "=>> 6. School Comment.\n")
            data2 = input("=>> ENTER MENU NUMBER TO CHOOSE RECORD TO CREATE: ")
            # function to create student record
            match data2:
                case "1":
                    Personal_data.create_personal_data()
                case "2":
                    Acedemic_performance_a.create_acedemic_performance_a()
                case "3":
                    Acedemic_performance_c.create_acedemic_performance_c()
                case "4":
                    Acedemic_performance_b.create_acedemic_performance_b()
                case "5":
                    Performance_analysis.create_performance_analysis()
                case "6":
                    School_comment.create_school_comment()

        case "Search":
            print("SEARCH RECORD:\n", "=>> 1. Personal Data.\n", "=>> 2. Acedemic Performance.\n", "=>> 3. Behavioural skills.\n",
                  "=>> 4. Psychomotor.\n", "=>> 5. Performance Analysis.\n", "=>> 6. School Comment.\n")

            data2 = input("=>> ENTER MENU NUMBER TO CHOOSE RECORD TO SEARCH: ")

            match data2:
                case "1":
                    print("=>> SEARCH PERSONAL DATA RECORD <<=")
                    lists = []
                    try:
                        with open("personal-data.csv") as file:
                            reader = csv.DictReader(file)
                            for row in reader:
                                lists.append(row)
                    except FileNotFoundError:
                        print("File not found!")

                    name = get_name()
                    clss = pupil_class()
                    term = school_term()

                    while True:
                        session = input("=>> Session: ").title()
                        if any(char.isdigit() for char in session) and session:
                            break
                        else:
                            print(
                                "Use correct format for session - (e.g) 2021/2022 Session!")
                            continue

                    for list in lists:
                        if name == list["name"] and clss == list["class"] and term == list["term"] and session == list["session"]:
                            print("=>> DATE: ", list["date"] + "\n" + "=>> REG NO: ", list["reg_no"] + "\n" + "=>> PUPILS NAME: ", list["name"] + "\n" + "=>> PUPILS CLASS: ", list["class"] + "\n" + "=>> TERM: ", list["term"] + "\n" +
                                  "=>> SESSION: ", list["session"] + "\n" + "=>> DATE OF BIRTH: ", list["date_of_birth"] + "\n" + "=>> GENDER: ", list["gender"] + "\n" + "=>> ADDRESS: ", list["address"] + "\n" + "=>> MOBILE NO: ", list["mobile_no"])
                            break
                    else:
                        print(
                            "You have entered an incorrect input in the prompt for Name or Pupils Class or Term or Session!")

                case "2":
                    print("=>> SEARCH ACEDEMIC PERFORMANCE RECORD <<=")
                    retrieve_subject()
                    lists = []
                    try:
                        with open(create_acedemic_performance_filename()) as file:
                            reader = csv.DictReader(file)
                            for row in reader:
                                lists.append(row)
                    except FileNotFoundError:
                        print("File not found!")

                    name = get_name()
                    sub = pupil_subject()
                    clss = pupil_class()
                    term = school_term()

                    while True:
                        session = input("=>> Session: ").title()
                        if any(char.isdigit() for char in session) and session:
                            break
                        else:
                            print(
                                "Use correct format for session - (e.g) 2021/2022 Session!")
                            continue

                    for list in lists:
                        if sub == list["subject"] and name == list["name"] and clss == list["class"] and term == list["term"] and session == list["session"]:
                            print("=>> Pupils Name: ", list["name"] + "\n" + "=>> Pupils Class: ", list["class"] + "\n" + "=>> Subject: ", list["subject"] + "\n" + "=>> Term: ", list["term"] + "\n" + "=>> Session: ", list["session"] + "\n" + "=>> CAT1: ", list["cat1"] + "\n" +
                                  "=>> CAT2: ", list["cat2"] + "\n" + "=>> Exam: ", list["exam"] + "\n" + "=>> Total: ", list["total"] + "\n" + "=>> Average Score: ", list["class_average"] + "\n" + "=>> Subject Position: ", list["subject_position"] + "\n" + "=>> Grade: ", list["grade"])
                            break
                    else:
                        print(
                            "You have entered an incorrect input in the prompt for Subject or Name or Pupils Class or Term or Session!")

                case "3":
                    print("=>> SEARCH PSYCHOMOTOR RECORD <<=")
                    lists = []
                    try:
                        with open("acedemic-performance-b.csv") as file:
                            reader = csv.DictReader(file)
                            for row in reader:
                                lists.append(row)
                    except FileNotFoundError:
                        print("File not found!")

                    name = get_name()
                    clss = pupil_class()
                    term = school_term()

                    while True:
                        session = input("Session: ").title()
                        if any(char.isdigit() for char in session) and session:
                            break
                        else:
                            print(
                                "Use correct format for session - (e.g) 2021/2022 Session!")
                            continue

                    for list in lists:
                        if name == list["name"] and clss == list["class"] and term == list["term"] and session == list["session"]:
                            print("=>> PUPILS NAME: ", list["name"] + "\n" + "=>> PUPILS CLASS: ", list["class"] + "\n" + "=>> TERM: ", list["term"] + "\n" + "=>> SESSION: ", list["session"] + "\n" + "=>> HANDWRITING: ", list["handwriting"] + "\n" +
                                  "=>> FLUENCY: ", list["fluency"] + "\n" + "=>> GAME: ", list["game"] + "\n" + "=>> DRAWING: ", list["drawing"] + "\n" + "MUSICAL SKILLS: ", list["musical_skill"] + "\n" + "=>> TOOL HANDLING: ", list["tool_handling"])
                            break
                    else:
                        print(
                            "You have entered an incorrect input in the prompt for Name or Pupils Class or Term or Session!")

                case "4":
                    print("=>> SEARCH BEHAVIOUR SKILL RECORD <<=")
                    lists = []
                    try:
                        with open("acedemic-performance-section-c.csv") as file:
                            reader = csv.DictReader(file)
                            for row in reader:
                                lists.append(row)
                    except FileNotFoundError:
                        print("File not found!")

                    name = get_name()
                    clss = pupil_class()
                    term = school_term()

                    while True:
                        session = input("Session: ").title()
                        if any(char.isdigit() for char in session) and session:
                            break
                        else:
                            print(
                                "Use correct format for session - (e.g) 2021/2022 Session!")
                            continue

                    for list in lists:
                        if name == list["name"] and clss == list["class"] and term == list["term"] and session == list["session"]:
                            print("=>> PUPILS NAME: ", list["name"] + "\n" + "=>> PUPILS CLASS: ", list["class"] + "\n" + "=>> TERM: ", list["term"] + "\n" + "=>> SESSION: ", list["session"] + "\n" + "=>> NEATNESS: ", list["neatness"] + "\n" + "=>> PUNCTUALITY: ", list["punctuality"] + "\n" + "=>> ATTENDANCE: ", list["attendance"] +
                                  "\n" + "=>> POLITENESS: ", list["politness"] + "\n" + "=>> HONESTY: ", list["honesty"] + "\n" + "=>> RELATIONSHIP: ", list["relationship"] + "\n" + "=>> SELF CONTROL: ", list["self_control"] + "\n" + "=>> ATTENTIVENESS: ", list["attentiveness"] + "\n" + "=>> INITIATIVE: ", list["initiative"])
                            break
                    else:
                        print(
                            "You have entered an incorrect input in the prompt for Name or Pupils Class or Term or Session!")

                case "5":
                    print("=>> SEARCH PERFORMANCE ANALYSIS RECORD <<=")
                    lists = []
                    try:
                        with open("performance-analysis.csv") as file:
                            reader = csv.DictReader(file)
                            for row in reader:
                                lists.append(row)
                    except FileNotFoundError:
                        print("File not found!")

                    name = get_name()
                    clss = pupil_class()
                    term = school_term()

                    while True:
                        session = input("=>> Session: ").title()
                        if any(char.isdigit() for char in session) and session:
                            break
                        else:
                            print(
                                "Use correct format for session - (e.g) 2021/2022 Session!")
                            continue

                    for list in lists:
                        if name == list["pupils_name"] and clss == list["pupils_class"] and term == list["term"] and session == list["session"]:
                            print("=>> Pupils Name: ", list["pupils_name"] + "\n" + "=>> Pupils Class: ", list["pupils_class"] + "\n" + "=>> Term: ", list["term"] + "\n" +
                                  "=>> Session: ", list["session"] + "\n" + "=>> NUMBER OF SUBJECT: ", list["no_subject"] + "\n" + "=>> GRAND TOTAL: ", list["grand_total_score"] + "\n" + "=>> AVERAGE: ", list["average_score"])
                            break
                    else:
                        print(
                            "You have entered an incorrect input in the prompt for Name or Pupils Class or Term or Session!")

                case "6":
                    print("=>> SEARCH SCHOOL COMMENT RECORD <<=")
                    lists = []
                    try:
                        with open("school-comment.csv") as file:
                            reader = csv.DictReader(file)
                            for row in reader:
                                lists.append(row)
                    except FileNotFoundError:
                        print("File not found!")

                    name = get_name()
                    clss = pupil_class()
                    term = school_term()

                    while True:
                        session = input("Session: ").title()
                        if any(char.isdigit() for char in session) and session:
                            break
                        else:
                            print(
                                "Use correct format for session - (e.g) 2021/2022 Session!")
                            continue

                    for list in lists:
                        if name == list["name"] and clss == list["class"] and term == list["term"] and session == list["session"]:
                            print("=>> PUPILS NAME: ", list["name"] + "\n" + "=>> PUPILS CLASS: ", list["class"] + "\n" + "=>> TERM: ", list["term"] + "\n" + "=>> SESSION: ",
                                  list["session"] + "\n" + "CLASS TEACHERS REMARK: ", list["class_teacher_remark"] + "\n" + "=>> SCHOOL HEAD COMMENT: ", list["school_head_comment"])
                            break
                    else:
                        print(
                            "You have entered an incorrect input in the prompt for Name or Pupils Class or Term or Session!")
                case _:
                    print("No record!")

        case "View All Student":
            print("VIEW ALL RECORD:\n", "=>> 1. Personal Data.\n", "=>> 2. Acedemic Performance.\n", "=>> 3. Behavioural skills.\n",
                  "=>> 4. Psychomotor.\n", "=>> 5. Performance Analysis.\n", "=>> 6. School Comment.\n")

            data2 = input("=>> ENTER MENU NUMBER TO CHOOSE RECORD TO VIEW: ")

            match data2:
                case "1":
                    print("=>> VIEW ALL PERSONAL DATA RECORD <<=")
                    lists = []
                    try:
                        with open("personal-data.csv") as file:
                            reader = csv.DictReader(file)
                            for row in reader:
                                lists.append(row)
                    except FileNotFoundError:
                        print("File not found!")

                    clss = pupil_class()
                    term = school_term()

                    while True:
                        session = input("=>> Session: ").title()
                        if any(char.isdigit() for char in session) and session:
                            break
                        else:
                            print(
                                "Use correct format for session - (e.g) 2021/2022 Session!")
                            continue

                    for list in lists:
                        if clss == list["pupils_class"] and term == list["term"] and session == list["session"]:
                            print("=>> DATE: ", list["date"] + "\n" + "=>> REG NO: ", list["reg_no"] + "\n" + "=>> PUPILS NAME: ", list["pupils_name"] + "\n" + "=>> PUPILS CLASS: ", list["pupils_class"] + "\n" + "=>> TERM: ", list["term"] + "\n" +
                                  "=>> SESSION: ", list["session"] + "\n" + "=>> DATE OF BIRTH: ", list["date_of_birth"] + "\n" + "=>> GENDER: ", list["gender"] + "\n" + "=>> ADDRESS: ", list["address"] + "\n" + "=>> MOBILE NO: ", list["mobile_no"] + "\n")

                case "2":
                    print("=>> VIEW ALL ACEDEMIC PERFORMANCE RECORD <<=")

                    retrieve_subject()
                    lists = []

                    try:
                        with open(create_acedemic_performance_filename()) as file:
                            reader = csv.DictReader(file)
                            for row in reader:
                                lists.append(row)
                    except FileNotFoundError:
                        print("File not found!")

                    name = get_name()
                    clss = pupil_class()
                    term = school_term()

                    while True:
                        session = input("=>> Session: ").title()
                        if any(char.isdigit() for char in session) and session:
                            break
                        else:
                            print(
                                "Use correct format for session - (e.g) 2021/2022 Session!")
                            continue

                    for list in lists:
                        if name == list["name"] and clss == list["class"] and term == list["term"] and session == list["session"]:
                            print("=>> Pupils Name: ", list["name"] + "\n" + "=>> Pupils Class: ", list["class"] + "\n" + "=>> Term: ", list["term"] + "\n" + "=>> Session: ", list["session"] + "\n" + "=>> Subject: ", list["subject"] + "\n" + "=>> CAT1: ", list["cat1"] + "\n" +
                                  "=>> CAT2: ", list["cat2"] + "\n" + "=>> Exam: ", list["exam"] + "\n" + "=>> Total: ", list["total"] + "\n" + "=>> Average Score: ", list["class_average"] + "\n" + "=>> Subject Position: ", list["subject_position"] + "\n" + "=>> Grade: ", list["grade"] + "\n")

                case "3":
                    print("=>> VIEW ALL BEHAVIOUR SKILL RECORD <<=")
                    lists = []
                    try:
                        with open("acedemic-performance-c.csv") as file:
                            reader = csv.DictReader(file)
                            for row in reader:
                                lists.append(row)
                    except FileNotFoundError:
                        print("File not found!")

                    clss = pupil_class()
                    term = school_term()

                    while True:
                        session = input("=>> Session: ").title()
                        if any(char.isdigit() for char in session) and session:
                            break
                        else:
                            print(
                                "Use correct format for session - (e.g) 2021/2022 Session!")
                            continue

                    for list in lists:
                        print("=>> PUPILS NAME: ", list["pupils_name"] + "\n" + "=>> PUPILS CLASS: ", list["pupils_class"] + "\n" + "=>> TERM: ", list["term"] + "\n" + "=>> SESSION: ", list["session"] + "\n" + "=>> NEATNESS: ", list["neatness"] + "\n" + "=>> PUNCTUALITY: ", list["punctuality"] + "\n" + "=>> ATTENDANCE: ", list["attendance"] +
                              "\n" + "=>> POLITENESS: ", list["politeness"] + "\n" + "=>> HONESTY: ", list["honesty"] + "\n" + "=>> RELATIONSHIP: ", list["relationship"] + "\n" + "=>> SELF CONTROL: ", list["self_control"] + "\n" + "=>> ATTENTIVENESS: ", list["attentiveness"] + "\n" + "=>> INITIATIVE: ", list["initiative"] + "\n")

                case "4":
                    print("=>> VIEW ALL PSYCHOMOTOR RECORD <<=")
                    lists = []
                    try:
                        with open("acedemic-performance-b.csv") as file:
                            reader = csv.DictReader(file)
                            for row in reader:
                                lists.append(row)
                    except FileNotFoundError:
                        print("File not found!")

                    clss = pupil_class()
                    term = school_term()

                    while True:
                        session = input("=>> Session: ").title()
                        if any(char.isdigit() for char in session) and session:
                            break
                        else:
                            print(
                                "Use correct format for session - (e.g) 2021/2022 Session!")
                            continue

                    for list in lists:
                        if clss == list["pupils_class"] and term == list["term"] and session == list["session"]:
                            print("=>> PUPILS NAME: ", list["pupils_name"] + "\n" + "=>> PUPILS CLASS: ", list["pupils_class"] + "\n" + "=>> TERM: ", list["term"] + "\n" + "=>> SESSION: ", list["session"] + "\n" + "=>> HANDWRITING: ", list["handwriting"] + "\n" +
                                  "=>> FLUENCY: ", list["fluency"] + "\n" + "=>> GAME: ", list["game"] + "\n" + "=>> DRAWING: ", list["drawing"] + "\n" + "=>> MUSICAL SKILLS: ", list["musical_skill"] + "\n" + "=>> TOOL HANDLING: ", list["tool_handling"] + "\n")

                case "5":
                    print("=>> VIEW ALL PERFORMANCE ANALYSIS RECORD <<=")
                    lists = []
                    try:
                        with open("performance-analysis.csv") as file:
                            reader = csv.DictReader(file)
                            for row in reader:
                                lists.append(row)
                    except FileNotFoundError:
                        print("File not found!")

                    clss = pupil_class()
                    term = school_term()

                    while True:
                        session = input("=>> Session: ").title()
                        if any(char.isdigit() for char in session) and session:
                            break
                        else:
                            print("Illigal input!")
                            continue

                    for list in lists:
                        if clss == list["pupils_class"] and term == list["term"] and session == list["session"]:
                            print("=>> Pupils Name: ", list["pupils_name"] + "\n" + "=>> Pupils Class: ", list["pupils_class"] + "\n" + "=>> Term: ", list["term"] + "\n" + "=>> Session: ",
                                  list["session"] + "\n" + "=>> NUMBER OF SUBJECT: ", list["no_subject"] + "\n" + "=>> GRAND TOTAL: ", list["grand_total_score"] + "\n" + "=>> AVERAGE: ", list["average_score"])
                            print("\n")

                case "6":
                    print("=>> VIEW ALL SCHOOL COMMENT RECORD <<=")
                    lists = []
                    try:
                        with open("school-comment.csv") as file:
                            reader = csv.DictReader(file)
                            for row in reader:
                                lists.append(row)
                    except FileNotFoundError:
                        print("File not found!")

                    clss = pupil_class()
                    term = school_term()

                    while True:
                        session = input("=>> Session: ").title()
                        if any(char.isdigit() for char in session) and session:
                            break
                        else:
                            print("Illigal input!")
                            continue

                    for list in lists:
                        if clss == list["pupils_class"] and term == list["term"] and session == list["session"]:
                            print("=>> PUPILS NAME: ", list["pupils_name"] + "\n" + "=>> PUPILS CLASS: ", list["pupils_class"] + "\n" + "=>> TERM: ", list["term"] + "\n" + "=>> SESSION: ",
                                  list["session"] + "\n" + "=>> CLASS TEACHERS REMARK: ", list["class_teacher_remark"] + "\n" + "=>> SCHOOL HEAD COMMENT: ", list["school_head_comment"] + "\n")

                case _:
                    print("No record!")

        case "View Each Student":
            print("\n")
            username = input("=>> ENTER USER'S UNIQUE USERNAME: ")
            ext = ".csv"
            name = get_name()
            clss = pupil_class()
            term = school_term()

            while True:
                session = input("=>> Session: ").title()
                if any(char.isdigit() for char in session) and session:
                    break
                else:
                    print("Use correct format for session - (e.g) 2021/2022 Session!")
                    continue

            lists = []
            try:
                with open("personal-data.csv") as file:
                    reader = csv.DictReader(file)                
                    for row in reader:
                        lists.append(row)
            except FileNotFoundError:
                print("File not found!")

            for list in lists:
                if name == list["pupils_name"] and clss == list["pupils_class"] and term == list["term"] and session == list["session"]:
                    print("\n=>> PERSONAL DATA <<=\n", "=>> Date: ", list["date"] + "\n" + "=>> Reg No: ", list["reg_no"] + "\n" + "=>> Pupils name: ", list["pupils_name"] + "\n" + "=>> Pupils class: ", list["pupils_class"] + "\n" + "=>> Term: ", list["term"] + "\n" + "=>> Session: ", list["session"] + "\n" +  "=>> date of Birth: ", list["date_of_birth"] + "\n" + "=>> Gender: ", list["gender"] + "\n" + "=>> Address: ", list["address"] + "\n" + "=>> Mobile No: ", list["mobile_no"] + "\n")

            lists = []
            try:    
                with open(f"{username + ext}") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        lists.append(row)
            except FileNotFoundError:
                print("File not found!")

            for list in lists:
                if name == list["pupils_name"] and clss == list["pupils_class"] and term == list["term"] and session == list["session"]:
                    print("=>> Subject: ", list["subject"] + "\n" + "=>> CAT1: ", list["cat1"] + "\n" + "=>> CAT2: ", list["cat2"] + "\n" + "=>> Exam: ", list["exam"] + "\n" + "=>> Total: ", list["total"] + "\n" + "=>> Average Score: ", list["class_average"] + "\n" + "=>> Subject Position: ", list["subject_position"] + "\n" + "=>> Grade: ", list["grade"] + "\n")

            lists = []
            try:
                with open("acedemic-performance-c.csv") as file:
                    reader = csv.DictReader(file)                
                    for row in reader:
                        lists.append(row)
            except FileNotFoundError:
                print("File not found!")

            for list in lists:
                if name == list["pupils_name"] and clss == list["pupils_class"] and term == list["term"] and session == list["session"]:
                    print("=>> BEHAVIOUR SKILL <<=\n", "=>> Neatness: ", list["neatness"] + "\n" + "=>> Punctuality: ", list["punctuality"] + "\n" + "=>> Attendance: ", list["attendance"] + "\n" + "=>> Politeness: ", list["politeness"] + "\n" + "=>> Relationship: ", list["relationship"] + "\n" + "=>> Self control: ", list["self_control"] + "\n" + "=>> Attentiveness: ", list["attentiveness"] + "\n" + "=>> Initiative: ", list["initiative"] + "\n")

            lists =[]
            try:
                with open("acedemic-performance-b.csv") as file:
                    reader = csv.DictReader(file)                
                    for row in reader:
                        lists.append(row)
            except FileNotFoundError:
                print("File not found!")

            for list in lists:
                if name == list["pupils_name"] and clss == list["pupils_class"] and term == list["term"] and session == list["session"]:
                    print("=>> PSYCHOMOTOR <<=\n", "=>> Handwriting: ", list["handwriting"] + "\n" + "=>> Fluency: ", list["fluency"] + "\n" + "=>> Game: ", list["game"] + "\n" + "=>> Drawing: ", list["drawing"] + "\n" + "=>> Musical skill: ", list["musical_skill"] + "\n" + "=>> Tool handling: ", list["tool_handling"] + "\n")


            lists =[]
            try:
                with open("performance-analysis.csv") as file:
                    reader = csv.DictReader(file)                
                    for row in reader:
                        lists.append(row)
            except FileNotFoundError:
                print("File not found!")

            for list in lists:
                print("=>> PERFORMANCE ANALYSIS <<=\n", "=>> Number of subject: ", list["no_subject"] + "\n" + "=>> Grand total score: ", list["grand_total_score"] + "\n" + "=>> Average score: ", list["average_score"] + "\n")
                

            lists = []
            try:
                with open("school-comment.csv") as file:
                    reader = csv.DictReader(file)                
                    for row in reader:
                        lists.append(row)
            except FileNotFoundError:
                print("File not found!")

            for list in lists:
                print("=>> SCHOOL COMMENT <<=\n", "=>> school teachers comment: ", list["class_teacher_remark"] + "\n" + "=>> school head comment: ", list["school_head_comment"] + "\n")
                            

        case "Edit":
            print("EDIT RECORD:\n" + "=>> 1. Personal Data.\n" + "=>> 2. Acedemic Performance.\n" + "=>> 3. Behavioural Skills.\n" +
                  "=>> 4. Psychomotor.\n" + "=>> 5. Performance Analysis.\n" + "=>> 6. School Comment.\n")
            itemtoedit = input("=>> ENTER NUMBER TO CHOOSE RECORD TO EDIT: ")
            match itemtoedit:
                case "1":
                    print("=>> UPDATE PUPILS PERSONAL DATA <<=")
                    updatedlist = []

                    clss = pupil_class()
                    term = school_term()

                    while True:
                        session = input("=>> Session: ").title()
                        if any(char.isdigit() for char in session) and session:
                            break
                        else:
                            print(
                                "Use correct format for session - (e.g) 2021/2022 Session!")
                            continue

                    try:
                        with open("personal-data.csv", newline="") as file:
                            reader = csv.DictReader(file)
                            itemtoupdate = get_name()
                            for row in reader:
                                if clss == row["pupils_class"] and term == row["term"] and session == row["session"]:
                                    if row["pupils_name"] != itemtoupdate:
                                        updatedlist.append(row)
                    except FileNotFoundError:
                        print("File not found!")

                    with open("personal-data.csv", "w") as file:
                        fieldnames = ["date", "reg_no", "pupils_name", "pupils_class", "term",
                                      "session", "date_of_birth", "gender", "address", "mobile_no"]
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(updatedlist)
                        print("File has been updated")

                    Personal_data.create_updated_personal_data()

                case "2":
                    print("=>> UPDATE ACEDEMIC PERFORMANCE DATA <<=")
                    updatedlist = []

                    clss = pupil_class()
                    term = school_term()

                    while True:
                        session = input("=>> Session: ").title()
                        if any(char.isdigit() for char in session) and session:
                            break
                        else:
                            print(
                                "Use correct format for session - (e.g) 2021/2022 Session!")
                            continue
                    try:
                        with open(create_acedemic_performance_filename(), newline="") as file:
                            reader = csv.DictReader(file)
                            itemtoupdate = pupil_subject()
                            for row in reader:
                                if clss == row["class"] and term == row["term"] and session == row["session"]:
                                    if row["subject"] != itemtoupdate:
                                        updatedlist.append(row)
                    except FileNotFoundError:
                        print("File not found!")

                    with open(create_acedemic_performance_filename(), "w") as file:
                        fieldnames = ["no_pupils", "name", "class", "term", "session", "subject",
                                      "cat1", "cat2", "exam", "total", "class_average", "subject_position", "grade"]
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(updatedlist)
                        print("File has been updated")

                    Acedemic_performance_a.create_update_acedemic_performance_a()

                case "3":
                    print("=>> UPDATE PUPILS BEHAVIOURAL SKILL DATA <<=")
                    updatedlist = []

                    clss = pupil_class()
                    term = school_term()

                    while True:
                        session = input("=>> Session: ").title()
                        if any(char.isdigit() for char in session) and session:
                            break
                        else:
                            print(
                                "Use correct format for session - (e.g) 2021/2022 Session!")
                            continue

                    try:
                        with open("acedemic-performance-section-c.csv", newline="") as file:
                            reader = csv.DictReader(file)
                            itemtoupdate = get_name()
                            for row in reader:
                                if clss == row["pupils_class"] and term == row["term"] and session == row["session"]:
                                    if row["pupils_name"] != itemtoupdate:
                                        updatedlist.append(row)
                    except FileNotFoundError:
                        print("File not found!")

                    with open("acedemic-performance-section-c.csv", "w") as file:
                        fieldnames = ["pupils_name", "pupils_class", "term", "session", "neatness", "punctuality",
                                      "attendance", "politeness", "honesty", "relationship", "self_control", "attentiveness", "initiative"]
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(updatedlist)
                        print("File has been updated")

                    Acedemic_performance_c.create_updated_acedemic_performance_c()
                case "4":
                    print("=>> UPDATE PUPILS PSYCHOMOTOR DATA <<=")
                    updatedlist = []

                    clss = pupil_class()
                    term = school_term()

                    while True:
                        session = input("=>> Session: ").title()
                        if any(char.isdigit() for char in session) and session:
                            break
                        else:
                            print(
                                "Use correct format for session - (e.g) 2021/2022 Session!")
                            continue

                    try:
                        with open("acedemic-performance-section-b.csv", newline="") as file:
                            reader = csv.DictReader(file)
                            itemtoupdate = get_name()
                            for row in reader:
                                if clss == row["pupils_class"] and term == row["term"] and session == row["session"]:
                                    if row["pupils_name"] != itemtoupdate:
                                        updatedlist.append(row)
                    except FileNotFoundError:
                        print("File not found!")

                    with open("acedemic-performance-section-b.csv", "w") as file:
                        fieldnames = ["pupils_name", "pupils_class", "term", "session", "handwriting",
                                      "fluency", "game", "drawing", "musical_skill", "tool_handling"]
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(updatedlist)
                        print("File has been updated")

                    Acedemic_performance_b.create_updated_acedemic_performance_b()
                case "5":
                    print("=>> UPDATE PUPILS PERFORMANCE ANALYSIS DATA <<=")
                    updatedlist = []

                    clss = pupil_class()
                    term = school_term()

                    while True:
                        session = input("=>> Session: ").title()
                        if any(char.isdigit() for char in session) and session:
                            break
                        else:
                            print(
                                "Use correct format for session - (e.g) 2021/2022 Session!")
                            continue

                    try:
                        with open("performance-analysis.csv", newline="") as file:
                            reader = csv.DictReader(file)
                            itemtoupdate = get_name()
                            for row in reader:
                                if clss == row["pupils_class"] and term == row["term"] and session == row["session"]:
                                    if row["pupils_name"] != itemtoupdate:
                                        updatedlist.append(row)
                    except FileNotFoundError:
                        print("File not found!")

                    with open("performance-analysis.csv", "w") as file:
                        fieldnames = ["pupils_name", "pupils_class", "term", "session",
                                      "no_subject", "grand_total_score", "average_score"]
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(updatedlist)
                        print("File has been updated")

                    Performance_analysis.create_updated_performance_analysis()
                case "6":
                    print("=>> UPDATE SCHOOL COMMENT <<=")
                    updatedlist = []

                    clss = pupil_class()
                    term = school_term()

                    while True:
                        session = input("=>> Session: ").title()
                        if any(char.isdigit() for char in session) and session:
                            break
                        else:
                            print(
                                "Use correct format for session - (e.g) 2021/2022 Session!")
                            continue

                    try:
                        with open("school-comment.csv", newline="") as file:
                            reader = csv.DictReader(file)
                            itemtoupdate = get_name()
                            for row in reader:
                                if clss == row["pupils_class"] and term == row["term"] and session == row["session"]:
                                    if row["pupils_name"] != itemtoupdate:
                                        updatedlist.append(row)
                    except FileNotFoundError:
                        print("File not found!")

                    with open("school-comment.csv", "w") as file:
                        fieldnames = ["pupils_name", "pupils_class", "term",
                                      "session", "class_teacher_remark", "school_head_comment"]
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(updatedlist)
                        print("File has been updated")

                    School_comment.create_updated_school_comment()

                case _:
                    print("Record not found!")

        case "Delete":
            print("DELETE RECORD:\n" + "=>> 1. Personal Data.\n" + "=>> 2. Acedemic Performance.\n" + "=>> 3. Behavioural skills.\n" +
                  "=>> 4. Psychomotor.\n" + "=>> 5. Performance Analysis.\n" + "=>> 6. School Comment.\n")

            data3 = input("=>> ENTER NUMBER TO CHOOSE RECORD TO DELETE: ")

            match data3:
                case "1":
                    # delete personal data
                    print("=>> DELETE PUPILS PERSONAL DATA <<=")
                    updatedlist = []

                    clss = pupil_class()
                    term = school_term()

                    while True:
                        session = input("=>> Session: ").title()
                        if any(char.isdigit() for char in session) and session:
                            break
                        else:
                            print(
                                "Use correct format for session - (e.g) 2021/2022 Session!")
                            continue

                    try:
                        with open("personal-data.csv", newline="") as file:
                            reader = csv.DictReader(file)
                            itemtoupdate = get_name()
                            for row in reader:
                                if clss == row["pupils_class"] and term == row["term"] and session == row["session"]:
                                    if row["pupils_name"] != itemtoupdate:
                                        updatedlist.append(row)
                    except FileNotFoundError:
                        print("File not found!")

                    with open("personal-data.csv", "w") as file:
                        fieldnames = ["date", "reg_no", "pupils_name", "pupils_class", "term",
                                      "session", "date_of_birth", "gender", "address", "mobile_no"]
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(updatedlist)
                        print("File has been deleted!")

                case "2":
                    # delete acedemic performance
                    print("=>> DELETE ACEDEMIC PERFORMANCE DATA <<=")
                    updatedlist = []

                    clss = pupil_class()
                    term = school_term()

                    while True:
                        session = input("=>> Session: ").title()
                        if any(char.isdigit() for char in session) and session:
                            break
                        else:
                            print(
                                "Use correct format for session - (e.g) 2021/2022 Session!")
                            continue
                    try:
                        with open(create_acedemic_performance_filename(), newline="") as file:
                            reader = csv.DictReader(file)
                            itemtoupdate = pupil_subject()
                            for row in reader:
                                if clss == row["class"] and term == row["term"] and session == row["session"]:
                                    if row["subject"] != itemtoupdate:
                                        updatedlist.append(row)
                    except FileNotFoundError:
                        print("File not found!")

                    with open(create_acedemic_performance_filename(), "w") as file:
                        fieldnames = ["no_pupils", "name", "class", "term", "session", "subject",
                                      "cat1", "cat2", "exam", "total", "class_average", "subject_position", "grade"]
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(updatedlist)
                        print("File has been deleted!")

                case "3":
                    # delete behavioural skill
                    print("=>> DELETE PUPILS BEHAVIOURAL SKILL DATA <<=")
                    updatedlist = []

                    clss = pupil_class()
                    term = school_term()

                    while True:
                        session = input("=>> Session: ").title()
                        if any(char.isdigit() for char in session) and session:
                            break
                        else:
                            print(
                                "Use correct format for session - (e.g) 2021/2022 Session!")
                            continue

                    try:
                        with open("acedemic-performance-section-c.csv", newline="") as file:
                            reader = csv.DictReader(file)
                            itemtoupdate = get_name()
                            for row in reader:
                                if clss == row["pupils_class"] and term == row["term"] and session == row["session"]:
                                    if row["pupils_name"] != itemtoupdate:
                                        updatedlist.append(row)
                    except FileNotFoundError:
                        print("File not found!")

                    with open("acedemic-performance-section-c.csv", "w") as file:
                        fieldnames = ["pupils_name", "pupils_class", "term", "session", "neatness", "punctuality",
                                      "attendance", "politeness", "honesty", "relationship", "self_control", "attentiveness", "initiative"]
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(updatedlist)
                        print("File has been deleted!")
                case "4":
                    # delete psychomotor skills
                    print("=>> DELETE PUPILS BEHAVIOURAL SKILL DATA <<=")
                    updatedlist = []

                    clss = pupil_class()
                    term = school_term()

                    while True:
                        session = input("=>> Session: ").title()
                        if any(char.isdigit() for char in session) and session:
                            break
                        else:
                            print(
                                "Use correct format for session - (e.g) 2021/2022 Session!")
                            continue

                    try:
                        with open("acedemic-performance-section-c.csv", newline="") as file:
                            reader = csv.DictReader(file)
                            itemtoupdate = get_name()
                            for row in reader:
                                if clss == row["pupils_class"] and term == row["term"] and session == row["session"]:
                                    if row["pupils_name"] != itemtoupdate:
                                        updatedlist.append(row)
                    except FileNotFoundError:
                        print("File not found!")

                    with open("acedemic-performance-section-c.csv", "w") as file:
                        fieldnames = ["pupils_name", "pupils_class", "term", "session", "neatness", "punctuality",
                                      "attendance", "politeness", "honesty", "relationship", "self_control", "attentiveness", "initiative"]
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(updatedlist)
                        print("File has been deleted!")
                case "5":
                    # delete performance analysis
                    print("=>> DELETE PUPILS PERFORMANCE ANALYSIS DATA <<=")
                    updatedlist = []

                    clss = pupil_class()
                    term = school_term()

                    while True:
                        session = input("=>> Session: ").title()
                        if any(char.isdigit() for char in session) and session:
                            break
                        else:
                            print(
                                "Use correct format for session - (e.g) 2021/2022 Session!")
                            continue

                    try:
                        with open("performance-analysis.csv", newline="") as file:
                            reader = csv.DictReader(file)
                            itemtoupdate = get_name()
                            for row in reader:
                                if clss == row["pupils_class"] and term == row["term"] and session == row["session"]:
                                    if row["pupils_name"] != itemtoupdate:
                                        updatedlist.append(row)
                    except FileNotFoundError:
                        print("File not found!")

                    with open("performance-analysis.csv", "w") as file:
                        fieldnames = ["pupils_name", "pupils_class", "term", "session",
                                      "no_subject", "grand_total_score", "average_score"]
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(updatedlist)
                        print("File has been deleted!")

                case "6":
                    # delete school comment
                    print("=>> DELETE SCHOOL COMMENT <<=")
                    updatedlist = []

                    clss = pupil_class()
                    term = school_term()

                    while True:
                        session = input("=>> Session: ").title()
                        if any(char.isdigit() for char in session) and session:
                            break
                        else:
                            print(
                                "Use correct format for session - (e.g) 2021/2022 Session!")
                            continue

                    try:
                        with open("school-comment.csv", newline="") as file:
                            reader = csv.DictReader(file)
                            itemtoupdate = get_name()
                            for row in reader:
                                if clss == row["pupils_class"] and term == row["term"] and session == row["session"]:
                                    if row["pupils_name"] != itemtoupdate:
                                        updatedlist.append(row)
                    except FileNotFoundError:
                        print("File not found!")

                    with open("school-comment.csv", "w") as file:
                        fieldnames = ["pupils_name", "pupils_class", "term",
                                      "session", "class_teacher_remark", "school_head_comment"]
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(updatedlist)
                        print("File has been deleted")

                case _:
                    print("Record not found!")
        case _:
            print("Record not found!")
