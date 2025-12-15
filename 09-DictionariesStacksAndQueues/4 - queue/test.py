def f(subjects):
    max_avg = -1
    best_subject = None
    for subject, grades in subjects.items():
        avg = sum(grades) / len(grades)
        if avg > max_avg:
            best_subject = subject
    return best_subject
        



print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))