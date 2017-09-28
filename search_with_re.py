import re

with open('source.txt') as fin:
    with open('result.log', 'a') as fout:
        for line in fin:
           match = re.search(r'regex*', line)
           if match:
               fout.write(line)