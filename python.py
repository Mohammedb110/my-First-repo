file_name  = "lab-sample.txt"

with open (file_name,mode="r",encoding="utf-8")as file:
   for line ,Line in enumerate(file,start=1):
      print(f"{line}: {Line.strip()}")





   