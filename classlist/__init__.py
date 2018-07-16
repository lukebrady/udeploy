import csv

def parse_classlist(csv_list):
    class_arr = []
    # Read the CSV from disk after being uploaded.
    with open(csv_list, newline = '') as classlist:
        classl = csv.reader(classlist, delimiter = ',')
        for c in classl:
            class_arr = c
    return class_arr


if __name__ == '__main__':
    parse_classlist('./test.csv')
    parse_classlist