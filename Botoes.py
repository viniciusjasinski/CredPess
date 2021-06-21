from Interface import Tela


class Botao_main:
    
    """
    Classe que representa os eventos dos botoes apertados e suas acoes correspondentes
    Cada um dos metodos tem como retorno uma tela da classe interface retornando uma janela
    """
    @classmethod
    def seguir(cls):
        return Tela.tela_planos()

    @classmethod
    def emprestimo_pessoal(cls):
        return Tela.tela_emp_pessoal()

    @classmethod
    def emprestimo_imovel(cls):
        return Tela.tela_emp_imovel()

    @classmethod
    def emprestimo_autonomo_negativado(cls):
        return Tela.tela_emp_aut_neg()

    @classmethod
    def emprestimo_negativado(cls):
        return Tela.tela_emp_neg()

    @classmethod
    def contratar_servico(cls):
        return Tela.tela_contratar()

    @classmethod
    def faltaram_dados(cls, valor_do_emp, prazo_do_emp, email_do_emp):

        """ 
        Esse metodo tem como objetivo retornar a janela de preencher os dados adequadamente e recebe como
        parametros os dados inseridos para verificar qual dos dados esta preenchido incorretamente

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
        return Tela.tela_preencha_dados(valor_do_emp, prazo_do_emp, email_do_emp)
    