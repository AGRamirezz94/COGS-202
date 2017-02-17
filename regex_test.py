
import re
import random
import sys

# Get the text for the constitution
#page = requests.get('https://www.usconstitution.net/const.txt', verify=True)
with open("const.txt") as myfile:
  const_text = myfile.read()
  #print const_text 
# A useful construct I'm leaving in, commented out
constitution_lines = const_text.split('\n')
# for line in constitution_lines:
# 	print "-->",line

# Define the regular expression and use it to find matches
regex = r"(Amendment) "
matches = re.findall(regex,  const_text)

# Do something with the matches
phrases = ["A M E N D M E N T", " Unconstitutional", ":::::::::<[]>:::::::::::"]
for match in matches:
	print random.choice(phrases)
	if random.choice(phrases) == " Unconstitutional":
                print " I plead the fifth :("

# Do a replace.  Uncomment to see it working
#backwards = re.sub(regex, r"--==>>\2 is the \1 in question<<==--", const_text)
#print backwards


