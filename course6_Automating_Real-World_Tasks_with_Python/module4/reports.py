#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from datetime import date
from reportlab.lib.styles import getSampleStyleSheet
import os

today = date.today()



def generate_report(attachment, title, paragraph):
    report = SimpleDocTemplate(attachment)
    empty_line = Spacer(1, 20)
    styles = getSampleStyleSheet()
    report_title =Paragraph(title + today.strftime("%B %d, %Y"), styles["h2"])
    content = []
    for line in paragraph:
        content.append(Paragraph(line))
        content.append(empty_line)
    #print(report_title)
    #print(empty_line)
    #print(paragraph)
    report.build([report_title]+[empty_line]+content)
