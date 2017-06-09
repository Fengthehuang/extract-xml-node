import glob, re

# Open the result file
result_file = open('result.txt',"w")

#Set up the regex in 3 groups
regex = '(<Z_ShippingInstructions.*?">)(.*?)(</Z_ShippingInstructions>)'

# Loop on all .rlx files in the current folder
for filename in glob.glob('*.rlx'):

	# Print the name of the current file in the result file
	print(filename, file=result_file)

	# Open the current file and read its content
	file = open(filename,"r")
	content = file.read()

	# Search the regex in content, '.' character includes newllines
	result = re.search(regex, content, flags=re.DOTALL)

	# If their is a result, print the 2nd group of the regex in the result file
	if result:
		print(result.group(2), file=result_file)
	else:
		print("no result", file=result_file)

	# Close the current file
	file.close()

# Close the result file
result_file.close()