done = ["NUL0000", "SEG2900", "ENG1112", "ITI1120", "PHY1321", "MAT1320", "MAT1348", "ITI1121", "ITI1100", "MAT1322", "PHY1322",
        "MAT1341", "CHM1311", "CSI2110", "SEG2105", "GNG1105", "GNG2101", "MAT2377", "SEG3102", "CEG2136", "SEG2901"]


def analyseExpression(expression):
    if 'or' in expression:
        options = expression.split('or')
        for option in options:
            if option in done:
                return True
        return False
    elif '|' in expression:
        expression = expression.replace('$', '')
        command = expression.split('|')
        numCourse = int(int(command[0])/3)
        allowedMajors = [command[1][i:i + 3] for i in range(0, len(command[1]), 3)]
        allowedYears = command[2].split(':')
        qualifying = 0
        for finished in done:
            if finished[0] + finished[1] + finished[2] in allowedMajors and finished[3] in allowedYears:
                qualifying += 1
        if qualifying >= numCourse:
            return True
        return False



def met(course):
    courseName = course[0] + course[1]
    removed = False
    if courseName in done:
        removed = True
        done.remove(courseName)
    prereqs = course[3]
    prereqs = prereqs.split(', ')
    for prereq in prereqs:
        prereq = prereq.replace(' ', '')
        if not metSinglePreReq(prereq):
            if removed:
                done.append(courseName)
                removed = False
            return False
    if removed:
        done.append(courseName)
        removed = False
    return True


def metSinglePreReq(prereq):
    if '$' not in prereq:
        if prereq in done:
            return True
        else:
            return False
    else:
        return analyseExpression(prereq)
