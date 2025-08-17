file1 = open("sample.txt","r")

try:
    
    readingFile = file1.read()
    print(readingFile)

except  Exception as e :
    print("The file sample.txt is not found")

finally:
    file1.close()
