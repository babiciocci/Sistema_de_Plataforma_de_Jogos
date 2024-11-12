# Projeto 2: Sistema de Plataforma de Jogos

Feito por: Bruno Arthur Basso Silva | Gabriela Molina Ciocci 
<br>
RA: 22.123.067-5 | 22.222.032-9 
<br>
Disciplina: CC5232 - Banco de Dados
<br>
Coordenador(a): Leonardo Anjoletto Ferreira
<br>
Ciclo: 5° Semestre. 
<br>
Curso: Ciência da Computação
<br>
Universidade: Centro Universitário FEI

======================================================================================================================================================

## INFORMAÇÕES NECESSÁRIAS

Certifique-se de criar o Banco de Dados e respectivas tabelas antes de utilizar o código.
<br>
O arquivo que contém as Queries de criação de tabelas no Banco de Dados chama-se "Queries SQL para Criação de Tabelas.txt".
<br>
O arquivo que contém as Queries e Questões de Álgebra Relacional criadas para esse projeto chama-se "Queries SQL para Álgebra Relacional.txt".
<br>
#### Obs: foram feitas mais de 10 perguntas.

======================================================================================================================================================

## CÓDIGO PARA CRIAÇÃO DE DADOS ALEATÓRIOS

Para utilizar o código, é obrigatório que os arquivos de texto estejam na mesma pasta que o programa em Python, são eles:

   -> usuarios.txt
   <br>
   -> jogos.txt
   <br>
   -> empresas.txt
   <br>
   -> conquistas.txt

Ao baixar todos os arquivos e colocá-los no mesmo local, então você poderá executar o código.
<br>
Para definir a quantidade de cada item que será gerado, você precisará descer até as últimas linhas do código onde estão localizadas as variáveis que armazenam o valor de cada item que será gerado.
<br>
Após definir os valores desejados, você poderá rodar o programa.
<br>
Neste momento, será mostrado um menu contendo todas as informações dos alunos envolvidos e da disciplina.
<br>
Ao apertar enter, o programa irá gerar dados aleatórios e criará um novo arquivo de texto contendo todos os itens gerados:

   -> codeSQL.txt

Você poderá fechar o programa após a criação do arquivo.
<br>
Neste arquivo contém as Queries para adição dos dados no banco de dados.
<br>
Para adicioná-las, basta abrir o arquivo "codeSQL.txt", copiar todo seu conteúdo e colar no terminal do SQL.

======================================================================================================================================================

```mermaid
erDiagram
    USUARIO {
        int id PK
        string nome
        string email
        date data_registro
    }

    JOGO {
        int id PK
        string titulo
        int empresa_id FK
        date data_lancamento
    }

    EMPRESA {
        int id PK
        string nome
        int fundacao
    }

    CONQUISTA {
        int id PK
    }

    BIBLIOTECA_JOGO_USUARIO {
        int usuario_id FK
        int jogo_id FK
        date data_aquisicao
    }

    CONQUISTA_JOGO {
        int jogo_id FK
        int conquista_id FK
    }

    CONQUISTA_USUARIO {
        int usuario_id FK
        int conquista_id FK
        date data_desbloqueio
    }

    AMIZADE {
        int usuario_id FK
        int amigo_id FK
        date data_amizade
    }

    USUARIO ||--o| AMIZADE : "tem"
    USUARIO ||--|| BIBLIOTECA_JOGO_USUARIO : "tem"
    USUARIO ||--o| CONQUISTA_USUARIO : "desbloqueia"
    JOGO ||--o| BIBLIOTECA_JOGO_USUARIO : "pertence a"
    JOGO ||--o| CONQUISTA_JOGO : "tem conquista"
    CONQUISTA ||--o| CONQUISTA_USUARIO : "tem"
    CONQUISTA ||--o| CONQUISTA_JOGO : "associada a"
    EMPRESA ||--o| JOGO : "desenvolve"
```
