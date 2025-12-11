CREATE TABLE IF NOT EXISTS expenses (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    amount NUMERIC(10,2) NOT NULL,
    payment_method TEXT NOT NULL,
    category TEXT NOT NULL,
    store TEXT
);

CREATE TABLE IF NOT EXISTS details (
    id SERIAL PRIMARY KEY,
    expense_id INT NOT NULL,
    line_number INT NOT NULL,
    amount NUMERIC(10,2) NOT NULL,
    description TEXT NOT NULL,
    CONSTRAINT fk_expense
      FOREIGN KEY(expense_id) REFERENCES expenses(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS income (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    amount NUMERIC(10,2) NOT NULL,
    description TEXT
);
