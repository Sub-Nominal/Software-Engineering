msg = str(input('Enter Text: '))
def convert():
    Newmsg = str(msg.replace(':)', "\N{slightly smiling face}" ))
    Newmsg = str(Newmsg.replace(':(', "\U0001F641" ))
    print( Newmsg)
convert()
