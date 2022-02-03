cipher="cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_MAZyqFQj}"
abc="abcdefghijklmnopqrstuvwxyz"
ABC="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
flagOutput=" "

for char in cipher:
	if(char == '{' or char =='}' or char == '_' or char == "'" or (ord(char)>=48 and ord(char)<=57) ):
		flagOutput+=char
	elif (ord(char) >= 97 and ord(char)<=122):
		flagOutput+=abc[(abc.find(char)+13)%26]
	elif (ord(char) >= 65 and ord(char)<=90):
		flagOutput+=ABC[(ABC.find(char)+13)%26]
	
print(flagOutput)
