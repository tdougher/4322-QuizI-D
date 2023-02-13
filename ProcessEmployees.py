'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file
infile = open("employee_data.csv", "r")
reader = csv.reader(infile)
next(reader)




#create an empty dictionary
new_salary = {}

#use a loop to iterate through the csv file
for row in reader:
    fname = row[1]
    lname = row[2]
    full_name = fname+' '+lname
    department = row[3]
    title = row[4]
    salary = float(row[5])
    #check if the employee fits the search criteria
    if department == "Marketing" and title == "CSR":
        print(f"Manager Name: {full_name} Current Salary: ${salary:,.2f}")
        salary*= 1.1
        new_salary[full_name] = salary
        


    

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout
for k, v in new_salary.items():
    print(f"Manager Name: {k} New Salary: ${v:,.2f}")


          
        

        
    
