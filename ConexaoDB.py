import pymysql.cursors


class Conexao:

    def __init__(self):
        self.__conectado = False
        self.__msg = ""
    
    
    def conectar(self, ip, porta, usuario, senha, banco_de_dados):
        
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
        return self.__conexao
    
    def get_msg(self):
        return self.__msg

    def set_msg(self, msg):
        self.__msg = msg
    

    def guarda_dados(self, valor_emp, prazo_emp, email):

        if self.__conectado:
            with self.__conexao.cursor() as cursor:

                sql = "INSERT INTO `dados_emp` (`valor_emp`, `prazo_emp`, `email`) VALUES (%s, %s, %s)"
                cursor.execute(sql, (valor_emp, prazo_emp, email))

            self.__conexao.commit()
    