#Task: Two-fer or 2-fer is short for two for one. One for you and one for me.
#“One for X, one for me.”
#When X is a name or “you”.
#If the given name is “Alice”, the result should be “One for Alice, one for me.” 
#If no name is given, the result should be “One for you, one for me.”

name=raw_input('Enter your name : ')

def two_fer(name):
  if len(name) > 0:
      print ("One for %s, one for me." % name)
  else:
      print ("One for you, one for me")
