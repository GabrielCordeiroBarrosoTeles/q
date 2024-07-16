'''
GRUPO 3

🚀 Desafio [005] Aplicação de Gestão de Tarefas

O objetivo do desafio é realizar a modelagem de um banco de dados simples e desenvolver uma aplicação de gestão de tarefas.

Deverá ser projetada uma aplicação onde os usuários podem criar, visualizar, atualizar e excluir suas tarefas. Cada tarefa pode ter um título, uma descrição, uma data de criação e uma data de conclusão, siga as orientações abaixo para concluir o desafio.

1.Identifique as Entidades e os Atributos:
    - Identifique as entidades que participam do processo, os seus atributos e o relacionamento entre elas.

2. Crie as Tabelas no Banco de Dados:
    - Utilize um SGBD de sua escolha (por exemplo, SQLite, MySQL, PostgreSQL) para criar as tabelas conforme o diagrama desenhado.

3.Consulte no Banco de Dados:
    - Crie um script que realize as operações básicas de um CRUD (Create, Read, Update, Delete) nas tabelas criadas.
    
4. Apresentação
    - Na avaliação serão cobrados os seguintes itens:
        1. Banco modelado
        2. Script
    - Organização de código e boas práticas serão exigidas.

Obs: Não será necessária uma interface, a aplicação poderá funcionar somente pelo terminal
'''
import mysql.connector
from datetime import datetime

# Conexão com o banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bd_cordeiro"
)
cursor = conexao.cursor()

while True:
    # Menu de opções
    opcao = int(input("Lista de Tarefas\n1-Criar \n2-Exibir \n3-Editar \n4-Deletar \n5-Encerrar\nEscolha uma opção: "))

    if opcao == 1:
        # Criar tarefa
        titulo = input("Informe o título da tarefa: ")
        descricao = input("Informe a descrição da tarefa: ")
        
        data_criacao = input("Informe a data de criação (dd/mm/yyyy): ")
        data_criacao = datetime.strptime(data_criacao, "%d/%m/%Y").date()
        
        data_conclusao = input("Informe a data de conclusão (dd/mm/yyyy): ")
        data_conclusao = datetime.strptime(data_conclusao, "%d/%m/%Y").date()
        
        # Verificação das datas
        if data_criacao > data_conclusao:
            print("Erro: A data de criação não pode ser maior que a data de conclusão.")
        else:
            comando = f"INSERT INTO tarefa (titulo, descricao, data_criacao, data_conclusao) VALUES ('{titulo}', '{descricao}', '{data_criacao}', '{data_conclusao}')"
            cursor.execute(comando)
            conexao.commit()
            print("Tarefa criada com sucesso.")

    elif opcao == 2:
        # Exibir todas as tarefas
        comando = 'SELECT * FROM tarefa'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for tarefa in resultado:
            id, titulo, descricao, data_criacao, data_conclusao = tarefa
            data_criacao = data_criacao.strftime("%d/%m/%Y")
            data_conclusao = data_conclusao.strftime("%d/%m/%Y")
            print(f"\nTítulo: {titulo}, \nDescrição: {descricao}, \nData de Criação: {data_criacao}, \nData de Conclusão: {data_conclusao}")

    elif opcao == 3:
        # Editar tarefa
        pesq_id = int(input("Informe o ID da tarefa que deseja editar: "))
        campo = input("Qual campo deseja atualizar (titulo, descricao, data_criacao, data_conclusao)? ")
        novo_valor = input(f"Informe o novo valor para {campo}: ")
        
        if campo in ["titulo", "descricao"]:
            novo_valor = f"'{novo_valor}'"  # Adiciona aspas para valores de texto
        elif campo in ["data_criacao", "data_conclusao"]:
            novo_valor = datetime.strptime(novo_valor, "%d/%m/%Y").date()
            novo_valor = f"'{novo_valor}'"
        
        comando = f"UPDATE tarefa SET {campo}={novo_valor} WHERE id={pesq_id}"
        cursor.execute(comando)
        conexao.commit()
        print("Tarefa atualizada com sucesso.")

    elif opcao == 4:
        # Deletar tarefa
        pesq_id = int(input("Informe o ID da tarefa que deseja deletar: "))
        comando = f"DELETE FROM tarefa WHERE id={pesq_id}"
        cursor.execute(comando)
        conexao.commit()
        print("Tarefa deletada com sucesso.")

    elif opcao == 5:
        # Encerrar
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida!")

# Fecha a conexão
cursor.close()
conexao.close()
