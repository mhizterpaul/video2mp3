import smtplib, os, json
from email.message import

def notification(message):
    try:
        message = json.loads(message)
        mp3_id = message['mp3_id']
        sender_address = os.environ.get('GMAIL_ADDRESS')
        sender_password = os.environ.get('GMAIL_PASSWORD')
        reciever_addresss = message['username']

        msg = EmailMessage()
        msg.set_content(f'mp3 file_id: {mp3_id} is now ready!')
        msg['Subject'] = 'MP3 Download'
        msg['From'] = sender_address
        msg['To'] = reciever_address

        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender_address, sender_password)
        session.send_message(msg, sender_address, reciever_address) 
        session.quit()
        print('Mail Sent')
    except Exception as e:
        print(e)
        return e