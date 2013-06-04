from Button import Button

class ButtonGroup:

    def __init__(self):
        self.buttons = [Button("Fold", 400, 400), Button("Deal", 500, 400), 
                        Button("Bet", 300, 400)]
        
    def pressed(self, x, y):
        for i in range(3):
            if self.buttons[i].rect.collidepoint(x, y):
                print "Successful"
                continue
    
    def draw(self,surface):
        for c in self.buttons:
            c.draw(surface)
