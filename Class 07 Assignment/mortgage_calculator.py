import streamlit as st
import pandas as pd
import math

def calculate_mortgage():
    st.title("Mortgage Repayments Calculator")

    st.write("### Input Data")
    col1, col2 = st.columns(2)
    home_value = col1.number_input("Home Value", min_value=0, value=500000)
    deposit = col1.number_input("Deposit", min_value=0, value=100000)
    interest_rate = col2.number_input("Interest Rate (in %)", min_value=0.0, value=5.5)
    loan_term = col2.number_input("Loan Term (in years)", min_value=1, value=30)

    # Calculations
    loan_amount = home_value - deposit
    monthly_rate = (interest_rate / 100) / 12
    months = loan_term * 12
    
    if monthly_rate > 0:
        monthly_payment = (loan_amount * monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
    else:  # Handle 0% interest case
        monthly_payment = loan_amount / months

    # Display results
    st.write("### Repayments")
    col1, col2, col3 = st.columns(3)
    col1.metric("Monthly Payment", f"${monthly_payment:,.2f}")
    col2.metric("Total Payments", f"${monthly_payment * months:,.0f}")
    col3.metric("Total Interest", f"${monthly_payment * months - loan_amount:,.0f}")

    # Generate amortization schedule
    balance = loan_amount
    schedule = []
    for month in range(1, months + 1):
        interest = balance * monthly_rate
        principal = monthly_payment - interest
        balance -= principal
        schedule.append({
            "Month": month,
            "Payment": monthly_payment,
            "Principal": principal,
            "Interest": interest,
            "Balance": max(balance, 0),  # Prevent negative balance
            "Year": math.ceil(month / 12)
        })

    # Show amortization chart
    st.write("### Payment Schedule")
    df = pd.DataFrame(schedule)
    yearly_balance = df.groupby("Year")["Balance"].min()
    st.line_chart(yearly_balance)

if __name__ == "__main__":
    calculate_mortgage()
