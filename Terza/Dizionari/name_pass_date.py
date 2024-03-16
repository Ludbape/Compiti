if __name__ == '__main__':
    usr = input('Inserisci il tuo nome: ')
    passwd = input('Inserisci la tua password: ')
    data = input('Inserisci la tua data di registrazione: ')
    dic = {'nome': usr, 'password': passwd, 'data': data}
    print("Vuoi iscriverti alla newsletter?")
    print("1. Si")
    print("2. No")
    scelta = input()
    while scelta != '1' and scelta != '2':
        print("Scelta non valida!!\nRiprova")
        scelta = input()
    if scelta == '1':
        email = input('Inserisci la tua email: ')
        dic['email'] = email
    else:
        print("Non ti iscrivi alla newsletter")
    print("Grazie per esserti iscritto!!")
    print(f"Nome: {dic["nome"]}")
    print(f"Data: {dic["data"]}")
    if 'email' in dic:
        print(f"Email: {dic["email"]}")
