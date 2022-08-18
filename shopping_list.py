shopping = {
    "piekarnia" : ["chleb", "bułki", "pączek"],
    "warzywniak" : ["marchew", "seler", "rukola"]
}

amount = len(shopping['piekarnia']) + len(shopping['warzywniak'])
for i in range(len(shopping['piekarnia'])):
    shopping['piekarnia'][i] = shopping['piekarnia'][i].capitalize()
for j in range(len(shopping['warzywniak'])):
    shopping['warzywniak'][j] = shopping['warzywniak'][j].capitalize()
for sklep, produkty in shopping.items():
    print(f"Idę do {sklep.title()} i kupuję tam {produkty}")
print(f"W sumie kupuję {amount} produktów")