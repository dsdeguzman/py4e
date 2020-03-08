x=input("Enter Hours: ")
y=input("Enter Rate: ")
hours=float(x)
rate=float(y)
if hours>40:
  excess=(hours-40)
  answer=(40*rate)+(excess*(rate*1.5))
else:
  answer=hours*rate
print("Pay:",answer)
