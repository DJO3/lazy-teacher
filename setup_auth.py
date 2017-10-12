from pprint import pprint
from lazy_teacher.drive import Drive
# from lazy_teacher.process import sanitize, count

drive = Drive()
auth = drive.get_credentials()

# files = drive.get_files()
# doc = files[0]['id']
# text = drive.get_text(doc, 'text/plain')

# clean_text = sanitize(text)
# index = count(clean_text)

# pprint(index)


