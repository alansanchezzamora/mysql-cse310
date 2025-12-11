from db import get_connection

# ------------------------------
# INSERT FUNCTIONS
# ------------------------------


def insert_expense(date, amount, payment_method, category, store):
    """
    Inserts a new row into the expenses table.
    """
    query = """
        INSERT INTO expenses (date, amount, payment_method, category, store)
        VALUES (%s, %s, %s, %s, %s) RETURNING id;
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, (date, amount, payment_method, category, store))
    expense_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return expense_id


def insert_detail(expense_id, line_number, amount, description):
    """
    Inserts a new line item associated with an expense.
    """
    query = """
        INSERT INTO details (expense_id, line_number, amount, description)
        VALUES (%s, %s, %s, %s);
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, (expense_id, line_number, amount, description))
    conn.commit()
    cur.close()
    conn.close()


def insert_income(date, amount, description):
    """
    Inserts a new income entry.
    """
    query = """
        INSERT INTO income (date, amount, description)
        VALUES (%s, %s, %s);
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, (date, amount, description))
    conn.commit()
    cur.close()
    conn.close()


# ------------------------------
# UPDATE FUNCTION
# ------------------------------


def update_expense_amount(expense_id, new_amount):
    """
    Updates the amount of a specific expense.
    """
    query = "UPDATE expenses SET amount = %s WHERE id = %s;"
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, (new_amount, expense_id))
    conn.commit()
    cur.close()
    conn.close()


# ------------------------------
# DELETE FUNCTION
# ------------------------------


def delete_expense(expense_id):
    """
    Deletes an expense and its associated details.
    """
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM details WHERE expense_id = %s;", (expense_id,))
    cur.execute("DELETE FROM expenses WHERE id = %s;", (expense_id,))

    conn.commit()
    cur.close()
    conn.close()


# ------------------------------
# SELECT (BASIC QUERY)
# ------------------------------


def list_expenses():
    """
    Returns all expenses.
    """
    query = "SELECT * FROM expenses ORDER BY date DESC;"
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


# ------------------------------
# JOIN BETWEEN expenses + details
# ------------------------------


def get_expense_with_details(expense_id):
    """
    Returns an expense and all its detail line items.
    """
    query = """
        SELECT e.id, e.date, e.amount, e.store,
               d.line_number, d.amount, d.description
        FROM expenses e
        JOIN details d ON e.id = d.expense_id
        WHERE e.id = %s
        ORDER BY d.line_number;
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, (expense_id,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


# ------------------------------
# AGGREGATES
# ------------------------------


def get_monthly_summary(year, month):
    """
    Returns SUM(income) and SUM(expenses) for a given month.
    """
    query_exp = """
        SELECT COALESCE(SUM(amount), 0)
        FROM expenses
        WHERE EXTRACT(YEAR FROM date) = %s
          AND EXTRACT(MONTH FROM date) = %s;
    """

    query_inc = """
        SELECT COALESCE(SUM(amount), 0)
        FROM income
        WHERE EXTRACT(YEAR FROM date) = %s
          AND EXTRACT(MONTH FROM date) = %s;
    """

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(query_exp, (year, month))
    total_expenses = cur.fetchone()[0]

    cur.execute(query_inc, (year, month))
    total_income = cur.fetchone()[0]

    cur.close()
    conn.close()

    return {
        "income": total_income,
        "expenses": total_expenses,
        "net": total_income - total_expenses,
    }


# ------------------------------
# DATE RANGE FILTER
# ------------------------------


def get_expenses_in_range(start_date, end_date):
    """
    Returns all expenses between two dates.
    """
    query = """
        SELECT *
        FROM expenses
        WHERE date BETWEEN %s AND %s
        ORDER BY date;
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, (start_date, end_date))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
