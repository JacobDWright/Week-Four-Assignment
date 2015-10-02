# Jacob Wright
# Week Four Assignment
# Pigettysburg Address
# Collaborated with Daniel McMurry, Evan Sauers, Marissa Gross

vowels="aeiouAEIOU"

# Define a function called piggy(string) that returns a string

def piggy(word):
	n = 0 
	endword = ""
	
	for letter in word:
		# Check if letter is a vowel
		if letter in vowels:
			if n == 0:# True?  We are done
				pig = word + "yay"
			
				return pig
			else:
				pig = word[n:] + endword + "ay"
				return pig
				
		else:
			# False? Consonant
			endword += word[n]
			n = n + 1
	
infile = gettytext
outfile = gettyfile
# Open the file *getty.txt* for reading.  
gettytext = open ( "getty.txt", "r")
# Open a new file *piggy.txt* for writing.  
gettyfile = open ("piggy.txt", "w")
# Read the getty.txt file into a string.  
gettystring = gettytext.read()
# Strip out bad characters (, - .).  
gettystring = gettystring,replace(",","")
gettystring = gettystring,replace("-","")
gettystring = gettystring,replace(".","")
# Split the string into a list of words.  
gettylist = gettystring.split ()
# Create a new empty string.  
piggystring = ""
# Loop through the list of words, pigifying each one.  
for word in gettylist:
# Add the pigified word (and a space) to the new string.  
  if len(word) >0:
  	piggystring = piggystring + piggy(word) + " "
# Write the new string to piggy.txt.  
print(piggystring, file = gettyfile)
# close the files.
gettytext.close()
gettyfile.close()