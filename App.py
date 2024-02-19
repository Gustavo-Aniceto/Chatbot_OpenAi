from tkinter import *
from tkinter import ttk, messagebox
from tkscrolledframe import ScrolledFrame
from PIL import Image, ImageTk
import openai

cor_fundo_1 = "#FFFFFF"
cor_fundo_2 = "#E1F2FD"
cor_letra = "#403d3d"

janela = Tk()
janela.title("ChatBot")
janela.geometry('500x580')
janela.configure(background=cor_fundo_1)
janela.resizable(width=False, height=False)

frameCima = Frame(janela, width=500, height=100, bg=cor_fundo_1, relief="flat")
frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frameMeio = Frame(janela, width=500, height=300, bg=cor_fundo_1, relief="solid")
frameMeio.grid(row=1, column=0, sticky=NSEW)
img_app = Image.open('C:/Users/guuha/PycharmProjects/Chatbot_OpenAi/bot.png')
img_app = img_app.resize((70, 70))
img_app = ImageTk.PhotoImage(img_app)
app_ = Label(frameCima, height=70, image=img_app, compound=LEFT, anchor='center', bg=cor_fundo_1)
app_.place(x=10, y=10)

app_logo = Label(frameCima, text="ChatBot de Suporte", compound=LEFT, padx=5, anchor=NW, font=('System 20 bold'), bg=cor_fundo_1, fg=cor_letra)
app_logo.place(x=100, y=20)
sf = ScrolledFrame(frameMeio, width=480, height=380)
sf.grid(row=1, column=0, sticky=NW)
sf.bind_arrow_keys(frameMeio)
sf.bind_scroll_wheel(frameMeio)
framecanva = sf.display_widget(Frame, bg=cor_fundo_1)
frame_chat = Frame(framecanva, width=480, height=480, bg=cor_fundo_2, relief="flat")
frame_chat.grid(row=0, column=0, sticky=NSEW, padx=7, pady=10)

text_chat = Text(frame_chat, wrap=WORD, state=DISABLED, font=('Arial 10'), bg=cor_fundo_2, fg=cor_letra)
text_chat.pack(expand=True, fill=BOTH)

frameBaixo = Frame(janela, width=500, height=100, bg=cor_fundo_1, relief="flat")
frameBaixo.grid(row=2, column=0, sticky=NSEW)

entry_mensagem = Entry(frameBaixo, font=('Arial 12'), width=48, relief="solid")
entry_mensagem.grid(row=0, column=0, padx=10, pady=5)

def enviar_mensagem():
    mensagem = entry_mensagem.get()
    # Chame a API da OpenAI para obter a resposta
    resposta = openai.Completion.create(
        model="text-davinci-002",  # Anteriormente era 'engine'
        prompt=mensagem,
        max_tokens=50
    )
    resposta_texto = resposta.choices[0].text.strip()
    exibir_resposta(resposta_texto)

def exibir_resposta(resposta):
    text_chat.config(state=NORMAL)
    text_chat.insert(END, "Bot: " + resposta + "\n")
    text_chat.config(state=DISABLED)

# ... (outros componentes)

button_imagem = Image.open('C:/Users/guuha/PycharmProjects/Chatbot_OpenAi/enviar.png')
button_imagem = button_imagem.resize((30, 30))
button_imagem = ImageTk.PhotoImage(button_imagem)

button_enviar = Button(frameBaixo, image=button_imagem, command=enviar_mensagem, bg=cor_fundo_1, relief=FLAT)
button_enviar.grid(row=0, column=1, padx=5, pady=5)



janela.mainloop()
