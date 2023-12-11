import time
import math

def turn_off():
    print("Turning off load balancer. . .")
    time.sleep(2)
    exit()

def access():
    try:
        Port_1 = int(input("How many access are on port 1: "))
        Port_2 = int(input("How many access are on port 2: "))
    except ValueError:
        print("Invalid number of accesses.")
    total = Port_1 + Port_2
    if total > 150:
        print("database's maximum capacity is 150")
    else: 
        load_balancer(Port_1, Port_2)

def load_balancer(Accesses_1, Accesses_2):
    global Server_1_Split_Accesses
    global Server_2_Split_Accesses
    global Split_Accesses
    Total_Accesses = Accesses_1 + Accesses_2
    if Total_Accesses // 2 != 0:
        Server_1_Split_Accesses = math.ceil(Total_Accesses / 2)
        Server_2_Split_Accesses = math.floor(Total_Accesses / 2) 
        server_1()
    else: 
        Split_Accesses = Total_Accesses / 2

def server_1():
    global Server_1_Split_Accesses
    global Server_2_Split_Accesses
    global Split_Accesses
    Server_1_capacity = 50
    if Server_1_Split_Accesses > Server_1_capacity: 
        Transferred = Server_1_Split_Accesses - Server_1_capacity
        Server_1_Split_Accesses = Server_1_Split_Accesses - Transferred
        print(f"Server 1 was overloaded, transferring {Transferred} accesses to server 2 . . .")
        time.sleep(1)
        print(f"Server 1 is handling: {Server_1_Split_Accesses}")
        server_2(Transferred)
    else: 
        print(f"Server 1 is handling: {Server_1_Split_Accesses}")

def server_2(Addded_Accesses):
    global Server_1_Split_Accesses
    global Server_2_Split_Accesses
    global Split_Accesses
    Server_2_Split_Accesses = Server_2_Split_Accesses + Addded_Accesses
    print(f"Server 2 is handling: {Server_2_Split_Accesses}")

match input("Enable the load balancer?(y/n): "):
    case "y":         
        access()
    case "n":
        turn_off()
    case _:
        print("Invalid input value.")
