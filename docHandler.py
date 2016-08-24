import zipfile
import shutil
import os
from contextlib import closing



def get_extension(fname):
    return fname.split(".")[-1]

#returns a string of xml or an empty string if error
def get_xml(fname):
    zf = zipfile.ZipFile(fname)

    try:
        #get document xml from docx
        return zf.read('word/document.xml')
    except:
        return  ""


def create_xml_file(xml_string, xml_file_name):
    with open(xml_file_name, 'w') as f:
        f.write(xml_string)


#Copies docx files from @old_doc_name to a tmp dir then builds a new docx
#file named @new_doc_name with the new docx xml file @new_xml_file
def create_new_docx(old_doc_name, new_doc_name, new_xml_file):
    old_doc = zipfile.ZipFile(old_doc_name, "r")
    old_doc.extractall('tmp')
    old_doc.close()

    with open(new_xml_file, 'r') as f:
        new_xml = f.read()

    with open('tmp/word/document.xml', 'w') as f:
        f.write(new_xml)


    assert os.path.isdir('tmp')
    with closing(zipfile.ZipFile(new_doc_name, "w", zipfile.ZIP_DEFLATED)) as z:
        for root, dirs, files in os.walk('tmp'):
            for fn in files:
                absfn = os.path.join(root, fn)
                zfn = absfn[len('tmp')+len(os.sep):]
                z.write(absfn, zfn)

    shutil.rmtree('tmp')
