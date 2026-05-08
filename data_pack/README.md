# Data Pack — Askari Bank AI/ML Internship Assessment

This ZIP contains everything you need for the 90-minute assessment.

## Files

| File | What it is |
|---|---|
| `transactions.csv` | ~740 rows of account activity across 30 customers, Oct 2025 – Mar 2026 |
| `customer_profiles.csv` | 30 customer profiles — occupation, declared income, city, account type, KYC dates |
| `askari_products.pdf` | 3 Askari Bank product sheets |
| `complaint_email.txt` | A customer complaint email |
| `isolation_forest_explainer.pdf` | One-page primer for Task 5 |

## Column reference

**transactions.csv**
- `txn_id` — unique transaction ID
- `customer_id` — links to customer_profiles.csv
- `datetime` — YYYY-MM-DD HH:MM local Pakistan time
- `amount_pkr` — transaction value in PKR
- `txn_type` — one of: cash_deposit, cash_withdrawal, transfer_in, transfer_out, card_purchase, bill_payment, cheque_withdrawal
- `channel` — one of: branch, ATM, internet_banking, mobile_app, POS, system
- `city` — where the transaction took place
- `counterparty` — who the money came from or went to (where applicable)
- `note` — free-text note

**customer_profiles.csv**
- `customer_id` — primary key
- `name`, `occupation`, `declared_monthly_income_pkr`
- `account_open_date`, `account_type`, `city`, `age`
- `cnic_last_4` — last 4 digits of CNIC (synthetic, for reference only)
- `kyc_refresh_date` — most recent KYC review

## Notes

- All data is synthetic. Names, amounts, CNIC fragments are fictional.
- Profit rates and fees in the product sheets are illustrative.
- There is no hidden answer key for the task questions. We are grading how you work, not whether you match a specific "correct" answer.

Good luck.
