
def readcsv(filename, variable)
    import csv
    for row in csv.reader(open(file_name)):
        variable_name = row[0]
        value = row[1]
        if variable == variable_name:
            return value
