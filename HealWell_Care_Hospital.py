#a day at healwell care hospital

def patient_details():
    name=input("Enter your name:")
    age=int(input("Enter your age:"))
    gender=input("Enter your gender Male/Female:")
    while True:
        contact = input("Enter your 10-digit phone number: ")
        if contact.isdigit() and len(contact) == 10:
            break
        else:
            print("Invalid contact number. Please enter exactly 10 digits.")
    return name,age,gender,contact
    
def services(available_services):
    selected_services = []

    print("Available Services:")
    for i, ser in enumerate(available_services, start=1):
        print(f"{i}. {ser}")

    line = input("Enter the numbers next to the services you want with comma: ")
    patient_selected = line.split(",")

    for num in patient_selected:
        ix = int(num.strip()) - 1
        if 0 <= ix < len(available_services):
            selected_services.append(available_services[ix])

    if not selected_services:
        print("No valid services selected.")

    return selected_services


#O(n) if u use dictionary
def costs_of_services(selected_services,ser_dict):
    sel_costs=[]
    for ser in selected_services:
        sel_costs.append(ser_dict[ser])
    
    return sel_costs

def totale(sel_costs):
    total_cost=round(sum(sel_costs),2)
    print("Total Cost (Before Tax):",total_cost)
    return total_cost

def gst_on_bill(total_cost):
    gst=round(0.18*total_cost,2)
    grand_total=gst+total_cost
    
    print("GST (18%):",gst)
    print("Grand Total:",grand_total)
    
    return gst,grand_total

def invoice(name, age, gender, contact, sel_services, sel_costs, total_cost, gst, grand_total):
    print("-----------------------------------------------")
    print("HealWell Care Hospital")
    print("Patient Invoice")
    print("-----------------------------------------------\n")

    print("Patient Information:")
    print("Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("Contact:", contact)
    print()

    print("Services Availed:")
    for i in range(len(sel_services)):
        print(f"{i+1}. {sel_services[i]}: ₹{sel_costs[i]}")

    print("\nSubtotal: ₹", total_cost)
    print("GST (18%): ₹", gst)
    print("Grand Total: ₹", grand_total)
    print("\nThank you for choosing HealWell Care Hospital!")

    
if __name__ == "__main__":
    Services=["General Consultation", "Blood Test", "Covid Test", "X-Ray", "CT Scan", "MRI"]  
    Costs=[500, 300, 800, 1500, 4000, 7000]  
    ser_dict = dict(zip(Services, Costs))

    name, age, gender, contact = patient_details()
    selected_services = services(Services)
    if not selected_services:
        print("Billing cannot be generated without selecting at least one valid service.")
        exit()
    sel_costs = costs_of_services(selected_services, ser_dict)
    total_cost = totale(sel_costs)
    gst, grand_total = gst_on_bill(total_cost)
    invoice(name, age, gender, contact, selected_services, sel_costs, total_cost, gst, grand_total)

    