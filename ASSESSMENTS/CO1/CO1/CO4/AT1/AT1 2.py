machines={"M1":"Active","M2":"Active","M3":"Maintenance","M4":"Active"}
produces={}
print("MACHINE STATUS")
for machine,status in machines.items():
    print(machine,"->",status)
print("\nINFERRED PRODUCTION")
for machine,status in machines.items():
    if status=="Active":
        print("Producing("+machine+")")
    elif status=="Maintenance":
        print("Not Producing("+machine+")")
print("\nPRODUCT AVAILABILITY")
if not produces:
    print("Cannot determine: no Produces(machine,product) facts are provided")
print("\nGEAR ANALYSIS")
print("Cannot determine whether Gear is affected because no machine-to-Gear production relation is provided")
