import PySimpleGUI as sg
from Interface import Tela
from Botoes import Botao_main
from ConexaoDB import Conexao

"""
Parte principal do codigo, realiza as solicitacoes de comunicacao com as outras classes
Para executar o codigo deixe essa pagina selecionada

Parametros
----------
con : Objeto utilizado para realizar a coneccao com o banco de dados
window : Recebe a tela inicial gerada pelo programa 
------
"""

con = Conexao() 

con.conectar('mysqlserver.ck7rcqskurbo.us-east-2.rds.amazonaws.com', # ip
             3306, # porta
             'admin', # usuário
             'admin123', # senha
             'dbdadosemprestimo') # nome do BD

window = Tela.tela()

def is_number(s):
    
    """
    Metodo utilizado se o parametro recebido e' um numero
    
    Parametro
    ----------
    s : str,
        Parametro que recebe o email_db para verificar se ele e' apenas numerico 
    ------
    """
    try:
        float(s)
        return True
    except ValueError:
        return False

def janela_contratacao(tela_contratacao):

    """
    Metodo utilizado para gerar a janela de contratacao
    
    Parametro
    ----------
    tela_contratacao : Janela gerada conforme o botao apertado na tela de planos 
    ------

    Esse metodo esconde a janela de planos e aguarda que sejam preenchidos os dados de valor_emp,
    prazo_meses e email

    Caso seja apertado o botao de voltar ele mostra novamente a tela de planos e fecha essa tela
    Caso seja apertado o botao de contratar ele verifica se os dados foram preenchidos corretamente
    e caso tenham sido preenchidos adequadamente abre a janela para finalizar a contratacao e guardar
    no banco de dados
    """
    tela_planos.Hide()

    while (True):
        event_contratacao, values_contratacao = tela_contratacao.read()

        if event_contratacao == sg.WIN_CLOSED:
            tela_contratacao.close()
            tela_planos.close()
            window.close()
            break 

        if event_contratacao == 'voltar':
            tela_planos.UnHide()
            tela_contratacao.close()
            break 

        if event_contratacao == 'contratar':

            try:
                valor_emp_db = int(values_contratacao['valor_emp'])
                prazo_meses_db = int(values_contratacao['prazo_meses'])
                email_db = values_contratacao['email']
                if not email_db or is_number(email_db) == True:
                    raise ValueError
                
            except ValueError:
                tela_erro = Botao_main.faltaram_dados(values_contratacao['valor_emp'], values_contratacao['prazo_meses'], values_contratacao['email'])
                while (True):
                    event_erro, values_erro = tela_erro.read()
                    if event_erro == sg.WIN_CLOSED:
                        tela_erro.close()
                        break 

                    if event_erro == 'ok':
                        tela_erro.close()
                        break
            
            else:
                tela_finalizar = Botao_main.contratar_servico()

                while (True):
                    event_finalizar, values_finalizar = tela_finalizar.read()
                    if event_finalizar == sg.WIN_CLOSED:
                        tela_finalizar.close()
                        break 

                    if event_finalizar == 'finalizar':
                        con.guarda_dados(valor_emp_db, prazo_meses_db, email_db)
                        con.desconectar()
                        tela_finalizar.close()
                        tela_contratacao.close()
                        tela_planos.close()
                        window.close()
                        break


while (True):

    """
    Enquanto a janela window estiver aberta o codigo executa essas tarefas
    A tela aguarda enquanto nao foi acionado nenhum evento, ou seja nenhum botao tenha sido pressionado
    Assim que pressionado o botao de seguir ele esconde a janela window e abre a janela de planos
    Aguardando com isso um novo evento e abrindo a janela conforme o plano selecionado
    """
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        window.close()
        break

    if event == 'botao_seguir':

        tela_planos = Botao_main.seguir()
        window.Hide()

        while (True):
            event_planos, values_planos = tela_planos.read()

            if event_planos == sg.WIN_CLOSED:
                tela_planos.close()
                window.close()
                break

            if event_planos == 'botao_emp_pessoal':
                tela_emp_pessoal = Botao_main.emprestimo_pessoal()
                janela_contratacao(tela_emp_pessoal)

            if event_planos == 'botao_emp_imovel':    
                tela_emp_imovel = Botao_main.emprestimo_imovel()
                janela_contratacao(tela_emp_imovel)

            if event_planos == 'botao_emp_aut_neg':        
                tela_emp_aut_neg = Botao_main.emprestimo_autonomo_negativado()
                janela_contratacao(tela_emp_aut_neg)

            if event_planos == 'botao_emp_neg':       
                tela_emp_neg = Botao_main.emprestimo_negativado()
                janela_contratacao(tela_emp_neg)
