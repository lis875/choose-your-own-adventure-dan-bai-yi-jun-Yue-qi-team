print("A long time ago, a queen of a certain country gave birth to a girl in winter.\n\
Her skin was as pure as snow, her lips were as red as blood, and her hair was as black as ebony and as beautiful as snow white.")
print(" ")
print("Therefore, she was named Snow White.\n\
Shortly after the queen gave birth to the princess, He passed away, and the king married a beautiful, proud, vicious and evil woman as the queen.")
print(" ")
print("At the same time, she also became Snow White's stepmother. \n\
On this day, the queen received a magical mirror that could answer all the questions in the world.")
      
print("Now you are chosen to play the role of the queen in the new snow white. Which question you want to ask the magic mirror?")
print(" ")
print("A.Who is the most beautiful woman in the world? \n\
B.Who is the richest man in the world? \n\
C.Who is the cleverest guy in the world?")

A = ("Who is the most beautiful woman in the world?")
B = ("Who is the richest man in the world?")
C = ("Who is the cleverest guy in the world?")

question = input("I choose: ")

if (question  == "A") or (question == "a"):
  print("The mirror says that Snow White is the most beautiful woman in the world.")
  print("You are now angry about the answer")
  print("It is time to make a new decision")
  print("A: Kill Snow White!")
  print("B: Destory the stupid mirror!")
  pickup = input("Which one do you prefer?")

  if (pickup  == "A") or (pickup == "a"):
    print("You ask the hunter to kill Snow White, but finally you fail and die.")
  elif (pickup  == "B") or (pickup == "b"):
    print("The mirror is broken and now you believe you are the most beautiful woman in the world!")
  else:
    print("That's not an answer!")
elif (question  == "C")or(question == "c"):
  print(" ")
  for num in range(3):
    print("The magic mirror says: I am the cleverest guy in the world!\n\
\n\
The queen says: What did you say? Dare you say that again?")
  print(" ")
  print("The queen says angrily: How dare you be cleverer than me! And then the queen broke the magic mirror.")

else:
  print("That's not an option!")


  
