"""
map between open image mids and cogniac subjects and visa versa 
"""

import csv

mid_to_subject = dict()   # map from open image mid to cogniac subject_uid
subject_to_mid = dict()   # map from cogniac subject_uid to open image mid

with open('cogniac_subjects.csv', 'rb') as f:
    reader = csv.reader(f)
    for mid, name, subject_uid in reader:
        mid_to_subject[mid] = subject_uid
        subject_to_mid[subject_uid] = mid
