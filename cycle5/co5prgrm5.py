import csv
cars=[{'NO' :1,'Company':'Ferrari','Model':'488GTB'},{'NO' :2,'Company':'Benz','Model':'345SDF'}]
csvfile=open('Names.csv','w')
field_names=list(cars[0].keys())
writer=csv.DictWriter(csvfile,fieldnames=field_names)
writer.writeheader()
writer.writerows(cars)
csvfile.close()
csv_file=open('Names.csv','r')
csv_reader=csv.reader(csv_file)
for line in  csv_file:
    print(line,end="")
