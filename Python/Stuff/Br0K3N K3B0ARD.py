msg = input('What did she say? ')
nmsgo = msg.replace( '###' , 'o')
nmsge = nmsgo.replace( '##' , 'e')
nmsga = nmsge.replace( '%%' , 'a')
print(f'She meant to say: {nmsga}')