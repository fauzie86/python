import pikepdf

old_pdf = pikepdf.Pdf.open("pdffile.pdf")

no_ext = pikepdf.Permissions(extract=False)

old_pdf.save("new.pdf" , encryption = pikepdf.Encryption(user = "12345abc" , owner = "sam" , allow=no_ext))
