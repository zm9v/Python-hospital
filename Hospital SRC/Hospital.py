USERNAME = input("Username :  ").lower().strip()

PASSWORD = input("Password :  ").strip()


def cc():

    import os

    command = "clear"

    if os.name in ("nt", "dos"):

        command = "cls"

    os.system(command)


if USERNAME == "nurse1" and PASSWORD == "nurse1pass":
    
    cc()

    print(f'Welcome back {USERNAME}')
    
    print(
        """
1 To view patients
2 to add a new patient
3 To clear
4 to close
"""
    )

    while True:

        import random

        INFO = []

        ZERO = 0

        INDEX = 1

        LIST = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789-_=+#~\\|!"£$%^&*()#,./l;\'p[]>?<L:@P{}@"'

        INPUT = input("> ").strip()

        if INPUT == "1":

            PATIENTS = open("patients.txt", "r")

            if len(PATIENTS.read()) == 0:

                PATIENTS.close()

                print("There's no patients yet !!!!")

            else:

                with open("patients.txt", "r") as P:

                    print(P.read()[::6])

        elif INPUT == "2":

            Patient_name = input("Patient name : ").lower().title().strip()

            Patient_age = input("Patient age : ").strip()

            Patient_weight_in_KG = f'{input("Patient weight in KG : ").strip()} KG'

            Patient_height = f'{input("Patient height in CM : ").strip()} CM'

            Patient_blood_type = input("Blood type : ").strip().upper()

            Patient_info = f"""
Patient name : {Patient_name}
Patient age : {Patient_age}
Patient weight in KG : {Patient_weight_in_KG}
Patient height : {Patient_height}
Patient blood type : {Patient_blood_type}\n"""

            for i in range(len(Patient_info)):

                INFO.append(Patient_info[ZERO])

                ZERO += 1

            for i in range(len(INFO)):

                INFO[INDEX:INDEX] = random.choices(LIST, k=5)

                INDEX += 6

            with open("Patients.txt", "a") as P:

                P.write("".join(INFO))

        elif INPUT == "3":

            cc()

            print(
                """
1 To view patients
2 to add a new patient
3 To clear
4 to close
            """
            )

        elif INPUT == "4":

            input("Press enter to close...")

            break

        else:

            print("Invalid input :(")

            continue

else:

    print("Invalid username or password :(")

    input("Press enter to close...")
