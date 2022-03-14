from configparser import DuplicateOptionError
from csv import reader

from numpy import save, sort
i = 0
csv_filename = "dataset/titles.csv"
dictionary = set()
with open(csv_filename.format(csv_filename), 'r') as csv_file:
    for line in reader(csv_file):
        for word in (line[0].split(' ')):
            dictionary.add(word)
a = sort(list(dictionary))
print(a)
f = open("sorted_titles.csv", "a")
for word in a:
    f.write("{}\n".format(word))
f.close()