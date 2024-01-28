from flat import Bill, Flatmate
from reports import PdfReport

"""
Creating a command line interface (CLI) for entering flatmate and bill data
"""

amount = float(input("Hey user, please enter the bill amount: "))
period = input("Hey user, please enter the bill period (E.g. December 2023): ")

name1 = input("Please enter the first flatmate's name: ")
name2 = input("Please enter the second flatmate's name: ")

days_in_house1 = float(input(f"Please input the amount of days {name1} was in the house: "))
days_in_house2 = float(input(f"Please input the amount of days {name2} was in the house: "))

final_bill = Bill(amount=amount, period=period)
flatmate1 = Flatmate(name=name1, days_in_house=days_in_house1)
flatmate2 = Flatmate(name=name2, days_in_house=days_in_house2)

print(f"{flatmate1.name} pays: ", round(flatmate1.pays(bill=final_bill, flatmate2=flatmate2), 2))
print(f"{flatmate2.name} pays: ", round(flatmate2.pays(bill=final_bill, flatmate2=flatmate1), 2))

pdf_report = PdfReport(filename=f"{final_bill.period}.pdf")
pdf_report.save(flatmate1, flatmate2, final_bill)
