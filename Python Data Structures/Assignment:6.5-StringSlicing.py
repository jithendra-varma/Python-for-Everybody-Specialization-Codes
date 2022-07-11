text = "X-DSPAM-Confidence:    0.8475"
no = text.find(':')
a = text[no+1:]
b = a.strip()
c = float(b)
print(c)