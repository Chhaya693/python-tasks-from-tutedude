dist = {"chhaya":80 , "maya":90 ,"satish":70,"ujwal":95,"Dharama":85,"shakti":88,"sudevi":79}
name = input("enter the student name for accessing marks :")
try:
    marks =  dist[name]
    print(f"{name} marks :{marks}")
except Exception as e:
    print("student not fount")


