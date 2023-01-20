#!/usr/bin/env python3
"""
Splitting pdf into single page pdfs and renaming the output files
"""

from PyPDF2 import PdfReader, PdfWriter

# Load the pdf to the PdfFileReader object with default settings
FILENAME = "original.pdf"

# Split each page to separate pdf
with open(FILENAME, "rb") as pdf_file:
    pdf_reader = PdfReader(pdf_file)

    for page_nr, page in enumerate(pdf_reader.pages, start=1):
        pdf_writer = PdfWriter()
        pdf_writer.add_page(page)

        # Set the name of the extracted page
        temp_name = f"{FILENAME[:-4]}-Page{page_nr}.pdf"
        with open(temp_name, "wb") as split_page:
            pdf_writer.write(split_page)