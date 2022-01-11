import os
user = input ("Enter hostname or ip: ")
def myping(host):
    response = os.system("ping -s 1000 " + host)
    
    if response == 0:
        return True
    else:
        return False
        
print(myping(user))
