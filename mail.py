import smtplib
sender = "davis.waris@gmail.com"
recipient = ["davis_waris@yahoo.com", "davis_waris@outlook.com", "warisdavis@gmail.com", "davewest06@outlook.com"]
password = "eebrvngzjydtyxpz"
Subject = "Hello David"
Text = "Please get back to me"
smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
smtp_server.login(sender,password)
message = "Subject:{}\n\n{}".format(Subject,Text)
smtp_server.sendmail(sender, recipient, message)
smtp_server.close()