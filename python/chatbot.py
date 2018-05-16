# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatterbot = ChatBot("Training Example")
#chatterbot.set_trainer(ChatterBotCorpusTrainer)

#chatterbot.train(
  #  "chatterbot.corpus.english.greetings",
 #   "chatterbot.corpus.english.conversations"
#)
# Get a response to the input text 'How are you?'
inputSentence = input('')
response = chatterbot.get_response(inputSentence)
print(response)