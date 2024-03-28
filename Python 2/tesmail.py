email = input("Enter your email:")

k,j,d = 0,0,0

if len(email)>=6:
    if email[0].isalpha():
        if "@" in email and email.count("@") ==1: #sam@gmail.co
            if(email[-4]=="." or email[-3]=="."): #sam@gmail.com
                for i in email:
                    if i.isspace():
                        k =1
                    elif i.isalpha():
                        if i.isupper():
                            j =1
                    elif i.isdigit():
                        continue
                    elif i in ["_" , "." , "@"]:  # simplified the condittion
                       continue
                else:
                    d = 1 
                if k==1 or j==1 or d==1:   
                   print("wrong email format") 
                else:
                    print("correct email format")
            else:
                    print("wrong email format: missing or misplace the dot")
        else: 
            print("wrong email fomat : incorrect number of @ symbol ")
    else:
        print("wrong email format: email must be start with a later") 
else:
    print("wrong email format lenth should be at least 6 characters")       




