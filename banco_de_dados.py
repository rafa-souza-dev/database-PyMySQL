import pymysql


def criar_database(nome):
    conexao = pymysql.connect(
        host="localhost",
        user="root",
        passwd=""
    )
    cursor = conexao.cursor()

    try:
        cursor.execute(f"CREATE DATABASE {nome}")
        print("Database criado")
    except:
        print("Algum erro ocorreu!")


def criar_tabela_ou_inserir(database, nome_da_tabela, nome_atributo1, nome_atributo2, id=None, atributo1=None,
                            atributo2=None):
    conexao = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        database=database
    )
    cursor = conexao.cursor()

    escolha = input("CONFIRMANDO / Deseja criar uma tabela ou inserir dados em uma ja existente? criar/inserir: "
                    "").upper()

    if escolha == "CRIAR":
        if id == None:
            cursor.execute(f"CREATE TABLE {nome_da_tabela}("
                           f"id INT AUTO_INCREMENT PRIMARY KEY,"
                           f"{nome_atributo1} VARCHAR(255), {nome_atributo2} VARCHAR(255))")
        else:
            cursor.execute(f"CREATE TABLE {nome_da_tabela}("
                           f"id({id}) INT AUTO_INCREMENT PRIMARY KEY,"
                           f"{nome_atributo1} VARCHAR(255), {nome_atributo2} VARCHAR(255))")
    if escolha == "INSERIR":
        if atributo1 and atributo2:
            inserir = f'INSERT INTO {nome_da_tabela}({nome_atributo1},{nome_atributo2}) VALUES (%s,%s)'
            atributos = (atributo1, atributo2)
            cursor.execute(inserir, atributos)

    conexao.commit()


def mostrar_tabela(database, nome_da_tabela):
    conexao = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        database=database
    )
    cursor = conexao.cursor()
    cursor.execute(f"SELECT * FROM {nome_da_tabela}")
    resultado = cursor.fetchall()

    for dado in resultado:
        print(dado)


def deletar_um_dado(database, nome_da_tabela, nome_atributo1, atributo1):
    conexao = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        database=database
    )

    cursor = conexao.cursor()
    deletar = f"DELETE FROM {nome_da_tabela} WHERE {nome_atributo1} = '{atributo1}'"

    cursor.execute(deletar)

    conexao.commit()

    print(cursor.rowcount, "Dado(s) apagado(s)!")


def deletar_uma_tabela(database, nome_da_tabela):
    conexao = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        database=database
    )
    cursor = conexao.cursor()

    cursor.execute(f"DROP TABLE {nome_da_tabela}")

    print("Tabela apagada")


def mostrar_menu():
    print("---------------------------------")
    print("0 - Criar um Banco de Dados")
    print("1 - Criar Tabela ou Inserir Dados")
    print("2 - Mostrar Tabela")
    print("3 - Deletar uma Tabela")
    print("4 - Deletar um Dado específico")
    print("5 - Finalizar Programa")
    print("---------------------------------")


if __name__ == "__main__":
    print("**********")
    print("BEM VINDO!")
    print("**********")
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")
        if escolha == "0":
            nome_do_banco = input("Qual será o nome do Database? ")
            criar_database(nome_do_banco)
        elif escolha == "1":
            escolher_banco = input("A qual database se refere? ")
            nome_da_tabela = input("Digite o nome da tabela: ")
            nome_atributo1 = input("Digite o nome do primeiro atributo: ")
            nome_atributo2 = input("Digite o nome do segundo atributo: ")
            escolha2 = input("Deseja criar uma tabela ou inserir dados em uma ja existente? criar/inserir: ").upper()

            if escolha2 == "CRIAR":
                criar_tabela_ou_inserir(escolher_banco, nome_da_tabela, nome_atributo1, nome_atributo2)
                print("Concluído!")
            elif escolha2 == "INSERIR":
                atributo1 = input(f"Diga o {nome_atributo1}: ")
                atributo2 = input(f"Diga o {nome_atributo2}: ")
                criar_tabela_ou_inserir(escolher_banco, nome_da_tabela, nome_atributo1, nome_atributo2,
                                        atributo1=atributo1, atributo2=atributo2)
                print("Concluído!")
        elif escolha == "2":
            nome_do_banco = input("A qual database se refere? ")
            nome_da_tabela = input("Diga o nome da tabela: ")
            mostrar_tabela(nome_do_banco, nome_da_tabela)
        elif escolha == "3":
            nome_do_banco = input("A qual database se refere? ")
            nome_da_tabela = input("Diga o nome da tabela: ")
            deletar_uma_tabela(nome_do_banco, nome_da_tabela)
        elif escolha == "4":
            nome_do_banco = input("A qual database se refere? ")
            nome_da_tabela = input("Diga o nome da tabela: ")
            nome_atributo1 = input("Digite o nome do primeiro atributo: ")
            atributo1 = input(f"Diga o {nome_atributo1}: ")
            deletar_um_dado(nome_do_banco, nome_da_tabela, nome_atributo1, atributo1)
        elif escolha == "5":
            break
        else:
            print("Opção inválida!")
            continue
    print("Até mais!")
