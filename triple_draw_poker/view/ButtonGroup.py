from Button import Button

class ButtonGroup:

    def __init__(self):
        self.buttons = [Button("Fold", 300, 400), Button("Call", 400, 400),
                        Button("Raise", 500, 400)]
        self.visiList = [1, 1, 1]

    def pressed(self, x, y):
        if self.buttons[0].pressed(x, y):
            return "Fold"
        elif self.buttons[1].pressed(x, y):
            return "CheckDraw"
        elif self.buttons[2].pressed(x, y):
            return "BetRaise"
        return False

    def hideButton(self, button):
        if button == "Fold":
            self.visiList[0] = 0
            self.buttons[0].setUnpressable()
        elif button == "CheckDraw":
            self.visiList[1] = 0
            self.buttons[1].setUnpressable()
        elif button == "BetRaise":
            self.visiList[2] = 0
            self.buttons[2].setUnpressable()

    def showButton(self, button):
        if button == "Fold":
            self.visiList[0] = 1
            self.buttons[0].setPressable()
        elif button == "CheckDraw":
            self.visiList[1] = 1
            self.buttons[1].setPressable()
        elif button == "BetRaise":
            self.visiList[2] = 1
            self.buttons[2].setPressable()

    def draw(self, surface):
        count = 0
        for c in self.buttons:
            if self.visiList[count] == 1:
                c.draw(surface)
            count += 1
