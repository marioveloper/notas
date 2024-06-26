def spell(txt):
    if len(txt)==1:
        print(txt)
    else:
        print(txt[len(txt)-1])
        spell(txt[:-1])

txt = 'HELLO'
spell(txt)

#print(dir(txt))