#socrates euthyphro relies on breaking logic loops in the audience
#Personally easier to think about it in terms on trendiness
#missing an arguement about Problem of Abhorrent Commands, but you can just think of some annoying vlogs or websites for that
def main():
  print "Hello Reader!\n"
  print "Please use y, Y, n, N for your answers"
  #a = nature to be loved
  #b = loved by its nature
  #c = nature to be trendy
  #d = loved by its trendiness
  #e = loved by all
  a = True
  b = True
  c = True
  d = True
  e = True
  while (a == b):
    start = raw_input("Do you believe that there is an independent standard of trendiness set by YouTube, Google, Facebook, or another company?  ")
    if (start.lower() == "y"):
      print ("Then the gods are not the only ones that can define piety or trendiness")
      c = False #because having an independent standard means the defination of piety is broken
    memes = raw_input("Do you believe that memes can die?  ")
    if (memes.lower() == "y"):
      print("Then you believe in the problem of triviality")
      d = False #because
      continue
    websites = raw_input("Do you believe being loved by all makes it trendy?  ")
    if (websites.lower() == "n"):
      print("So this independent of the internet gods commanding trendiness")
      e = False #ex, everyone loves dogs but they are not constantly trendy
    if (c == False or d == False or e == False):
      print ("Socrates changed your definition of piety and trendiness")
      a = False #could put b depending on your own opinion

  print "Goodbye Master\n"
main()
