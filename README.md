import tkinter as tk
import threading
import random

perguntas = {
    "Matemática": {
        "Pergunta 1": ["a) Resposta 1", "b) Resposta 2", "c) Resposta 3", "d) Resposta 4"],
        
    },
    "História": {
        "Pergunta 1": ["a) Resposta 1", "b) Resposta 2", "c) Resposta 3", "d) Resposta 4"],
        
    },
    "Português": {
        "Pergunta 1": ["a) Resposta 1", "b) Resposta 2", "c) Resposta 3", "d) Resposta 4"],
        
    },
    "Ciências": {
        "Qual é o maior planeta do sistema solar?": ["a) Terra", "b) Vênus", "c) Marte", "d) Júpiter"],
        
    },
    "Esporte": {
        "Pergunta 1": ["a) Resposta 1", "b) Resposta 2", "c) Resposta 3", "d) Resposta 4"],
        
    },
    "Perguntatrix": {
        "Pergunta 1": ["a) Resposta 1", "b) Resposta 2", "c) Resposta 3", "d) Resposta 4"],
        
    }
}

respostas = {
    "Qual é o maior planeta do sistema solar?": "d",
}

pontuacao = 0
pergunta_atual = 0
perguntas_selecionadas = []
tempo_por_pergunta = 10  # Defina o tempo limite para cada pergunta em segundos
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
            opcoes_botao[i].config(text=opcao, command=lambda i=i: verificar_resposta(i), fg='black', bg='yellow', font=('Helvetica', 16 if fullscreen else 14), height=2, width=30 if fullscreen else 20)
        
        tempo_restante = tempo_por_pergunta
        visor_tempo.config(text=f"Tempo restante: {tempo_restante} s", fg='white', bg='navy', font=('Helvetica', 14 if fullscreen else 12))
        janela.title(f"PERGUNTATRIX - JOGO DE PERGUNTAS E RESPOSTAS")
        iniciar_timer()
        pergunta_atual += 1
    else:
        resultado_label.config(text=f"Sua pontuação final é: {pontuacao}/{len(perguntas_selecionadas)}", fg='white', bg='navy', font=('Helvetica', 16 if fullscreen else 14))
        botao_reiniciar.pack()  # Mostra o botão de reiniciar

def verificar_resposta(escolha):
    global pontuacao
    resposta_correta = respostas[perguntas_selecionadas[pergunta_atual - 1]]
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
