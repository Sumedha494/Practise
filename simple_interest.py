#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("╔════════════════════════════════════════════════════════╗")
print("║         💰 SIMPLE INTEREST CALCULATOR 💰              ║")
print("╚════════════════════════════════════════════════════════╝")

print("""
📌 FORMULA:
   ┌─────────────────────────────┐
   │  SI = (P × R × T) / 100     │
   └─────────────────────────────┘

   Where:
   • P = Principal Amount (Initial Investment)
   • R = Rate of Interest (% per annum)
   • T = Time Period (in years)

   Total Amount (A) = P + SI
""")


# In[2]:


def calculate_simple_interest(principal, rate, time):
    """
    Calculate Simple Interest

    Parameters:
    - principal: Initial amount (P)
    - rate: Interest rate per annum (R)
    - time: Time period in years (T)

    Returns:
    - simple_interest: The calculated interest
    """
    simple_interest = (principal * rate * time) / 100
    return simple_interest

p = 10000  # Principal
r = 5      # Rate (5%)
t = 2      # Time (2 years)

si = calculate_simple_interest(p, r, t)
print(f"Principal: ₹{p:,}")
print(f"Rate: {r}% per annum")
print(f"Time: {t} years")
print(f"Simple Interest: ₹{si:,.2f}")


# In[3]:


def calculate_si_and_amount(principal, rate, time):
    """
    Calculate Simple Interest and Total Amount

    Returns:
    - tuple: (simple_interest, total_amount)
    """
    simple_interest = (principal * rate * time) / 100
    total_amount = principal + simple_interest

    return simple_interest, total_amount

# Test
p = 50000  # Principal
r = 8      # Rate (8%)
t = 3      # Time (3 years)

si, total = calculate_si_and_amount(p, r, t)

print("=" * 40)
print("💰 SIMPLE INTEREST CALCULATION")
print("=" * 40)
print(f"  Principal Amount  : ₹{p:>12,}")
print(f"  Rate of Interest  : {r:>12}%")
print(f"  Time Period       : {t:>12} years")
print("-" * 40)
print(f"  Simple Interest   : ₹{si:>12,.2f}")
print(f"  Total Amount      : ₹{total:>12,.2f}")
print("=" * 40)


# In[4]:


def calculate_si_breakdown(principal, rate, time):
    """
    Calculate Simple Interest with yearly breakdown
    """
    yearly_interest = (principal * rate) / 100

    print("\n📊 YEAR-BY-YEAR BREAKDOWN:")
    print("-" * 60)
    print(f"{'Year':<8} {'Interest Earned':<18} {'Total Interest':<18} {'Balance':<15}")
    print("-" * 60)

    total_interest = 0

    for year in range(1, int(time) + 1):
        total_interest += yearly_interest
        balance = principal + total_interest
        print(f"{year:<8} ₹{yearly_interest:<17,.2f} ₹{total_interest:<17,.2f} ₹{balance:<14,.2f}")

    print("-" * 60)
    print(f"{'TOTAL':<8} ₹{total_interest:<17,.2f} ₹{total_interest:<17,.2f} ₹{principal + total_interest:<14,.2f}")
    print("-" * 60)

    return total_interest

p = 100000
r = 10
t = 5

si = calculate_si_breakdown(p, r, t)


# In[5]:


def calculate_si_flexible(principal, rate, time, time_unit='years'):
    """
    Calculate Simple Interest with flexible time units

    Parameters:
    - time_unit: 'years', 'months', 'days'
    """

    if time_unit.lower() == 'years':
        time_in_years = time
    elif time_unit.lower() == 'months':
        time_in_years = time / 12
    elif time_unit.lower() == 'days':
        time_in_years = time / 365
    else:
        raise ValueError("Invalid time unit. Use 'years', 'months', or 'days'")

    simple_interest = (principal * rate * time_in_years) / 100
    total_amount = principal + simple_interest

    return simple_interest, total_amount, time_in_years

print("📅 SIMPLE INTEREST WITH DIFFERENT TIME UNITS:\n")

si1, amt1, _ = calculate_si_flexible(10000, 12, 2, 'years')
print(f"1. ₹10,000 at 12% for 2 years")
print(f"   SI = ₹{si1:,.2f}, Amount = ₹{amt1:,.2f}\n")

si2, amt2, _ = calculate_si_flexible(10000, 12, 18, 'months')
print(f"2. ₹10,000 at 12% for 18 months")
print(f"   SI = ₹{si2:,.2f}, Amount = ₹{amt2:,.2f}\n")

si3, amt3, _ = calculate_si_flexible(10000, 12, 90, 'days')
print(f"3. ₹10,000 at 12% for 90 days")
print(f"   SI = ₹{si3:,.2f}, Amount = ₹{amt3:,.2f}")


# In[6]:


def find_principal(simple_interest, rate, time):
    """Find Principal when SI, R, T are known"""
    principal = (simple_interest * 100) / (rate * time)
    return principal

def find_rate(simple_interest, principal, time):
    """Find Rate when SI, P, T are known"""
    rate = (simple_interest * 100) / (principal * time)
    return rate

def find_time(simple_interest, principal, rate):
    """Find Time when SI, P, R are known"""
    time = (simple_interest * 100) / (principal * rate)
    return time

print("🔍 FINDING MISSING VARIABLES:\n")

si, r, t = 5000, 10, 2
p = find_principal(si, r, t)
print(f"1. Find Principal:")
print(f"   SI = ₹{si:,}, Rate = {r}%, Time = {t} years")
print(f"   Principal = ₹{p:,.2f}\n")

si, p, t = 3000, 25000, 2
r = find_rate(si, p, t)
print(f"2. Find Rate:")
print(f"   SI = ₹{si:,}, Principal = ₹{p:,}, Time = {t} years")
print(f"   Rate = {r:.2f}%\n")

si, p, r = 6000, 20000, 10
t = find_time(si, p, r)
print(f"3. Find Time:")
print(f"   SI = ₹{si:,}, Principal = ₹{p:,}, Rate = {r}%")
print(f"   Time = {t:.2f} years")


# In[7]:


def si_calculator_input():
    """Interactive Simple Interest Calculator"""

    print("\n" + "=" * 50)
    print("💰 SIMPLE INTEREST CALCULATOR")
    print("=" * 50)

    try:
        principal = float(input("\n📝 Enter Principal Amount (₹): "))
        rate = float(input("📝 Enter Rate of Interest (%): "))
        time = float(input("📝 Enter Time Period (years): "))

        si = (principal * rate * time) / 100
        total = principal + si

        print("\n" + "=" * 50)
        print("📊 RESULTS")
        print("=" * 50)
        print(f"  Principal Amount    : ₹{principal:>15,.2f}")
        print(f"  Rate of Interest    : {rate:>15.2f}%")
        print(f"  Time Period         : {time:>15.2f} years")
        print("-" * 50)
        print(f"  Simple Interest     : ₹{si:>15,.2f}")
        print(f"  Total Amount        : ₹{total:>15,.2f}")
        print("=" * 50)

        return si, total

    except ValueError:
        print("❌ Invalid input! Please enter numeric values.")
        return None, None

print("✅ Function ready! Call si_calculator_input() to use.")


# In[8]:


def compare_rates(principal, time, rates):
    """Compare SI at different interest rates"""

    print(f"\n📊 COMPARING DIFFERENT RATES")
    print(f"   Principal: ₹{principal:,} | Time: {time} years")
    print("=" * 60)
    print(f"{'Rate':<12} {'Simple Interest':<20} {'Total Amount':<20}")
    print("-" * 60)

    results = []

    for rate in rates:
        si = (principal * rate * time) / 100
        total = principal + si
        results.append((rate, si, total))
        print(f"{rate:>6}% {'':>5} ₹{si:>15,.2f} {'':>4} ₹{total:>15,.2f}")

    print("=" * 60)

    return results

principal = 100000
time = 5
rates = [5, 6, 7, 8, 9, 10, 12, 15]

results = compare_rates(principal, time, rates)


# In[9]:


def compare_rates(principal, time, rates):
    """Compare SI at different interest rates"""

    print(f"\n📊 COMPARING DIFFERENT RATES")
    print(f"   Principal: ₹{principal:,} | Time: {time} years")
    print("=" * 60)
    print(f"{'Rate':<12} {'Simple Interest':<20} {'Total Amount':<20}")
    print("-" * 60)

    results = []

    for rate in rates:
        si = (principal * rate * time) / 100
        total = principal + si
        results.append((rate, si, total))
        print(f"{rate:>6}% {'':>5} ₹{si:>15,.2f} {'':>4} ₹{total:>15,.2f}")

    print("=" * 60)

    return results

principal = 100000
time = 5
rates = [5, 6, 7, 8, 9, 10, 12, 15]

results = compare_rates(principal, time, rates)


# In[10]:


def compare_si_ci(principal, rate, time):
    """Compare Simple Interest and Compound Interest"""

    si = (principal * rate * time) / 100
    si_amount = principal + si

    ci_amount = principal * ((1 + rate/100) ** time)
    ci = ci_amount - principal

    difference = ci - si

    print(f"\n⚖️ SIMPLE INTEREST vs COMPOUND INTEREST")
    print("=" * 60)
    print(f"  Principal: ₹{principal:,} | Rate: {rate}% | Time: {time} years")
    print("=" * 60)

    print(f"\n  📗 SIMPLE INTEREST:")
    print(f"     Interest Earned : ₹{si:>15,.2f}")
    print(f"     Total Amount    : ₹{si_amount:>15,.2f}")

    print(f"\n  📘 COMPOUND INTEREST (Yearly):")
    print(f"     Interest Earned : ₹{ci:>15,.2f}")
    print(f"     Total Amount    : ₹{ci_amount:>15,.2f}")

    print(f"\n  📊 DIFFERENCE:")
    print(f"     Extra with CI   : ₹{difference:>15,.2f}")
    print(f"     Percentage More : {(difference/si)*100:>15.2f}%")
    print("=" * 60)

    return si, ci, difference

si, ci, diff = compare_si_ci(100000, 10, 5)


# In[11]:


def compare_si_ci(principal, rate, time):
    """Compare Simple Interest and Compound Interest"""

    si = (principal * rate * time) / 100
    si_amount = principal + si

    ci_amount = principal * ((1 + rate/100) ** time)
    ci = ci_amount - principal

    difference = ci - si

    print(f"\n⚖️ SIMPLE INTEREST vs COMPOUND INTEREST")
    print("=" * 60)
    print(f"  Principal: ₹{principal:,} | Rate: {rate}% | Time: {time} years")
    print("=" * 60)

    print(f"\n  📗 SIMPLE INTEREST:")
    print(f"     Interest Earned : ₹{si:>15,.2f}")
    print(f"     Total Amount    : ₹{si_amount:>15,.2f}")

    print(f"\n  📘 COMPOUND INTEREST (Yearly):")
    print(f"     Interest Earned : ₹{ci:>15,.2f}")
    print(f"     Total Amount    : ₹{ci_amount:>15,.2f}")

    print(f"\n  📊 DIFFERENCE:")
    print(f"     Extra with CI   : ₹{difference:>15,.2f}")
    print(f"     Percentage More : {(difference/si)*100:>15.2f}%")
    print("=" * 60)

    return si, ci, difference

si, ci, diff = compare_si_ci(100000, 10, 5)


# In[12]:


import matplotlib.pyplot as plt
def visualize_si_growth(principal, rate, time):
    """Create bar chart showing SI growth over time"""

    years = list(range(1, time + 1))
    interests = [(principal * rate * y) / 100 for y in years]
    amounts = [principal + si for si in interests]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    bars1 = ax1.bar(years, interests, color='#3498db', edgecolor='black')
    ax1.set_xlabel('Years', fontsize=12)
    ax1.set_ylabel('Interest Earned (₹)', fontsize=12)
    ax1.set_title(f'Simple Interest Growth\nP=₹{principal:,}, R={rate}%', fontsize=14)
    ax1.set_xticks(years)

    for bar, interest in zip(bars1, interests):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 500,
                f'₹{interest:,.0f}', ha='center', fontsize=9)

    bars2 = ax2.bar(years, amounts, color='#2ecc71', edgecolor='black')
    ax2.axhline(y=principal, color='red', linestyle='--', label=f'Principal (₹{principal:,})')
    ax2.set_xlabel('Years', fontsize=12)
    ax2.set_ylabel('Total Amount (₹)', fontsize=12)
    ax2.set_title(f'Total Amount Over Time\nP=₹{principal:,}, R={rate}%', fontsize=14)
    ax2.set_xticks(years)
    ax2.legend()

    for bar, amount in zip(bars2, amounts):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1000,
                f'₹{amount:,.0f}', ha='center', fontsize=9)

    plt.tight_layout()
    plt.show()

visualize_si_growth(100000, 10, 5)
print("✅ Bar chart displayed!")


# In[13]:


def visualize_si_vs_ci(principal, rate, time):
    """Create line chart comparing SI and CI"""

    years = list(range(0, time + 1))

    si_amounts = [principal + (principal * rate * y) / 100 for y in years]
    ci_amounts = [principal * ((1 + rate/100) ** y) for y in years]

    plt.figure(figsize=(12, 6))

    plt.plot(years, si_amounts, 'b-o', linewidth=2, markersize=8, label='Simple Interest')
    plt.plot(years, ci_amounts, 'g-s', linewidth=2, markersize=8, label='Compound Interest')
    plt.axhline(y=principal, color='red', linestyle='--', linewidth=1, label=f'Principal (₹{principal:,})')

    plt.fill_between(years, si_amounts, ci_amounts, alpha=0.3, color='yellow', label='CI Advantage')

    plt.xlabel('Years', fontsize=12)
    plt.ylabel('Amount (₹)', fontsize=12)
    plt.title(f'Simple Interest vs Compound Interest\nP=₹{principal:,}, R={rate}%', fontsize=14)
    plt.legend(loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.xticks(years)

    plt.annotate(f'SI: ₹{si_amounts[-1]:,.0f}', xy=(time, si_amounts[-1]),
                xytext=(time-1, si_amounts[-1]+5000), fontsize=10)
    plt.annotate(f'CI: ₹{ci_amounts[-1]:,.0f}', xy=(time, ci_amounts[-1]),
                xytext=(time-1, ci_amounts[-1]+5000), fontsize=10)

    plt.tight_layout()
    plt.show()

visualize_si_vs_ci(100000, 10, 10)
print("✅ Line chart displayed!")


# In[14]:


def visualize_pie_chart(principal, rate, time):
    """Create pie chart showing Principal vs Interest breakdown"""

    si = (principal * rate * time) / 100
    total = principal + si

    labels = ['Principal', 'Interest']
    sizes = [principal, si]
    colors = ['#3498db', '#e74c3c']
    explode = (0, 0.1)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    wedges, texts, autotexts = ax1.pie(sizes, explode=explode, labels=labels, colors=colors,
                                        autopct='%1.1f%%', shadow=True, startangle=90,
                                        textprops={'fontsize': 12})
    ax1.set_title(f'Principal vs Interest Breakdown\nTotal: ₹{total:,.0f}', fontsize=14)

    wedges2, texts2, autotexts2 = ax2.pie(sizes, explode=explode, labels=labels, colors=colors,
                                           autopct=lambda pct: f'₹{pct*total/100:,.0f}',
                                           shadow=True, startangle=90,
                                           textprops={'fontsize': 10})
    centre_circle = plt.Circle((0, 0), 0.5, fc='white')
    ax2.add_patch(centre_circle)
    ax2.set_title(f'Amount Breakdown\nP=₹{principal:,}, R={rate}%, T={time}yrs', fontsize=14)

    plt.tight_layout()
    plt.show()

visualize_pie_chart(100000, 10, 5)
print("✅ Pie chart displayed!")


# In[15]:


class SimpleInterestCalculator:
    """Class for Simple Interest calculations"""

    def __init__(self, principal, rate, time, time_unit='years'):
        self.principal = principal
        self.rate = rate
        self.time = time
        self.time_unit = time_unit
        self.time_in_years = self._convert_time()
        self.simple_interest = self._calculate_si()
        self.total_amount = self.principal + self.simple_interest

    def _convert_time(self):
        """Convert time to years"""
        if self.time_unit == 'years':
            return self.time
        elif self.time_unit == 'months':
            return self.time / 12
        elif self.time_unit == 'days':
            return self.time / 365
        else:
            return self.time

    def _calculate_si(self):
        """Calculate Simple Interest"""
        return (self.principal * self.rate * self.time_in_years) / 100

    def get_interest(self):
        """Return Simple Interest"""
        return self.simple_interest

    def get_amount(self):
        """Return Total Amount"""
        return self.total_amount

    def get_monthly_interest(self):
        """Return monthly interest"""
        return self.simple_interest / (self.time_in_years * 12)

    def display(self):
        """Display all details"""
        print("\n" + "=" * 50)
        print("💰 SIMPLE INTEREST DETAILS")
        print("=" * 50)
        print(f"  Principal        : ₹{self.principal:>15,.2f}")
        print(f"  Rate             : {self.rate:>15.2f}%")
        print(f"  Time             : {self.time:>15.2f} {self.time_unit}")
        print(f"  Time (in years)  : {self.time_in_years:>15.2f}")
        print("-" * 50)
        print(f"  Simple Interest  : ₹{self.simple_interest:>15,.2f}")
        print(f"  Total Amount     : ₹{self.total_amount:>15,.2f}")
        print(f"  Monthly Interest : ₹{self.get_monthly_interest():>15,.2f}")
        print("=" * 50)

    def __str__(self):
        return f"SI(P=₹{self.principal:,}, R={self.rate}%, T={self.time} {self.time_unit}) = ₹{self.simple_interest:,.2f}"

calc1 = SimpleInterestCalculator(50000, 8, 3, 'years')
calc1.display()

calc2 = SimpleInterestCalculator(100000, 12, 18, 'months')
print(calc2)

calc3 = SimpleInterestCalculator(25000, 10, 180, 'days')
print(calc3)


# In[16]:


def calculate_loan_emi_flat(principal, rate, tenure_months):
    """
    Calculate EMI using Flat Rate (Simple Interest) method
    """

    tenure_years = tenure_months / 12
    total_interest = (principal * rate * tenure_years) / 100
    total_amount = principal + total_interest
    emi = total_amount / tenure_months

    print("\n🏦 LOAN EMI CALCULATOR (Flat Rate)")
    print("=" * 50)
    print(f"  Loan Amount        : ₹{principal:>15,.2f}")
    print(f"  Interest Rate      : {rate:>15.2f}%")
    print(f"  Tenure             : {tenure_months:>15} months")
    print("-" * 50)
    print(f"  Total Interest     : ₹{total_interest:>15,.2f}")
    print(f"  Total Amount       : ₹{total_amount:>15,.2f}")
    print(f"  Monthly EMI        : ₹{emi:>15,.2f}")
    print("=" * 50)

    return emi, total_interest, total_amount

emi, interest, total = calculate_loan_emi_flat(500000, 10, 36)


# In[17]:


def loan_repayment_schedule(principal, rate, tenure_months):
    """Generate loan repayment schedule"""

    tenure_years = tenure_months / 12
    total_interest = (principal * rate * tenure_years) / 100
    total_amount = principal + total_interest
    emi = total_amount / tenure_months
    monthly_principal = principal / tenure_months
    monthly_interest = total_interest / tenure_months

    print(f"\n📋 LOAN REPAYMENT SCHEDULE")
    print(f"   Loan: ₹{principal:,} | Rate: {rate}% | Tenure: {tenure_months} months")
    print(f"   EMI: ₹{emi:,.2f}")
    print("=" * 80)
    print(f"{'Month':<8} {'EMI':<15} {'Principal':<15} {'Interest':<15} {'Balance':<15}")
    print("-" * 80)

    balance = principal
    total_principal_paid = 0
    total_interest_paid = 0

    for month in range(1, min(tenure_months + 1, 13)):  # Show first 12 months
        balance -= monthly_principal
        total_principal_paid += monthly_principal
        total_interest_paid += monthly_interest

        print(f"{month:<8} ₹{emi:<14,.2f} ₹{monthly_principal:<14,.2f} ₹{monthly_interest:<14,.2f} ₹{max(0, balance):<14,.2f}")

    if tenure_months > 12:
        print(f"{'...':<8} {'...':<15} {'...':<15} {'...':<15} {'...':<15}")
        print(f"{tenure_months:<8} ₹{emi:<14,.2f} ₹{monthly_principal:<14,.2f} ₹{monthly_interest:<14,.2f} ₹{0:<14,.2f}")

    print("-" * 80)
    print(f"{'TOTAL':<8} ₹{total_amount:<14,.2f} ₹{principal:<14,.2f} ₹{total_interest:<14,.2f}")
    print("=" * 80)

loan_repayment_schedule(100000, 12, 24)


# In[18]:


def fd_calculator(principal, rate, tenure_months, payout='maturity'):
    """
    Fixed Deposit Calculator

    payout: 'maturity', 'monthly', 'quarterly', 'yearly'
    """

    tenure_years = tenure_months / 12
    total_interest = (principal * rate * tenure_years) / 100
    maturity_amount = principal + total_interest

    print("\n🏦 FIXED DEPOSIT CALCULATOR")
    print("=" * 50)
    print(f"  Deposit Amount     : ₹{principal:>15,.2f}")
    print(f"  Interest Rate      : {rate:>15.2f}%")
    print(f"  Tenure             : {tenure_months:>15} months")
    print(f"  Interest Payout    : {payout:>15}")
    print("-" * 50)

    if payout == 'maturity':
        print(f"  Interest Earned    : ₹{total_interest:>15,.2f}")
        print(f"  Maturity Amount    : ₹{maturity_amount:>15,.2f}")
    elif payout == 'monthly':
        monthly_interest = total_interest / tenure_months
        print(f"  Total Interest     : ₹{total_interest:>15,.2f}")
        print(f"  Monthly Payout     : ₹{monthly_interest:>15,.2f}")
        print(f"  Maturity (Principal): ₹{principal:>15,.2f}")
    elif payout == 'quarterly':
        quarterly_interest = total_interest / (tenure_months / 3)
        print(f"  Total Interest     : ₹{total_interest:>15,.2f}")
        print(f"  Quarterly Payout   : ₹{quarterly_interest:>15,.2f}")
        print(f"  Maturity (Principal): ₹{principal:>15,.2f}")
    elif payout == 'yearly':
        yearly_interest = (principal * rate) / 100
        print(f"  Total Interest     : ₹{total_interest:>15,.2f}")
        print(f"  Yearly Payout      : ₹{yearly_interest:>15,.2f}")
        print(f"  Maturity (Principal): ₹{principal:>15,.2f}")

    print("=" * 50)

    return maturity_amount, total_interest

print("📌 FD with different payout options:\n")

fd_calculator(500000, 7, 36, 'maturity')
fd_calculator(500000, 7, 36, 'monthly')
fd_calculator(500000, 7, 36, 'quarterly')


# In[19]:


def compare_investments(principal, years):
    """Compare returns from different investment options"""

    investments = {
        'Savings Account': 3.5,
        'Fixed Deposit': 6.5,
        'Recurring Deposit': 6.0,
        'Post Office Scheme': 7.1,
        'PPF': 7.1,
        'Corporate Bonds': 8.5,
        'Govt. Bonds': 7.0
    }

    print(f"\n📊 INVESTMENT COMPARISON")
    print(f"   Principal: ₹{principal:,} | Time: {years} years")
    print("=" * 70)
    print(f"{'Investment':<20} {'Rate':<10} {'Interest':<18} {'Maturity':<18}")
    print("-" * 70)

    results = []

    for name, rate in investments.items():
        si = (principal * rate * years) / 100
        total = principal + si
        results.append((name, rate, si, total))
        print(f"{name:<20} {rate:>6.1f}% {'':>2} ₹{si:>14,.2f} {'':>2} ₹{total:>14,.2f}")

    print("=" * 70)

    best = max(results, key=lambda x: x[2])
    print(f"\n✅ Best Option: {best[0]} with ₹{best[2]:,.2f} interest")

    return results

results = compare_investments(100000, 5)


# In[20]:


def interactive_si_calculator():
    """Interactive menu-driven SI calculator"""

    while True:
        print("\n" + "=" * 50)
        print("💰 SIMPLE INTEREST CALCULATOR - MENU")
        print("=" * 50)
        print("1. Calculate Simple Interest")
        print("2. Find Principal Amount")
        print("3. Find Interest Rate")
        print("4. Find Time Period")
        print("5. SI vs CI Comparison")
        print("6. Loan EMI Calculator")
        print("7. FD Calculator")
        print("8. Compare Investment Options")
        print("9. Generate Comparison Table")
        print("0. Exit")
        print("=" * 50)

        choice = input("\n👉 Enter your choice (0-9): ")

        if choice == '0':
            print("\n👋 Thank you for using SI Calculator! Goodbye!")
            break

        elif choice == '1':
            try:
                p = float(input("Enter Principal (₹): "))
                r = float(input("Enter Rate (%): "))
                t = float(input("Enter Time (years): "))

                si, total = calculate_si_and_amount(p, r, t)
                print(f"\n✅ Simple Interest: ₹{si:,.2f}")
                print(f"✅ Total Amount: ₹{total:,.2f}")
            except ValueError:
                print("❌ Invalid input!")

        elif choice == '2':
            try:
                si = float(input("Enter Simple Interest (₹): "))
                r = float(input("Enter Rate (%): "))
                t = float(input("Enter Time (years): "))

                p = find_principal(si, r, t)
                print(f"\n✅ Principal Amount: ₹{p:,.2f}")
            except ValueError:
                print("❌ Invalid input!")

        elif choice == '3':
            try:
                si = float(input("Enter Simple Interest (₹): "))
                p = float(input("Enter Principal (₹): "))
                t = float(input("Enter Time (years): "))

                r = find_rate(si, p, t)
                print(f"\n✅ Interest Rate: {r:.2f}%")
            except ValueError:
                print("❌ Invalid input!")

        elif choice == '4':
            try:
                si = float(input("Enter Simple Interest (₹): "))
                p = float(input("Enter Principal (₹): "))
                r = float(input("Enter Rate (%): "))

                t = find_time(si, p, r)
                print(f"\n✅ Time Period: {t:.2f} years")
            except ValueError:
                print("❌ Invalid input!")

        elif choice == '5':
            try:
                p = float(input("Enter Principal (₹): "))
                r = float(input("Enter Rate (%): "))
                t = int(input("Enter Time (years): "))

                compare_si_ci(p, r, t)
            except ValueError:
                print("❌ Invalid input!")

        elif choice == '6':
            try:
                p = float(input("Enter Loan Amount (₹): "))
                r = float(input("Enter Rate (%): "))
                t = int(input("Enter Tenure (months): "))

                calculate_loan_emi_flat(p, r, t)
            except ValueError:
                print("❌ Invalid input!")

        elif choice == '7':
            try:
                p = float(input("Enter Deposit Amount (₹): "))
                r = float(input("Enter Rate (%): "))
                t = int(input("Enter Tenure (months): "))

                fd_calculator(p, r, t)
            except ValueError:
                print("❌ Invalid input!")

        elif choice == '8':
            try:
                p = float(input("Enter Principal (₹): "))
                t = int(input("Enter Time (years): "))

                compare_investments(p, t)
            except ValueError:
                print("❌ Invalid input!")

        elif choice == '9':
            try:
                p = float(input("Enter Principal (₹): "))
                r = float(input("Enter Rate (%): "))
                t = int(input("Enter Max Years: "))

                si_ci_comparison_table(p, r, t)
            except ValueError:
                print("❌ Invalid input!")

        else:
            print("❌ Invalid choice! Please try again.")

        input("\n⏎ Press Enter to continue...")

print("✅ Interactive calculator ready! Call interactive_si_calculator() to start.")


# In[22]:


si = lambda p, r, t: (p * r * t) / 100

amount = lambda p, r, t: p + (p * r * t) / 100

principal = lambda si, r, t: (si * 100) / (r * t)

rate = lambda si, p, t: (si * 100) / (p * t)

time = lambda si, p, r: (si * 100) / (p * r)

ci = lambda p, r, t: p * ((1 + r/100) ** t) - p

print("⚡ QUICK ONE-LINER CALCULATIONS:\n")
print(f"SI on ₹10,000 at 5% for 2 years  : ₹{si(10000, 5, 2):,.2f}")
print(f"Amount for ₹50,000 at 8% for 3yr : ₹{amount(50000, 8, 3):,.2f}")
print(f"Principal for SI ₹5000, R=10%, T=2: ₹{principal(5000, 10, 2):,.2f}")
print(f"Rate for SI ₹3000, P=₹25000, T=2 : {rate(3000, 25000, 2):.2f}%")
print(f"Time for SI ₹6000, P=₹20000, R=10: {time(6000, 20000, 10):.2f} years")


# In[23]:


import csv
def export_si_to_csv(principal, rate, max_years, filename='simple_interest.csv'):
    """Export SI calculations to CSV file"""

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['Year', 'Principal', 'Rate (%)', 'Interest', 'Total Amount'])

        for year in range(1, max_years + 1):
            si = (principal * rate * year) / 100
            total = principal + si
            writer.writerow([year, principal, rate, f"{si:.2f}", f"{total:.2f}"])

    print(f"✅ Data exported to '{filename}'")

export_si_to_csv(100000, 10, 10, 'si_report.csv')


# In[24]:


def real_world_examples():
    """Show real-world SI calculation examples"""

    print("\n" + "=" * 60)
    print("🌍 REAL-WORLD SIMPLE INTEREST EXAMPLES")
    print("=" * 60)

    print("\n📌 Example 1: Bank Fixed Deposit")
    print("-" * 50)
    p, r, t = 200000, 6.5, 2
    si = (p * r * t) / 100
    print(f"   Deposit: ₹{p:,} at {r}% for {t} years")
    print(f"   Interest: ₹{si:,.2f}")
    print(f"   Maturity: ₹{p + si:,.2f}")

    print("\n📌 Example 2: Car Loan (Flat Rate)")
    print("-" * 50)
    p, r, t = 500000, 9, 5
    si = (p * r * t) / 100
    emi = (p + si) / (t * 12)
    print(f"   Loan: ₹{p:,} at {r}% for {t} years")
    print(f"   Total Interest: ₹{si:,.2f}")
    print(f"   Monthly EMI: ₹{emi:,.2f}")
    print(f"   Total Payment: ₹{p + si:,.2f}")

    print("\n📌 Example 3: Personal Loan")
    print("-" * 50)
    p, r, t_months = 100000, 14, 24
    t_years = t_months / 12
    si = (p * r * t_years) / 100
    emi = (p + si) / t_months
    print(f"   Loan: ₹{p:,} at {r}% for {t_months} months")
    print(f"   Total Interest: ₹{si:,.2f}")
    print(f"   Monthly EMI: ₹{emi:,.2f}")

    print("\n📌 Example 4: Treasury Bills (91 days)")
    print("-" * 50)
    p, r, t_days = 100000, 6.5, 91
    t_years = t_days / 365
    si = (p * r * t_years) / 100
    print(f"   Investment: ₹{p:,} at {r}% for {t_days} days")
    print(f"   Interest: ₹{si:,.2f}")
    print(f"   Maturity: ₹{p + si:,.2f}")

    print("\n📌 Example 5: Education Loan")
    print("-" * 50)
    p, r, t = 1000000, 8.5, 7
    si = (p * r * t) / 100
    print(f"   Loan: ₹{p:,} at {r}% for {t} years")
    print(f"   Total Interest: ₹{si:,.2f}")
    print(f"   Total Repayment: ₹{p + si:,.2f}")

    print("\n" + "=" * 60)

real_world_examples()


# In[25]:


def print_summary():
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    💰 SIMPLE INTEREST - QUICK REFERENCE                      ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  📐 FORMULAS:                                                                ║
║  ────────────────────────────────────────────────────────────────────────    ║
║  │ Simple Interest    : SI = (P × R × T) / 100                          │    ║
║  │ Total Amount       : A = P + SI                                      │    ║
║  │ Find Principal     : P = (SI × 100) / (R × T)                        │    ║
║  │ Find Rate          : R = (SI × 100) / (P × T)                        │    ║
║  │ Find Time          : T = (SI × 100) / (P × R)                        │    ║
║  └──────────────────────────────────────────────────────────────────────┘    ║
║                                                                              ║
║  📝 WHERE:                                                                   ║
║     P = Principal (Initial Amount)                                           ║
║     R = Rate of Interest (% per annum)                                       ║
║     T = Time Period (in years)                                               ║
║     SI = Simple Interest                                                     ║
║     A = Total Amount (Maturity Value)                                        ║
║                                                                              ║
║  ⏰ TIME CONVERSIONS:                                                        ║
║     • Months to Years: T = months / 12                                       ║
║     • Days to Years  : T = days / 365                                        ║
║                                                                              ║
║  📊 QUICK EXAMPLES:                                                          ║
║     • ₹10,000 at 10% for 2 years: SI = ₹2,000                               ║
║     • ₹50,000 at 8% for 3 years : SI = ₹12,000                              ║
║     • ₹1,00,000 at 12% for 5 yrs: SI = ₹60,000                              ║
║                                                                              ║
║  💡 KEY POINTS:                                                              ║
║     • Interest is calculated only on principal                               ║
║     • Interest remains same every year                                       ║
║     • Simpler than compound interest                                         ║
║     • Used in: FDs, Loans (flat rate), Treasury Bills                       ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
""")

print_summary()

