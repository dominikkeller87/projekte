print("Hallo Welt")

age_a = input("Bitte gebe das Alter von Person A ein: ")
age_b = input("Bitte gebe das Alter von Person B ein: ")

if age_a > age_b:
    age_aelter = age_a
    age_juenger = age_b
else:
    age_juenger = age_b
    age_aelter = age_a

age_dif = int(age_juenger) - int(age_aelter)

print("Der Altersunterschied zwischen Person A und B beträgt " + str(age_dif) + " Jahre!")
