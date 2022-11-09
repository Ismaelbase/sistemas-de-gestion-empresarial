DISFRAZ_DEFECTO="PECERA"
adversario=input("Quien tienes enfrente")

if adversario.lower()=="loki":
	misterio="Lady Loki"
elif adversario.lower()=="hulk":
	misterio="Thanos"
elif adversario.lower()=="thor":
	misterio="Odin"
elif adversario.lower()=="superman":
	misterio="Darkseid"
else:
    misterio=DISFRAZ_DEFECTO		
	
print(f"Misterio se disfraza:{misterio}")


