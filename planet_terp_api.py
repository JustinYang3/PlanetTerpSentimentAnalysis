from planetterp import professors

def add_all_professors():
    offset = 0
    all_professors = list()
    # Adds all professors in PlanetTerp API to all_professors
    while True:
        temp_professors = professors("professor", True, 100, offset*100)
            
        if len(temp_professors) != 100:
            all_professors.extend(temp_professors)
            print("Number of Professors added: " + str(offset * 100 + len(temp_professors)))
            break
        
        all_professors.extend(temp_professors)
        print("Number of Professors added: " + str((offset + 1) * 100))
        offset += 1
        
    all_professors = all_reviews(all_professors)
    
    return all_professors

def all_reviews(professors):
    reviews_string = ""

    # Replaces reviews dict to only include the reviews
    for professor in professors:
        for review in professor['reviews']:
            reviews_string += "{" + review['review'] + "}\n\n"
        professor['reviews'] = reviews_string
    
    return professors

all_departments = {'ENRE', 'AREC', 'NAVY', 'CBMG', 'TLTC', 'EXST', 'BSGC', 'ARSC', 'MSBB', 'ARTT', 'TDPS',
                   'EDPS', 'CPSN', 'KORA', 'FOLA', 'AMST', 'LARC', 'ARTH', 'ENST', 'DATA', 'ISRL', 'GEOL',
                   'SPAN', 'HEBR', 'HLTH', 'AASP', 'GVPT', 'CLAS', 'NFSC', 'MATH', 'BSST', 'MUSC', 'PEER',
                   'ARMY', 'JWST', 'MUED', 'HESP', 'INFM', 'CONS', 'UMEI', 'AAST', 'MUET', 'MITH', 'CPET',
                   'ARAB', 'MLSC', 'BIOI', 'DANC', 'GERS', 'EDCI', 'BMGT', 'ENSP', 'BSCI', 'ENES', 'EDSP',
                   'PHSC', 'GREK', 'WMST', 'CPSS', 'BUDT', 'RDEV', 'IMDM', 'BIOL', 'CHSE', 'GEOG', 'IDEA',
                   'EDMS', 'WEID', 'BULM', 'NACS', 'PLSC', 'ENPM', 'HNUH', 'CPSF', 'URSP', 'ENEE', 'LING',
                   'FGSM', 'BMSO', 'RUSS', 'INAG', 'SLAA', 'ENMA', 'BSCV', 'CPSA', 'AMSC', 'PERS', 'CLFS',
                   'WGSS', 'CMSC', 'EDUC', 'CPJT', 'EPIB', 'MAIT', 'ENCE', 'BUSM', 'PHIL', 'MSML', 'ENCH',
                   'JOUR', 'BUFN', 'HLSA', 'LBSC', 'MLAW', 'USLT', 'HISP', 'ENFP', 'PSYC', 'HLSC', 'ENBC',
                   'PHYS', 'FREN', 'ECON', 'CHPH', 'HBUS', 'SPHL', 'TLPL', 'BCHM', 'MIEH', 'IMMR', 'ARCH',
                   'HESI', 'VMSC', 'STAT', 'LATN', 'EMBA', 'BDBA', 'CPBE', 'HEIP', 'CPGH', 'INST', 'ENTM',
                   'ANTH', 'LACS', 'ANSC', 'CMLT', 'CHIN', 'PLCY', 'RELS', 'BUMK', 'LASC', 'HGLO', 'ENTS',
                   'CPMS', 'NEUR', 'BEES', 'SURV', 'HLMN', 'COMM', 'CPSP', 'BIOE', 'LEAD', 'AOSC', 'BIOM',
                   'CHEM', 'PUAF', 'HIST', 'GEMS', 'BUAC', 'HACS', 'FMSC', 'BUMO', 'SOCY', 'CCJS', 'ENCO',
                   'ENSE', 'THET', 'ENAE', 'BSOS', 'ENPP', 'BUSI', 'EDHD', 'LGBT', 'CINE', 'BUSO', 'ENNU',
                   'EDCP', 'FIRE', 'CHBE', 'KNES', 'MEES', 'HDCC', 'ENME', 'CPSD', 'AGNR', 'ARHU', 'SLLC',
                   'FILM', 'MSQC', 'UNIV', 'ITAL', 'ASTR', 'HONR', 'BISI', 'CPPL', 'ENEB', 'JAPN', 'HHUM',
                   'PORT', 'ENGL', 'EDHI', 'GERM'}        
    #count = 0.0
    #departments = set()

    # Loops through all of the professors and writes the bad professors into txt file and prints them out
    #for professor in all_professors:
        # for review in professor["reviews"]:
        #     if review != None and review["review"] != None:
        #         flag |= str(review["review"]).find("disorganize") != -1 or str(review["review"]).find("unorganize") != -1
        
        # Bad professor if the average rating is less than 3 while having more than 5 reviews
        # rating_criteria = professor["average_rating"] != None and professor["average_rating"] <= 3 and len(professor["reviews"]) > 5
        # if rating_criteria:
        #     count += 1.0
        #     with open("bad_professors.txt", "a") as file:
        #         file.write(str(professor["courses"])[2:6] + ": " + str(professor["name"]) + "\n")
        #     print(str(professor["courses"])[2:6] + ": " + str(professor["name"]))
        
        # Adds all of the departments to set
    #    departments.add(str(professor["courses"])[2:6])
            
    # Prints percentage of bad professors and all departments
    # print(count / float(len(all_professors)) * 100)
    # print(departments)

