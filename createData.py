# Projeto 2: Sistema de Plataforma de Jogos
# Feito por: Bruno Arthur Basso Silva 
#            Gabriela Molina Ciocci
# RA:        22.123.067-5 
#            22.222.032-9
# Disciplina: CC5232 - Banco de Dados
# Coordenador(a): Leonardo Anjoletto Ferreira
# Ciclo: 5° Semestre. 
# Curso: Ciência da Computação
# Universidade: Centro Universitário FEI

# Para começar o projeto, primeiro precisamos importar todas as bibliotecas que iremos utilizar.

import random

# Utilizamos a biblioteca random para poder criar valores randômicos.

# Abrimos os arquivos onde contém os nomes para jogos, conquistas e nomes de usuário.
# OBS: não esqueça de verificar se os arquivos estão na mesma pasta do programa!

archive_games = open("jogos.txt", "r")
archive_games_read = archive_games.read()
archive_games.close()

archive_achievements = open("conquistas.txt", "r")
archive_achievements_read = archive_achievements.read()
archive_achievements.close()

archive_names = open("usuarios.txt", "r")
archive_names_read = archive_names.read()
archive_names.close()

archive_companies = open("empresas.txt", "r")
archive_companies_read = archive_companies.read()
archive_companies.close()

# Formatação dos arquivos para facilitar o processo de criação dos itens.

archive_games_read = archive_games_read.split("\n")
archive_achievements_read = archive_achievements_read.split("\n")
archive_names_read = archive_names_read.split("\n")
archive_companies_read = archive_companies_read.split("\n")

# Criamos uma lista para variar os endereços de e-mail dos usuários.

emailTypes = ["@outlook.com", "@gmail.com", "@hotmail.com"]

# Lista que será responsável por armazenar os valores de ID existentes no programa.
existingID = []

# Lista que será responsável por armazenar os usuários, músicas, artistas e discos existentes no programa.

users = []
games = []
achievements = []
companies = []
game_user = []
achievement_game = []
achievement_user = []
friendship = []

# Função responsável por criar as datas em dia, mês e ano.

def createDate(type):
    day = random.randint(1, 28)
    mounth = random.randint(1, 12)

    if day < 10:
        day = "0" + str(day)
    if mounth < 10:
        mounth = "0" + str(mounth)

    # Tipo 1: para datas de nascimento.
    if type == 1:
        year = random.randint(1950, 2005)
    
    # Tipo 2: para datas de registro ou lançamento.
    if type == 2:
        year = random.randint(1997, 2024)

    # Tipo 3: para datas de aquisição
    if type == 3:
        year = random.randint(2013, 2024)

    return day, mounth, year


# Aqui estão loaclizadas as funções necessárias para que o programa possa ser executado com êxito.
# createUser: Cria um usuário.
# Começamos gerando um ID de usuário aleatório. Utilizamos random para gerar um número aleatório de 0 até o comprimento do arquivo
# de usuários e fazemos a comparação com os ID's existentes para evitar IDs duplicados. Enquanto o valor do ID existir na lista de
# ID's existentes, o programa irá alterar o valor. 

def createUser(archive):
    user_id = random.randint(0, len(archive) - 1)
    while user_id in existingID:
        user_id = random.randint(0, len(archive) - 1)

    # Obtém o nome do usuário a partir do arquivo de nomes usando o user_id gerado.
    name = archive[user_id]
    # Cria um email baseado no nome do usuário, substituindo espaços por underscores, convertendo para minúsculas e adicionando 
    # um domínio de email aleatório com base na lista de e-mails.
    email = name.replace(" ", "_").lower() + emailTypes[random.randint(0, len(emailTypes) - 1)]
    # Cria uma data de registro chamando a função createDate.
    born_date = createDate(1)

    # Adiciona o ID do usuário à lista de ID's existentes para evitar duplicatas no futuro.
    existingID.append(user_id)
    # Adiciona os detalhes do usuário na lista de usuários. As listas finais serão a biblioteca de jogos do usuário, as
    # conquistas que o usuário possui e a lista de amigos do usuário.
    users.append([user_id, name, email, born_date, [], [], []])
    # Retorna o ID, nome, email e data de registro do usuário recém-criado. Não é necessário, mas foi colocado para manter 
    # formalidade no código.
    return user_id, name, email, born_date

# createGame: Cria um jogo.
# Iniciamos novamente a geração de um ID de jogo aleatório e repetimos o processo anterior. 
# Enquanto o ID gerado já existir na lista de IDs existentes, o programa continuará a gerar um novo valor. 
# No final, somamos 50 com o resultado apenas para padronização e identificação de ID's de jogos.

def createGame(archive):
    game_id = random.randint(0, len(archive) - 1) + 50
    while game_id in existingID:
        game_id = random.randint(0, len(archive) - 1) + 50

    # Obtém o nome do jogo a partir do arquivo de jogos usando o game_id gerado.
    title = archive[game_id - 50]
    # Cria uma data de criação chamando a função createDate.
    release_date = createDate(2)
    # Obtém o nome da empresa a partir do arquivo de jogos usando o company_id gerado.
    company_id = companies[random.randint(0, len(companies) - 1)][0]
    # Adiciona o ID do jogo à lista de ID's existentes para evitar duplicatas no futuro.
    existingID.append(game_id)
    # Adiciona os detalhes do jogo na lista de jogos. A lista vazia no final irá conter o id das conquistas que pertencem ao
    # jogo.
    games.append([game_id, title, company_id, release_date, []])
    # Retorna o ID, nome e data de lançamento do jogo recém-criado. Não é necessário, mas foi colocado para manter formalidade 
    # no código.
    return game_id, title, company_id, release_date

# createCompany: Cria uma empresa.
# Iniciamos novamente a geração de um ID de empresa aleatório e repetimos o processo anterior. 
# Enquanto o ID gerado já existir na lista de IDs existentes, o programa continuará a gerar um novo valor.
# O ID padronizado para empresa são de valores maiores que 500.

def createCompany(archive):
    company_id = random.randint(0, len(archive) - 1) + 500
    while company_id in existingID:
        company_id = random.randint(0, len(archive) - 1) + 500
    
    # Obtém o nome da empresa a partir do arquivo de nomes de empresas usando o company_id gerado.
    name = archive[company_id - 500]
    # Cria uma data de fundação da empresa chamando a função createDate.
    fundation_date = createDate(2)

    # Adiciona o ID da empresa à lista de ID's existentes para evitar duplicatas no futuro.
    existingID.append(company_id)
    # Adiciona os detalhes da empresa na lista de empresas.
    companies.append([company_id, name, fundation_date])
    # Retorna o ID, nome e data de fundação.
    return company_id, name, fundation_date

# createAchievement: Cria uma conquista.
# Iniciamos novamente a geração de um ID de conquista aleatório e repetimos o processo anterior. 
# Enquanto o ID gerado já existir na lista de IDs existentes, o programa continuará a gerar um novo valor.
# O ID padronizado para conquistas são de valores maiores que 600.

def createAchievement(archive):
    achievement_id = random.randint(0, len(archive) - 1) + 600
    while achievement_id in existingID:
        achievement_id = random.randint(0, len(archive) - 1) + 600

    # Obtém o título da conquista a partir do arquivo de conquistas usando o achievement_id gerado.
    title = archive[achievement_id - 600]

    # Adiciona o ID da conquista à lista de ID's existentes para evitar duplicatas no futuro.
    existingID.append(achievement_id)
    # Adiciona os detalhes da conquista na lista de conquistas.
    achievements.append([achievement_id, title])
    # Retorna o ID, título e jogo da conquista recém-criada.
    return achievement_id, title

# createGameUser: Cria um jogo para o usuário.
# Iniciamos novamente a geração de um ID de jogo para um usuário aleatório e repetimos o processo anterior. 
# Enquanto o ID gerado já existir na lista de IDs existentes, o programa continuará a gerar um novo valor.
# O ID padronizado para playlists são de valores maiores que 1000 e menores que 2500.

def createGameUserLibrary():
    gameUser_id = random.randint(1000, 2500)
    while gameUser_id in existingID:
        gameUser_id = random.randint(1000, 2500)

    # Obtemos um usuário existente para adicionar um jogo.
    user = users[random.randint(0, len(users) - 1)]
    # Obtemos o id do usuário.
    user_id = user[0]
    # Criamos uma data de aquisição do jogo na conta do usuário
    acquisition_date = createDate(3)
    # Obtemos o id de um jogo já existente.
    game_id = games[random.randint(0, len(games) - 1)][0]

    # Verificamos se o jogo na qual queremos adicionar já contém na biblioteca, se sim, o programa gera novamente um ID de
    # jogo até que encontre um jogo que não contém na biblioteca do usuário.
    while game_id in user[4]:
        game_id = games[random.randint(0, len(games) - 1)][0]
    
    # Adiciona o id do jogo na biblioteca.
    user[4].append(game_id)
    
    # Adiciona o ID da música da playlist à lista de ID's existentes para evitar duplicatas no futuro.
    existingID.append(gameUser_id)
    # Adiciona os detalhes do jogo na biblioteca na lista de jogos da biblioteca.
    game_user.append([gameUser_id, user_id, game_id, acquisition_date])
    # Retorna o ID do usuário, o ID do jogo e a data de aquisição do jogo adicionada na biblioteca.
    return gameUser_id, user_id, game_id, acquisition_date

# createGameAchievement: Adiciona uma conquista para um jogo.
# Iniciamos novamente a geração de um ID de conquista para um jogo aleatório e repetimos o processo anterior. 
# Enquanto o ID gerado já existir na lista de IDs existentes, o programa continuará a gerar um novo valor.
# O ID padronizado para músicas em playlists são de valores maiores que 3000 e menores que 4500.

def createGameAchievement():
    gameAchievement_id = random.randint(3000, 4500)
    while gameAchievement_id in existingID:
        gameAchievement_id = random.randint(3000, 4500)

    # Obtemos um jogo existente para adicionar uma conquista.
    game = games[random.randint(0, len(games) - 1)]
    # Obtemos o id do jogo.
    game_id = game[0]
    # Obtemos o id de uma conquista já existente.
    achievement_id = achievements[random.randint(0, len(achievements) - 1)][0]

    # Verificamos se a conquista na qual queremos adicionar ao jogo já pertence a esse jogo, se sim, o programa gera novamente 
    # um ID de conquista até que encontre uma conquista que o jogo não possua.
    while achievement_id in game[4]:
        achievement_id = achievements[random.randint(0, len(achievements) - 1)][0]

    # Adiciona o id da conquista nas conquistas do jogo.
    game[4].append(achievement_id)

    # Adiciona o ID da conquista do jogo à lista de ID's existentes para evitar duplicatas no futuro.
    existingID.append(gameAchievement_id)
    # Adiciona os detalhes da conquista do jogo na lista de conquistas de jogos.
    achievement_game.append([gameAchievement_id, game_id, achievement_id])
    # Retorna o ID do jogo e o ID da conquista.
    return game_id, achievement_id


# createAchievementUser: Adiciona uma conquista para um usuário.
# Iniciamos novamente a geração de um ID de artista para a música aleatório e repetimos o processo anterior. 
# Enquanto o ID gerado já existir na lista de IDs existentes, o programa continuará a gerar um novo valor.
# O ID padronizado para músicas em playlists são de valores maiores que 5000 e menores que 6500.

def createUserAchievement():
    userAchievement_id = random.randint(5000, 6500)
    while userAchievement_id in existingID:
        userAchievement_id = random.randint(3000, 4500)

    # Obtemos um usuário existente para adicionar uma conquista.
    user = users[random.randint(0, len(users) - 1)]
    # Obtemos o id do usuário.
    user_id = user[0]
    # Obtemos um jogo já existente na biblioteca do usuário.
    game = user[4][random.randint(0, len(user[4]) - 1)]

    # Localizamos o jogo na lista de jogos existentes para poder obter todas as suas expecificações
    for videogame in games:
        if videogame[0] == game:
            game_id = game
            game = videogame
            break

    # Lista todas as conquistas possíveis do jogo.
    all_achievements = set(videogame[4])

    # Encontra as conquistas que o usuário já possui para esse jogo.
    user_achievements = {achievement[1] for achievement in user[5] if achievement[0] == game_id}

    # Conquistas restantes que o usuário ainda não possui.
    available_achievements = list(all_achievements - user_achievements)

    # Verifica se ainda há conquistas disponíveis para serem atribuídas ao usuário.
    if available_achievements:
        # Seleciona aleatoriamente uma conquista disponível.
        achievement_id = random.choice(available_achievements)
        # Adiciona a nova conquista ao usuário.
        user[5].append([game_id, achievement_id])
        # Adiciona o ID da conquista do jogo à lista de ID's existentes para evitar duplicatas no futuro.
        existingID.append(userAchievement_id)
        # Adiciona os detalhes da conquista do jogo na lista de conquistas de jogos.
        achievement_user.append([userAchievement_id, user_id, achievement_id, game_id])
        # Retorna o ID do jogo e o ID da conquista.
        return user_id, achievement_id, game_id
    
    else:
        return




# createFriendshipUser: Adiciona um usuário a outro usuário.
# Iniciamos novamente a geração de um ID de usuário para outro usuário aleatório e repetimos o processo anterior. 
# Enquanto o ID gerado já existir na lista de IDs existentes, o programa continuará a gerar um novo valor.
# O ID padronizado para músicas em playlists são de valores maiores que 7000 e menores que 8000.

def createFriendshipUser():
    usersFriendship_id = random.randint(7000, 8000)
    while usersFriendship_id in existingID:
        usersFriendship_id = random.randint(7000, 8000)

    # Obtemos dois usuários existentes para adicioná-los.
    user1 = users[random.randint(0, len(users) - 1)]
    user2 = users[random.randint(0, len(users) - 1)]

    # Verificamos se o usuário escolhido foi igual ou se os dois já são amigos.
    while user1 == user2 or user2[0] in user1[6]:
        user2 = users[random.randint(0, len(users) - 1)]

    # Se ele percorreu tudo e ainda assim caiu neste problema, retornamos pois não é possível adicionar neste caso.
    if user1 == user2 or user2[0] in user1[6]:
        return

    # Obtemos o id dos usuários.
    user1_id = user1[0]
    user2_id = user2[0]

    # Adicionamos os dois na lista de amigos um do outro.
    user1[6].append(user2_id)
    user2[6].append(user1_id)

    # Adiciona o ID da amizade à lista de ID's existentes para evitar duplicatas no futuro.
    existingID.append(usersFriendship_id)
    # Adiciona a amizade na lista de amigos.
    friendship.append([usersFriendship_id, user1_id, user2_id])
    # Retorna o ID dos dois usuários.
    return user1_id, user2_id

# Função responsável por mostrar no terminal todos os itens gerados pelo programa.

def printAllItems():
    for i in users:
        print("Usuário:     ", i)
    print()
    for i in games:
        print("Jogos:     ", i)
    print()
    for i in companies:
        print("Empresas:      ", i)
    print()
    for i in achievements:
        print("Conquistas:       ", i)
    print()

# Função responsável por gerar o arquivo txt que contém os códigos SQL para adicionar todos os itens no banco de dados.
# O nome do arquivo gerado será "codeSQL.txt" e será encontrado na mesma pasta em que o programa está localizado.

def createExportCode(users, games, companies, achievements, game_user, achievement_game, achievement_user, friendship):
    code_archive = open("codeSQL.txt", "w")
    code_archive.write("DELETE FROM conquista_usuario;\n")
    code_archive.write("DELETE FROM conquista_jogo;\n")
    code_archive.write("DELETE FROM biblioteca_jogo_usuario;\n")
    code_archive.write("DELETE FROM amizade;\n")
    code_archive.write("DELETE FROM conquista;\n")
    code_archive.write("DELETE FROM empresa;\n")
    code_archive.write("DELETE FROM jogo;\n")
    code_archive.write("DELETE FROM usuario;\n")


    for i in users:
        code_archive.write("INSERT INTO usuario (id, nome, email, data_registro) VALUES (" + str(i[0]) + ", '" + i[1] + "', '" + i[2] + "', '" + str(i[3][2]) + "-" + str(i[3][1]) + "-" + str(i[3][0]) + "');\n")
    
    for i in games:
        code_archive.write("INSERT INTO jogo (id, titulo, empresa_id, data_lancamento) VALUES (" + str(i[0]) + ", '" + i[1] + "', '" + str(i[2]) + "', '" + str(i[3][2]) + "-" + str(i[3][1]) + "-" + str(i[3][0]) + "');\n")

    for i in companies:
        code_archive.write("INSERT INTO empresa (id, nome, data_fundacao) VALUES (" + str(i[0]) + ", '" + i[1] + "', '" + str(i[2][2]) + "-" + str(i[2][1]) + "-" + str(i[2][0]) + "');\n")

    for i in achievements:
        code_archive.write("INSERT INTO conquista (id, titulo) VALUES (" + str(i[0]) + ", '" + i[1] + "');\n")

    for i in game_user:
        code_archive.write("INSERT INTO biblioteca_jogo_usuario (usuario_id, jogo_id, data_aquisicao) VALUES (" + str(i[1]) + ", " + str(i[2]) + ", '" + str(i[3][2]) + "-" + str(i[3][1]) + "-" + str(i[3][0]) + "');\n")

    for i in achievement_game:
        code_archive.write("INSERT INTO conquista_jogo (jogo_id, conquista_id) VALUES (" + str(i[1]) + ", " + str(i[2]) + ");\n")

    for i in achievement_user:
        code_archive.write("INSERT INTO conquista_usuario (usuario_id, conquista_id, jogo_id) VALUES (" + str(i[1]) + ", " + str(i[2]) + ", " + str(i[3]) + ");\n")

    for i in friendship:
        code_archive.write("INSERT INTO amizade (usuario1_id, usuario2_id) VALUES (" + str(i[1]) + ", " + str(i[2]) + ");\n")

    code_archive.close()
    print("---> Dados gerados com sucesso!")
    print("---> Nome do arquivo: codeSQL.txt")


# Menu para o terminal. Apenas para fins estéticos do código, não altera a lógica do programa.

def menu():
    print("|=================================================|")
    print("|         Sistema de Plataforma de Jogos          |")
    print("|=================================================|")
    print()
    print("|=====================[INFOS]=====================|")
    print("| Ciclo: 5° semestre                              |")
    print("| Curso: Ciência da Computação - FEI              |")
    print("| Disciplina: CC5232 - Banco de Dados             |")
    print("| Data: 19/11/2024                                |")
    print("|=================================================|")
    print()
    print("|================[DESENVOLVEDORES]================|")
    print("| Nomes: Bruno Arthur Basso Silva                 |")
    print("|        Gabriela Molina Ciocci                   |")
    print("| RA:    22.123.067-5                             |")
    print("|        22.222.032-9                             |")
    print("|=================================================|")
    print()
    print("|=================================================|")
    print("|            Aperte enter para iniciar!           |")
    print("|=================================================|")

# Função principal do programa.
# Aqui é onde toda a lógica é criada. 

def main():
    for _ in range(0, num_users):
        createUser(archive_names_read)
    for _ in range(0, num_companies):
        createCompany(archive_companies_read)
    for _ in range(0, num_games):
        createGame(archive_games_read)
    for _ in range(0, num_achievements):
        createAchievement(archive_achievements_read)
    for _ in range(0, num_gamesLibrary):
        createGameUserLibrary()
    for _ in range(0, num_gamesLibrary):
        createGameAchievement()
    for _ in range(0, num_gamesLibrary):
        createUserAchievement()
    for _ in range(0, num_Friendships):
        createFriendshipUser()

    # printAllItems()

    createExportCode(users, games, companies, achievements, game_user, achievement_game, achievement_user, friendship)


# Função de início do programa
def start():

    menu()
    input()
    main()

    print("Obrigado por utilizar!")
    print()

# Variáveis responsáveis por informar a quantidade de cada item o usuário gostaria de criar.
num_users = 32
num_games = 80
num_companies = 15
num_achievements = 201

# Quantidade de jogos que serão adicionados em bibliotecas.
num_gamesLibrary = 500
# Quantidade de conquistas que serão adicionados em jogos.
num_gameAchievement = 500
# Quantidade de conquistas que serão adicionados em usuários.
num_userAchievement = 500
# Quantidade de amizades feitas.
num_Friendships = 100

start()