def isPalindrome(self, s: str) -> bool:

	# Converting s to all Lower Case
	s = s.lower()
	string = ''
	alphabets = 'abcdefghijklmnopqrstuvwxyz0123456789'
	for char in s:
		if char in alphabets:
			string += char

	# Check if string is a palindrome
	i,j = 0,len(string)-1
	while (i < j):
		print(string[i],string[j])
		if string[i] != string[j]:
			return False
		i += 1
		j -= 1

	return True


# Input
s = "race a car"

print(isPalindrome(0,s))