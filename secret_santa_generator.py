import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#instructions/input
print("Welcome to the Secret Santa Name Selector!")
total_people = int(input("How many people will be participating? "))

email_dict = {}
pairs_dict = {}
names_list = []
for x in range(total_people):
    name = input("Enter the name of person number " + str(x+1) + " ")
    email = input("Enter their email address ")
    email_dict[name] = email
    names_list.append(name)

#random selector
for name in email_dict:
    while True:
        num = random.randint(0, x)
        if(names_list[num] != name and names_list[num] != 0):
            break
    pairs_dict[name] =  names_list[num]
    names_list[num] = 0

#master list of pairings
names_str = ""
for name in pairs_dict:
    names_str = names_str + name + "->" + pairs_dict[name] + "\n"



#sending email
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
s.starttls() 

#add own master email and its password from which emails will be sent
s.login("from email", "password") 



for name in pairs_dict:

    #message = "Your person is " + pairs_dict[name]
    message = MIMEMultipart()
    msg = MIMEText("Your person is " + pairs_dict[name] ,'plain')
    message['From'] = "from email"
    message['To'] = email_dict[name]
    message['Subject'] = "Secret Santa"
    message.attach(msg)
    s.sendmail("from email", email_dict[name], message.as_string()) 
    


#sends master list of pairs to itself
s.sendmail("from email", "from email", names_str)
s.quit() 

    

