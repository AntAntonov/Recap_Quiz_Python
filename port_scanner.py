import sys
import socket
from datetime import datetime
  

     
# translate hostname to IPv4
target = socket.gethostbyname(input("Which site to scan:"))
print(target)
 

print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))

  
try:
     
    # scan range of ports
    for port in range(77,81):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
         
       
        result = s.connect_ex((target,port))
        if result ==0:
            print(f"Port {port} is open")
        s.close()
         
except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()

except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()