print ("               __ ")
print ("    .,-;-;-,. /'_\    ______________________")
print ("  _/_/_/_|_\_\) /   <|Let's start dos attack|")
print ("'-<_><_><_><_>=/\     ----------------------")
print (" `/_/====/_/-'\_\ ")
print ("  ''     ''    '' ")
import os
user = input ("Enter hostname or ip: ")
def ping(host):
    response = os.system("ping " + host)
    
    if response == 0:
        return True
    else:
        return False
        
print(ping(user))
