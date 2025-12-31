student_records = []
stats = {}
unique_scores = set()
grade_distribution = {}


student_records = [
    ("Haidar", 90),
    ("Elias", 80),
    ("Bro", 76),
    ("Digga", 70),
    ("Ahmed", 70),
    ("Bruder", 61)
]

scores = [score for _, score in student_records]

stats= {"Highest": max(scores) ,
        'Lowest': min(scores),
        "Average": sum(scores)/len(scores),
        }


unique_scores = set(scores)


grade_distribution = {}

for score in scores:
    grade_distribution[score] = grade_distribution.get(score, 0) + 1




print("\n=== STUDENT RECORDS ===")
print(student_records)
print("\n=== STUDENT STATISTICS ===")
print(stats)
print("\n ===UNIQUE SCORES===")
print(unique_scores)
print("\n ===GRADE DISTRIBUTION===")
print(grade_distribution)