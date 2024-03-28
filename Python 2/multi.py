import smtplib as s

ob = s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()

ob.login('pojikibot@gmail.com' , '')

subject = "testing mail"
body = " i love python"
message = "subject:{}\n\n".format(subject,body)

listadd = ['samraizbhatti06@gmail.com' ,'' , '']

ob.sendmail('' , listadd , message)
print("Mail sent succesfully")
ob.quit()