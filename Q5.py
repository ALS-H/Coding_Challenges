#farmer problem statement

#vegetables (Tomato,Potato, Cabbage) -> chemical free after 6 months
#sunflower -> after another 4 months-> 10 months
#sugarcane -> after another 4 months -> 14 months
# 1 tonne =1000kg
# So after 11 months chemical free crops are Tomato, Potato, Cabbage and Sunflower
#Sugarcane still under conversion

#without Decimal the float values are so huge it gives OverflowError.
#for large values,money,finance use Decimal not float

def farmer_sales():
    acres_per_crop = 16  # acres per crop

    # 30% at 10t/acre and 70% at 12t/acre, price per kg 7
    tomatoes_30 = 0.3 * acres_per_crop * 10 * 1000 * 7
    tomatoes_70 = 0.7 * acres_per_crop * 12 * 1000 * 7
    tomato_sales = tomatoes_30 + tomatoes_70

    # Other crops
    potatoes_sales = acres_per_crop * 10 * 1000 * 20
    cabbage_sales = acres_per_crop * 14 * 1000 * 24
    sunflower_sales = acres_per_crop * 0.4 * 1000 * 200
    sugarcane_sales = acres_per_crop * 45 * 4000

    # Overall sales across 80 acres
    total_sales = tomato_sales + potatoes_sales + cabbage_sales + sunflower_sales + sugarcane_sales

    # Sales from chemical-free farming (excluding sugarcane)
    chemical_free_sales = tomato_sales + potatoes_sales + cabbage_sales + sunflower_sales

    # Round to 2 decimal places
    total_sales = round(total_sales, 2)
    chemical_free_sales = round(chemical_free_sales, 2)

    return total_sales, chemical_free_sales


if __name__ == "__main__":
    total, chemical_free = farmer_sales()
    print("Total sales across 80 acres of land:", total)
    print("Chemical-free sales at 11 months:", chemical_free)
