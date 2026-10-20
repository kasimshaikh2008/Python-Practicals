# Function Program 4

def unique(lst):
    u = []
    for x in lst:
        if x not in u:
            u.append(x)
    return u
sample = [1, 2, 3, 3, 3, 3, 4, 5]
print("Sample List :", sample)
print("Unique List :", unique(sample))
