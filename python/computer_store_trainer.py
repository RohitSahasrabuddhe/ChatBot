from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(
    'Norman',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database='./database.sqlite3'
)
bot.set_trainer(ListTrainer)
#Training starts here
bot.train(["Hi ",	"Hello, how can I help you?",
"Hello",	"Hi, how can I help you?",
"Do you have apple pencil?",	"Let me check, We do have it. Do you want me to keep it on hold?",	"Yes please",	"We need your name and USC ID",	"Here is my name and USC ID",	"Done, can I help you with anything else","No, thanks",	"Bye, Have a nice day",
"Do you have apple air pods?",	"Let me check, We do have it. Do you want me to keep it on hold?",	"Yes please",	"We need your name and USC ID",	"Here is my name and USC ID",	"Done, can I help you with anything else","No, thanks",	"Bye, Have a nice day",
"Do you have apple macbook pro 13 inch?",	"Let me check, We do have it. Do you want me to keep it on hold?",	"Yes please",	"We need your name and USC ID",	"Here is my name and USC ID",	"Done, can I help you with anything else","No, thanks",	"Bye, Have a nice day",
"Do you have apple macbook pro 15 inch?",	"Let me check, We do have it. Do you want me to keep it on hold?",	"Yes please",	"We need your name and USC ID",	"Here is my name and USC ID",	"Done, can I help you with anything else","No, thanks",	"Bye, Have a nice day",
"Do you have apple macbook air ?",	"Let me check, We do have it. Do you want me to keep it on hold?",	"Yes please",	"We need your name and USC ID",	"Here is my name and USC ID",	"Done, can I help you with anything else","No, thanks",	"Bye, Have a nice day","No, thanks",	"Bye, Have a nice day",
"Do you have apple ear phones?",	"Let me check, We do have it. Do you want me to keep it on hold?",	"Yes please",	"We need your name and USC ID",	"Here is my name and USC ID",	"Done, can I help you with anything else","No, thanks",	"Bye, Have a nice day",
"Do you have apple iMac?",	"Let me check, We do have it. Do you want me to keep it on hold?",	"Yes please",	"We need your name and USC ID",	"Here is my name and USC ID",	"Done, can I help you with anything else","No, thanks",	"Bye, Have a nice day",
"Can you repair my mac?",	"We don't repair computers in store, but we do send it to repair center. It usually takes 5 business days to get it back.",	"Okay, I want to repair",	"We need your name and USC ID",	"Here is my name and USC ID",	"Done, can I help you with anything else","No, thanks",	"Bye, Have a nice day",
"repair",	"We don't repair computers in store, but we do send it to repair center. It usually takes 5 business days to get it back.",	"No, I dont want to repair",	"Have a nice day",
"broken mac",	"We don't repair computers in store, but we do send it to repair center. It usually takes 5 business days to get it back.",	"Okay, I want to repair",	"We need your name and USC ID",	"Here is my name and USC ID",	"Done, can I help you with anything else","No, thanks",	"Bye, Have a nice day",
"macbook not working",	"We don't repair computers in store, but we do send it to repair center. It usually takes 5 business days to get it back.",	"No, I dont want to repair",	"Have a nice day",
"Thanks",	"Have a nice day",
"bye",	"Bye, have a nice day",
"Good Bye",	"Bye Bye, have a nice day",
]);

