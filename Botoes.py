from Interface import Tela


class Botao_main:
    
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
        return Tela.tela_preencha_dados(valor_do_emp, prazo_do_emp, email_do_emp)
    