import csv
with open('studentdetails.csv','r')as csv_file1:
    csv_reader=csv.reader(csv_file1)
    with open('newstudentdetails1.csv','w')as csv_file2:
        csv_writer=csv.writer(csv_file2)
        for line in csv_reader:
            csv_writer.writerow(line)