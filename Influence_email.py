#http://effbot.org/pyfaq/how-do-i-send-mail-from-a-python-script.htm
#import smtplib
import os
import random
from subprocess import Popen, PIPE
def main():
  print "Hello Haley\n"
  reminders = ["Don't Complain", "Appreciation", "Eagerness", "Be interested in others", "Smile", "Remember Names", "Listen", "Talk in Terms of Other's Interest", "Make people feel important", "avoid arguments", "show respect", "Admit when you are wrong", "Begin in a friendly way", "Get the other person to say yes", "Let others do the talking", "Let others think the idea was theirs", "Be sympathetic", "See the other point of view", "Appeal to the nobler motives", "Dramatize your ideas", "Throw down a challenge", "Begin with praise", "Call attention to mistakes indirectyl", "Talk about your own mistakes first", "Ask questions instead of giving orders", "Let the other person save face", "Praise slight improvements", "Give the other person a reputation to live up to", "Use encouragement", "Make the Other person happy"]
  #sendmail_location = "/usr/sbin/sendmail" # your choce
  p = os.popen("%s -t" % sendmail_location, "w")
  #p.write("From: %s\n" % "someone") #your choice
  #p.write("To: %s\n" % "someone") #your choice
  p.write("Subject: Influence Reminder\n")
  p.write("\n") # blank line separating headers from body
  p.write("You made an automated email")
  index1 = random.randint(0,(len(list_1)-1))
  p.write(reminders[index1])
  status = p.close()
  if status != 0:
    print "Sendmail exit status", status
  print "Goodbye Master\n"
main()
