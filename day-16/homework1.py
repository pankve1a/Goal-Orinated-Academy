# შექმენით ქუჩის ქვიზი, 
# სადაც ბენსიმონებში გაზმანული შავი ბიჭი გამვლელს შეეკითხება "რა კაცი ხარ" 

# ხოლო სავარაუდო პასუხების მიხედვით გადაწყდება მისი ბედი
# 1) ცემა 
# 2) დაძმაკაცება 
# 3) ფულის ახევა


def ask():
    print("რა კაცი ხარ?")
    print("1) კაი ბიჭი")
    print("2) მომპარავი ბიჭი")
    print("3) პატიოსანი ბიჭი")

option1 = "დაძმაკაცება."
option2 = "ცემა."
option3 = "ფულის ახევა."
wrong_answer = "არასწორი პასუხი: ცემა."

ask()

 
asnwer = int(input("enter here: "))
if asnwer == 1:
    print(option1)
    answer = True
elif asnwer == 2:
    print(option1)
elif asnwer == 3:
    print(option1)
else:
    print(wrong_answer)



    
    

