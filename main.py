import time
import numpy as np
print ("Welcome to the Average and Percentiles Calculator")
time.sleep (1)

def start():
  while True:
    dataset = []
    n = int()
    n = int(input("Enter number of elements : "))
    print ("Please enter dataset here (Numbers only, one number at a time)")
    for i in range(0, n):
      ele = int(input())
      dataset.append(ele)
    time.sleep (1)
    print (dataset)
    time.sleep (1)
    while True:
      print ("Is the data correct (Y/N)")
      correct = input().upper()
      if correct == "Y":
        time.sleep (1)
        print ("Data accepted")
        menu(dataset)
      elif correct == "N":
        time.sleep (1)
        print ("Please try again")
        time.sleep (1)
        start()
      else:
        time.sleep (1)
        print ("Invalid input")



def reset(dataset):
  time.sleep (1)
  print ("Would you like to restart (Y/N)")
  while True:
    choice = input().upper()
    if choice == "Y":
      time.sleep(1)
      print ("Would you like to start from the beginning (Y) or use the same dataset (N)")
      while True:
        choice = input().upper()
        if choice == "Y":
          start()
          return
        elif choice == "N":
          menu(dataset)
          return
        else:
          print ("Invalid input")
    elif choice == "N":
      time.sleep (1)
      print ("Thank you for using the Averages and Percentiles calculator")
      time.sleep (3)
      exit()
    else:
      print ("Invalid input")

def menu(dataset):
  time.sleep (1)
  print ("What would you like to calculate?")
  print ("Mean (M), Median (MD), 25th percentile (25P), 75th percentile (75P), Standard Deviation (STD), Variance (V)")
  while True:
    choice = input().upper()
    if choice == "M":
      mean(dataset)
      return
    elif choice == "MD":
      median(dataset)
      return
    elif choice == "25P":
      percentile25(dataset)
      return
    elif choice == "75P":
      percentile75(dataset)
      return
    elif choice == "STD":
      standard(dataset)
      return
    elif choice == "V":
      variance(dataset)
      return
    else:
      print ("Invalid input")

def mean(dataset):
  time.sleep (1)
  print ("Mean:",np.mean(dataset))
  time.sleep(1)
  reset(dataset)
  
def median(dataset):
  time.sleep (1)
  print ("Median (50th percentile):",np.percentile(dataset, 50))
  time.sleep (1)
  reset(dataset)
  
def percentile25(dataset):
  time.sleep (1)
  print ("25th Percentile:",np.percentile(dataset, 25))
  time.sleep (1)
  reset(dataset)
  
def percentile75(dataset):
  time.sleep (1)
  print ("75th Percentile:",np.percentile(dataset, 75))
  time.sleep (1)
  reset(dataset)
  
def standard(dataset):
  time.sleep (1)
  print ("Standard deviation:",np.std(dataset))
  time.sleep (1)
  reset(dataset)
  
def variance(dataset):
  time.sleep (1)
  print ("Variance:",np.var(dataset))
  time.sleep (1)
  reset(dataset)

start()