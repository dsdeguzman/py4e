def computegrade(score):
  if score <0.0 or score>1.0:
    print("Bad Score")
    quit()
  elif score>=0.9:
    grade="A"
  elif score>=0.8:
    grade="B"
  elif score>=0.7:
    grade="C"
  elif score>=0.6:
    grade="D"
  elif score<0.6:
    grade="F"
  return grade

x=input("Enter Score: ")
try:
  score=float(x)
except:
  print("Bad Score")
  quit()

z=computegrade(score)
print("Grade: ", z)
