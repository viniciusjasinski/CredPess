import pymysql.cursors


class Conexao:
    
    """
    Classe que representa uma conexão com o banco de dados (DB)
    """

    def __init__(self):
        self.__conectado = False
        self.__msg = ""
    

    def conectar(self, ip, porta, usuario, senha, banco_de_dados):

        """
        Realiza a tentativa de conectar ao banco de dados no servidor dos parâmetros recebidos
        Caso a conexao não seja bem sucedida, retorna uma exceção e mostra no terminal

        Parametros
        ----------
        ip : str,
            O endereço IP do servidor onde está o DB
        porta: int, 
            Porta usada pelo DB depara receber as conexões 
        usuario: str,
            O nome do usuario do DB
        senha: str,
            A senha do DB
        banco_de_dados: str,
            O nome do DB utilizado
        ------
        """
        conexao = None
        porta = int(porta)

        try:
            conexao = pymysql.connect(
                host = ip,
                port = porta,
                user = usuario,
                password = senha,
                database = banco_de_dados,
                cursorclass = pymysql.cursors.DictCursor,
                ssl={"fake_flag_to_enable_tls":False})     

        except:
            self.__msg = "\n Erro ao conectar com o Banco de Dados!"
            print(self.get_msg())

        else:
            self.__conexao = conexao
            self.__conectado = True
            self.__msg = "\n Conectado ao Banco de Dados com sucesso!"
            print(self.get_msg())
            
    
    def desconectar(self):

        """
        Realiza a tentativa de desconectar o DB.
        Caso a desconexao ja tenha sido realizada mostra que ela ja foi realizada mostrando no terminal
        """
        if self.__conectado:
            try:
                self.__conexao.close()
                self.__conectado = False
                self.__msg = "\n Desconectado com sucesso!"
                print(self.get_msg())

            except:
                self.__msg = "\n Erro ao desconectar do Banco de Dados!"
                print(self.get_msg())

        else:
            self.__msg = "\n Banco de Dados já estava desconectado!"
            print(self.get_msg())
        
        
    def get_conexao(self):

        """
        Permite mostrar se a conexao com o DB esta ativa ou nao
        """
        return self.__conexao
    
    def get_msg(self):

        """
        Permite mostrar a mensagem desejada no terminal
        """
        return self.__msg

    def set_msg(self, msg):

        """
        Permite poder modificar a mensagem mostrada no terminal
        """
        self.__msg = msg
    

    def guarda_dados(self, valor_emp, prazo_emp, email):

        """
        Realiza a tentativa de guardar os dados no DB com os parâmetros recebidos
        Caso a conexao esteja ativa realizar o comando de insercao de dados no DB conectado

        Ao final realiza um commit para atualizar os valores novos no DB

        Parametros
        ----------
        valor_emp : int,
            Representa o valor do emprestimo solicitado
        prazo_emp: int, 
            Prazo para realizar o pagamento do emprestimo 
        email: str,
            Corresponde ao email do usuario para terminar as coletas de informacoes
        ------
        """
        if self.__conectado:
            with self.__conexao.cursor() as cursor:

                sql = "INSERT INTO `dados_emp` (`valor_emp`, `prazo_emp`, `email`) VALUES (%s, %s, %s)"
                cursor.execute(sql, (valor_emp, prazo_emp, email))

            self.__conexao.commit()
    