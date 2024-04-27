import pandas as pd
from planetterp import professor
import csv


df = pd.read_csv("all_professors_temp.csv", usecols=["Professor"])
row = 1
prof_count = 1
field_names = ['id', 'Professor', 'Course', 'Average Rating', 'Review']
    
with open("all_professors_clean.csv", "a", newline='') as csv_file:
    for professor_line in df.index:
        
        temp_professor = professor(df['Professor'][professor_line], True)
        
        for review in temp_professor['reviews']:
            writer = csv.DictWriter(csv_file, fieldnames=field_names)
            
            if row == 1:
                writer.writeheader()
                
            writer.writerow({'id': str(row), 'Professor': str(temp_professor['name']), 'Course': str(review['course']),
                            'Average Rating': str(temp_professor['average_rating']), 'Review': str(review['review'])})
            print("Row added")
            row += 1
        print("Professor #" + str(prof_count) + " added")
        prof_count += 1
        
        
    # all_professors.append(temp_professor)
        
    # if count == 1:
    #     del all_professors[0]
        
    # print("Professors added: " + str(count))
    # count += 1
    # if count == 3:
    #     break
    # sleep(0.15)