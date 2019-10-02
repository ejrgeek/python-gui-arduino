from tkinter import *
from pyfirmata import Arduino


class ControleSemaforo:
    board = Arduino("/dev/ttyACM1")

    LED_RED = board.digital[13]
    LED_YELLOW = board.digital[12]
    LED_GREEN = board.digital[11]

    def __init__(self, toplevel):

        # Janela
        toplevel.title('Controle Semaforo')
        toplevel.geometry("300x300")

        # Espaçamento
        self.frame1 = Frame(toplevel)
        self.frame1.pack()

        # Operações
        self.frame4 = Frame(toplevel, pady=12)
        self.frame4.pack()

        # Botões
        self.frame6 = Frame(toplevel, pady=12)
        self.frame6.pack()

        # Cor e tamanho das letras
        Label(self.frame1, text='', fg='black',
              font=('Verdana', '10'), height=1).pack()
        fonte1 = ('Verdana', '10')

        # Botão led vermelho
        btn_red_on = Button(self.frame4, width=15, font=fonte1, text='Vermelho ON', command=self.led_red_on)
        btn_red_on.pack()

        btn_red_off = Button(self.frame4, width=15, font=fonte1, text='Vermelho OFF', command=self.led_red_off)
        btn_red_off.pack()

        # Botão led amarelo
        btn_yellow_on = Button(self.frame4, width=15, font=fonte1, text='Amarelo ON', command=self.led_yellow_on)
        btn_yellow_on.pack()

        btn_yellow_on = Button(self.frame4, width=15, font=fonte1, text='Amarelo OFF', command=self.led_yellow_off)
        btn_yellow_on.pack()

        # Botão led verde
        btn_green_on = Button(self.frame4, width=15, font=fonte1, text='Verde ON', command=self.led_green_on)
        btn_green_on.pack()

        btn_green_off = Button(self.frame4, width=15, font=fonte1, text='Verde OFF', command=self.led_green_off)
        btn_green_off.pack()

        # Botão Sair
        sair = Button(self.frame6, width=15, font=fonte1, text='Sair', command=self.sair)
        sair.pack()

    #######################
    def led_red_on(self):
        self.LED_RED.write(1)

    def led_red_off(self):
        self.LED_RED.write(0)

    #######################
    def led_yellow_on(self):
        self.LED_YELLOW.write(1)

    def led_yellow_off(self):
        self.LED_YELLOW.write(0)

    #######################
    def led_green_on(self):
        self.LED_GREEN.write(1)

    def led_green_off(self):
        self.LED_GREEN.write(0)

    def sair(self):
        self.led_red_off()
        self.led_yellow_off()
        self.led_green_off()
        app.destroy()


app = Tk()
ControleSemaforo(app)
app.mainloop()
