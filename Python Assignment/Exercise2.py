class Aircraft:
    x=0
    y=0
    acceleration=1
    def move_up(self):
        print("Moved up . . .")
        self.y +=1
    def move_down(self):
        print("Moved down . . .")
        self.y -=1
    def move_right(self):
        print("Moved right . . .")
        self.x +=1
    def move_left(self):
        print("Moved left . . .")
        self.y -=1



abhi_bom_to_dfw= Aircraft()
print "Initial X-Coord:",abhi_bom_to_dfw.x
print "Initial X-Coord:",abhi_bom_to_dfw.y
abhi_bom_to_dfw.move_up()
abhi_bom_to_dfw.move_left()
abhi_bom_to_dfw.move_down()
abhi_bom_to_dfw.move_up()
abhi_bom_to_dfw.move_up()
abhi_bom_to_dfw.move_right()
abhi_bom_to_dfw.move_down()
abhi_bom_to_dfw.move_left()
abhi_bom_to_dfw.move_up()
abhi_bom_to_dfw.move_down()
abhi_bom_to_dfw.move_left()
abhi_bom_to_dfw.move_right()

print "Final X-Coord:",abhi_bom_to_dfw.x
print "Final X-Coord:",abhi_bom_to_dfw.y




