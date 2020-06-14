import yagmail

receiver = 'artles00@wp.pl'
body = 'Hello from Yagmail!'
filename = 'cookie.jpg'

yag = yagmail.SMTP('fastklapsylan@gmail.com')
yag.send(
    to=receiver,
    subject='Yagmail test with attachment',
    contents=body,
    attachments=filename
)
