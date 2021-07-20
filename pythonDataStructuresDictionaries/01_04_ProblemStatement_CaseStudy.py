#getting a dictionary from a text file
#Getting a dictionary from a CSV file
import  csv
with open('pythonDataStructuresDictionaries/treeorderssubsetnodupes.csv', mode='r') as infile:
    reader = csv.reader(infile)
   #creating a dictionary - walk through code.
   # And introduce the idea of a Case Study
    mydict ={}
    

    for row in reader:
        key = row[0]
        mydict[key]=row[1]
        
    size = len(mydict)
    print(f'the size of Data {size}')
    
    mydict['205'] = 10
    print(mydict['205'])
    
    mydict['999'] = 12
    print(mydict['999'])
    
    for i in mydict:
        print(f'{i} : {mydict[i]}')
    
    infile.close()
    	

    	
