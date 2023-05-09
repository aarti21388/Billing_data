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

def process_bill():
    list_file=os.listdir(path)
    for bill_file in list_file:
        with open(path+"\\"+bill_file) as bill_read:
            bill_data=json.load(bill_read)
        print(bill_data)

        result=bill_data

       
       '''sorted_dic=OrderedDict(sorted(bill_data['BillDetails'].items()))
        print(sorted_dic["1"])'''

        #empty list to store dictonery reader data
        
        total=0
        for key,val in result['BillDetails'].items():
            for keys1 in product_list_data:
                if key==keys1['product_id']:
                    total+=float(keys1['unit_price'])*val
                    #print("product_id",key,"quantity",val,"unit_price",keys1['unit_price'],"price",total,float(keys1['unit_price'])*val)
        result["BillTotal"]=total

        updated_new="C:\\Users\\Admin\\Desktop\\Python_Trainning\\Billing\\Bills\\"+bill_file
        process_file="C:\\Users\\Admin\\Desktop\\Python_Trainning\\Billing\\Processed\\Processed_file_"+bill_file
        #print(process_file)
        with open(updated_new,'a') as f1:
            json.dump(bill_data,f1,indent=2)
        shutil.move(updated_new,process_file)
    
        #print(bill_data)
    time.sleep(2)


# process_bill()
# # def main():
# #     try:
# #         if not os.listdir(path):
# #             print("There are no bills to be processed")
# #         else:            
# #             t1=Thread(target=process_bill)
# #             t1.start()
# #     except FileNotFound as e:
# #         print(e)

# # #if __name__=='__main__':main()

   # updated_new="C:\\Users\\Admin\\Desktop\\Python_Trainning\\Billing\\Bills\\"+bill_file
process_file="C:\\Users\\Admin\\Desktop\\Python_Trainning\\Billing\\Processed\\process_"+bill_file
            #print(process_file)
            
f1=open(process_file,'w')
#f1.write(json.dumps(result,indent=2))
f1.close()
           # f1.close()
time.sleep(2)
        os.remove(path+"\\"+bill_file)

        time.sleep(2)
        