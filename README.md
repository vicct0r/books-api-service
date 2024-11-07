

# Livro-API: Serviço de Livraria Online

## Descrição

Este repositório contém a implementação de uma API que tem como objetivo disponibilizar livros específicos para o **projeto de livraria online** em andamento. A API será responsável por fornecer informações sobre os livros, incluindo a capa e o arquivo em formato PDF, utilizando o armazenamento em nuvem da **Amazon S3**.

## Motivação

Atualmente, não existem APIs em português que forneçam livros em formato PDF de forma estruturada e com imagens de capa para o público em geral. Portanto, decidi criar esse serviço para resolver uma necessidade específica: reunir e disponibilizar livros de domínio público (ou de uso permitido) para uma **livraria online**, permitindo que os usuários tenham acesso a livros em português sem a necessidade de procurar manualmente por cada um deles.

Essa abordagem facilita o desenvolvimento e a manutenção do projeto, aplicando o conceito de **responsabilidade única**. Em vez de sobrecarregar o sistema da livraria online com a parte de armazenamento e gerenciamento dos livros, essa API se torna responsável por gerenciar os dados dos livros, enquanto a livraria pode focar em exibir e organizar o conteúdo de maneira mais eficiente.

## Objetivo

O objetivo principal desta API é:

- Disponibilizar livros de domínio público ou com permissão de distribuição, incluindo informações como a **capa do livro** e o **arquivo PDF**.
- Utilizar o serviço de **Amazon S3** para o armazenamento de arquivos, garantindo escalabilidade e segurança.
- Permitir que a API seja consumida por outros projetos (como a livraria online), centralizando o gerenciamento dos livros em um único serviço.

## Funcionalidades

- **Armazenamento em nuvem**: Os livros serão armazenados no **Amazon S3** (imagens de capa e arquivos PDF), garantindo uma solução escalável e segura.
- **Endpoint único**: A API terá um único endpoint que permitirá buscar e acessar os dados dos livros.
- **Integração com Django**: A API está projetada para integrar-se facilmente com o front-end do sistema da livraria online, onde os dados dos livros serão exibidos.

## Estrutura do Projeto

Este repositório contém a implementação de uma API simples com os seguintes componentes:

- **Endpoints** para acessar os dados dos livros.
- **Integração com o Amazon S3** para o armazenamento dos arquivos.
- **Controle e validação** dos dados dos livros, incluindo a verificação da existência do arquivo e da capa do livro.

## Próximos Passos

*Até o final do desenvolvimento do projeto, a API passará a contar com as seguintes funcionalidades adicionais:*

- **Autenticação e Autorização**: Será implementado um sistema de autenticação para garantir que apenas usuários com permissão de **staff** possam adicionar ou alterar livros na plataforma.
- **Gestão de Usuários**: Será possível gerenciar os privilégios de usuários dentro da API, permitindo ações de leitura e modificação apenas por aqueles que possuem a permissão de **staff**.
- **Testes e Melhorias**: Implementação de testes automatizados para garantir a estabilidade e segurança da API.
- **Documentação Completa**: Será criada uma documentação adicional para detalhar o uso da autenticação e as permissões de usuários no sistema.

*Essas funcionalidades estão em andamento e serão integradas à medida que o desenvolvimento do projeto avance.*
