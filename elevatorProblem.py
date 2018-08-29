import os
import random
def main():
  print "Hello Master"
  #get another elevator bag of words
  elv_arr = ["two", "2", "elevators", "elevator", "months", "ask", "move up", "get", "another", "new elvator", "backlog", "line", "town"]
  #keep current residents happy and healthy bag of words
  keep_arr = ["stairs", "faster", "happy", "amenties", "feedback", "tenants", "rent", "lobby", "stop", "moving", "health"] 
  #get news residents to keep building full and manager happy bag of words
  new_arr = ["manager", "full", "happy", "job", "ads", "recruit", "tenants", "discount", "rent", "find", "new"] 

  print "The manage of a large office building has been receiving an increasing number of complaints about the building's elevator service, particularly during rush hours.\n"
  print "Several of the long term tenants in the building have threatened to move out unless the service is improved. In response the manager recently inquired into the possibility to adding 1-2 elevators to the buidling." 
  print "\nAlthough it would be feasible, the only elevator company in the area has a 6 month backlog of orders. As an assistant to the magager, you were asked to come up with a plan to get 2 new elevators installed within 3 months.\n"
  print "You must present the plan at the next staff meeting.\n" 
  
  #get input from user
  answer = raw_input ("Type 1-3 sentences about how you will solve the problem: ")
  answer = str(answer)
  #a simple bag of words matrix approach 
  elv_cnt = 0
  keep_cnt = 0
  new_cnt = 0
  for i in range (0, (len(elv_arr) - 1)): 
    if (elv_arr[i] in answer): 
      elv_cnt = elv_cnt + 1
  for j in range (0, (len(keep_arr) - 1)): 
    if (keep_arr[j] in answer): 
      keep_cnt = keep_cnt + 1
  for h in range (0, (len(new_arr) - 1)): 
    if (new_arr[h] in answer):
      new_cnt = new_cnt + 1
  if ((elv_cnt >= keep_cnt) and (elv_cnt >= new_cnt)):
    print "You chose the elevator route\n" 
  elif ((keep_cnt >= elv_cnt) and (keep_cnt >= new_cnt)): 
    print "You chose the keeping the old/current tenants\n"
  elif ((new_cnt >= elv_cnt) and (new_cnt >= keep_cnt)):
    print "You chose to get new tenants\n"
  else: 
    print "I did not find a pattern"

  print "\nIs that the real problem?\n"
  print "Goodbye Master" 
  #next step will be able to do this a real array/array
main()
