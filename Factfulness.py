import os
import random
def main():
  print "Hello Master"
  list1 = []
  #generate a list of random integers
  #can import a list or change to rational numbers to be more accurate
  for i in range (0, 100):
    num1 =  random.randint(-100,100)
    list1.append(num1)
  #i am sorting them to create the illusion of time with the fake/randomized data
  #because if the list is too random, then the final calculations won't be much use
  list1.sort()
  pos_nums = 0
  neg_nums = 0
  slope = 0
  for i in range (0, 100):
    if (list1[i] < 0):
      neg_nums += 1
    if (list1[i] >= 0):
      pos_nums += 1
    #avoiding the index outbounds error
    if (i < 99):
      #assuming after sorting that it is 1 unit
      slope = slope + ((list1[i+1] - list1[i])/2)
  print "The stats are  \n"
  if (neg_nums > pos_nums):
    print "Mostly negative numbers"
  if (pos_nums > neg_nums):
    print "Mostly positive numbers"
  print "Average Slope is ", slope

  #next step will be able to do this a real array/array
main()
