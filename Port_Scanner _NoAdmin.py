#Port Scanner, John Greim, CT206, 3/25/19, Assignment 7
import socket
import datetime


#Prints banner
print("[CT206 Port Scanner 2000]")
print("[This Tool is for Education and Research Purposes Only!]")

try:
    #Takes user input for address target
    usrtarget = input("Enter a hostname/IP address for target: ")
    address = socket.gethostbyname(usrtarget)
    print("Target: ", address)

    #Write Target to File
    with open("portscan_results.txt","a") as file:
        file.write("Target: " + address + "\n")

    #Get min and max port for range
    MinPort = int(input("Enter the Minimum Port to Scan: "))
    MaxPort = int(input("Enter the Maximum Port to Scan: "))

    #Gets Start Date/Time
    x = datetime.datetime.now()
    print("Start Date and Time:", x)

    # Writes Start Time to File
    with open("portscan_results.txt","a") as file:
        file.write("Start Time: " + str(x) + "\n")
    
    #Loops through port range and attempts to connect
    #for port in range (1, 201):
    for port in range (MinPort,MaxPort):
        
        #Attempts to create socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((address, port))
        
        #Checks if port is open/closed writes to file
        if result == 0:
            print ("Port {}: Open" .format(port))
            
            with open("portscan_results.txt","a") as file:
                file.write("Port {}: Open\n" .format(port))
        else:
            print ("Port {}: Closed" .format(port))
            
            with open("portscan_results.txt","a") as file:
                file.write("Port {}: Closed\n" .format(port))
        sock.close()
        
    #Gets End Date/Time
    y = datetime.datetime.now()
    print ("End Date and Time:", str(y))

    #Writes End Time to File
    with open("portscan_results.txt","a") as file:
            file.write("End Time: " + str(x) + "\n")
    
    #Gets difference in Date/Time
    duration = y - x
    print ("Total Time of Scan:", duration)

    #Writes Duration Time to File
    with open("portscan_results.txt","a") as file:
            file.write("Total Time Taken: " + str(duration) + "\n")
    
except ConnectionRefusedError:
    print("Could Not Connect to Server")
except KeyboardInterrupt:
    print("You Pressed Ctrl+C")
except ValueError:
    print("Wrong Value Type Input!")
except IOError:
    print("File Could Not Write Try running as Administrator")
except:
    print("Something Went Wrong!")


