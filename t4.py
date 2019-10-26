import smtplib
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login("1aqsdadsasdasd23asd7654321@gmail.com", "qq1122334455qq")
smtpObj.sendmail('1aqsdadsasdasd23asd7654321@gmail.com','el.piankova@gmail.com', 'I did it! (IgorKalinovskii')
smtpObj.quit()