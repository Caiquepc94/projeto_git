

secret_word="ema" 

guess=""
guess_count=0
guess_limit=5
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
	if guess_count < guess_limit:
		dif=guess_limit-guess_count
		guess=raw_input("Voce possui: "+str(dif)+" chances. Tente adivinhar a palavra: ")
		guess_count += 1
		if 2<dif < 4 and guess != secret_word:
			print("Dica1: animal.")
		if 1 <dif <3 and guess != secret_word:
			print("Dica2:Comeca com e.") 
	else:
		out_of_guesses = True

if out_of_guesses:
	print("Voce perdeu! A palavra era: "+secret_word)
else:
	print("Voce ganhou!")


