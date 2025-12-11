# mysql-cse310

Documentation for setting up PostgreSQL locally and with AWS RDS.

CSE310 - Sprint 3 project (EXPENSE TRACKER)
https://youtu.be/FVmhGH6UuI0
This project is an Expense Tracker App that allows users to:

- Add daily expenses
- Modify or delete existing expenses
- Retrieve expenses
- View summary reports using aggregates
- Filter expenses by date range
- Use multiple tables with JOIN

PostgreSQL Setup Guide (Local + RDS)

Full Step-by-Step Documentation

🐘 Overview

1️⃣ Install PostgreSQL Locally on Windows
Step 1 — Download PostgreSQL

Download PostgreSQL (version 18 or the latest) from:
https://www.postgresql.org/download/windows/

Add : Command Line Tools

Username: alan

Password: alan

Port: 5432

Locale: default

2️⃣ Verify Installation

Check version
psql --version

If you see something like:

psql (PostgreSQL) 18.1

Then it is installed correctly.

3️⃣ Add PostgreSQL to the System PATH

If you get errors running psql inside VS Code, ensure PATH is configured.

Open PowerShell as Administrator
setx /M PATH "$((Get-ChildItem Env:Path).Value);C:\Program Files\PostgreSQL\18\bin"

Close VS Code → Reopen it.

Test again:
psql --version

4️⃣ Connect to Your Local PostgreSQL

Open PowerShell:

psql -U postgres

It will ask for your password (the one you set during installation).

If connection succeeds, you will see:

psql (18.x)
Type "help" for help.

5️⃣ Connect to your AWS RDS PostgreSQL
Step A — In AWS RDS, modify your DB instance:

Set Public Access = Yes

Add inbound rule in the security group:

Type: PostgreSQL

Port: 5432

Source: Your IP (check your IP on checkip.amazonaws.com)

Step B — Get your RDS endpoint

Example:

mydb.abc123xyz.us-east-1.rds.amazonaws.com

Step C — Connect from your laptop
psql -h <your-rds-endpoint> -U postgres -d postgres

Example:

psql -h mydb.abc123xyz.us-east-1.rds.amazonaws.com -U postgres -d postgres
