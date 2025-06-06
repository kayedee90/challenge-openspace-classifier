import csv
from utils.openspace import Openspace 


def load_names_file (filename):
    """ Read CSV file and send names to a list 
    """
    names = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0]
            names.append(name)
            
    return names

if __name__ == "__main__":
    names = load_names_file("utils/colleagues.csv")
    openspace = Openspace()
    openspace.organize(names)
    openspace.display()



