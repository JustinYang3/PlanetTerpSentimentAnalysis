import csv
from planet_terp_api import add_all_professors

all_professors = add_all_professors()

count = 0
# Loops through all of the professors and adds the professor and respective data to csv file
with open("all_professors.csv", "a", newline='') as csv_file:
    for professor in all_professors:
        field_names = ['id', 'Professor', 'Courses', 'Average Rating', 'Reviews']
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        
        if count == 1:
            writer.writeheader()
            
        writer.writerow({'id': str(count), 'Professor': str(professor['name']), 'Courses': str(professor['courses']),
                         'Average Rating': str(professor['average_rating']), 'Reviews': str(professor['reviews'])})
        print("Row added")
        count += 1