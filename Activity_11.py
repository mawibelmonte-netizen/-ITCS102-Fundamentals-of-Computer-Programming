#import demo
import getpass

username = "mawikun"
password = "Pogi_si_mawi_123"

u = input("input USERNAME ---> ")
p = getpass.getpass("input PASSWORD --->")

if u == username and p == password:
	print("Username and Password is Correct")

else:
	print("Access Denied")