#WRITE A PSEUDOCODE
password = ("sesameOil") # User need to write the correct passsword otherwisedenied
hello = input("Enter the password: ")
while hello != password:
    print ("Access denied")
    hello = input("Enter the password: ")
    if hello == password:
        print ("Login successfull!")
        
        