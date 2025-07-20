import pandas as pd
from model import *

df = pd.read_csv("data/spam_assassin.csv")

mailbuf = []
for i in range(df.shape[0]):
    header, body = preprocess(df.text[i])
    mailbuf.append(parse_mail(header, body))

df = pd.DataFrame(mailbuf)
