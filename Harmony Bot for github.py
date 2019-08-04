import discord
from discord.ext import commands

#Bot by Yarmoski
#Can easily be customized to fit any needs, not just socialism related :)

### DISCLAIMER: Requires discord.py and discord developer tools

#add "uacceptable words" here, this is not an exhaustive list

raw_words = """republic
freedom
america
usa
united
states
democracy
president
ability
exemption
flexibility
immunity
opportunity
power
privilege
right
abandon
abandonment
bent
compass
discretion
facility
indulgence
latitude
laxity
leeway
liberty
margin
play
prerogative
profligacy
range
rein
rope
scope
sweep
swing
unrestraint
carte blanche
elbowroom
free rein
full play
full swing
laissez faire
own accord
plenty of rope
rampancy
equality
freedom
justice
commonwealth
egalitarianism
emancipation
equalitarianism
republic
suffrage
liberal government
representative government
australia
austria
canada
costa rica
denmark
finland
germany
iceland
ireland
luxembourg
malta
mauritius
netherlands
new Zealand
norway
spain
sweden
switzerland
united kingdom
uruguay
eu
usa
uk
britain
british
american
mexico
mexican
canadian
austrailian
voting
vote
rights
tiananmen
square
april
15
1989
protest
demonstration
riot
rebel
rebellion
taiwan"""

#Since I scraped this data from online, I needed to better format it before using it with the bot
words_into_list = raw_words.split('\n')
list_of_lists = [i.split(' ') for i in words_into_list]
unacceptable_terms = [i for sublist in list_of_lists for i in sublist]

#No commands are present, but commands can be implemented
bot = commands.Bot(command_prefix = '.') #Do not delete this though



#EVENTS

#Shows in console when bot is up and running
@bot.event
async def on_ready():
	print('Bot is ready!')

#Main harmony ensurer logic
@bot.event
async def on_message(message):
	if message.author.id != 607331665563484160: #If not the bot
		review = False
		new_message = []
		#individual words of message are put onto this list
		contents = message.content.split(" ") 
		print(contents)
		
		#Loops through each word in message and replaces any unacceptable words
		#The words are either replaced or unchanged and added to new_message list
		for word in contents:
			if word.lower() in unacceptable_terms:
				if word.lower() == 'democracy':
					new_message.append('Socialism')
				elif word.lower() in ['usa', 'america', 'united states', 'taiwan']:
					new_message.append("People's Republic of China")
				elif word.lower() in ['tiananmen', 'square']:
					new_message.append("Nothing")
				else:
					new_message.append('-' * len(word))
			else:
				new_message.append(word)

		#Loops through each word in message
		#if it comes across banned word, informs user and stops looping
		for word in contents:
			if word.lower() in unacceptable_terms:
				await message.delete()
				await message.channel.send(f'{message.author.mention}, your message must be reviewed by the party.')
				review = True
				break
			else:
				pass

		#If a banned word was detected, the newly edited message from new_message list will be sent
		if review == True:
			await message.channel.send('Your party approved message is: ' + ' '.join(new_message))




#Needs bot token to work
bot.run('BOT TOKEN GOES HERE')