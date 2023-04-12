#!/usr/bin/env python3
import reports
import emails
import os
from reportlab.platypus import Paragraph, Spacer

sender = "automation@example.com"
recipient = "student-03-d4d909a6d70f@example.com"
subject = "Upload Completed - Online Fruit Store"
email_body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
attachment_path = "/tmp/processed.pdf"
description_folder = "supplier-data/descriptions/"

if __name__ == "__main__":
    title = "Processed Update on "
    report_body = []
    empty_line = Spacer(1, 20)
    for description in os.listdir(description_folder):
        if (not description.startswith('.')) and description.endswith('txt'):
            with open(description_folder + description, 'r') as opened:
                lines = opened.readlines()
                name = lines[0].strip()
                weight = lines[1].strip()
                report_body.append("name: "+name)
                report_body.append("weight: "+weight)
    #print(report_body)
    reports.generate_report(attachment_path, title, report_body)
    message = emails.generate_email(sender, recipient, subject, email_body, attachment_path)
    emails.send_email(message)
