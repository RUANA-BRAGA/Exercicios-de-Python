Frase = str("alô  mundo").strip()
print(Frase.capitalize().replace(" ",",",1) +"!","") #primeira letra da palavra em maiuscula
print(Frase.upper().replace("ô","O"),"","") #palavra toda maiuscula
print(Frase.lower().replace(" ",",",1)+".","") #palavra toda minuscula
print(Frase.replace("alô","ALo").replace("do","DO"),"")#palavra com as duas primeiras e as duas ultimas em maiusculo
print(Frase.capitalize().replace("m","M").replace(" ",",",1) +"!","") #cada palavra tem a primeira letra maiuscula

