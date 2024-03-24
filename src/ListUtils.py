def saveListToFile(l, filename):
    with open(filename, 'w') as file:
        for element in l:
            file.write(str(element) + '\n')

def readListFromFile(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]