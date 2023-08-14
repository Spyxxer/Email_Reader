import imaplib
import email, getpass, sys, time, re
from bs4 import BeautifulSoup
def animated_please_wait():
    animation = "|/-\\"
    i = 0
    while True:
        sys.stdout.write("\rPlease wait..." + animation[i % len(animation)])
        sys.stdout.flush()
        time.sleep(0.15)
        i += 1

        if i == 25:
        	break

def load_animate():
	try:
		animated_please_wait()
	finally:
		sys.stdout.write('\rDone...')
		sys.stdout.write('\r')

def mail_type():
	m_no = None
	try:
	    print("Select type of Mail:\n1.Gmail\n2.YahooMail\n3.Outlook\n4.Fastmail\n5.Apple_Icloud")
	    m_no = int(input("Choose number: "))
	except:
		print("Wrong Input, Try again..")
		mail_type()
	else:
		return m_no

def get_user_pass():
	name = None; pwd = None
	try:
		name = str(input("Your email: "))
		pwd = getpass.getpass("Your password: ")
	except:
		print("Wrong_Input")
		get_user_pass()
	return name, pwd
def confirm_login():
	name, pwd = get_user_pass()
	try:
		mail.login(name, pwd)
	except:
		print("Wrong credentials")
		confirm_login()
def read_no_of_emails():
	n = None
	try:
		n = int(input("Enter number of mails to read: "))
	except:
		print("Wrong Input, Try again")
		read_no_of_emails()
	else:
		return n
def spec_mail_to_read():
	name = input("Insert name of mail to be read: ")
	return name


def find_tag(name_of_tag):
	soup = BeautifulSoup(html_content, 'html.parser')
	soup.findall(name_of_tag)

mail_imap = {1:'imap.gmail.com', 2:'imap.mail.yahoo.com', 
3:'outlook.office365.com',
4:'imap.fastmail.com',
5:'imap.mail.me.com'}



select_mail = mail_type()
load_animate()
mail = imaplib.IMAP4_SSL(mail_imap.get(select_mail))
confirm_login()
val = read_no_of_emails()
mail.select('INBOX')
status, email_ids = mail.search(None, f'UNSEEN FROM {spec_mail_to_read()}')
email_id_list = email_ids[0].split()

i = 0

for email_id in email_id_list:
	status, msg_body = mail.fetch(email_id, '(RFC822)')
	msg = email.message_from_bytes(msg_body[0][1])

	subject = msg['subject']; from_address = msg['from']; date = msg['date']

	print(f"Subject: {subject}")
	print(f"From: {from_address}")
	print(f"Date: {date}")

	if msg.is_multipart():
		for part in msg.walk():
			if part.get_content_type() == "text/plain":
				body = part.get_payload(decode=True).decode("utf-8")
				print("Body:", body)
	else:
		body = msg.get_payload(decode=True).decode("utf-8")
		print("Body:", body)

	print("=====")
	i += 1
	if i == val:
		break






