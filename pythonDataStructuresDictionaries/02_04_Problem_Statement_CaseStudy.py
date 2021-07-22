#getting a dictionary from a text file
#Getting a dictionary from a CSV file
import  csv
with open('pythonDataStructuresDictionaries/TreeOrdersSubset.csv', mode='r') as infile:
    reader = csv.reader(infile)
   #1st Video - creating a dictionary - walk them through this. And introduce the idea of a Case Study
    treeOrders ={}
    for row in reader:
        key = row[0]
        if key not in treeOrders:
            treeNum = row[1]
            treeOrders[key] = treeNum
        else:
            treeNum = row[1]
            prev_count = treeOrders[key]
            treeOrders[key] = int(prev_count) + int(treeNum)
            
    print(treeOrders.items())  
    
    infile.close()
    	

