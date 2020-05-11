Alvo = input("Alvo da pesquisa: ")
Amostra = int(input("Valor da amostra: "))


import Algorithmia
import tweepy
import matplotlib.pyplot as plt
# Authenticate to Twitter

L = []
l1 = []
x = ['Positivo', 'Negativo','Neutro']
y = [0,0,0]
auth = tweepy.OAuthHandler("I0zcxu19rwF4icBKvqRs7vhYO","QeoSUQmjiPj4qKbKdK1Onwm8FtWgjJOUBpg4aedy61QF88TV4i")
auth.set_access_token("1230299033555677184-7mqrNtDnV7Znsf0HANsSzRE4yq4o5U", 
    "DOkA4IgS0a7Sx8IkrAjXJ6vCh2JeUhtenNWbPoRO88KKl")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
for tweet in api.search(q = Alvo, lang="en", rpp = Amostra):
    L.append((f"{tweet.text}")) 
print(L)
A = list(range(0, len(L)-1))
for e in A:
    inputn = {
            "document": L[e]
      }
    client = Algorithmia.client('simtgm5pFbIPnPjlO3T0iVinV+M1')
    algo = client.algo('nlp/SentimentAnalysis/1.0.5')
    algo.set_options(timeout=300) # optional
    print(algo.pipe(inputn).result)
    print(type(algo.pipe(inputn).result))
    l1.append(algo.pipe(inputn).result[0]['sentiment'])
print(l1)    
for j in l1:
    if j > 0:
        y[0] += 1
    elif j < 0:
        y[1] += 1
    else:
        y[2] += 1
plt.bar(x,y,color= "red")        
