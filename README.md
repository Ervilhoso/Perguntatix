# Perguntatix
 import tkinter as tk
import threading


perguntas = {
    "Qual é a capital do Brasil?": ["a) São Paulo", "b) Rio de Janeiro", "c) Brasília", "d) Belo Horizonte"],
    "Qual é o maior planeta do sistema solar?": ["a) Terra", "b) Vênus", "c) Marte", "d) Júpiter"],
    "Qual é o animal terrestre mais rápido?": ["a) Leopardo", "b) Guepardo", "c) Leão", "d) Elefante"]
}

respostas = {
    "Qual é a capital do Brasil?": "c",
    "Qual é o maior planeta do sistema solar?": "d",
    "Qual é o animal terrestre mais rápido?": "b"
}

pontuacao = 0
pergunta_atual = 0
perguntas_keys = list(perguntas.keys())

tempo_por_pergunta = 10  
tempo_restante = tempo_por_pergunta  
timer = None
fullscreen = False  

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

def iniciar_jogo():
    global pontuacao, pergunta_atual, tempo_restante
    pontuacao = 0
    pergunta_atual = 0
    tempo_restante = tempo_por_pergunta
    botao_inicio.pack_forget()  
    for botao in opcoes_botao:
        botao.pack()  
    proxima_pergunta()

def reiniciar_jogo():
    iniciar_jogo()
    resultado_label.config(text="")
    botao_reiniciar.pack_forget()  

def proxima_pergunta():
    global pergunta_atual, timer, tempo_restante
    if timer:
        timer.cancel()  

    if pergunta_atual < len(perguntas):
        pergunta = perguntas_keys[pergunta_atual]
        opcoes = perguntas[pergunta]
        pergunta_label.config(text=pergunta, fg='white', bg='navy', font=('Helvetica', 18 if fullscreen else 16))
        for i, opcao in enumerate(opcoes):
            opcoes_botao[i].config(text=opcao, command=lambda i=i: verificar_resposta(i), fg='black', bg='yellow', font=('Helvetica', 16 if fullscreen else 14), height=2, width=30 if fullscreen else 20)
        
        tempo_restante = tempo_por_pergunta
        visor_tempo.config(text=f"Tempo restante: {tempo_restante} s", fg='white', bg='navy', font=('Helvetica', 14 if fullscreen else 12))
        janela.title(f"Jogo de Perguntas e Respostas - Tempo Restante: {tempo_restante} s")
        iniciar_timer()
        pergunta_atual += 1
    else:
        resultado_label.config(text=f"Sua pontuação final é: {pontuacao}/{len(perguntas)}", fg='white', bg='navy', font=('Helvetica', 16 if fullscreen else 14))
        botao_reiniciar.pack()  

def verificar_resposta(escolha):
    global pontuacao
    resposta_correta = respostas[perguntas_keys[pergunta_atual - 1]]
    if escolha == ord(resposta_correta) - ord('a'):
        pontuacao += 1
    proxima_pergunta()

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
        botao.config(font=('Helvetica', 16 if fullscreen else 14), height=2, width=30 if fullscreen else 20)
    resultado_label.config(font=('Helvetica', 16 if fullscreen else 14))
    visor_tempo.config(font=('Helvetica', 14 if fullscreen else 12))
    botao_fullscreen.config(text="Sair da Tela Cheia" if fullscreen else "Entrar na Tela Cheia", font=('Helvetica', 10))


janela = tk.Tk()
janela.title("Jogo de Perguntas e Respostas")


janela.configure(bg='navy')  


menu_label = tk.Label(janela, text="Bem-vindo ao PERGUNTATRIX!", fg='white', bg='navy')
menu_label.pack(pady=20)

botao_inicio = tk.Button(janela, text="Iniciar Jogo", command=iniciar_jogo, fg='black', bg='yellow', font=('Helvetica', 14), height=2, width=20)
botao_inicio.pack()


pergunta_label = tk.Label(janela, text="", fg='white', bg='navy')
pergunta_label.pack(pady=10)

opcoes_botao = []
for _ in range(4):
    botao = tk.Button(janela, text="", fg='black', bg='yellow')
    botao.pack(pady=(10 if fullscreen else 5))  
    opcoes_botao.append(botao)


resultado_label = tk.Label(janela, text="", fg='white', bg='navy')
resultado_label.pack(pady=10)


visor_tempo = tk.Label(janela, text="", fg='white', bg='navy')
visor_tempo.pack(pady=10)


botao_reiniciar = tk.Button(janela, text="Reiniciar Jogo", command=reiniciar_jogo, fg='black', bg='yellow')
botao_reiniciar.pack()
botao_reiniciar.pack_forget()  


botao_fullscreen = tk.Button(janela, text="Entrar na Tela Cheia", command=toggle_fullscreen, fg='black', bg='yellow', font=('Helvetica', 10))
botao_fullscreen.pack(side=tk.LEFT, padx=10, pady=10)

janela.mainloop()

# Perguntatix
