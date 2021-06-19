import PySimpleGUI as sg


def linha_em_branco():
    return [sg.Text(' ', justification='center', background_color=('#1D4F91'))]

def cria_espacamento_topico():
    return sg.Text(' ', pad=(8,0), justification='center', size=(30,1), background_color=('#1D4F91'))

def cria_imagem_topico():
    return sg.Image("seta_topico.png", background_color='#1D4F91')


class Tela:

    @classmethod
    def tela_planos(cls):

        box0 = [[sg.Text('Nossos Planos', pad=(8,0), font=("Helvetica", 18), size=(43,1), justification='center')]]
        
        box1 = [linha_em_branco(),
                [sg.Button('Empréstimo pessoal Online:', font=("Helvetica", 10), key='botao_emp_pessoal', size=(30,1), border_width=2),
                cria_imagem_topico(),
                sg.Text('Pagamento de dívidas;', font=("Helvetica", 10), background_color=cls.cor_azul, size=(38,1))],
                [cria_espacamento_topico(), cria_imagem_topico(),
                sg.Text('Compras de alto valor;', font=("Helvetica", 10), background_color=cls.cor_azul, size=(38,1))],
                [cria_espacamento_topico(), cria_imagem_topico(),
                sg.Text('Investimentos;', font=("Helvetica", 10), background_color=cls.cor_azul, size=(38,1))],                
                [cria_espacamento_topico(), cria_imagem_topico(),
                sg.Text('E muito mais;', font=("Helvetica", 10), background_color=cls.cor_azul, size=(38,1))],                
                linha_em_branco(),
                

                [sg.Button('Empréstimo com garantia de imóvel:', font=("Helvetica", 10), key='botao_emp_imovel', size=(30,1), border_width=2),
                cria_imagem_topico(),
                sg.Text('Use sua casa, apartamento, terrenos ou imóveis comerciais como garantia do seu empréstimo;', font=("Helvetica", 10), background_color=cls.cor_azul, size=(38,2))],
                [cria_espacamento_topico(), cria_imagem_topico(),
                sg.Text('Transforme até 60% do valor do seu imóvel em crédito para seu empréstimo;', font=("Helvetica", 10), background_color=cls.cor_azul, size=(38,2))],
                [cria_espacamento_topico(), cria_imagem_topico(),
                sg.Text('Os parceiros do Serasa eCred oferecem limites e serviços variados para cada perfil de consumidor, inclusive com opções sem anuidade.', font=("Helvetica", 10), background_color=cls.cor_azul, size=(38,3))],
                [cria_espacamento_topico(), cria_imagem_topico(),
                sg.Text('Com essa garantia, você consegue maiores prazos de pagamento e as menores taxas de juros;', font=("Helvetica", 10), background_color=cls.cor_azul, size=(38,2))],                
                linha_em_branco(),               


                [sg.Button('Empréstimo para autônomo negativado:', font=("Helvetica", 10), key='botao_emp_aut_neg', size=(30,1), border_width=2),
                cria_imagem_topico(),
                sg.Text('Fim da bola de neve: limpe seu nome e se livre das contas. Quando você não possui restrições no CPF, pode ser mais fácil conseguir outros tipos de crédito.', font=("Helvetica", 10), background_color=cls.cor_azul, size=(38,3))],
                [cria_espacamento_topico(), cria_imagem_topico(),
                sg.Text('Sonhe mais alto: use o empréstimo para autônomo negativado para realizar os seus objetivos pessoais.', font=("Helvetica", 10), background_color=cls.cor_azul, size=(38,2))],
                [cria_espacamento_topico(), cria_imagem_topico(),
                sg.Text('Mais tranquilidade: após ter seu pedido aprovado, você pode reorganizar seus gastos e fazer um bom planejamento das suas finanças.', font=("Helvetica", 10), background_color=cls.cor_azul, size=(38,3))],                                
                [cria_espacamento_topico(), cria_imagem_topico(),
                sg.Text('Não precisa sair de casa: use a internet a seu favor e realize seu pedido de forma totalmente online.', font=("Helvetica", 10), background_color=cls.cor_azul, size=(38,2))],                
                linha_em_branco(),


                [sg.Button('Empréstimo para negativado:', font=("Helvetica", 10), key='botao_emp_neg', size=(30,1), border_width=2),
                cria_imagem_topico(),
                sg.Text('Simulações ilimitadas, sem impactar o seu Score;', font=("Helvetica", 10), background_color=cls.cor_azul, size=(38,1))],
                [cria_espacamento_topico(), cria_imagem_topico(),
                sg.Text('A oferta ideal para o seu perfil financeiro;', font=("Helvetica", 10), background_color=cls.cor_azul, size=(38,1))],
                [cria_espacamento_topico(), cria_imagem_topico(),
                sg.Text('Empréstimo para negativado com a garantia da Serasa;', font=("Helvetica", 10), background_color=cls.cor_azul, size=(38,2))],                
                [cria_espacamento_topico(), cria_imagem_topico(),
                sg.Text('Crédito sem burocracia.', font=("Helvetica", 10), background_color=cls.cor_azul, size=(38,1))],                               
                linha_em_branco()]
                
                #[sg.Image("serasa_logo_branca.png", background_color=cls.cor_azul)]]

        layout_planos = [[sg.Column(box0)],
                         [sg.Column(box1, background_color=cls.cor_azul, scrollable = True, vertical_scroll_only=True)]]
        window_planos = sg.Window('Descrição dos Planos', layout_planos, background_color=(cls.cor_preto))
        
        return window_planos


    @classmethod
    def tela_emp_pessoal(cls):
        
        box0 = [[sg.Text('Empréstimo pessoal Online',  font=("Helvetica", 18), size=(40,1), justification='center')]]
        
        box1 = [linha_em_branco(),
                [sg.Text('A sua oportunidade de conseguir um empréstimo pessoal com uma taxa de apenas 0.75% a.m. conforme o valor desejado.', pad=(50,0), font=("Helvetica", 11), size=(50,2), justification='center', background_color=(cls.cor_azul))],
                linha_em_branco(),
                
                [sg.Text(' ', pad=(35,0), size=(5,1), background_color=(cls.cor_azul)),
                sg.Text('R$', justification='center', size=(2,1), background_color=(cls.cor_azul)),
                sg.Input(' ', key='valor_emp', justification='center', size=(10,1), background_color=(cls.cor_branco)),
                sg.Text(' Prazo em meses: ', justification='center', size=(13,1), background_color=(cls.cor_azul)),
                sg.Input(' ', key='prazo_meses', justification='center', size=(10,1), background_color=(cls.cor_branco))],
                linha_em_branco(),                
                
                [sg.Text(' ', pad=(35,0), size=(5,1), background_color=(cls.cor_azul)),
                sg.Text('Informe o seu email:', background_color=cls.cor_azul, size=(15,1)),
                sg.Input(key='email', size=(29,1), do_not_clear = False, background_color=cls.cor_branco)],
                linha_em_branco(),
                
                [sg.Text('O valor será depositado em até 2 dias úteis na sua conta após contratação do empréstimo, os dados relacionados a conta bancária serão coletados posteriormente, após a confirmação da instituição prestadora de crédito.', pad=(50,0), font=("Helvetica", 11), size=(50,4), justification='center', background_color=(cls.cor_azul))],
                linha_em_branco(),

                [sg.Button('Voltar', key='voltar'), sg.Text(' ', pad=(50,0), justification='center', size=(43,1), background_color=(cls.cor_azul)), sg.Button('Contratar', key='contratar')]]


        layout_emp_pessoal = [[sg.Column(box0)],
                              [sg.Column(box1, background_color=cls.cor_azul)]]

        window_emp_pessoal = sg.Window('Descrição dos Planos', layout_emp_pessoal, background_color=(cls.cor_preto)) #background_color=cls.cor_azul) #background_color=(cls.cor_preto)
        
        return window_emp_pessoal


    @classmethod
    def tela_emp_imovel(cls):
        
        box0 = [[sg.Text('Empréstimo com garantia de imóvel',  font=("Helvetica", 18), size=(40,1), justification='center')]]
        
        box1 = [linha_em_branco(),
                [sg.Text('A sua oportunidade de conseguir um empréstimo pessoal com uma taxa de apenas 0.75% a.m. conforme o valor desejado.', pad=(50,0), font=("Helvetica", 11), size=(50,2), justification='center', background_color=(cls.cor_azul))],
                linha_em_branco(),
                
                [sg.Text(' ', pad=(35,0), size=(5,1), background_color=(cls.cor_azul)),
                sg.Text('R$', justification='center', size=(2,1), background_color=(cls.cor_azul)),
                sg.Input(' ', key='valor_emp', justification='center', size=(10,1), background_color=(cls.cor_branco)),
                sg.Text(' Prazo em meses: ', justification='center', size=(13,1), background_color=(cls.cor_azul)),
                sg.Input(' ', key='prazo_meses', justification='center', size=(10,1), background_color=(cls.cor_branco))],
                linha_em_branco(), 

                [sg.Text(' ', pad=(35,0), size=(5,1), background_color=(cls.cor_azul)),
                sg.Text('Informe o seu email:', background_color=cls.cor_azul, size=(15,1)),
                sg.Input(key='email', size=(29,1), do_not_clear = False, background_color=cls.cor_branco)],
                linha_em_branco(),

                [sg.Text('O valor será depositado em até 2 dias úteis na sua conta após contratação do empréstimo, os dados relacionados a conta bancária serão coletados posteriormente, após a confirmação da instituição prestadora de crédito.', pad=(50,0), font=("Helvetica", 11), size=(50,4), justification='center', background_color=(cls.cor_azul))],
                linha_em_branco(),

                [sg.Button('Voltar', key='voltar'), sg.Text(' ', pad=(50,0), justification='center', size=(43,1), background_color=(cls.cor_azul)), sg.Button('Contratar', key='contratar')]]


        layout_emp_imovel = [[sg.Column(box0)],
                             [sg.Column(box1, background_color=cls.cor_azul)]]

        window_emp_imovel = sg.Window('Descrição dos Planos', layout_emp_imovel, background_color=(cls.cor_preto)) #background_color=cls.cor_azul) #background_color=(cls.cor_preto)
        
        return window_emp_imovel


    @classmethod
    def tela_emp_aut_neg(cls):
        
        box0 = [[sg.Text('Empréstimo para autônomo negativado',  font=("Helvetica", 18), size=(40,1), justification='center')]]
        
        box1 = [linha_em_branco(),
                [sg.Text('A sua oportunidade de conseguir um empréstimo pessoal com uma taxa de apenas 0.75% a.m. conforme o valor desejado.', pad=(50,0), font=("Helvetica", 11), size=(50,2), justification='center', background_color=(cls.cor_azul))],
                linha_em_branco(),
                
                [sg.Text(' ', pad=(35,0), size=(5,1), background_color=(cls.cor_azul)),
                sg.Text('R$', justification='center', size=(2,1), background_color=(cls.cor_azul)),
                sg.Input(' ', key='valor_emp', justification='center', size=(10,1), background_color=(cls.cor_branco)),
                sg.Text(' Prazo em meses: ', justification='center', size=(13,1), background_color=(cls.cor_azul)),
                sg.Input(' ', key='prazo_meses', justification='center', size=(10,1), background_color=(cls.cor_branco))],
                linha_em_branco(),  

                [sg.Text(' ', pad=(35,0), size=(5,1), background_color=(cls.cor_azul)),
                sg.Text('Informe o seu email:', background_color=cls.cor_azul, size=(15,1)),
                sg.Input(key='email', size=(29,1), do_not_clear = False, background_color=cls.cor_branco)],
                linha_em_branco(),

                [sg.Text('O valor será depositado em até 2 dias úteis na sua conta após contratação do empréstimo, os dados relacionados a conta bancária serão coletados posteriormente, após a confirmação da instituição prestadora de crédito.', pad=(50,0), font=("Helvetica", 11), size=(50,4), justification='center', background_color=(cls.cor_azul))],
                linha_em_branco(),

                [sg.Button('Voltar', key='voltar'), sg.Text(' ', pad=(50,0), justification='center', size=(43,1), background_color=(cls.cor_azul)), sg.Button('Contratar', key='contratar')]]


        layout_emp_aut_neg = [[sg.Column(box0)],
                              [sg.Column(box1, background_color=cls.cor_azul)]]

        window_emp_aut_neg = sg.Window('Descrição dos Planos', layout_emp_aut_neg, background_color=(cls.cor_preto)) #background_color=cls.cor_azul) #background_color=(cls.cor_preto)
        
        return window_emp_aut_neg


    @classmethod
    def tela_emp_neg(cls):
        
        box0 = [[sg.Text('Empréstimo para negativado',  font=("Helvetica", 18), size=(40,1), justification='center')]]
        
        box1 = [linha_em_branco(),
                [sg.Text('A sua oportunidade de conseguir um empréstimo pessoal com uma taxa de apenas 0.75% a.m. conforme o valor desejado.', pad=(50,0), font=("Helvetica", 11), size=(50,2), justification='center', background_color=(cls.cor_azul))],
                linha_em_branco(),
                
                [sg.Text(' ', pad=(35,0), size=(5,1), background_color=(cls.cor_azul)),
                sg.Text('R$', justification='center', size=(2,1), background_color=(cls.cor_azul)),
                sg.Input(' ', key='valor_emp', justification='center', size=(10,1), background_color=(cls.cor_branco)),
                sg.Text(' Prazo em meses: ', justification='center', size=(13,1), background_color=(cls.cor_azul)),
                sg.Input(' ', key='prazo_meses', justification='center', size=(10,1), background_color=(cls.cor_branco))],
                linha_em_branco(),  

                [sg.Text(' ', pad=(35,0), size=(5,1), background_color=(cls.cor_azul)),
                sg.Text('Informe o seu email:', background_color=cls.cor_azul, size=(15,1)),
                sg.Input(key='email', size=(29,1), do_not_clear = False, background_color=cls.cor_branco)],
                linha_em_branco(),

                [sg.Text('O valor será depositado em até 2 dias úteis na sua conta após contratação do empréstimo, os dados relacionados a conta bancária serão coletados posteriormente, após a confirmação da instituição prestadora de crédito.', pad=(50,0), font=("Helvetica", 11), size=(50,4), justification='center', background_color=(cls.cor_azul))],
                linha_em_branco(),

                [sg.Button('Voltar', key='voltar'), sg.Text(' ', pad=(50,0), justification='center', size=(43,1), background_color=(cls.cor_azul)), sg.Button('Contratar', key='contratar')]]


        layout_emp_neg = [[sg.Column(box0)],
                          [sg.Column(box1, background_color=cls.cor_azul)]]

        window_emp_neg = sg.Window('Descrição dos Planos', layout_emp_neg, background_color=(cls.cor_preto)) #background_color=cls.cor_azul) #background_color=(cls.cor_preto)
        
        return window_emp_neg


    @classmethod
    def tela_preencha_dados(cls, valor_do_emp, prazo_do_emp, email_do_emp):

        try:
           int(valor_do_emp)
        except:
            if valor_do_emp == '' or (type(valor_do_emp) != int and type(valor_do_emp) != float):
                box1 = [[sg.Text(' ', justification='center', size=(24,1), background_color=(cls.cor_azul))],
                        [sg.Text('Por favor insira um valor de empréstimo válido, contendo apenas um número inteiro. Exemplo de preenchimento correto no campo R$: 1200',size=(35,5), font=("Helvetica", 11), justification='center',background_color=(cls.cor_azul))],
                        [sg.Text(' ', justification='center', size=(24,1), background_color=(cls.cor_azul))],                
                        [sg.Text(' ', size=(15,1), background_color=(cls.cor_azul)), 
                        sg.Button('Ok', key='ok', size=(5,1))]]
        else:
            try:
                int(prazo_do_emp)
            except:
                box1 = [[sg.Text(' ', justification='center', size=(24,1), background_color=(cls.cor_azul))],
                        [sg.Text('Por favor insira um prazo de empréstimo válido, contendo apenas um número inteiro. Exemplo de preenchimento correto no campo Prazo: 14',size=(35,5), font=("Helvetica", 11), justification='center',background_color=(cls.cor_azul))],
                        [sg.Text(' ', justification='center', size=(24,1), background_color=(cls.cor_azul))],                
                        [sg.Text(' ', size=(15,1), background_color=(cls.cor_azul)), 
                        sg.Button('Ok', key='ok', size=(5,1))]]
            else:
                if email_do_emp != '':
                    try:
                        float(email_do_emp)
                        box1 = [[sg.Text(' ', justification='center', size=(24,1), background_color=(cls.cor_azul))],
                                [sg.Text('Por favor insira e-mail válido. Exemplo de preenchimento correto no campo e-mail: usuario@gmail.com',size=(35,5), font=("Helvetica", 11), justification='center',background_color=(cls.cor_azul))],
                                [sg.Text(' ', justification='center', size=(24,1), background_color=(cls.cor_azul))],                
                                [sg.Text(' ', size=(15,1), background_color=(cls.cor_azul)), 
                                sg.Button('Ok', key='ok', size=(5,1))]]
                    except:
                        pass
                else:
                    box1 = [[sg.Text(' ', justification='center', size=(24,1), background_color=(cls.cor_azul))],
                            [sg.Text('Por favor insira e-mail válido. Exemplo de preenchimento correto: usuario@gmail.com',size=(35,5), font=("Helvetica", 11), justification='center',background_color=(cls.cor_azul))],
                            [sg.Text(' ', justification='center', size=(24,1), background_color=(cls.cor_azul))],                
                            [sg.Text(' ', size=(15,1), background_color=(cls.cor_azul)), 
                            sg.Button('Ok', key='ok', size=(5,1))]]        
        finally:

            layout_erro = [[sg.Column(box1, background_color=cls.cor_azul)]]
            window_erro = sg.Window('Erro no preenchimento dos dados', layout_erro, background_color=(cls.cor_preto), disable_minimize=True, keep_on_top=True)
            
            return window_erro


    @classmethod
    def tela_contratar(cls):

        box1 = [[sg.Text('Contratação Realizada!',size=(39,1), font=("Helvetica", 16), justification='center',background_color=(cls.cor_azul))],
                linha_em_branco(),                
                [sg.Text(' ', pad=(50,0), size=(10,1), background_color=(cls.cor_azul)), 
                sg.Button('Finalizar', key='finalizar', size=(15,1))]]

        layout_contratar = [[sg.Column(box1, background_color=cls.cor_azul)]]
        window_contratar = sg.Window('Descrição dos Planos', layout_contratar, background_color=(cls.cor_preto), disable_minimize=True, keep_on_top=True)
        
        return window_contratar


    @classmethod
    def tela(cls):

        cls.cor_preto = '#161616'
        cls.cor_azul = '#1D4F91'
        cls.cor_branco = 'white'
        sg.theme('Dark Blue 17')

        box1 = [linha_em_branco(),
                linha_em_branco(),
                [sg.Text('Seja Bem Vindo ao Programa',  font=("Helvetica", 16), justification='center', size=(29,1), background_color=(cls.cor_azul))],
                linha_em_branco(),                    
                [sg.Text('Crédito Para Todxs do Serasa',  font=("Helvetica", 16), justification='center', size=(29,1), background_color=(cls.cor_azul))],          
                linha_em_branco(),
                linha_em_branco(),
                linha_em_branco(),
                linha_em_branco(),
                [sg.Button('Seguir', font=("Helvetica", 14), key='botao_seguir')],
                linha_em_branco(),
                linha_em_branco(),
                linha_em_branco(),
                [sg.Image("serasa_logo_branca.png", background_color=cls.cor_azul)],
                linha_em_branco()]

        layout_tela = [[sg.Column(box1, background_color=(cls.cor_azul), element_justification='center')]]
        window_tela = sg.Window('Crédito Para Todxs - Serasa', layout_tela, resizable=True, finalize=True, element_justification='center', background_color=(cls.cor_preto))

        return window_tela