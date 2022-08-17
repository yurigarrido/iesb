users = []


def create_user(nome, email, telefone, twitter, instagram):

    new_user = {
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "twitter": twitter,
        "instagram": instagram,
    }
    users.append(new_user)

    print(
        f" \n"
        f"Nome: {nome}\n"
        f"Email: {email}\n"
        f"Telefone: {telefone}\n"
        f"Twitter: {twitter}\n"
        f"Instagram: {instagram}\n"
        f"Usuário cadastrado.\n"
    )


def get_user_by_name():
    filter_name = input("UserName do usuário: ")

    for user in users:
        if user["nome"] == filter_name:
            print(
                f" \n"
                f"Nome: {user['nome']}"
                f"Email: {user['email']}"
                f"Telefone: {user['telefone']}"
                f"Twitter: {user['twitter']}"
                f"Instagram: {user['instagram']}"
                f"Usuário alterado."
            )


def edit_user():
    filter_name = input("Nome do usuário: ")

    for user in users:
        if user["nome"] == filter_name:
            print(user)

    edit = input("Deseja atualizar esse usuário?\n [s]im ou [n]ão\n    ")

    if edit == "s":
        nome = input("Novo Nome do usuário: ")
        email = input("Novo Email do usuário: ")
        telefone = input("Novo Telefone do usuário: ")
        twitter = input("Novo Twitter do usuário: ")
        instagram = input("Novo Instagram do usuário: ")

        for user in users:
            if user["nome"] == filter_name:
                user["nome"] = nome
                user["email"] = email
                user["telefone"] = telefone
                user["twitter"] = twitter
                user["instagram"] = instagram
                print(
                    f" \n"
                    f"Nome: {nome}\n"
                    f"Email: {email}\n"
                    f"Telefone: {telefone}\n"
                    f"Twitter: {twitter}\n"
                    f"Instagram: {instagram}\n"
                    f"Usuário alterado.\n"
                )


def delete_user():
    filter_name = input("Nome do usuário: ")

    for i in range(len(users)):
        if users[i]["nome"] == filter_name:
            del users[i]
            break
    print("Usuário removido.")


while True:

    option = input(
        "O que você deseja?\n"
        "1 - Inserir um novo contato\n"
        "2 - Fazer uma consulta de um nome já cadastrado\n"
        "3 - Fazer alteração em um contato previamente cadastrado\n"
        "4 - Remover um contato previamente cadastrado\n"
        "5 - Gerar relatório\n"
        "6 - Gerar relatório simples\n"
        "7 - Sair\n"
    )

    if option == "1":
        nome = input("Nome do usuário: ")
        email = input("Email do usuário: ")
        telefone = input("Telefone do usuário: ")
        twitter = input("Twitter do usuário: ")
        instagram = input("Instagram do usuário: ")
        create_user(nome, email, telefone, twitter, instagram)

    elif option == "2":
        get_user_by_name()

    elif option == "3":
        edit_user()

    elif option == "4":
        delete_user()

    elif option == "5":
        print(
            "\n{:<15} {:<15} {:<15} {:<25} {:<15} {:<15}".format(
                "Nro", "Nome", "Telefone", "email", "Twitter", "Instagram"
            )
        )
        for i in range(len(users)):
            print(
                f"{i:<15} {users[i]['nome']:<15} {users[i]['telefone']:<15} {users[i]['email']:<25} {users[i]['twitter']:<15} {users[i]['instagram']:<15}"
            )
        print(" \n")

    elif option == "6":

        for i in range(len(users)):
            print(
                f"{users[i]['nome']},{users[i]['telefone']},{users[i]['email']},{users[i]['twitter']},{users[i]['instagram']}"
            )
    else:
        break
