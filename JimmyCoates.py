import random
def main():
  print "Hello Master\n"
  jimmyAssassin = ""
  index = random.randint(0,100)
  #based on the books. He has a 30 % to ignore his program completely
  #change 30 to a higher number if you want to include the times when he ignores his program paritially.
  if (index < 30):
    jimmyAssassin = "Yes"
  else:
    jimmyAssassin = "No"
  print (jimmyAssassin)
  print "\nGoodbye Master\n"
main()
