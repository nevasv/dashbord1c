data = b'\x00\x00\x04e'

# Try decoding as UTF-8 (may fail if not valid UTF-8)
try:
    text = data.hex()
    print("Decoded as UTF-8:", text)
except UnicodeDecodeError:
    print("Not valid UTF-8.")

# Try decoding as Latin-1 (ISO-8859-1)
text_latin1 = data.decode('latin-1')
print("Decoded as Latin-1:", text_latin1)