import multiprocessing.pool
import pandas as pd
from planetterp import professor
import csv
from time import sleep
import multiprocessing


def all_reviews(professors):
    reviews_string = ""

    # Replaces reviews dict to only include the reviews
    for professor in professors:
        for review in professor['reviews']:
            reviews_string += "{" + review['review'] + "}\n\n"
        professor['reviews'] = reviews_string
    
    return professors

def add_professors(df):
    all_professors = [{'Professor' : "", 'Courses': "", "Average Rating" : None, "Reviews" : ""}]
    count = 1
    
    for professor_line in df.index:
        temp_professor = professor(df['Professor'][professor_line], True)
        
        del temp_professor['slug']
        del temp_professor['type']
        
        all_professors.append(temp_professor)
        
        if count == 1:
            del all_professors[0]
        
        print("Professors added: " + str(count))
        count += 1
        if count == 3:
            break
        sleep(0.15)
        
    with multiprocessing.Pool(1) as pool:
        result = pool.map(all_reviews, all_professors)
        all_professors = result
        
    return all_professors
        
df = pd.read_csv("all_professors_temp.csv", usecols=["Professor"])
 
all_professors = add_professors(df)

count = 1
# Loops through all of the professors and adds the professor and respective data to csv file
with open("all_professors_clean.csv", "a", newline='') as csv_file:
    for prof in all_professors:
        field_names = ['id', 'Professor', 'Courses', 'Average Rating', 'Reviews']
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        
        if count == 1:
            writer.writeheader()
            
        writer.writerow({'id': str(count), 'Professor': str(prof['name']), 'Courses': str(prof['courses']),
                         'Average Rating': str(prof['average_rating']), 'Reviews': str(prof['reviews'])})
        print("Row added")
        count += 1