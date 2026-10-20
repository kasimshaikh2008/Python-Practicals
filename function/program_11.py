# Function Program 11

def findString(str1, str2='all'):
    positions = []
    for i in range(len(str1)):
        if str1[i:i + len(str2)] == str2:
            positions.append(i)
    if len(positions) == 0:
        print("String 2 not found")
    else:
        return positions
str1 = "Hello all, Good Morning to all."
print("String 2 found at positions:", findString(str1, 'all'))
print("String 2 found at positions:", findString(str1))
