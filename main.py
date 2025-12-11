from queries import (
    insert_expense,
    insert_detail,
    insert_income,
    update_expense_amount,
    delete_expense,
    list_expenses,
    get_expense_with_details,
    get_monthly_summary,
    get_expenses_in_range,
)


def main():
    print("=== Expense Tracker Demo ===\n")

    # INSERT DEMO -----------------------------
    print("Inserting sample expense...")
    exp_id = insert_expense("2025-01-10", 500.00, "Cash", "Groceries", "Walmart")
    insert_detail(exp_id, 1, 300.00, "Chicken, Bread")
    insert_detail(exp_id, 2, 200.00, "Cleaning supplies")
    print(f"Expense inserted with ID: {exp_id}\n")

    print("Inserting income...")
    insert_income("2025-01-05", 2000.00, "Salary")
    print("Income inserted.\n")

    # UPDATE DEMO -----------------------------
    print("Updating expense amount...")
    update_expense_amount(exp_id, 550.00)
    print("Expense updated.\n")

    # JOIN DEMO -----------------------------
    print("Fetching expense with details...")
    rows = get_expense_with_details(exp_id)
    for r in rows:
        print(r)
    print()

    # AGGREGATE DEMO -----------------------------
    print("Monthly summary for January 2025:")
    summary = get_monthly_summary(2025, 1)
    print(summary)
    print()

    # DATE RANGE -----------------------------
    print("Expenses between Jan 1–15:")
    rng = get_expenses_in_range("2025-01-01", "2025-01-15")
    for r in rng:
        print(r)
    print()

    # DELETE DEMO -----------------------------
    print("Deleting expense...")
    delete_expense(exp_id)
    print("Expense deleted.\n")

    # FINAL LIST -----------------------------
    print("Current expenses:")
    for r in list_expenses():
        print(r)


if __name__ == "__main__":
    main()
