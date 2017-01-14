# importing the required modules
import PyPDF2

#Creating a pdf file object
pdfFileObj = open('python_tutorial.pdf', 'rb')

#creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#printing the number of pdf pages
print(pdfReader.numPages)

#creating a page object
pageObj = pdfReader.getPage(1)

#exrtacting the page from the specified page
print(pageObj.extractText())

#closing the pdf file object
pdfFileObj.close()
