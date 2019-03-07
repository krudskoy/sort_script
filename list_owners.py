import sys
import json
import csv

if len(sys.argv) != 3:
    print("!!!Wrong number of arguments.Use it like 'script filename.csv car_model'")
    sys.exit()

filename = str(sys.argv[1])
car = str(sys.argv[2])

count = 0
data = {}
dict = {}
dict["owners"] = []
dict["years"] = []
with open(filename) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    print("\nOwners:")
    for row in csv_reader:
        if row["car"] == car:
            if str(row["year"]) in data:
               data[str(row["year"])] += 1
            else:
               data[str(row["year"])] = 1
            count += 1
            dict["owners"].append({"firstname":str(row["first_name"]),"lastname":str(row["last_name"])})
            print(str(row["first_name"]) + " " + str(row["last_name"]))
    if data:
        print("\nYears:")
        for key, value in sorted(data.iteritems(), key=lambda (k,v): (v,k)):
            print("{}:{}".format(key,value))
            dict["years"].append({"year":str(key),"number":str(value)})
    with open('data.json', 'w') as outfile:
        json.dump(dict, outfile)
