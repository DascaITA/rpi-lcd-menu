from rpilcdmenu.base_menu import BaseMenu

from RPLCD import i2c
lcdmode = 'i2c'
cols = 16
rows = 2
charmap = 'A00'
i2c_expander = 'PCF8574'
address = 0x27 # If you don't know what yours is, do i2cdetect -y 1
port = 1 # 0 on an older Pi

# Initialise the LCD
#lcd = i2c.CharLCD(i2c_expander, address, port=port, charmap=charmap,
#                  cols=cols, rows=rows)


class RpiI2cMenu(BaseMenu):
    def __init__(self):
        """
        Initialize menu
        """

        self.lcd = i2c.CharLCD(i2c_expander, address, port=port, charmap=charmap, cols=cols, rows=rows)

#        self.lcd.initDisplay()
        self.clearDisplay()

        super(self.__class__, self).__init__()

    def clearDisplay(self):
        """
        Clear LCD Screen
        """
        self.lcd.clear
        #self.lcd.delayMicroseconds(3000)  # 3000 microsecond sleep, clearing the display takes a long time

        return self

    def message(self, text, line):

        self.lcd.cursor_pos = (line,0)
        self.lcd.write_string(text)
        return self

    def displayTestScreen(self):
        """
        Display test screen to see if your LCD screen is wokring
        """
        self.message("test line 0", 0)
        self.message("test line 1", 1)

        return self

    def render(self):
        """
        Render menu
        """
        self.clearDisplay()

        if len(self.items) == 0:
            self.message('Menu is empty',0)
            return self
        elif len(self.items) <= 2:
            self.message((self.current_option == 0 and ">" or " ") + self.items[0].text,0)
            if len(self.items) == 2:
                self.message((self.current_option == 1 and ">" or " ") + self.items[1].text,1)
            return self

        options = ">" + self.items[self.current_option].text

        if self.current_option + 1 < len(self.items):
            self.message(self.items[self.current_option + 1].text,1)
        else:
            self.message(self.items[0].text,0)
        return self
