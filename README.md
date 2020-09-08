# Credit Limit

## Things implemented
- The said functionalities were implemented
- OCA module web_notify is referenced to notify user when exceeding the credit limit

## What to do when payment made
When a payment is made we should check all orders with `credit_limit_block == True` and `state in ['draft', 'sent']` to the partner. For performance I would like to make this feature asynchronous, like with help of the OCA module queue_job.

Furthermore I think we should do the check as well, when `credit_limit` is changed. when we edit a sale order, like remove some products, as well.
