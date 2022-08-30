INVENTORY MANAGEMENT SYSTEM

This software can be used in any sales unit where products are stocked and sold to customers.

This software will work with an input device that can read and write product barcode. If the product does not
have a barcode, then the user must assign a unique id to each product. This necessary for this software to work.

THE SOFTWARE CAN:
1. create stock record.
2. create sales record.
3. display sales details
4. calculate the following:
  a. Quantity of product sold
  b. Profit and loss
  c. Quantity of product remaining in stock
  d. Total amount of product sold
  e. ...etc
5. It can detect expired product in which case sales details will not be displayed

6. The sales summary contains:
  a. Product name
  b. quantity of each product bought/sold
  c. Selling price per product
  d. Total quantity bought/sold.
  e. Total cost of product bought/sold  

The user have no need to do any calculations by themselves. Once the barcode of a product is read the software automatically displays the details of the product stored in the stock file. At the end of sales after all barcode have been read, a summary of sales details is displayed for the user to conclude sale with buyer.

When barcode scanner reads the barcode of a product it matches it with product details in the stock file and then displays product information for user to make a decision. If the barcode number matches with product details recorded in the stock file and the current date is not equal to the expiration date of the product then product information is displayed, else a message is displayed to warn seller that product is either out of stock or expired. In which case an expired product file is immediately created by the program.



THINGS TO ADD CODE:

a. include a function to edit stock record in case of error, this can mean deleting and reentering
an item.
b. do same for sales record -- create a function to delete sales entering incase of error.

If these functionality are add it will enable the business owner to monitor business where ever they are.
c. Enable sms/email alert to be sent everytime:

1. A sale is made -- send a copy of sales details
2. Product is stocked -- creates and sends a copy of stock record
3. Expired/damaged product -- sends a copy of record when expired product is detected or a damaged
product is recorded.

 



WORK IN PROGRESS.......


