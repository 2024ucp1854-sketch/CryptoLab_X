# Hospital Management System
# Test Cases - Lab Assignment 3

## Functional Test Cases

| ID | Test Case | Input | Expected Result |
|---|---|---|---|
| TC01 | Admin Login | admin / admin123 | Admin dashboard displayed |
| TC02 | Doctor Login | doctor / doctor123 | Doctor dashboard displayed |
| TC03 | Patient Login | patient / patient123 | Patient dashboard displayed |
| TC04 | Patient Registration | Valid patient details | Patient registered |
| TC05 | Patient Search | Existing patient name | Patient details displayed |
| TC06 | Book Appointment | Valid appointment data | Appointment created |
| TC07 | Add Prescription | Valid prescription data | Prescription created |
| TC08 | Create Bill | Valid bill data | Bill created |
| TC09 | Upload Report | Valid report | Report uploaded |
| TC10 | Download Report | Existing filename | Report displayed |

---

# Security Test Cases

## TC11 - SQL Injection

### Objective

Test whether user input can modify an SQL query.

### Location

Patient Search / Login

### Input

```text
' OR '1'='1