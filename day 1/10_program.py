"""The flight ticket rates for a round-trip(Mumbai-Dubai) were as follows:
Rate per Adult: Rs. 37550.0
Rate per Child: 1/3rd of the rate per adult
Service Tax: 7% of the ticket amount (including all passengers) As it was a holiday season,
the airline also offered 10% discount on the final ticket cost(after inclusion of the service tax).
Find and display the total ticket cost for a group which had adults and children.

Sample input:                                                           Expected output:
Number of adults                                                       Number of children
       5                                                                           2         Total ticket cost:204910.35
       3                                                                           1         Total ticket cost: 120535.5  """


n_adults=int(input("Enter the number of adults"))
n_children=int(input("Enter the number of children"))
total=((n_adults*37550.0)+(n_children*37550.0))
print(total)
total1=total*0.07
total2=total+total1
print("with ur setrvice text",total2)

total_amount=total2*0.90
print(total_amount)

      
