def chatbot(bot_name):
  print('Hello! My name is {0}.'.format(bot_name))

def remind_name():
  print('\n Please,remind me your name.')  
  name=input()
  print('\n What a great name it is,{0}!'.format(name))

def feel():
  print('\n Are you okay? Yes/No')  
  input()

def colour():
  print('\n Which is your favourite colour?')
  favcolour=input()
  print('\n I also like {0}.'.format(favcolour))

def end():
  print('\n Have a nice day!')
  input()
  print('Bye!')

chatbot('chatty')
remind_name()
feel()
colour()
end()
