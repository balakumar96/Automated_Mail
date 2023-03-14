import smtplib, schedule, time
from email.message import EmailMessage

def send_email():
    receiver = 'arsalan.jhnson@gmail.com', '<receiver mail 2>'
    sender = '<sender mail>
    password = '<password>'
    
    msg = EmailMessage()

    msg['Subject'] = 'Python automated mail delivery'
    msg['From'] = sender
    #msg['To'] = receiver

    #EmailMessage Template
    filename_0 = 'template.txt'
    file_0 = open(filename_0)
    data_0 = file_0.read()
    print (data_0)
    msg.set_content(data_0)

    #Attachment
    filename_1 = 'report.docx'
    file_1 = open(filename_1, 'rb')
    data_1 = file_1.read()
    msg.add_attachment(data_1, maintype='application', subtype='docx', filename=filename_1)


    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())
    server.close()
    print ('Mail sent successfully to', receiver)

#Timer functions
schedule.every().day.at("00:00").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(1)
    

