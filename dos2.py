print ("               __ ")
print ("    .,-;-;-,. /'_\    ______________________")
print ("  _/_/_/_|_\_\) /   <|Let's start dos attack|")
print ("'-<_><_><_><_>=/\     ----------------------")
print (" `/_/====/_/-'\_\ ")
print ("  ''     ''    '' ")
import os
user = input ("Enter hostname or ip: ")
print ("DOS ATTACK STARTED!")
def myping(host):
    response = os.system("ping -s 1000 " + host)
    
    if response == 0:
        return True
    else:
        return False
        
print(myping(user))
