from bs4 import BeautifulSoup as bs
from DocXHandler import *

#set up filenames
old_file_name = 'letter.docx'
new_file_name = 'letter2.docx'

#get xml of old word document
old_doc_xml = get_xml(old_file_name)

#parse xml
soup = bs(old_doc_xml, "html.parser")

#find all text in xml file
text = soup.find_all('w:t')

#replace everything with 123 test
for t in text:
	t.string = "123 test"

#create new xml file
create_xml_file(str(soup), 'tmp-doc.xml')

#create new word doc using new xml file
create_new_docx(old_file_name, new_file_name, 'tmp-doc.xml')
