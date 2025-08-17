file1 = open('output.txt','w')
userinput1 = input("enter text to write to the file: ")
filewriting = file1.write(userinput1)

print("data successfully written to output.txt")

print()
file1 = open('output.txt','a')
userinput1 = input("Enter additional text to append :")
filewriting = file1.write(f"\n{userinput1}") 

print("data successfully append")
print()

file1 = open('output.txt','r')
print("final content of output.txt ")
filereading = file1.read()
print(filereading)