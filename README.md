# Wallet
Automated data entry for Wallet (by BudgetBakers) webapp using Selenium

## Overview
This script allows quicker data entry to the Wallet webapp by collecting record data into a csv file.

### Sample Demo
![Sample Demo](./assets/wallet-sample-demo.gif)

### Data Input
Bulk of transaction data should be stored in a csv file with the following columns:
| Column | Details |
| --- | --- |
| type | options: Expense, Income, or Transfer |
| account | [Account](https://web.budgetbakers.com/accounts)¹ |
| date | format: "Mmm DD, YYYY" |
| time | format "H:MM PM" |
| amount | `number` |
| currency | *Currency (PHP/USD/etc) |
| payee | `string`|
| note | `string` |
| payType | Payment Type² |
| payStatus | options: Cleared, Uncleared, or Reconciled |
| category | Wallet-defined [Category](https://web.budgetbakers.com/settings/categories)³ |
| labels | User-defined [Label](https://web.budgetbakers.com/settings/labels)⁴|

**NOTES**  
¹ User-defined Account name (case-sensitive)  
² options: Cash, Debit card, Credit card, Transfer, Voucher, Mobile payment, Web payment  
³ Default or user-defined Category (case-sensitive), add `" "` if contains comma  
⁴ User-defined labels, add `" "` for multiple, comma-separated values  
 

## Setup
### Dependencies
This repo uses `venv` to manage python packages.

**Running Virtual Environment**  
On root, run `python -m venv .venv` to setup virtual environment.

Then, activate the virtual environment:  
*For Windows*
```bash
.venv\scripts\activate
```

*For Linux/Mac*
```bash
source .venv/scripts/activate
```

To deactivate:
```bash
deactivate
```

**Installing Packages**  
Install using the requirements.txt file  
```
pip install -r requirements.txt
```

### Credentials
This repo uses the `python-dotenv` libraries to manage Wallet login credentials.  
Create `.env` file on root, with the following contents:  
```env
APP_USERNAME=foo@bar.com
APP_PASSWORD=password

```

### Usage 
1. Run the script using  `python src/main.py`.
2. When prompted, enter the filepath of the csv file.