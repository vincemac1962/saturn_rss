from csv import reader
import requests

def getrss(url, filename):
    url = url
    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)
 
# skip first line i.e. read header first and then iterate over each row od csv as a list
with open('feeds.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    # Check file as empty
    if header != None:
        # Iterate over each row
        # after the header in the csv
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            getrss(row[2], row[3])