import pdftotext
import pathlib
import glob

x=0
file_= open('output.text','w')
for pdf_file in pathlib.Path('/Users/BrandenKang/Desktop/extract_pdf/sample ocr').glob('*.pdf'):
    # do something with "txt_file"
    with open(pdf_file,"rb") as f: 
        pdf = pdftotext.PDF(f)
        # file_ = open('output.text','w')
        for page in pdf: 
            file_.write(page)
        file_.write('END')
        # file_.close() 
        x+=1 
        print(x)
file_.close()


# Load PDF
# with open("/", "rb") as f:
#     pdf = pdftotext.PDF(f)

# f = open('output.txt','w')
# f.write(pdf[0])
# f.close()


# Iterate over all the pages
# for page in pdf:
    # print(page)

# Read some individual pages
# print(pdf[0])

# Read all the text into one string
# print("\n\n".join(pdf))