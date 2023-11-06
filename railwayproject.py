#list of trains
#need to import time
#ticket generation
#list of passengers
#type of tickets,ac and sleepers
#source and distenation
import datetime
username={"sai":'2244',"koti":'1234',"hari":'3344',"sita":'4455'}
list_of_trains={"chennai_express":'1234',"tirupathi_express":'5678',"eastgurd_express":'91011',"mumbai_express":'121314',"guntur_rayagada":'151617'}
user_name=input("enter your username:")
password_train=input("enter your password:")
if user_name in user_name:
    if password_train in username[user_name]:
        print("yes,vaild")
        for k,v in list_of_trains.items():
            print("trainname",k,"trainnumber",v)
            
trains_rates={"chennai_express":'123',"tirupathi_express":'567',"eastgurd_express":'910',"mumbai_express":'121',"guntur_rayagada":'151'}          
for k,v in trains_rates.items():
    print("select_train:",k,"trainrate:",v)    

tra=input("enter your required train:")
pas=int(input("enter  number of passengers:"))

if tra in trains_rates:
    print("ticket_rate:",int(trains_rates[tra])*pas)
    
print("your ticket is confirmed")
user_date=int(input("enter your reservation date:"))
date=datetime.datetime(2023,8,user_date)
print("your reservation date:",date)
print(datetime.datetime.now())

 
            


