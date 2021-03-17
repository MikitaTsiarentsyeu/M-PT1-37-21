deposite = 20000
rate = 0.15
months = 12
years = 5 
total = deposite * ((1 + rate / months ) ** (months * years))
print(round(total))