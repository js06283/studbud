#Sends emails informing students of their groups using SMTP 

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Collect user input for email information
port = 465
password = input("Password: ")
link = input("Class times link: ")
course = input("Course name: ")
from_address = "studbud.columbia@gmail.com"

test = {'Group 1': [['Jessica Shi',2,2,2,3,1, 'jessicashi605@gmail.com'],
        ['Junping Shi',2,3,1,4,5,'junpingshi@gmail.com']],
        'Group 2': [['Jess Shi', 4,4,2,3,1,'jjs2295@columbia.edu']]}

context = ssl.create_default_context()

#Connect to SMTP Gmail server
with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as server:
  server.login(from_address, password)
  for key in test:
    group = key
    group_list = test[key]

    #Writes and sends email for each student in the dataset
    for student in group_list:
      name = student[0]
      to_address = student[6]
      list_temp = group_list
      list_temp.remove(student)
      info = ""
      for i in list_temp:
        info = info + i[0] + ", " + i[6] + "\n"

      message = MIMEMultipart("alternative")

      message["Subject"] = "StudBud Group Match for " + course
      message["From"] = from_address
      message["To"] = to_address

      text = """
        Hi {name},
        Welcome to StudBud!
        Your group for {course} is {group}.
        The other members of your group are:
        {info}
        We will help facilitate your first meeting, but after that it's up to you.
        Fill out this survey to help find the best time for you to meet! 
        {link}
        Thanks!
        The StudBud Team"""

      html = """\
        <html>
          <head></head>
          <body>
          <p>Hi {name},<br>
            <b>Welcome to StudBud!</b> <br>
            Your group for {course} is {group}.<br>
            The other members of your group are:<br>
            {info} <br>
            We will help facilitate your first meeting, but after that it's up to you.<br>
            Fill out this <a href={link}>survey</a> to help find the best time for you to meet!<br>

            Thanks!<br>
            The StudBud Team
         </p>
       </body>
      </html>
      """

      part1 = MIMEText(text.format(name=name,group=group,info=info,link=link,course=course),"plain")
      part2 = MIMEText(html.format(name=name,group=group,info=info,link=link,course=course),"html")

      message.attach(part1)
      message.attach(part2)

      server.sendmail(from_address,to_address,message.as_string())