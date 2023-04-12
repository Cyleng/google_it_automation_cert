#! /usr/bin/env python3

import os
import email.message
import smtplib
import shutil
import psutil
import socket


event_message = {
    "cpu": "Error - CPU usage is over 80%",
    "disk": "Error - Available disk space is less than 20%",
    "ram": "Error - Available memory is less than 500MB",
    "localhost": "Error - localhost cannot be resolved to 127.0.0.1"
}

def generate(sender, recipient, subject, body):
    """Creates an email with an attachement."""
    # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)
    return message


def send(message):
    """Sends the message to the configured SMTP server."""
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()

def check_disk_usage():
    """Returns True if there is enough free disk space, False otherwise."""
    du = shutil.disk_usage("/")
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    if percent_free < 20:
        return True
    return False

def check_cpu_usage():
    """Returns True if there is enough unused CPU, False otherwise."""
    usage = psutil.cpu_percent(1)
    return usage > 80

def check_ram_usage():
    """Returns True if there is enough unused RAM, False otherwise."""
    usage = psutil.virtual_memory().available
    return usage < 500000000

def check_localhost():
    """Returns True if localhost resolves to 127.0, False otherwise."""
    localhost = socket.gethostbyname('localhost')
    return not localhost == "127.0.0.1"

if __name__ == "__main__":
  
    sender = "automation@example.com"
    recipient = "student-03-d4d909a6d70f@example.com"
    message_body = "Please check your system and resolve the issue as soon as possible."

    if check_cpu_usage():
        send(generate(sender, recipient,event_message["cpu"], message_body))
  
    if check_disk_usage():
        send(generate(sender, recipient,event_message["disk"], message_body))
  
    if check_ram_usage():
        send(generate(sender, recipient,event_message["ram"], message_body))
  
    if check_localhost():
        send(generate(sender, recipient,event_message["localhost"], message_body))

