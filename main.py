import quopri

def quopri_encoding(matn):
    encoded_matn = quopri.encodestring(matn.encode('utf-8')).decode('utf-8')
    return encoded_matn

matn = "Hello, World!"
encoded_matn = quopri_encoding(matn)
print(encoded_matn)
```

```python
import quopri

def quopri_decoding(encoded_matn):
    decoded_matn = quopri.decodestring(encoded_matn.encode('utf-8')).decode('utf-8')
    return decoded_matn

encoded_matn = "Hello, World!"
decoded_matn = quopri_decoding(encoded_matn)
print(decoded_matn)
