from BPfunctions import GraadigeAlgoritmen

#GraadigeAlgoritmen funksjonen tar inn et tall og en liste med denominatorer
#og deler tallet opp i de denominatorene

#det er greit å ha listen med denominatorer i en variabel. Typiske tall er:
denominators = [25, 10, 5, 1]
#en ting å huske på er at du bør starte listen med det høyeste tallet du
#deler opp i, og bør avslutte med en 1ner slik at du er sikker på at du
#får delt det fullstendig opp

tallSomSkalDeles = 111
#vi har nå alt vi trenger for å kjøre funskjonen. Funskjonen returnerer en
#liste med tall, som vi kan sette i en ny variabel
resultat = GraadigeAlgoritmen(tallSomSkalDeles, denominators)
print(resultat)
#du ser at du får en liste med nye tall: [4, 1, 0, 1] Disse tallene sier
#noe om hvor mange av hver denominator tallet har blitt delt opp i.
#plassen i resultatlisten tilhører plassen til tallene i denominatorlisten
#Vi får da (4*25)+(1*10)+(0*5)+(1*1) = 111

print('\n\n\n\n')

#men du er ikke begrenset til det standard settet med denominatorer. Du kan
#fjerne og legge til som du vil!
denominatorsTwo = [25,12,5,1]
print(GraadigeAlgoritmen(tallSomSkalDeles, denominatorsTwo))

print(GraadigeAlgoritmen(14135,[34,27,15,7,3,1]))

print(GraadigeAlgoritmen(135908085, [412,341,189,25,2,1]))
