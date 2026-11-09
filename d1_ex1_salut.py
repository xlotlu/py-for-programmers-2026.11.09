print("Salut!")

# Task:
# Cereți utilizatorului numele său (cu input)
# capturați-l într-o variabilă
# și faceți print unui string de forma
# "Salutare <nume>!"

#print("Cum te numești?")
#name = input()
#print("Salutare " + name + "!")


name = input("Cum te numești? ")
print("Salutare " + name + "!")

# old-school string interpolation:
"un string %s interpolat" % "bla!!"
"un string %s interpolat și un %d număr" % ("bla!!", 12)

# new-school string interpolation:
"un string {} interpolat cu {} un număr".format("ceva", 123)

# cu named arguments:
"un string {my_str} interpolat cu {my_num} un număr".format(my_str="ceva", my_num=123)

TEMPLATE = "Salutare {name},\n\nContactează-ne la {phone}.\n\nCu drag, echipa {team}."
# alternativ, folosim multi-line string:
TEMPLATE = """Salutare {name},

Contactează-ne la {phone}.
Cu drag, echipa {team}."""

TEMPLATE.format(name="Gigel Gigescu", phone="+40123456789", team="Our team")

# următoarea evoluție, "formatted strings", sau f-strings:
# date fiind variabilele gata definite pe stack:
name = "John"
age = 22

f"Evaluez aici între acolade {name} și {age} -- se evaluează drept Python code"

