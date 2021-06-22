<h1 align="center">Processo Seletivo Proway - Serasa</h1>


<!-- Tabela de Conteúdos -->
<details open="open">
  <summary>Tabela de Conteúdos</summary>
  <ol>
    <li>
      <a href="#sobre-o-projeto">Sobre o Projeto</a>
    </li>
    <li>
      <a href="#primeiros-passos">Primeiros Passos</a>
      <ul>
        <li><a href="#pré-requisitos">Pré Requisitos</a></li>
        <li><a href="#instalação">Instalação</a></li>
      </ul>
    </li>
    <li><a href="#como-usar">Como Usar</a></li>
    <li><a href="#contato">Contato</a></li>
  </ol>
</details>



<!-- Sobre o Projeto -->
## Sobre o Projeto

Este projeto foi desenvolvido como desafio para o processo seletivo do Serasa Experian, realizado pela ProWay. O projeto consiste em fornecer acesso a alternativas e propostas para contratar um empréstimo pessoal. Dentre os requisitos estavam:

* Listar as ofertas de crédito de acordo com o descritivo técnico.
*  Detalhar a oferta do usuário ao momento de escolha.
*  Apresentar a revisão das informações e permitir que o usuário realize a contratação do empréstimo.

Além disso, para o projeto foi de livre escolha a linguagem de programação utilizada e para este código foi utilizado o Python na sua versão 3.8.6. Disponível em:

* [Python](https://www.python.org/)


<!-- Primeiros Passos -->
## Primeiros Passos

Para rodar o código fornecido em seu pleno funcionamento é necessário utilizar de uma conexão com a internet, pois ele realiza a comunicação com um banco de dados para armazenamento das informações, além disso é necessário que todos os arquivos se encontrem na mesma pasta.

### Pré Requisitos

Esta é a lista de bibliotecas do Python que são necessárias para o funcionamento do código.

* [PySimpleGUI](https://pypi.org/project/PySimpleGUI/)
  ```sh
  pip install PySimpleGUI
  ```
* [PyMySQL](https://pypi.org/project/PyMySQL/)
  ```sh
  pip install PyMySQL
  ```

### Instalação

1. Baixe uma IDE que possa rodar o Python como o [Visual Studio Code](https://code.visualstudio.com/)
2. Dê um Clone no repositório do Github através do comando no terminal
   ```sh
   git clone https://github.com/viniciusjasinski/CredPess.git
   ```
3. Instale as duas bibliotecas necessárias demonstradas nos <a href="#prerequisitos">Pré Requisitos</a>

Esses primeiros passos servem para a compilação e funcionamento adequado do código, contudo caso deseje acessar também o banco de dados e visualizar os registros do dados coletados é necessário seguir os próximos passos demonstrados.

4. Baixe um programa que possua leitura e conexão com o banco de dados online como o [MySQL Workbench](https://www.mysql.com/products/workbench/)

5. Adicione uma nova conexão conforme os dados de login fornecidos no código Main.

<!-- Como Usar -->
## Como Usar

O código funciona de maneira bem intuitiva, inicialmente é apresentada uma tela de apresentação na qual para prosseguir basta pressionar o botão "Seguir". 

<p align="center">
<img src="https://user-images.githubusercontent.com/73205357/122987290-d0589500-d376-11eb-8669-865314b6d89e.png" />
</p>

Assim que apertado, o botão abrirá uma nova janela, denominada Planos, com as 4 diferentes opções de créditos e suas respectivas vantagens. As opções que possuem um botão para ser apertado são "Empréstimo pessoal Online", "Empréstimo com garantia de imóvel", "Empréstimo para autônomo negativado" e "Empréstimo para negativado", assim que decidida a opção mais adequada para o seu perfil basta pressionar o respectivo botão com o plano desejado.

<p align="center">
<img src="https://user-images.githubusercontent.com/73205357/122987324-db132a00-d376-11eb-819f-d9bd889a4097.png" />
<img src="https://user-images.githubusercontent.com/73205357/122987365-e6feec00-d376-11eb-9733-8c97288f7043.png" />
</p>

Após ter sido selecionado o plano, é apresentado um maior detalhamento sobre como funcionará o empréstimo, assim como seu descritivo técnico. Caso esse não seja o plano desejado é possível apertar o botão "Voltar" para retornar à tela de Planos. Assim que decidido o plano adequado é necessário preencher o campo do valor em reais do empréstimo desejado, a quantidade de meses que levará até finalizar o pagamento do empréstimo e o seu e-mail para poder coletar as informações restantes necessárias, destaca-se que devido a esse código funcionar apenas para o desafio da ProWay nenhuma dessas informações terá um uso futuro. Além disso, enquanto não preenchidas adequadamente as informações, não será possível realizar a contratação do serviço. 

<p align="center">
<img src="https://user-images.githubusercontent.com/73205357/122988084-bb303600-d377-11eb-8966-54b41cefc69f.png" />
</p>

Após preenchidos os valores de empréstimo e seu prazo com números inteiros, além do e-mail não ter sido preenchido com apenas números será possível abrir a tela de contratação e clicar no botão de finalizar. Caso tenha sido preenchida alguma informação de maneira equivocada, basta fechar a janela de finalizar contratação e corrigir essas informações.

<p align="center">
<img src="https://user-images.githubusercontent.com/73205357/122987447-fc741600-d376-11eb-88f4-4b403cc4bf13.png" />
</p>

Assim que finalizado, o programa é encerrado e os dados preenchidos são armazenados em um banco de dados online, guardando assim as informações do empréstimo solicitado, assim como o e-mail para entrar em contato.

<!-- Contato -->
## Contato

Vinícius César Jasinski - vinicius.jasinski@gmail.com

Link do Projeto: [https://github.com/viniciusjasinski/CredPess](https://github.com/viniciusjasinski/CredPess)
