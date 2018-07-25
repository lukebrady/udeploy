import csv

# parse_classlist:
# This function reads a .csv file uploaded to the application
# and then returns the list of names that can be used to name the VMs.
# @param csv_list: The CSV file that has been uploaded to the server
# that will be parsed and returned.
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