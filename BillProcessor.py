import csv
import json
import os
from threading import Thread
import time
import shutil
#from collections import OrderedDict
path="C:\\Users\\Admin\\Desktop\\Python_Trainning\\Billing\\Bills"
product_list_data=list()

#read the csv as dictnory 
with open("C:\\Users\\Admin\\Desktop\\Python_Trainning\\Billing\\MasterData\\products.csv") as file:
        product_data=csv.DictReader(file)

        #append each dictory data to list
        for row in product_data:
            product_list_data.append(
                {
                    "product_id":row['product_id'],
                    "product_category":row['product_category'],
                    "product_name":row['product_name'],
                    "unit_price":row['unit_price']
                }
            )
        #data=json.dumps(product_list_data,indent=2) 
        #print(data)

#process bill method for processing 
# bill total and move to processed folder
def process_bill():
    
    list_file=os.listdir(path) #store list of bills file in list_file variable
    for bill_file in list_file:
         
        #read the json file and fetch data in bill_data variable
        with open("C:\\Users\\Admin\\Desktop\\Python_Trainning\\Billing\\Bills\\"+bill_file) as bill_read:
            bill_data=json.load(bill_read)
            
        #store the bill_data in local variable result dictionery
        result=bill_data
            
        #empty list to store dictonery reader data
            
        total=0 #local variable to store total of bill
        for key,val in result['BillDetails'].items():
            for keys1 in product_list_data:
                if key==keys1['product_id']:
                    total+=float(keys1['unit_price'])*val

        #add total bill key to result dictionery
        result["BillTotal"]=total
        #store the current bill_file to local variable
        updated_new="./Bills/"+bill_file
        #store the processed folder file name in local variable
        process_file="./Processed/"+"process_"+bill_file
            
        #open the current bill_file to add result updated data in write mode
        f1=open(updated_new,'w')
        #write the json string to file with indent 2
        f1.write(json.dumps(result,indent=2))
        #close the file after wrtinting result data
        f1.close()
       
        #sleep for 2 second
        time.sleep(2)
       
        #move the updated file from Bills folder to Processed folder
        #with help of shutil module's move function
        shutil.move(updated_new,process_file)

        #time.sleep(2)
       

try:
    #loop the until the Bills folder has file to process.
    while len(os.listdir(path)):
        #Thred to call process_bill function
        t1=Thread(target=process_bill)
        #start the thread
        t1.start()

        #use thread join function to work on thread and not move to other process
        t1.join()
       
    else:
        print("No file exist in bills folder")
except Exception as e:
    print(e)

