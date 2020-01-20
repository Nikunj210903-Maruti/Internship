import os
file_types= ['csv']
from .constants import FILE_PATH

def get_body_text(e_mail):
    body = ""
    if e_mail.is_multipart():
        for part in e_mail.walk():
            ctype = part.get_content_type()
            cdispo = str(part.get('mailtent-Disposition'))
            if ctype == 'text/plain' and 'attachment' not in cdispo:
                body = part.get_payload(decode=True)
                break
    else:
        body = e_mail.get_payload(decode=True)
    return body.decode('utf-8')


def store_attechment(e_mail, filename):
    for part in e_mail.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('content-Disposition') is None:
            continue
        file = part.get_filename()
        if bool(file):
            extension = file.split('.')[1]
            if extension in file_types:
                extension  = "." + extension
                with open(file, 'wb') as f:
                    f.write(part.get_payload(decode=True))
                os.rename(file, FILE_PATH + filename + extension)




