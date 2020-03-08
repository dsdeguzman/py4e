number=0
total=0
while True:
  x=input("Enter a number: ")
  try:
    value=int(x)
  except:
    if x=="done":
      break
    else:
      print("Invalid input")
      continue
  number=number+1
  total=total+value

print(total, number, total/number)
