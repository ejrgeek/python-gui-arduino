from pyfirmata import Arduino


class Semaforo:
    board = Arduino("/dev/ttyACM0")

    LED_RED = board.digital[13]
    LED_YELLOW = board.digital[12]
    LED_GREEN = board.digital[11]

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
