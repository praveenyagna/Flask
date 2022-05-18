import re
from docx import Document
doc=Document("C://Users//ESN//Desktop//Praveen//Praveen_Business Analyst.docx")
def getText(doc):
    for para in doc.paragraphs:
        r = re.compile(r"^\s+", re.MULTILINE)
        lines= r.sub("", para.text)
        reg_mail=re.compile(r'\w+\.\w+?@\w+\.\w+')
        reg_ph=re.compile(r'[+]?[0-9]{2}?[-]?\d{10}')
        emails= re.finditer(reg_mail,lines)
        Phone = re.finditer(reg_ph, lines)
        for email in emails:
            print("Email:", email.group())
        for ph in Phone:
            print("Phone number:", ph.group())


getText(doc)