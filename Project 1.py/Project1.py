from PyPDF2 import PdfMerger
allpdf = ["Project 1.py/my.pdf", "Project 1.py/my2.pdf"]
MyMerger = PdfMerger()

for Newpdf in allpdf:
    MyMerger.append(Newpdf)

MyMerger.write("Saruf Khan.pdf")
MyMerger.close()