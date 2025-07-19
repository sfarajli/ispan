#!/usr/bin/env python3

from email.parser import Parser
from email.parser import Parser
from email import message_from_string
from email.policy import default

def preprocess(raw):
    # TODO: separate the header and body and then parse the header
    words = raw.split()
    result = []
    current_key = None
    current_value = []

    i = 0
    while i < len(words):
        word = words[i]
        if ':' in word:
            parts = word.split(':', 1)
            key = parts[0]
            val = parts[1].strip()

            # If we already have a key, flush it with its value
            if current_key is not None:
                if current_value:
                    result.append(f"{current_key}: {' '.join(current_value)}")
                else:
                    # If value is empty, treat this key:value as the value
                    current_value.append(f"{key}: {val}")
                    i += 1
                    continue  # Don't treat the current as new key

            current_key = key
            current_value = [val] if val else []
        else:
            current_value.append(word)

        i += 1

    if current_key is not None and current_value:
        result.append(f"{current_key}: {' '.join(current_value)}")

    return '\n'.join(result)

def parse_mail(mail):
    msg = Parser().parsestr(mail)

    mail = {
            "from": msg['From'],
            "to": msg['to'],
            "subject": msg['Subject'],
            "date": msg['Date'],
            "body": msg.get_payload()
    }

    return mail

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
