# Function Program 35

scores = [88, 92, 78, 95, 86]
grade = lambda s: 'A' if s >= 90 else ('B' if s >= 80 else ('C' if s >= 70 else ('D' if s >= 60 else 'F')))
print(list(map(grade, scores)))
