import csv

from ngram import NGram

records = NGram()

with open('./data/houses.csv', 'r', encoding='windows-1251') as f:
    for line in csv.reader(f, delimiter=';'):
        records.add(' '.join(list(line)).lower())

while True:
    print('Enter search text:')
    search_text = input().lower()
    print('find', records.find(search_text), 0.8)

