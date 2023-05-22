def get_ratarata():
    with open("bonus/data1.txt", 'r') as file:
        data = file.readlines()[1:]
    data = [float(i) for i in data]
    average = sum(data) / len(data)
    return average

print(get_ratarata())

### **Coding Exercise 1**

#The code below is incomplete. 
# It should calculate and print out the maximum value of the `grades` list. 
# Please complete the function and then call it.

def get_max():
    grades = [9.6, 9.2, 9.7]
    max_grades = max(grades)
    min_grades = min(grades)
    message = f"Max : {max_grades}, Min : {min_grades}"    
    return message

print(get_max())


#The output of your code should be:`9.7`

#Hint: You can use the `max(list)` function to find the maximal value of a list.

### **Coding Exercise 2**

#The function we wrote in exercise 1 returned `9.7`.  
# Change the function so this time it returns `Max: 9.7, Min: 9.2` 
# where 9.7 is the maximum and 9.2 is the minimum.'

### **Bug-Fixing Exercise 1**