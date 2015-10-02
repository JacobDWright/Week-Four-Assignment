# 
# File Header
#
# Define vowels

vowels = "aeiouAEIOU"

# Ask for word

word = input("Please enter a word: ")

# Loop through word, one letter at a time
n = 0 
endword = ""

for letter in word:
	# Check if letter is a vowel
	if letter in vowels:
		if n == 0:# True?  We are done
			pig = word + "yay"
			break
		#	return pig
		else:
			pig = word[n:] + endword + "ay"
		#	return pig
			break


	else:
		# False? Consonant
		endword += word[n]
		n = n + 1
print(pig)
