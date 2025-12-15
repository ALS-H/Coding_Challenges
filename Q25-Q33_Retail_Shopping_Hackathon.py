#Retail Shopping Hackathon


#Q25  Basic Item Entry and Total Calculation
def basic_input():
    item_total = 0
    item_code=input("Enter the item code:")
    item_desc=input("Enter the item desc:")
    item_quan=int(input("Enter the quantity:"))
    item_price=float(input("Enter the item price:"))
    
    item_total=round(item_quan*item_price,2)
    item_total=promo_disc(item_code,item_total)
        
    print("Initial Item Total:", item_total)
    return item_code,item_desc,item_quan,item_price,item_total

#Q26  Iterative Item Entry and Grand Total 
def iter_input():
    n = int(input("How many items do you want to enter?: "))
    
    items = []
    total_qty=0
    grand_total = 0

    for _ in range(n):
        item_code,item_desc,item_quan,item_price,item_total=basic_input()
        items.append((item_code,item_desc,item_quan,item_price))
        total_qty+=item_quan
        grand_total+=item_total
        
    print("Initial Grand Total:", grand_total)
    return items,total_qty,round(grand_total, 2)


#Q27 Applying Discounts 
def apply_discounts(grand_total, total_quan):
    discount = 0

    if grand_total > 10000:
        d1 = 0.10 * grand_total
        grand_total -= d1
        discount += d1

    if total_quan > 20:
        d2 = 0.05 * grand_total
        grand_total -= d2
        discount += d2

    print("Total Discount Applied:", round(discount, 2))
    print("Total after Discounts:", round(grand_total, 2))
    return round(grand_total, 2)
    
#Q28
def mem_disc(grand_total):
    mem_status = input("Are you a member? (y/n): ")
    if mem_status.lower() == "y":
        discount = 0.02 * grand_total
        grand_total -= discount
        print("Membership Discount:", round(discount, 2))
    else:
        print("No Membership Discount")

    return round(grand_total, 2)

#Q29
def tax_cal(grand_total):
    if grand_total < 5000:
        tax = 0.05 * grand_total
    elif grand_total <= 20000:
        tax = 0.10 * grand_total
    else:
        tax = 0.15 * grand_total

    grand_total += tax
    print("Tax Applied:", round(tax, 2))
    print("Total after Tax:", round(grand_total, 2))
    return round(grand_total, 2)       

#Q30
def promo_disc(item_code, item_total):
    if item_code == "PROMO10":
        return round(item_total * 0.9, 2)  # 10% off
    return round(item_total, 2)            # NO PROMO → original price


#Q31
def pay_mode_rules(grand_total):
    mode = input("Enter your mode of payment (Cash / Credit Card): ")
    if mode.lower() == "cash":
        surcharge = 0
    elif mode.lower() == "credit card":
        surcharge = round(grand_total * 0.02, 2)
    else:
        raise ValueError("Invalid payment mode")

    final_amount = round(grand_total + surcharge, 2)
    print("Payment Mode:", mode)
    print("Surcharge:", surcharge)
    print("Final Payable Amount:", final_amount)

    return final_amount

#Q32
def min_pur_req(grand_total):
    if grand_total < 500:
        print("Minimum purchase amount of ₹500 not met.")
        return False
    return True

#Q33
def loyalty_points(grand_total):
    points = int(grand_total // 100)
    print("Loyalty Points Earned:", points)
    return points

if __name__=="__main__":
    
    items,total_qty,grand_total = iter_input()   # Q26
    grand_total = apply_discounts(grand_total, total_qty)  # Q27
    grand_total = mem_disc(grand_total)             # Q28

    grand_total = tax_cal(grand_total)               # Q29
    
    grand_total = pay_mode_rules(grand_total)        # Q31

    if not min_pur_req(grand_total):                 # Q32
        exit()

    points = loyalty_points(grand_total) #Q33

    print("\n----- FINAL INVOICE -----")
    for item in items:
        print(item)

    print("Final Amount Payable:", grand_total)
    print("Total Loyalty Points:", points)