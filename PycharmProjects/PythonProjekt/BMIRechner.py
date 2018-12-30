#Aufgabe: Schreibe ein Programm, welches die Körpergröße und das Gewicht einer Person abfragt
#         und auf Basis dieser Daten dann den BMI ausrechnet und ausgibt.
#Hinweis: Die Formel für den BMI lautet:
#         BMI= (Gewicht in kg) / (Körpergröße in Meter)^2


print("Hallo, dieses kleine Programm wird dir deinen BMI berechen.")

user_weight = input("Gib hier bitte dein Gewicht in Kilogramm an (Beispiel: 85): ")

user_height = input("Gib hier bitte deine Größe in Metern an (Beispiel: 1,85): ")



user_bmi = round(float(user_weight.replace(",",".")) / float(user_height.replace(",","."))**2,2)

print("Dein BMI lautet: " + str(user_bmi))