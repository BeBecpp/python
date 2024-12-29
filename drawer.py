import pydrawer

# Зургийн шинэ самбар үүсгэх
drawer = pydrawer.Drawer()

# Энгийн дүрс нэмэх (жишээ нь, дөрвөлжин)
drawer.add_rectangle(10, 10, 100, 50, color="red")

# Самбар дээрх зургийг хадгалах
drawer.save("output.png")

