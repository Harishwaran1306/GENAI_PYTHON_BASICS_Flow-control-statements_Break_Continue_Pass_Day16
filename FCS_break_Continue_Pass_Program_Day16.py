#Flow Control Statements
#Break

'''for i in range(1,12):
    print(i,end=' ' )
    if i == 7:
        break'''



Password=12025
attempt = 0

'''for attempt in range(1,7):
    pin = int(input('Enter the Password:'))

    if pin == Password:
        print('Correct Password')
        print('Access Granted')
        break

    else:
        print('Access Denied')

    if  attempt==5:
        print('Final Attempt')'''

#=======================================================================================    

#Continue

'''for i in range(1,12):
    if i == 7:
        continue
    print(i)'''




'''Transaction_History = [{"Customer_Name": "Victor", "Trans_id": 8545, "Amount": 100500, "Flaged_Status": "failed"},
                       {"Customer_Name": "Justin", "Trans_id": 8549, "Amount": 200500, "Flaged_Status": "failed"},
                       {"Customer_Name": "Tony",   "Trans_id": 8559, "Amount": 400500, "Flaged_Status": "Success"},
                       {"Customer_Name": "Bruce",  "Trans_id": 8569, "Amount": 400500, "Flaged_Status": "failed"}]

for Transaction in Transaction_History:
    if Transaction['Flaged_Status'] == 'Success':
        continue
    print('failed transaction')
    print('-'*30)
    print(f"Customer : {Transaction['Customer_Name']}")
    print(f"Trans ID : {Transaction['Trans_id']}")
    print(f"Amount   : {Transaction['Amount']}")
    print(f"Status   : {Transaction['Flaged_Status']}") '''




#=====================================================================================================================


#Pass

'''for i in range(1,10):
    if i == 5:
        print(i)
    pass'''




'''Transaction_History = [{"Customer_Name": "Victor", "Trans_id": 8545, "Amount": 100500, "Flaged_Status": "failed"},
                       {"Customer_Name": "Justin", "Trans_id": 8549, "Amount": 200500, "Flaged_Status": "failed"},
                       {"Customer_Name": "Tony",   "Trans_id": 8559, "Amount": 400500, "Flaged_Status": "Success"},
                       {"Customer_Name": "Bruce",  "Trans_id": 8569, "Amount": 400500, "Flaged_Status": "failed"}]

for Transaction in Transaction_History:
    if Transaction['Flaged_Status'] == 'Success':
        
        print('Success transaction')
        print('-'*30)
        print(f"Customer : {Transaction['Customer_Name']}")
        print(f"Trans ID : {Transaction['Trans_id']}")
        print(f"Amount   : {Transaction['Amount']}")
        print(f"Status   : {Transaction['Flaged_Status']}") 
    pass'''

   





















    



