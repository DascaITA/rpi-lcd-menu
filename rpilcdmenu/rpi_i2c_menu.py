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

    def defMessage(self, text):
        """ Send long string to LCD. 17th char wraps to second line"""
        i = 0
        lines = 0

        for char in text:
            if char == '\n':
                self.lcd.crlf() # next line
                i = 0
                lines += 1
            else:
                self.lcd.write(ord(char))
                i = i + 1

            if i == 16:
                self.lcd.crlf()  # last char of the line
            elif lines == 2:
                break

        return self

    def displayTestScreen(self):
        """
        Display test screen to see if your LCD screen is wokring
        """
        self.message("test line 0", 0)
        self.message("test line 1", 1)

        return self
    
    def defDisplayTestScreen(self):
        """
        Display test screen to see if your LCD screen is wokring
        """
        self.message('Hum. body 36,6\xDFC\nThis is test')

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
            self.message((self.current_option == 0 and ">" or " ") + self.items[0].text.ljust(15),0)
            if len(self.items) == 2:
                self.message((self.current_option == 1 and ">" or " ") + self.items[1].text.ljust(15),1)
            return self

        self.message(">" + self.items[self.current_option].text.ljust(15),0)

        if self.current_option + 1 < len(self.items):
            self.message(self.items[self.current_option + 1].text.ljust(15),1)
        else:
            self.message(self.items[0].text.ljust(15),0)
        return self

    def defRender(self):
        """
        Render menu
        """
        self.clearDisplay()

        if len(self.items) == 0:
            self.message('Menu is empty')
            return self
        elif len(self.items) <= 2:
            options = (self.current_option == 0 and ">" or " ") + self.items[0].text
            if len(self.items) == 2:
                options += "\n" + (self.current_option == 1 and ">" or " ") + self.items[1].text
            print(options)
            self.message(options)
            return self

        options = ">" + self.items[self.current_option].text

        if self.current_option + 1 < len(self.items):
            options += "\n " + self.items[self.current_option + 1].text
        else:
            options += "\n " + self.items[0].text

        self.message(options)

        return self
