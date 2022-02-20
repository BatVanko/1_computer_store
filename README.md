# 1_computer_store
1.	Computer Store
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2517#0.

Write a program that prints you a receipt for your new computer. You will receive the parts' prices (without tax) until you receive what type of customer this is - special or regular. Once you receive the type of customer you should print the receipt.
The taxes are 20% of each part's price you receive. 
If the customer is special, he has a 10% discount on the total price with taxes.
If a given price is not a positive number, you should print "Invalid price!" on the console and continue with the next price.
If the total price is equal to zero, you should print "Invalid order!" on the console.
Input
•	You will receive numbers representing prices (without tax) until command "special" or "regular":
Output
•	The receipt should be in the following format: 
"Congratulations you've just bought a new computer!
Price without taxes: {total price without taxes}$
Taxes: {total amount of taxes}$
-----------
Total price: {total price with taxes}$"
Note: All prices should be displayed to the second digit after the decimal point! The discount is applied only on the total price. Discount is only applicable to the final price!

Input
1050
200
450
2
18.50 
16.86 
special

Output
Congratulations you've just bought a new computer!
Price without taxes: 1737.36$
Taxes: 347.47$
-----------
Total price: 1876.35$
1050 – valid price, total 1050
200 – valid price, total 1250
…
16.86 – valid price, total 1737.36
We receive special
Price is positive number, so it is valid order 
Price without taxes is 1737.36
Taxes: 20% from 1737.36 = 347.47
Final price = 1737.36 + 347.47 = 2084.83
Additional 10% discount for special customers
2084.83 – 10% = 1876.35 


