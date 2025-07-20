#!/usr/bin/env python3

from email.parser import Parser
from email.parser import Parser
from email import message_from_string
from email.policy import default
import re

KNOWN_HEADERS = [
    # Standard
    'From', 'To', 'Cc', 'Bcc', 'Subject', 'Date', 'Message-ID', 'In-Reply-To',
    'References', 'Reply-To', 'Sender', 'Return-Path', 'Delivered-To',
    'Received', 'MIME-Version', 'Content-Type', 'Content-Transfer-Encoding',
    'Content-Disposition', 'Content-Language', 'Content-ID',
    # Extended
    'X-Mailer', 'X-Originating-IP', 'X-Spam-Status', 'X-Spam-Score',
    'X-Spam-Flag', 'X-Priority', 'X-UIDL', 'List-Id', 'List-Unsubscribe',
    'Archived-At', 'Auto-Submitted'
]

HEADER_REGEX = re.compile(r'\b(' + '|'.join(map(re.escape, KNOWN_HEADERS)) + r')\b\s*:', re.IGNORECASE)

def preprocess(raw_line):
    raw_line = raw_line.strip()

    # Find where the first known header starts
    match = HEADER_REGEX.search(raw_line)
    if not match:
        return ''

    # Trim everything before the first header
    trimmed = raw_line[match.start():]

    # Add newline before each header
    with_newlines = HEADER_REGEX.sub(r'\n\1:', trimmed).strip()

    # Parse the last line explicitly so that body separates from header
    tmp = with_newlines.split('\n')
    last_line = tmp.pop().split()
    tmp.append(' '.join(last_line[:2]))

    header = '\n'.join(tmp)
    body = ' '.join(last_line[2:])

    return header, body

def parse_mail(header, body):
    msg = Parser().parsestr(header)
    ret = dict(msg)
    ret ['Body'] = body
    return ret

def train():
    # Train the model
    pass

def predict():
    # Predict whether it is spam or not from the input mail
    pass

def main():
    pass

if __name__ == "__main__":
    main()
