cse=100
ece=80
mech=70
if cse>0 and ece>0 and mech>0:
    if (cse==ece==mech):
        print("None of the department got highest placements")
    elif cse>ece and cse>mech:
        print("CSE")
    elif ece>cse and ece>mech:
        print("ECE")
    elif mech>cse and mech>ece:
        print("MECH")
else:
    print("Input is invalid")