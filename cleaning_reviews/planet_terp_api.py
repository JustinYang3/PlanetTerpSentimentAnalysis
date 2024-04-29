from planetterp import professors
from time import sleep

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
        sleep(0.5)
        
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
