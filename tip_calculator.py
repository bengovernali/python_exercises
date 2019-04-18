service_status = False

while service_status == False:
    bill    = float(input("Total bill amount? "))
    service = input("Level of service? ")
    if service == "good":
        service_status = True
    elif service == "fair":
        service_status = True
    elif service_status == "bad":
        service_status = True

def calculate_tip(bill, service):

    if service == "good":
        tip_percent = 0.20
    elif service == "fair":
        tip_percent = 0.15
    elif service == "bad":
        tip_percent = 0.10
    
    tip_amount = bill * tip_percent
    print("Tip amount: $%.2f" % tip_amount)

    total_amount = bill + tip_amount
    print("Total amount: $%.2f" % total_amount)

calculate_tip(bill, service)
