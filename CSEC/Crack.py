from string import digits, ascii_letters, punctuation, ascii_lowercase
from datetime import time, timezone, tzinfo, datetime
x=datetime.now()
for i in ascii_letters: 
    for j in ascii_letters: 
        for k in ascii_letters: 
            for l in ascii_letters: 
                print(i, j, k, l)
y=datetime.now()
print(y-x)