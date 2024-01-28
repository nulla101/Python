import webbrowser
import os

from fpdf import FPDF


class PdfReport:
    """
    Creates a PDF file containing data about the flatmates,
    such as their names, their due amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def save(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2=flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate2=flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Adding icon
        pdf.image("files/house.png", w=30, h=30)

        # Adding report title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Adding period label and value
        pdf.set_font(family='Times', size=20, style='B')
        pdf.cell(w=270, h=40, txt="Period:", border=0, align="R")
        pdf.set_font(family='Times', size=20, style='I')
        pdf.cell(w=200, h=40, txt=bill.period, border=0, align="L", ln=1)
        pdf.ln(h=40)

        # Adding first flatmate's name and value of bill share to pay
        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=100, h=40, txt=flatmate1.name + ':', border=0, align="R")
        pdf.set_font(family='Times', size=18, style='I')
        pdf.cell(w=100, h=40, txt=flatmate1_pay, border=0, ln=1)

        # Adding second flatmate's name and value of bill share to pay
        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=100, h=40, txt=flatmate2.name + ':', border=0, align="R")
        pdf.set_font(family='Times', size=18, style='I')
        pdf.cell(w=100, h=40, txt=flatmate2_pay, border=0)

        # Change directory to files, generating PDF and opening the pdf in the browser
        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)
