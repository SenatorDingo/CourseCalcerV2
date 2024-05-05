coursesToDo

def permuterAndCombinator(courses, required, coursesPerTerm, terms):
    createEmptyCalenderArray(terms)


def createEmptyCalenderArray(terms):
    sequence = []
    i = 0
    while i < terms + 1:
        sequence.append([])
        i += 1

def compareCourse(requiredCourse, courses):
    for course in courses:
        if requiredCourse[0] + requiredCourse[1] ==
