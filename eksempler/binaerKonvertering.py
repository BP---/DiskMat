from BPfunctions import ToBin, FromBin

#her er det importert to funksjoner som gjør at du enkelt kan konvertere
#fra og til binære tall. ToBin tar et tall i titalssystemet, og gjør det
#til et binært tall. FromBin gjør det motsatte

a = ToBin(18)
b = FromBin(1000100101)
print(a, '\t', b)
