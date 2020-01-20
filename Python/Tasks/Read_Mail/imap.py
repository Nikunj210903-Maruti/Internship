import imaplib, email
import re


def config(user, password, imap_url, box_select):
  con = imaplib.IMAP4_SSL(imap_url)
  con.login(user, password)
  con.select(box_select)
  return con


def get_body(e_mail):
    if e_mail.is_multipart():
        return get_body(e_mail.get_payload(0))
    else:
        e_mail.get_payload(None, True)


def search(key, value,con):
    result, data = con.search(None, key, "{}".format(value))
    return data


def get_emails(result_bytes, con):
    e_mails = []
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        data = email.message_from_bytes(data[0][1])
        e_mails.append(data)
    return e_mails


def get_attechment(e_mail,filename):
    import os
    for part in e_mail.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        file = part.get_filename()
        extension = "." + file.split('.')[1]
        if bool(file):
            with open(file, 'wb') as f:
                f.write(part.get_payload(decode=True))
            os.rename(file,filename + extension)


con = config("kunjvadodariya040798@gmail.com", "Kunjvadodariya040798#", "imap.gmail.com", 'INBOX')
search = search(None, "ALL",con)
e_mails = get_emails(search,con)

for e_mail in e_mails:
    if re.match("(Date_of_)([0-2][0-9]|(3)[0-1])(-)(((0)[0-9])|((1)[0-2]))(-)\d{4}#(\d)+" , e_mail['Subject']):
        filename = "date" + str(e_mail['Subject'].split('#')[0][7:]) + "_" + str(e_mail['Subject'].split('#')[1])
        get_attechment(e_mail,filename)



