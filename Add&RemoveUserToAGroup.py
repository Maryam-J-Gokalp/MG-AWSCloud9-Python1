import os, subprocess

#Adds new user to the system
def new_user(): 
    confirm = "N" 
    while confirm != "Y":
        username = input("Enter the name of the user to add: ") 
        print("Use the username '" + username + "'? (Y/N)")
        confirm = input().upper()
        
    os.system("sudo adduser " + username) 

#Removes user from system        
def remove_user():
    confirm = "N" 
    while confirm != "Y":
        username = input("Enter the name of the user to remove: ")
        print("Remove the user : '" + username + "'? (Y/N)")
        confirm = input().upper()
    
    os.system("sudo userdel -r " + username)

#Adds user to group
def add_user_to_group():
    username = input("Enter the name of the user that you want to add to a group: ") 
    output = subprocess.Popen('groups', stdout=subprocess.PIPE).communicate()[0] 
    print("Enter a list of groups to add the user to") 
    print("The list should be separated by spaces, for example:\r\n group1 group2 group3") 
    print("The available groups are: ")
    print(output) 
    chosenGroups = str(input("Groups: "))
    output = str(output).split(" ") 
    print("Add To: " + chosenGroups) 
    chosenGroups = chosenGroups.split(" ") 
    groupString = ""
    
    for grp in chosenGroups:
        if grp in output:
            print(f"Group {grp} found")
            groupString = groupString + grp + ","

        else:
            print(f"Group {grp} not found. Please first add group to the system")
            
    groupString = groupString[:-1] + " " 
    confirm = ""
    
    while confirm != "Y" and confirm != "N" : 
        print("Add user '" + username + "' to these groups? " + groupString + " (Y/N)") 
        confirm = input().upper()
        
    if confirm == "N": 
        print("User " + username + " not added")
    elif confirm == "Y":
        os.system("sudo usermod -aG " + groupString + username) 
        print("User "+ username + " added")
        

def install_or_remove_packages():
    iOrR = "" 
    while iOrR != "I" and iOrR != "R":
        print("Would you like to install or remove packages? (I/R)")
        iOrR = input().upper()
        
    if iOrR == "I": 
        iOrR = "install"
        
    elif iOrR == "R": 
        iOrR = "remove"
        
    print("Enter a list of packages to install") 
    print("The list should be separated by spaces, for example:") 
    print(" package1 package2 package3") 
    print("Otherwise, input 'default' to " + iOrR + " the default packages listed in this program") 
    packages = input().lower() 
    
    if packages == "default": 
        packages = ""
        os.system("sudo yum update -y")
        os.system("sudo yum upgrade -y")
        
    if iOrR == "install":
        os.system("sudo yum install " + packages + " -y")
        
    elif iOrR == "remove": 
        while True: 
            print("Purge files after removing? (Y/N)") 
            choice = input().upper() 
            
            if choice == "Y":
                os.system("sudo yum " + iOrR + " " + packages + " -y") 
                os.system("sudo yum autoremove -y") 
                break
            
            elif choice == "N":
                os.system("sudo yum " + iOrR + " " + packages + " -y") 
                break

        
#Cleans the environment after an uninstall    
def clean_environment(): 
        os.system("sudo yum autoremove") 
        # os.system("sudo yum autoclean")
        
#Updates the default modules
def update_environment():
    os.system("sudo yum update") 
    os.system("sudo yum upgrade") 
    os.system("sudo yum update --security")


    
# new_user()
# remove_user()
# add_user_to_group()
# clean_environment()
# update_environment()
# install_or_remove_packages()