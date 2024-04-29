import csv
from planet_terp_api import add_all_professors
from datetime import datetime

all_professors = add_all_professors()

# add time to csv later
# now = datetime.now()
# date_time = now.strftime("%m/%d/%Y %H:%M:%S")
count = 1

# Loops through all of the professors and adds the professor and respective data to csv file
with open("review_csv_files/all_professors.csv", "a", newline='') as csv_file:
    field_names = ['id', 'Professor', 'Courses', 'Average Rating', 'Review', 'Rating']
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    for professor in all_professors:
        for review in professor['reviews']:
            
            # if count == 1:
            #     writer.writeheader()
                
            writer.writerow({'id': str(count), 'Professor': str(professor['name']), 'Courses': str(review['course']),
                            'Average Rating': str(professor['average_rating']), 'Review': str(review['review']),
                            'Rating': str(review['rating'])})
            print("Row added #" + str(count))
            count += 1