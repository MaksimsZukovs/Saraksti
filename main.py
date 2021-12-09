print('Kuru no uzdevumiem vēlies realizēt')
print('Izvēlies ciparu')
print('1 - pirmo uzdevumu')
print('2 - otro uzdevumu')
print('3 - trešo uzdevumu')
print('____________________')
print('Tu es izvēlējies uzdevumu nr. ')

#2.uzd
visi_skaitli = []
for i in range(8):
  skaitlis = int(input("ievadiskaitli intervālā [- 10 ; 10]"))
  visi_skaitli.append(skaitlis)
print("saraksta garums ir " , len(visi_skaitli))
lielaki_skaitli = 0
if visi_skaitli[0]> visi_skaitli[5]:
  lielaki_skaitli += 2
if visi_skaitli[3]> visi_skaitli[5]:
  lielaki_skaitli += 2
if visi_skaitli[1]> visi_skaitli[5]:
  lielaki_skaitli += 2
if visi_skaitli[4]> visi_skaitli[5]:
  lielaki_skaitli += 2
print(lielaki_skaitli)
print(visi_skaitli)


#3.uzd
def check_guess(guess, answer):
global score
still_guessing = True
attempt = 0
while still_guessing and attempt < 5:
if guess.lower() == answer.lower():
print("Correct Answer")
score = score + 2
still_guessing = False
else:
if attempt < 5:
guess = input("Sorry Wrong Answer, try again")
attempt = attempt + 4
if attempt == 6:
print("The Correct answer is ",answer )
score = 0
print("Sniedz atbildes uz jautajumiem")
guess1 = input("Kada ir popularaka programa kodešanai? ")
check_guess(guess1, "python")
guess2 = input("kura gada izveidoja python? ")
check_guess(guess2, "1968")
guess3 = input("vai c++ ir programma kodešanai ja vai ne? ")
check_guess(guess3, "ja")
guess4 = input("vai tev patik programmet? ")
check_guess(guess4, "ne")
