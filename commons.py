#############
# CVE Class #
#########################################################################
# CVE_ID = Id of the CVE                                                #
# vType = Type of vunerability                                          #
# pDate = Publication date                                              #
# uDate = Update date                                                   #
# score = Score of severity                                             #
# gainedAccessLevel = If the vuln. allows to gain access to the machine #
# access = The way to execute the vuln.                                 #
# complexity = The complexity to execute the vuln.                      #
# authentication = If it require authentication to perform              #
# confidentiality = The state of confidentiality breach                 #
# integrity = The state of integrity breach                             #
# availability = The state of availability breach                       #
#########################################################################
class CVE:
    def __init__(self, CVE_ID, vType, pDate, uDate, score, gainedAccessLevel, access, complexity, authentication, confidentiality, integrity, availability):
        self.CVE_ID = CVE_ID
        self.vType = vType
        self.pDate = pDate
        self.uDate = uDate
        self.score = score
        self.gainedAccessLevel = gainedAccessLevel
        self.access = access
        self.complexity = complexity
        self.authentication = authentication
        self.confidentiality = confidentiality
        self.integrity = integrity
        self.availability = availability