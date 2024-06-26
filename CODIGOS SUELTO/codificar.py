msg = 'd89%l++r19o07W*o22332l234l234e234H'

dec = ''

for i in msg:
    if i.isalpha():
        dec+=i
        if i.isupper():
            dec+=' '
dec = dec[::-1]
dec = dec[1:]