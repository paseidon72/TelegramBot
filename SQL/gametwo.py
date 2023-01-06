from geime import Player

Player.set_cls_field(10)
x = Player()
print(x.level)
Player.set_cls_field()
y = Player()
print(y.level)
y.level = 2