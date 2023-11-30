import tkinter as tk
import threading
import random


perguntas = {
    "Matemática": {
     "Qual é a propriedade associativa da adição?": ["a) Comutativa", "b) Distributiva", "c) Associativa", "d) Identidade"],
    "O que representa a letra 'x' em uma equação?": ["a) Raiz quadrada", "b) Variável", "c) Número primo", "d) Coeficiente"],
    "Qual é o oposto aditivo de -5?": ["a) 5", "b) -5", "c) 0", "d) -1"],
    "O que são números inteiros?": ["a) Números positivos", "b) Números decimais", "c) Números naturais", "d) Números negativos"],
    "Qual é a propriedade distributiva da multiplicação em relação à adição?": ["a) Associativa", "b) Comutativa", "c) Distributiva", "d) Identidade"],
    "O que é um número irracional?": ["a) Número inteiro", "b) Número decimal", "c) Número fracionário", "d) Não pode ser expresso como fração"],
    "O que é um polinômio?": ["a) Expressão algébrica", "b) Número complexo", "c) Número racional", "d) Número inteiro"],
    "Qual é o valor de pi (π)?": ["a) 3.14", "b) 2.71", "c) 1.618", "d) 0.577"],
    "O que é um número primo?": ["a) Divisível por 2", "b) Divisível por 1 e por ele mesmo", "c) Divisível por 10", "d) Divisível por 5"],
    "Qual é a propriedade comutativa da multiplicação?": ["a) Associativa", "b) Comutativa", "c) Distributiva", "d) Identidade"]
},
    "História": {
"Quem foi o primeiro imperador do Brasil?": ["a) Dom Pedro II", "b) Dom Pedro I", "c) Getúlio Vargas", "d) Tiradentes"],
    "Em que ano o Brasil foi descoberto por Pedro Álvares Cabral?": ["a) 1500", "b) 1492", "c) 1600", "d) 1550"],
    "Qual foi o período conhecido como República Velha no Brasil?": ["a) 1889-1930", "b) 1930-1945", "c) 1946-1964", "d) 1964-1985"],
    "Quem foi o líder da independência do Brasil?": ["a) Tiradentes", "b) Dom Pedro I", "c) Getúlio Vargas", "d) Joaquim Nabuco"],
    "Qual foi a primeira capital do Brasil?": ["a) Brasília", "b) Rio de Janeiro", "c) Salvador", "d) São Paulo"],
    "Em que ano foi proclamada a independência do Brasil?": ["a) 1822", "b) 1500", "c) 1889", "d) 1750"],
    "Quem foi o presidente do Brasil durante a Segunda Guerra Mundial?": ["a) Getúlio Vargas", "b) Juscelino Kubitschek", "c) João Goulart", "d) Fernando Collor"],
    "Qual movimento político-militar governou o Brasil de 1964 a 1985?": ["a) República Velha", "b) Ditadura Militar", "c) Era Vargas", "d) República Nova"],
    "O que foi o movimento conhecido como Diretas Já?": ["a) Movimento abolicionista", "b) Protesto contra a Ditadura Militar", "c) Revolução Constitucionalista", "d) Campanha pela eleição direta para presidente"],
    "Quem foi o líder das Diretas Já e se tornou presidente do Brasil?": ["a) Tancredo Neves", "b) Fernando Collor", "c) Fernando Henrique Cardoso", "d) Luiz Inácio Lula da Silva"]
},
    "Português": {
"Qual alternativa apresenta um verbo de ligação?": ["a) Corre", "b) Está", "c) Come", "d) Vive"],
    "O que é um sujeito indeterminado na frase?": ["a) Não possui sujeito", "b) Sujeito oculto", "c) Sujeito composto", "d) Sujeito simples"],
    "Qual é a função da conjunção subordinativa condicional?": ["a) Estabelecer comparação", "b) Indicar causa", "c) Expressar condição", "d) Marcar tempo"],
    "O que caracteriza um discurso direto?": ["a) Fala de um narrador", "b) Reprodução fiel da fala de alguém", "c) Uso de aspas", "d) Interação com o leitor"],
    "O que é uma antítese na construção de frases?": ["a) Repetição de palavras", "b) Contraste de ideias", "c) Uso de sinônimos", "d) Expressão de causa"],
    "Qual é a função do pronome relativo 'que' na frase?": ["a) Indicar posse", "b) Estabelecer uma condição", "c) Conectar termos da frase", "d) Expressar quantidade"],
    "O que é uma elipse no contexto da língua portuguesa?": ["a) Figura de linguagem", "b) Omissão de termos", "c) Uso de pleonasmo", "d) Ambiguidade na frase"],
    "Qual é o antônimo de 'efêmero'?": ["a) Permanente", "b) Rápido", "c) Breve", "d) Passageiro"],
    "O que caracteriza uma oração subordinada adjetiva restritiva?": ["a) Adiciona informação essencial", "b) Indica uma condição", "c) Pode ser omitida sem prejuízo", "d) Inicia a frase"],
    "O que é uma metáfora na linguagem figurada?": ["a) Comparação direta", "b) Repetição de palavras", "c) Uso de conjunções", "d) Expressão literal"]
},
    "Ciências": {
    "Qual é a unidade de medida de temperatura no sistema internacional?": ["a) Kelvin", "b) Celsius", "c) Fahrenheit", "d) Rankine"],
    "O que é um átomo?": ["a) Partícula subatômica", "b) Molécula", "c) Elemento químico", "d) Íon"],
    "Quem é considerado o pai da genética?": ["a) Charles Darwin", "b) Gregor Mendel", "c) Albert Einstein", "d) Marie Curie"],
    "O que estuda a física nuclear?": ["a) Movimento dos corpos", "b) Átomos e suas interações", "c) Energia térmica", "d) Óptica"],
    "Qual é a fórmula da água?": ["a) H2O2", "b) CO2", "c) H2O", "d) O2"],
    "O que é a mitose?": ["a) Processo de reprodução celular", "b) Respiração celular", "c) Fotossíntese", "d) Digestão"],
    "Qual é o número atômico do carbono?": ["a) 12", "b) 6", "c) 14", "d) 8"],
    "O que é uma reação exotérmica?": ["a) Libera calor", "b) Absorve calor", "c) Não libera nem absorve calor", "d) Libera e absorve calor"],
    "Qual é a função dos ribossomos na célula?": ["a) Produção de energia", "b) Síntese de proteínas", "c) Armazenamento de nutrientes", "d) Controle do ciclo celular"],
    "O que estuda a física óptica?": ["a) Eletricidade", "b) Movimento dos corpos", "c) Propagação da luz", "d) Termodinâmica"],
},
    "Esporte": {
    "Qual esporte utiliza uma bola redonda?": ["a) Futebol", "b) Basquete", "c) Tênis", "d) Golfe"],
    "Em qual esporte se utiliza um taco e uma bola?": ["a) Beisebol", "b) Futebol", "c) Vôlei", "d) Handebol"],
    "Quem é considerado o maior jogador de basquete de todos os tempos?": ["a) LeBron James", "b) Michael Jordan", "c) Kobe Bryant", "d) Shaquille O'Neal"],
    "Em que esporte se utiliza um tabuleiro e peças para jogar?": ["a) Xadrez", "b) Tênis de mesa", "c) Snooker", "d) Atletismo"],
    "Qual esporte é conhecido como o 'esporte das raquetes'?": ["a) Tênis", "b) Badminton", "c) Squash", "d) Golfe"],
    "Qual é o esporte mais popular no Brasil?": ["a) Futebol", "b) Basquete", "c) Vôlei", "d) Natação"],
    "Quantos jogadores compõem uma equipe de futebol em campo?": ["a) 9", "b) 11", "c) 7", "d) 5"],
    "Quem é considerado o rei do futebol?": ["a) Lionel Messi", "b) Cristiano Ronaldo", "c) Pelé", "d) Neymar"],
    "Em qual esporte se utiliza uma rede e uma peteca?": ["a) Tênis", "b) Badminton", "c) Vôlei", "d) Golfe"],
    "Qual país sediou as Olimpíadas de 2016?": ["a) Estados Unidos", "b) China", "c) Rússia", "d) Brasil"]
},
    "Perguntatrix": { 
    "Qual é a propriedade associativa da adição?": ["a) Comutativa", "b) Distributiva", "c) Associativa", "d) Identidade"],
    "O que é um átomo?": ["a) Partícula subatômica", "b) Molécula", "c) Elemento químico", "d) Íon"],
    "Quem foi o primeiro imperador do Brasil?": ["a) Dom Pedro II", "b) Dom Pedro I", "c) Getúlio Vargas", "d) Tiradentes"],
    "Qual alternativa apresenta um verbo de ligação?": ["a) Corre", "b) Está", "c) Come", "d) Vive"],
    "Qual esporte utiliza uma bola redonda?": ["a) Futebol", "b) Basquete", "c) Tênis", "d) Golfe"],
    "Qual é a fórmula da água?": ["a) H2O2", "b) CO2", "c) H2O", "d) O2"],
    "Quem foi o líder da independência do Brasil?": ["a) Tiradentes", "b) Dom Pedro I", "c) Getúlio Vargas", "d) Joaquim Nabuco"],
    "O que é um número irracional?": ["a) Número inteiro", "b) Número decimal", "c) Número fracionário", "d) Não pode ser expresso como fração"],
    "Quem é considerado o maior jogador de basquete de todos os tempos?": ["a) LeBron James", "b) Michael Jordan", "c) Kobe Bryant", "d) Shaquille O'Neal"],
    "O que é uma antítese na construção de frases?": ["a) Repetição de palavras", "b) Contraste de ideias", "c) Uso de sinônimos", "d) Expressão de causa"]
}

}

respostas = {
    #ciencias
    "Qual é a unidade de medida de temperatura no sistema internacional?": "b",
    "O que é um átomo?": "a",
    "Quem é considerado o pai da genética?": "b",
    "O que estuda a física nuclear?": "b",
    "Qual é a fórmula da água?": "c",
    "O que é a mitose?": "a",
    "Qual é o número atômico do carbono?": "b",
    "O que é uma reação exotérmica?": "a",
    "O que estuda a física óptica?": "c",
    "Qual é a função dos ribossomos na célula?": "b",
    #esportes
     "Qual esporte utiliza uma bola redonda?": "a",
    "Em qual esporte se utiliza um taco e uma bola?": "a",
    "Quem é considerado o maior jogador de basquete de todos os tempos?": "b",
    "Em que esporte se utiliza um tabuleiro e peças para jogar?": "a",
    "Qual esporte é conhecido como o 'esporte das raquetes'?": "a",
    "Qual é o esporte mais popular no Brasil?": "a",
    "Quantos jogadores compõem uma equipe de futebol em campo?": "b",
    "Quem é considerado o rei do futebol?": "c",
    "Em qual esporte se utiliza uma rede e uma peteca?": "b",
    "Qual país sediou as Olimpíadas de 2016?": "d",
    #Historia
    "Quem foi o primeiro imperador do Brasil?": "b",
    "Em que ano o Brasil foi descoberto por Pedro Álvares Cabral?": "a",
    "Qual foi o período conhecido como República Velha no Brasil?": "a",
    "Quem foi o líder da independência do Brasil?": "b",
    "Qual foi a primeira capital do Brasil?": "c",
    "Em que ano foi proclamada a independência do Brasil?": "a",
    "Quem foi o presidente do Brasil durante a Segunda Guerra Mundial?": "a",
    "Qual movimento político-militar governou o Brasil de 1964 a 1985?": "b",
    "O que foi o movimento conhecido como Diretas Já?": "d",
    "Quem foi o líder das Diretas Já e se tornou presidente do Brasil?": "a",
    #Portugues 
    "Qual alternativa apresenta um verbo de ligação?": "b",
    "O que é um sujeito indeterminado na frase?": "a",
    "Qual é a função da conjunção subordinativa condicional?": "c",
    "O que caracteriza um discurso direto?": "b",
    "O que é uma antítese na construção de frases?": "b",
    "Qual é a função do pronome relativo 'que' na frase?": "c",
    "O que é uma elipse no contexto da língua portuguesa?": "b",
    "Qual é o antônimo de 'efêmero'?": "a",
    "O que caracteriza uma oração subordinada adjetiva restritiva?": "a",
    "O que é uma metáfora na linguagem figurada?": "a",
    #Matematica
    "Qual é a propriedade associativa da adição?": "c",
    "O que representa a letra 'x' em uma equação?": "b",
    "Qual é o oposto aditivo de -5?": "a",
    "O que são números inteiros?": "d",
    "Qual é a propriedade distributiva da multiplicação em relação à adição?": "c",
    "O que é um número irracional?": "d",
    "O que é um polinômio?": "a",
    "Qual é o valor de pi (π)?": "a",
    "O que é um número primo?": "b",
    "Qual é a propriedade comutativa da multiplicação?": "b"
}

pontuacao = 0
pergunta_atual = 0
perguntas_selecionadas = []
tempo_por_pergunta = 10  
tempo_restante = tempo_por_pergunta  
timer = None
fullscreen = False  
modo_selecionado = ""  

def iniciar_timer():
    global timer, tempo_restante
    timer = threading.Timer(1, atualizar_tempo)
    timer.start()

def atualizar_tempo():
    global timer, tempo_restante
    if tempo_restante > 0:
        tempo_restante -= 1
        visor_tempo.config(text=f"Tempo restante: {tempo_restante} s")
        iniciar_timer()
    else:
        tempo_expirado()

def tempo_expirado():
    proxima_pergunta()

def mostrar_botao_opcoes():
    for botao in opcoes_botao:
        botao.pack(pady=(20 if fullscreen else 10))  
        visor_tempo.pack(pady=(20 if fullscreen else 10))  
        botao_reiniciar.pack(pady=(20 if fullscreen else 10))  
        botao_reiniciar.pack_forget()

def iniciar_jogo(modo):
    global pontuacao, pergunta_atual, tempo_restante, perguntas_selecionadas, modo_selecionado
    modo_selecionado = modo
    if modo_selecionado:
        pontuacao = 0
        pergunta_atual = 0
        tempo_restante = tempo_por_pergunta
        perguntas_selecionadas = random.sample(list(perguntas[modo_selecionado].keys()), len(perguntas[modo_selecionado]))

        
        menu_label.config(text=modo_selecionado.capitalize())

        for botao in botoes_modo:
            botao.pack_forget()  
        for botao in opcoes_botao:
            botao.pack()  
        proxima_pergunta()
        mostrar_botao_opcoes()  
        
def reiniciar_jogo():
    iniciar_jogo(modo_selecionado)
    resultado_label.config(text="")
    botao_reiniciar.pack_forget()  

def proxima_pergunta():
    global pergunta_atual, timer, tempo_restante, perguntas_selecionadas
    if timer:
        timer.cancel()  

    if pergunta_atual < len(perguntas_selecionadas):
        pergunta = perguntas_selecionadas[pergunta_atual]
        opcoes = perguntas[modo_selecionado][pergunta]
        pergunta_label.config(text=pergunta, fg='white', bg='navy', font=('Helvetica', 18 if fullscreen else 16))
        for i, opcao in enumerate(opcoes):
            opcoes_botao[i].config(text=opcao, command=lambda i=i, opcao=opcao: verificar_resposta(i, opcao), fg='black', bg='yellow', font=('Helvetica', 16 if fullscreen else 14), height=2, width=60 if fullscreen else 40)
        
        tempo_restante = tempo_por_pergunta
        visor_tempo.config(text=f"Tempo restante: {tempo_restante} s", fg='white', bg='navy', font=('Helvetica', 14 if fullscreen else 12))
        janela.title(f"PERGUNTATRIX - JOGO DE PERGUNTAS E RESPOSTAS")
        iniciar_timer()
        pergunta_atual += 1
    else:
        resultado_label.config(text=f"Sua pontuação final é: {pontuacao}/{len(perguntas_selecionadas)}", fg='white', bg='navy', font=('Helvetica', 16 if fullscreen else 14))
        botao_reiniciar.pack()  

def verificar_resposta(escolha, opcao):
    global pontuacao
    resposta_correta = respostas[perguntas_selecionadas[pergunta_atual - 1]]
    if escolha == ord(resposta_correta) - ord('a'):
        pontuacao += 1
        opcoes_botao[escolha].config(bg='green')  
    else:
        opcoes_botao[escolha].config(bg='red')  
        opcoes_botao[ord(resposta_correta) - ord('a')].config(bg='green')  
    janela.after(1000, proxima_pergunta)  

def toggle_fullscreen():
    global fullscreen
    fullscreen = not fullscreen
    janela.attributes("-fullscreen", fullscreen)
    update_ui()

def update_ui():
    global fullscreen
    menu_label.config(font=('Helvetica', 18 if fullscreen else 16))
    botao_inicio.config(font=('Helvetica', 14 if fullscreen else 12), height=2, width=20)
    pergunta_label.config(font=('Helvetica', 18 if fullscreen else 16))
    for botao in opcoes_botao:
        botao.config(font=('Helvetica', 16 if fullscreen else 14), height=4, width=60 if fullscreen else 40, bg='yellow')  # Resetar a cor do botão para amarelo
    resultado_label.config(font=('Helvetica', 16 if fullscreen else 14))
    visor_tempo.config(font=('Helvetica', 14 if fullscreen else 12))

janela = tk.Tk()
janela.title("PERGUNTATRIX - JOGO DE PERGUNTAS E RESPOSTAS")

janela.configure(bg='navy')  

menu_label = tk.Label(janela, text="Escolha o Modo:", fg='white', bg='navy', font=('Helvetica', 18))
menu_label.pack(pady=20)

botoes_modo = []
for modo in perguntas.keys():
    botao_modo = tk.Button(janela, text=modo, command=lambda modo=modo: iniciar_jogo(modo), fg='black', bg='yellow', font=('Helvetica', 14))
    botao_modo.pack(pady=10)
    botoes_modo.append(botao_modo)

botao_reiniciar = tk.Button(janela, text="Reiniciar Jogo", command=reiniciar_jogo, fg='black', bg='yellow')
botao_reiniciar.pack()
botao_reiniciar.pack_forget()  

pergunta_label = tk.Label(janela, text="", fg='white', bg='navy')
pergunta_label.pack(pady=10)

opcoes_botao = []
for _ in range(4):
    botao = tk.Button(janela, text="", fg='black', bg='yellow')
    botao.pack_forget()  
    opcoes_botao.append(botao)

resultado_label = tk.Label(janela, text="", fg='white', bg='navy')
resultado_label.pack(pady=10)

visor_tempo = tk.Label(janela, text="", fg='white', bg='navy')
visor_tempo.pack(pady=10)

janela.mainloop()

# Perguntatix
++
