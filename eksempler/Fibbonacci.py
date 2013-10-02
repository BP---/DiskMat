from BPfunctions import FibbonacciList, InputCheck

tall = InputCheck('int', 'Skriv inn et tall', 'Ikke et heltall')

print(FibbonacciList(tall))
