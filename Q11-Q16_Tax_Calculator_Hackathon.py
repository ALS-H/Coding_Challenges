#Tax calculator Hackathon

from tabulate import tabulate

class tax_calculator:
    def __init__(self,name,empid,basic_salary,special_allowance,bonus_percent):
        self.name=name
        self.empid=empid
        self.basic_salary=basic_salary
        self.special_allowance=special_allowance
        self.bonus_percent=bonus_percent

        #initialised
        self.gross_monthly_sal=0
        self.annual_gross_sal=0
        self.taxable_income=0
        self.tax_payable=0
        self.annual_net_salary=0

    #Independent Utility functions
    #Q16- Input Validation
    @staticmethod
    def validate_name(name):
        return name.isalpha() and len(name)<=50

    @staticmethod
    def validate_empid(empid):
        return empid.isalnum() and 5<=len(empid)<=10
    
    @staticmethod
    def validate_salary(basic_salary):
        return basic_salary>0 and basic_salary<=10000000
    
    @staticmethod
    def validate_allowance(special_allowance):
        return special_allowance>=0 and special_allowance<=10000000
    
    @staticmethod
    def validate_bonus_percent(bonus_percent):
        try:
            val=float(bonus_percent)
            return 0<=val<=100
        except:
            return False
        
    #Q11_salary calculation
    def sal_cal(self):
        self.gross_monthly_sal=self.basic_salary+self.special_allowance
        bonus_amt=(self.bonus_percent/100)*(self.gross_monthly_sal*12)
        self.annual_gross_sal=(self.gross_monthly_sal*12)+bonus_amt

        #display the output
        print("Employee name:",self.name)
        print("Emp ID:",self.empid)
        print("Gross Monthly Salary:",self.gross_monthly_sal)
        print("Annual Gross Salary:",self.annual_gross_sal)

    #Q12_taxable_income_calc
    def taxable_income_calc(self):
        std_deduction=50000
        #guard against negative taxable income
        self.taxable_income = max(0, self.annual_gross_sal - std_deduction)

        #display the output
        print("Gross Salary: ",self.annual_gross_sal)
        print("Standard Deductions: ",std_deduction)
        print("Taxable Income: ",self.taxable_income)

    #Q13-tax and rebate calculation
    def tax_rebate_calc(self):
        ti = self.taxable_income
        tax = 0

        #rebate
        if ti <= 700000:
            self.tax_payable = 0
            return

        # slab-wise calculation
        if ti > 1500000:
            tax += (ti - 1500000) * 0.30
            ti = 1500000

        if ti > 1200000:
            tax += (ti - 1200000) * 0.20
            ti = 1200000

        if ti > 900000:
            tax += (ti - 900000) * 0.15
            ti = 900000

        if ti > 600000:
            tax += (ti - 600000) * 0.10
            ti = 600000

        if ti > 300000:
            tax += (ti - 300000) * 0.05

        cess = tax * 0.04
        self.tax_payable = round(tax + cess)

        #display tax breakdown
        print("\nDetailed Tax Breakdown:")
        print("--------------------------------------------------")
        print("Slab Range                         | Tax Rate")
        print("--------------------------------------------------")
        print("₹3,00,001  -  ₹6,00,000            |     5%")
        print("₹6,00,001  -  ₹9,00,000            |    10%")
        print("₹9,00,001  -  ₹12,00,000           |    15%")
        print("₹12,00,001 -  ₹15,00,000           |    20%")
        print("Above ₹15,00,000                   |    30%")
        print("--------------------------------------------------")
        print(f"Total Tax (before cess): {tax:,.2f}")
        print(f"4% Health & Education Cess: {cess:,.2f}")
        print("--------------------------------------------------")
        print(f"Total Tax Payable: {self.tax_payable}")
    
    #Q14- net salary calculation
    def net_salary_calc(self):
        self.annual_net_salary=self.annual_gross_sal-self.tax_payable

        print("Annual Gross Salary:",self.annual_gross_sal)
        print("Total Tax Payable(including cess):",self.tax_payable)
        print("Annual Net Salary:",self.annual_net_salary)
    
    #Q15-report generation
    def gen_report(self):
        #summarize everything
        data=[
            ["Employee Name",self.name],
            ["Employee ID",self.empid],
            ["Gross Monthly Salary",f"{self.gross_monthly_sal:,}"],
            ["Annual Gross Salary",f"{self.annual_gross_sal:,}"],
            ["Taxable Income",f"{self.taxable_income:,}"],
            ["Annual Net Salary",f"{self.annual_net_salary:,}"]
        ]
        
        print(tabulate(data, headers=["Field", "Details"], tablefmt="fancy_grid"))

def get_validated_input():
    while True:
        name=input("Enter Name:")
        if tax_calculator.validate_name(name):
            break
        print("Invalid Name! Only Alphabets allowed (max 50 char)")
    
    while True:
        empid=input("Enter EmpID:")
        if tax_calculator.validate_empid(empid):
            break
        print("Invalid empid! Must be Alphanumeric 5-10 char")
    
    while True:
        try:
            basic=float(input("Enter your basic salary: "))
            if tax_calculator.validate_salary(basic):
                break
        except:
            pass
        print("Invalid basic salary! Must be positive and ≤ 1 crore")
        
    while True:
        try:
            allowance=float(input("Enter your monthly allowance: "))
            if tax_calculator.validate_allowance(allowance):
                break
        except:
            pass
        print("Invalid allowance! Must be ≥ 0 and <=1cr")

    while True:
        try:
            bonus=float(input("Enter your bonus percent: "))
            if tax_calculator.validate_bonus_percent(bonus):
                break
        except:
            pass
        print("Invalid bonus! Must be between 0-100%.")
    
    return name,empid,basic,allowance,bonus
        
    
#input validation test cases
# ----- Name Validation -----
assert tax_calculator.validate_name("Rahul") == True
assert tax_calculator.validate_name("A"*50) == True
assert tax_calculator.validate_name("A"*51) == False
assert tax_calculator.validate_name("Rahul123") == False
assert tax_calculator.validate_name("R@hul") == False

# ----- EmpID Validation -----
assert tax_calculator.validate_empid("EMP12") == True
assert tax_calculator.validate_empid("A1B2C3D4E5") == True
assert tax_calculator.validate_empid("ABC") == False
assert tax_calculator.validate_empid("A"*11) == False
assert tax_calculator.validate_empid("EMP!23") == False

# ----- Basic Salary Validation -----
assert tax_calculator.validate_salary(50000) == True
assert tax_calculator.validate_salary(10000000) == True
assert tax_calculator.validate_salary(10000001) == False
assert tax_calculator.validate_salary(-10) == False
assert tax_calculator.validate_salary(0) == False

# ----- Allowance Validation -----
assert tax_calculator.validate_allowance(20000) == True
assert tax_calculator.validate_allowance(0) == True
assert tax_calculator.validate_allowance(10000000) == True
assert tax_calculator.validate_allowance(10000001) == False
assert tax_calculator.validate_allowance(-1) == False

# ----- Bonus Percent Validation -----
assert tax_calculator.validate_bonus_percent(10) == True
assert tax_calculator.validate_bonus_percent(0) == True
assert tax_calculator.validate_bonus_percent(100) == True
assert tax_calculator.validate_bonus_percent(-5) == False
assert tax_calculator.validate_bonus_percent("abc") == False
#salary calculation test cases
tc = tax_calculator("A", "EMP01", 50000, 10000, 10)
tc.sal_cal()
assert tc.gross_monthly_sal == 60000
assert tc.annual_gross_sal == 720000 + 72000  # 7,92,000
tc = tax_calculator("B", "EMP02", 80000, 20000, 0)
tc.sal_cal()
assert tc.annual_gross_sal == (100000 * 12)  # 12,00,000
tc = tax_calculator("C", "EMP03", 100000, 0, 50)
tc.sal_cal()
assert tc.annual_gross_sal == (100000 * 12) + 600000  # 18,00,000
#taxable income test cases
tc = tax_calculator("A", "EMP01", 50000, 10000, 10)
tc.sal_cal()
tc.taxable_income_calc()
assert tc.taxable_income == tc.annual_gross_sal - 50000
#tax rebate cess test cases
#full rebate  T1
tc = tax_calculator("A", "EMP14", 25000, 5000, 0) # Annual = 3,60,000
tc.sal_cal()
tc.taxable_income_calc()
tc.tax_rebate_calc()
assert tc.tax_payable == 0
    

#T2
tc = tax_calculator("A", "EMP56", 90000, 0, 0)
tc.sal_cal()
tc.taxable_income_calc()
tc.tax_rebate_calc()
assert tc.tax_payable == 67080
  
#T3
tc = tax_calculator("A", "EMP46", 120000, 0, 0)
tc.sal_cal()
tc.taxable_income_calc()
tc.tax_rebate_calc()
assert tc.tax_payable == 133120


print("All test cases passed!")