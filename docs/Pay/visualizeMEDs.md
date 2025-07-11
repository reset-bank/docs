# How to visualize MEDs
## Prerequisites
- Have a **registered user** with an **active account** (refer to [Account Registration for API Usage](accountRegistration.md)).

---

Users will be able to view cases with MED status set to awaiting payment, paid, or rejected, as shown in the screenshot below.

![][image1]

To do so, simply:

1. Navigate to **Pix > Payments**
2. Apply a filter.
3. Select the "**Refund**" (Estorno) method
4. Clear the "Status" filters to see all cases, regardless of their status.

![][image2]

The possible statuses for a Pix MED (refund) are as follows:

- **Awaiting Payment** (Pendente): The amount is locked in the user's account while the request is under review.

- **Paid** (Pago): If the defense is unsuccessful, the amount is refunded to the claimant.

- **Rejected** (Rejeitado): The refund request was denied, and the amount is released back to the user (i.e., it is not refunded to the claimant). _This status label may be slightly ambiguous but refers to the rejection of the refund request_.


[image1]: /docs/images/Pay/meds/meds-1.png
[image2]: /docs/images/Pay/meds/meds-2.png