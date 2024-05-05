coursesToDo = ["SEG2900", "ENG1112", "ITI1120", "PHY1321", "MAT1320", "MAT1348", "ITI1121", "ITI1100", "MAT1322", "PHY1322",
        "MAT1341", "CHM1311", "CSI2110", "SEG2105", "GNG1105", "GNG2101", "MAT2377", "SEG3102", "CEG2136", "SEG2901",
               'CSI3131', 'SEG3103', 'SEG3125', 'CSI2101', 'CSI2132', 'SEG2106', 'SEG2911', 'CSI3105', 'SEG3101',
               'FRE1000', 'FRE1001', 'FRE1002', 'FRE1003', 'PVS1000', 'CLE1000', 'CLE1001', 'SEE1000', 'SEG4145', 'SEG4910', 'SEG4911',
               'SEG4105', 'SEG3901', 'SEG3902', 'SEG4901', 'SEG4902']
#PVS1000 is Astronomy/EVS
#FRE are free electives and FRE1003 is complementary studies
#CLE is Computing elective
#SEE is Software Elective



# RULES
# COOP Takes up entire slot (maybe 1)
# Code SEG4911 specially
# Code last 2 coops as optional
# Code CLE1000 & CLE1001 as special case
#
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
