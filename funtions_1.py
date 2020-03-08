def computepay(hours, rate):
  if hours>40:
    excess=(hours-40)
    answer=(40*rate)+(excess*(rate*1.5))
  else:
    answer=hours*rate
  return answer

x=input("Enter Hours: ")
y=input("Enter Rate: ")
hours=float(x)
rate=float(y)

z=computepay(hours, rate)

print("Pay:", z)
