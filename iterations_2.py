smallest=None
largest=None

while True:
  x=input("Enter a number: ")
  try:
    value=int(x)
    if smallest is None or largest is None:
      smallest=value
      largest=value
    elif value<smallest:
      smallest=value
    elif value>largest:
      largest=value
  except:
    if x=="done":
      break
    else:
      print("Invalid input")
      continue

print("Minimum:", smallest)
print("Maximum:", largest)
