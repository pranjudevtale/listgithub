 
# question_list = [
#     "How many continents are there?",             
#     "What is the capital of India?",            
#     "NG mei kaun se course padhaya jaata hai? "  
# ]

# options_list = [
#     ["Four", "Nine", "Seven", "Eight"],
#     ("Chandigarh", "Bhopal", "Chennai", "Delhi")
#     ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
# ]

# solution_list = [3, 4, 1] 

print("how many contient are there? ")
print("A- four ")
print("B- Nine ")
print("C- seven ")
print("D- eight ")

option1= "A"
option2="B"
option3="C"
option4="D"
a=input("please choose your answer")
if a==str(option1):
    print("your wrong")
elif a==str(option2):
    print("your wrong")
elif a==str(option3):
    print("your right")
elif a==str(option4):
    print("your wrong")
else:
    print("please choose a valid option")
