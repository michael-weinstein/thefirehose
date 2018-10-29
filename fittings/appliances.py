import os
import random

class Name(object):

    def __init__(self, gender: str, first: str, middle: str, last: str):
        self.gender = gender
        self.first = first
        self.middle = middle
        self.last = last


class Strawman(object):

    def __init__(self, gender:str = "", domain:str = ""):
        if not gender:
            gender = randomGender()
        gender = gender.lower()
        assert gender in ("male",
                          "female"), "Gender must be entered as male or female here.  No offense to the non-binary folk out there."
        firstname = getRandomFirstName(gender)
        middlename = getRandomFirstName(gender)
        lastname = getRandomLastName()
        self.name = Name(gender, firstname, middlename, lastname)
        self.email = generateEmail(self.name, domain)
        self.password = getRandomPassword()


def populateNameLists():
    nameLists = {}
    nameLists["first"] = {"male":[], "female":[]}
    nameLists["last"] = []
    maleFirstNameFile = open(os.path.join(dataFolder, "topMaleNames.txt"), 'r')
    for line in maleFirstNameFile:
        nameLists["first"]["male"].append(line.strip())
    maleFirstNameFile.close()
    femaleFirstNameFile = open(os.path.join(dataFolder, "topFemaleNames.txt"), 'r')
    for line in femaleFirstNameFile:
        nameLists["first"]["female"].append(line.strip())
    femaleFirstNameFile.close()
    lastNameFile = open(os.path.join(dataFolder, "topSurnames.txt"), 'r')
    for line in lastNameFile:
        nameLists["last"].append(line.strip())
    lastNameFile.close()
    return nameLists

def populatePasswordList():
    passwordList = []
    passwordFile = open(os.path.join(dataFolder, "passwords.txt"), 'r')
    for line in passwordFile:
        passwordList.append(line.strip())
    passwordFile.close()
    return passwordList

def populateDomainList():
    domainList = []
    domainFile = open(os.path.join(dataFolder, "topDomains.txt"), 'r')
    for line in domainFile:
        domainList.append(line.strip())
    domainFile.close()
    return domainList

def randomGender():
    randomValue = random.randint(0, 1)
    if randomValue == 0:
        return "male"
    else:
        return "female"

def getRandomFirstName(gender:str):
    return random.choice(nameLists["first"][gender])

def getRandomLastName():
    return random.choice(nameLists["last"])

def generateEmail(name:Name, domain:str = None):
    useDots = random.randint(0, 1)
    useFullFirst = random.randint(0, 9)
    useMiddle = random.randint(0, 5)
    if useMiddle:
        useFullMiddle = random.randint(0, 1)
    else:
        useFullMiddle = False
    useFullLast = random.randint(0, 19)
    if useDots:
        dots = "."
    else:
        dots = ""
    if useFullFirst:
        first = name.first
    else:
        first = name.first[0]
    if useMiddle:
        if useFullMiddle:
            middle = name.middle
        else:
            middle = name.middle[0]
    else:
        middle = ""
    if useFullLast:
        last = name.last
    else:
        last = name.last[0]
    if not useDots and not useMiddle:
        if not random.randint(0, 2):
            middle = random.randint(1, 9999)
            middle = str(middle)
            if not random.randint(0, 4):
                middle = middle.zfill(random.randint(1, 5))
    useEndNumber = random.randint(0, 5)
    if middle.isdigit():
        useEndNumber = False
    shortAddress = not ((useFullFirst and useFullLast) or (useFullMiddle and useFullLast))
    if shortAddress:
        useEndNumber = True
    if useEndNumber:
        endNumber = random.randint(1, 9999)
        endNumber = str(endNumber)
        if not random.randint(0, 3):
            endNumber = endNumber.zfill(random.randint(1, 5))
    else:
        endNumber = ""
    user = "%s%s%s%s%s%s" %(first, dots, middle, dots, last, endNumber)
    user = user.replace("..", ".")  #in case there is an empty middle name with dots
    if not domain:
        domain = random.choice(domainList)
    else:
        domain = domain.replace("@", "")
    emailAddress = "%s@%s" %(user, domain)
    return emailAddress.lower()

def getRandomPassword():
    return random.choice(passwordList)

dataFolder = os.path.join(os.path.split(__file__)[0], "watersupply")
nameLists = populateNameLists()
passwordList = populatePasswordList()
domainList = populateDomainList()