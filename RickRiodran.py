#Rick Riordan Recommendations
def main():
  print "Hello Reader!\n"
  print "Please use y, Y, n, N for your answers"
  start = raw_input("Do you like Greek and Roman Mythology?  ")
  if (start.lower() == "y"):
    politics = raw_input("Do you consider yourself more liberal/left-leaning?  ")
    if (politics.lower() == "y"):
      print("You should read the Trials of Apollo")
    else:
      age = raw_input("Do you like smaller books?  ")
      if (age.lower() == "y"):
        print("You should read Percy Jackson and the Olympians")
      else:
        print("You should read Heroes of Olympus")
  else:
    egypt = raw_input("Do you prefer it when the characters don't have magical parents?  ")
    if (egypt.lower() == "y"):
      print("You should read the Kane Chronicles")
    else:
      print("You should read the Magnus Chase and the Gods of Asgard")
  print "Goodbye Master\n"
main()
