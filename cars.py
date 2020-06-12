showroom = set()
showroom.add("Tesla 3")
showroom.add("Mazda 3")
showroom.add("Firebird")
showroom.add("Phantom Corsair")

print('Initital Showroom: ', showroom)

print("length of showroom:", len(showroom))

showroom.add("Phantom Corsair")
print("showroom length after adding dupe:", len(showroom))
print('Showroom after dupe: ', showroom)

showroom.update({"Ashton Martin Atom", "Chevy Mako Shark", "Alfa Romeo BAT"})
showroom.discard("Mazda 3")

junkyard = {"Chevy Vega", "Lancia Beta",
            "Phantom Corsair"}

print('What junkyard has that showroom also has',
      junkyard.intersection(showroom))

showroom.union(junkyard)

print('Showroom after doing Union with junkyard: ', showroom)

showroom.discard("Chevy Vega")
print('Final Showroom', showroom)
