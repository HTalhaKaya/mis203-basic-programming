# Week 3 Lab: Order Approval Policy

### Test Table (Boundary Cases)
| Case | Order Amount | Available Stock | Requested Qty | Member? | Expected Result |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Below 500 | 499 TRY | 10 | 2 | Yes | Approved, No discount (Final: 499 TRY) |
| Exact 500 | 500 TRY | 10 | 2 | Yes | Approved, 10% discount (Final: 450 TRY) |
| Above 500 | 501 TRY | 10 | 2 | Yes | Approved, 10% discount (Final: 450.90 TRY) |

### Test & Reflection Note
- **One test I ran:** Tested with order_amount = 500, available_stock = 5, requested_qty = 1, is_member = yes.
- **One thing I changed after testing:** Changed the condition from `order_amount > 500` to `order_amount >= 500` to include exactly 500 TRY in the discount logic.
