#student report card problem

def report_card(name, score1, score2, score3):
    for s in (score1, score2, score3):
        if s < 0 or s > 100:
            raise ValueError("Scores must be between 0 and 100")

    total = score1 + score2 + score3
    avg = round(total / 3, 2)

    if avg >= 60:
        res = "1st Class"
    elif avg >= 50:
        res = "2nd Class"
    elif avg >= 35:
        res = "Pass Class"
    else:
        res = "Fail"

    return {
        "name": name,
        "total": total,
        "average": avg,
        "class": res
    } #returns a dict of values

#test cases
r = report_card("Asha", 70, 65, 60)
assert r["class"] == "1st Class"
try:
    report_card("Invalid", -10, 50, 60)
    assert False
except ValueError:
    assert True

try:
    report_card("Invalid", 110, 90, 80)
    assert False
except ValueError:
    assert True

print("All test cases passed!")

if __name__=="__main__":
    name=input("Enter your name:")
    score1=float(input("Enter your score in subj1: "))
    score2=float(input("Enter your score in subj2: "))
    score3=float(input("Enter your score in subj3: "))

    val=report_card(name,score1,score2,score3)
    print(val["name"])
    print(val["total"])
    print(val["average"])
    print(val["class"])

