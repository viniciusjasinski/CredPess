import PySimpleGUI as sg
from Interface import Tela
from Botoes import Botao_main
from ConexaoDB import Conexao


con = Conexao() 


con.conectar('mysqlserver.ck7rcqskurbo.us-east-2.rds.amazonaws.com', # ip
             3306, # porta
             'admin', # usuário
             'admin123', # senha
             'dbdadosemprestimo') # nome do BD

window = Tela.tela()
tela_planos = None
tela_emp_pessoal = None
tela_mudar_bd = None
tela_confirmacao = None

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def janela_contratacao(tela_contratacao):

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
                        tela_emp_pessoal.close()
                        tela_planos.close()
                        window.close()


while (True):

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
