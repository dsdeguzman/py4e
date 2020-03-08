x=input("Enter Hours: ")
try:
  hours=float(x)
except:
  print("Error, please enter numeric input")
  quit()

y=input("Enter Rate: ")
try:
  rate=float(y)
except:
  print("Error, please enter numeric input")
  quit()
#print("Computation:", hours, "*", rate)
if hours>40:
  excess=(hours-40)
  answer=(40*rate)+(excess*(rate*1.5))
else:
  answer=hours*rate
print("Pay:",answer)
