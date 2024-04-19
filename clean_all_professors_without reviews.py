import pandas as pd
import csv


#count = 1

cols = ["Professor", "Courses", "Average Rating"]

df = pd.read_csv("all_professors_raw.csv", usecols=cols)



df = df.drop(df[df["Courses"] == "[]"].index)
df = df.drop(df[df["Average Rating"].isna()].index)

df.to_csv("all_professors_temp.csv", index=False)
print("done")


# with pd.read_csv("all_professors_raw.csv", chunksize=1589) as reader:
#     with open("all_professors_clean.csv", "a", newline='') as csv_file:
#         for chunk_num, chunk in enumerate(reader, start=1):
#             chunk = chunk.drop(chunk[chunk['Courses'] == '[]'].index)
#             chunk = chunk.drop(chunk[chunk['Average Rating'] == None].index)

#             field_names = ['id', 'Professor', 'Courses', 'Average Rating', 'Reviews']
#             writer = csv.DictWriter(csv_file, fieldnames=field_names)
            
#             if count == 1:
#                 writer.writeheader()
                    
#             writer.writerow({'id': str(count), 'Professor': str(chunk['Professor']), 'Courses': str(chunk['Courses']),
#                             'Average Rating': str(chunk['Average Rating']), 'Reviews': str(chunk['Reviews'])})
#             print("Row added")
#             count += 1


    
    
    
    # for chunk in pd.read_csv("all_professors_raw.csv", chunksize=1589):
    #     chunk = chunk.drop(chunk[chunk['Courses'] == '[]'].index)
    #     chunk = chunk.drop(chunk[chunk['Average Rating'] == None].index)
        
    #     field_names = ['id', 'Professor', 'Courses', 'Average Rating', 'Reviews']
    #     writer = csv.DictWriter(csv_file, fieldnames=field_names)
        
    #     if count == 1:
    #         writer.writeheader()
                
    #     writer.writerow({'id': str(count), 'Professor': str(chunk['Professor']), 'Courses': str(chunk['Courses']),
    #                     'Average Rating': str(chunk['Average Rating']), 'Reviews': str(chunk['Reviews'])})
    #     print("Row added")
    #     count += 1