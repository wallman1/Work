import Weapons

weapon1 = Weapons.Weapon("Johnathan", "Axe", 200)
weapon2 = Weapons.Sword("Jimmy", "Sword", 90, "Slashing")
weapon3 = Weapons.Bow("Jamie", "Bow", 120, "Piercing")
weapon4 = Weapons.ShortBow("Jimbo", "Bow", 80, "Bludgoning", 80)
weapon5 = Weapons.LongBow("Jonny", "Bow", 150, "Poison", 150)

weapon1.getstats()
weapon2.getstats()
weapon3.getstats()
weapon4.getstats()
weapon5.getstats()