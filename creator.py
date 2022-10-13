#!/usr/bin/env python3
from random import randint, randrange

while True:
	# Question if you want to generate a ID or don´t want to
	IDGeneration = input("Do you want to generate a ID y/n: ")
	
	if IDGeneration == "y":
		# Generating the random ID
		value1 = randint(100, 999)
		value2 = randint(100, 999)
	
		# Making the Integer to a String to "add" the Numbers
		value1str = str(value1)
		value2str = str(value2)
	
		# Make a space between value1 and value2
		ID = " ".join([value1str, value2str])
	
		# Print the generated ID
		print("Your ID is:")
		print(ID)
		print("")
		print("Please write it on to the certificate")
		break
	
	elif IDGeneration == "n":
		# Asks what your ID should be
		print("Please enter the ID like this: XXX XXX")
		ID = input("What should be the ID?: ")
		
		# Checks if the ID is in the right format
		if len(ID) == 7:
			print("Thanks!")
			break
		else:
			print("Please enter it in this format: XXX XXX")
			print("")
	
	print("Please enter y or n !")
	
print("--------------------")

# Enter the name
while True:
	# Ask the name
	Who = input("For how should be the certificate? (Name + Last Name) : ")
	
	# Check if name has over 2 Characters
	if len(Who) > 2:
		print("The name that you entered is:", Who)
		who_correct = input("Is the name correct? y/n : ")
		if who_correct == "y":
			print("Great!")
			break
		elif who_correct == "n":
			print("Okay!")
		else:
			print("--------------------")
			print("Please enter y/n")
	else:
		print("--------------------")
		print("Please enter a correct name!")
		print("")

# Ask for the date
while True:
	# Enter the date
	print("--------------------")
	print("Please enter the date like this: DD.MM.YYYY")
	When = input("When was the Certificate created?: ")
	
	# Check if the date is in right format
	if len(When) == 10:
		print("Thanks!")
		break
	else:
		print("Not correct!")

# Asks for what the Certificate is
while True:
	print("--------------------")
	What = input("Please enter for what the certificate is in use for (More than 10 Chars): ")
	
	# Check if it is over 10 Chars
	if len(What) > 10:
		print("Thanks!")
		break
	else:
		print("------------------")
		print("More than 10 Characters!")

# Making the ID perfect for the code
IDCut = ID[:-4];
IDNoSpace = ID.replace(" ", "")

# Printing the JavaScript Code
print("--------------------")
print("JavaScript:")
print("Please add the script to the script.js file")
print()
print("First Snippet")
print("var validvid" + IDCut +"= $('#vid').val() === '" + ID + "';")
print()
print("Second Snippet")
print("else if (validvid" + IDCut + " == true) {")
print("		$('#valid').css('display', 'block');")
print("		window.location.replace('" + IDNoSpace + ".html""');")
print("     }")

#Printing the HTML Code
print("------------------")
print("HTML:")
print("Please create a file with the name of the ID like this XXXXXX.html and add the HTML Code to that file")
print("")
print("")
print("<!DOCTYPE html>")
print("<html>")
print("		<head>")
print("			<meta charset='UTF-8'>")
print("			<meta name='robots' content='noindex'>")
print("			<title>Zertifikat - " + ID + "</title>")
print("		</head>")
print("	<style>")
print("		@import url('https://fonts.googleapis.com/css2?family=EB+Garamond&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');")
print("		body")
print("		{")
print("			display: flex;")
print("			justify-content: center;")
print("			align-items: center;")
print("			min-height: 100vh;")
print("			flex-direction: column;")
print("			gap: 30px;")
print("			background-color: #4C6663;")
print("		}	")
print("")
print("		#infoform {")
print("			background-color: #1d2b3a;")
print("			width: 400px;")
print("			border-radius: 5px;")
print("			box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;")
print("		}")
print("		")
print("		#status {")
print("			background-color: #80CFA9;")
print("			height: 100px;")
print("			width: 400px;")
print("			padding-top: 1%;")
print("			padding-bottom: 1%;")
print("			border-radius: 5px;")
print("		}")
print("		")
print("		h1{")
print("			color: white;")
print("			font-family: 'Poppins', sans-serif;")
print("			margin-bottom: -10px;")
print("		}")
print("		h2{")
print("			color: white;")
print("			font-family: 'Poppins', sans-serif;")
print("			margin-bottom: -10px;")
print("		}")
print("		h3{")
print("			color: white;")
print("			font-family: 'Poppins', sans-serif;")
print("			margin-bottom: -10px;")
print("		}")
print("		p{")
print("			color: white;")
print("			font-family: 'Poppins', sans-serif;")
print("			margin-bottom: -10px;")
print("		}")
print("")
print("		#back ")
print("		{")
print("			/*			width: 20.8%;*/")
print("			width: 50%;")
print("			padding: 10px;")
print("			margin-top: 10%;")
print("			margin-bottom: 10%;")
print("			border: 1px solid rgba(255, 255, 255, 0.25);")
print("			background-color: #1d2b3a;")
print("			border-radius: 5px;")
print("			outline: none;")
print("			color: #fff;")
print("			font-size: 1em;")
print("			transition: 0.5s;")
print("		}")
print("")
print("		#back:hover")
print("		{")
print("			background-color: #00dfc4;")
print("		}")
print("		img {")
print("			visibility: hidden;")
print("		}")
print("")
print("		.disclaimer{")
print("			visibility: hidden;")
print("		}")
print("	</style>")
print("	<body>")
print("		<div id='infoform'>")
print("			<div id='status'>")
print("				<center>")
print("				<h3>Gültiges Zertifikat</h3>")
print("				<h3>ID: " + ID + "</h3>")
print("				</center>")
print("			</div>")
print("			<center>")
print("<!--			<h1>Zertifikat</h1>-->")
print("<!--			<h2>ID: " + ID + "</h2>-->")
print("				<h3>Aussgestellt für:</h3>")
print("				<p>" + Who + "</p>")
print("				<h3>Datum der Ausstellung:</h3>")
print("				<p>" + When + "</p>")
print("				<h3>Informationen:</h3>")
print("				<p>" + What + "</p>")
print("				<a href='index.html'><button id='back'>Zurück</button></a>")
print("			</center>")
print("		</div>")
print("	</body>")
print("</html>")