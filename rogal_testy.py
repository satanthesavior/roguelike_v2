
import os
import random
import platform
import items
#import scisors2
try:
	from msvcrt import getch #For windows
except ImportError: #For linux and maybe mac...

	def getch():

		import sys, tty, termios
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch

def pressedkey():
	return getch()

	
		  # 0   1   2   3   4   5   6   7   8   9  10   11  12  13  14  15  16  17  18  19  20  21  22  23 
room = {1:['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'], # ^
		2:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'], # |
		3:['#','.','.','.','.','.','.','.','.','#','#','#','#','.','.','.','.','.','.','.','.','.','.','#'], # |
		4:['#','.','.','.','.','.','.','#','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','#'], # |
		5:['#','.','.','.','.','.','@','#','.','#','.','.','#','.','.','.','.','.','.','.','.','.','.','#'], # |
		6:['#','.','.','.','.','.','.','#','.','.','.','.','#','.','.','.','.','.','.','.','C','.','.','#'], # |
		7:['#','.','.','.','.','#','#','#','.','#','#','C','#','.','.','.','.','.','.','.','.','.','.','#'], # |
		8:['#','.','.','.','.','.','.','.','.','.','#','#','#','.','.','.','.','.','.','.','.','.','.','#'], # |
		9:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'], # |
		10:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'],# |
		11:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','#','#','#','#','#','#','#'],# x
		12:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#'],# |
		13:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#'],# |
		14:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#'],# |
		15:['#','.','.','.','.','.','.','.','$','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#'],# |
		16:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','1','.','.','#'],# |
		17:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#'],# |
		18:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#'],# |
		19:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#'],# |
		20:['#','.','$','.','.','.','.','.','.','.','.','.','.','.','.','#','A','.','.','.','.','.','.','#'],# |
		21:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#'],# |
	    22:['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']}# |
		# <--------------------------------------------y------------------------------------------------------->
stuff  = {'wall'  :  "#",
		  'player':  "@",
		  'empty' :  ".",
		  'money' :  "$",
		  'chest' :  "C"}
potion = {'hp': 10,'exp': 0,'def': 1,'atc': 1,'lvl': 1}
print(potion)
	
GOWNO_KTORE_ZEBRALEM = []
inna_lista = []
pos = [] # 0 is X,1 is Y

def zbieranie():
	for key in room:
		print(room[key])# ta linijka wyswietla duza mape XD

	if pos == [20, 2] and 'melon' in inna_lista:
		print()
	elif pos == [20, 2] and 'melon' not in inna_lista:
		inna_lista.append('melon')
		GOWNO_KTORE_ZEBRALEM.append('hp')
		GOWNO_KTORE_ZEBRALEM.append('hp')
		add_to_inventory(potion, GOWNO_KTORE_ZEBRALEM)
		print("dodoano hp")
		GOWNO_KTORE_ZEBRALEM.clear()

	if pos == [15, 8] and 'sliwka' in inna_lista:
		print()
	elif pos == [15, 8] and 'sliwka' not in inna_lista:
		inna_lista.append('sliwka')
		GOWNO_KTORE_ZEBRALEM.append('hp')
		add_to_inventory(potion, GOWNO_KTORE_ZEBRALEM)
		print("dodoano hp")
		GOWNO_KTORE_ZEBRALEM.pop()

	if pos == [6, 20] and 'rekawice robocze' in inna_lista:
		print()
	elif pos == [6, 20] and 'rekawice robocze' not in inna_lista:
		inna_lista.append('rekawice robocze')
		GOWNO_KTORE_ZEBRALEM.append('def')
		add_to_inventory(potion, GOWNO_KTORE_ZEBRALEM)
		print("dodoano def")
		GOWNO_KTORE_ZEBRALEM.pop()

	if pos == [7, 11] and 'zbroja wielkiego kutanga' in inna_lista:
		print()
	elif pos == [7, 11] and 'zbroja wielkiego kutanga' not in inna_lista:
		inna_lista.append('zbroja wielkiego kutanga')
		GOWNO_KTORE_ZEBRALEM.append('def')
		GOWNO_KTORE_ZEBRALEM.append('def')
		add_to_inventory(potion, GOWNO_KTORE_ZEBRALEM)
		print("dodoano def")
		GOWNO_KTORE_ZEBRALEM.clear()

	if pos == [20, 16] and 'miecz walusa' in inna_lista:
		print()
	elif pos == [20, 16] and 'miecz walusa' not in inna_lista:
		inna_lista.append('miecz walusa')
		GOWNO_KTORE_ZEBRALEM.append('atc')
		GOWNO_KTORE_ZEBRALEM.append('atc')
		add_to_inventory(potion, GOWNO_KTORE_ZEBRALEM)
		print("dodoano atc")
		GOWNO_KTORE_ZEBRALEM.clear()


	if pos == [16, 20] and 'nazgul' in inna_lista:
		print()
	elif pos == [16, 20] and 'nazgul' not in inna_lista:
		inna_lista.append('nazgul')
		import scisors2
		GOWNO_KTORE_ZEBRALEM.append('exp')
		add_to_inventory(potion, GOWNO_KTORE_ZEBRALEM)
		GOWNO_KTORE_ZEBRALEM.clear()

		
################################################################################
################################################################################





def add_to_inventory(inventory, added_items):
	for item in added_items:
		inventory.setdefault(item, 0)
		inventory[item] += 1
	#print()
	#print(inventory)
	return inventory


'''
	if stuff['player'] in room:
		if stuff['player'] == pos[20, 2]:
			print('jupi')
	else:
		print('grrrr')
'''
	#for pos == [20, 2] in room:
		#if pos[stuff['player']] == pos[stuff['$']]:
		#if stuff['player'] in pos[20, 2]:
			#potion['hp'] == potion['hp'] + 2
			#print(potion['hp'])


############################################################################################################
##########################################################################################################
#########################################################################################################
def gamemap():
	for i in range(1,len(room)+1):
		print("".join(room[i]))

def player_pos():
	for i in range(1,len(room)+1):
		if stuff['player'] in room[i]:
			x_axis = i
			y_axis = room[i].index(stuff['player'])
			global pos
			del pos[:]
			pos.append(x_axis)
			pos.append(y_axis)

def updater():
	if platform.system() =='Windows':
		os.system('cls')
	elif platform.system() == 'Linux':
		os.system('clear') #For linux.. I don't know what to do about mac :/
	gamemap()
	player_pos()
	zbieranie()
	print(GOWNO_KTORE_ZEBRALEM)
	print(potion)
	print(inna_lista)
 

def up(ditcioary,inst_replace,inst_player):
	(ditcioary[pos[0]]).pop(pos[1])
	(ditcioary[pos[0]]).insert(pos[1],inst_replace)
	(ditcioary[pos[0]-1]).pop(pos[1])
	(ditcioary[pos[0]-1]).insert(pos[1],inst_player)


def down(ditcioary,inst_replace,inst_player):
	(ditcioary[pos[0]]).pop(pos[1])
	(ditcioary[pos[0]]).insert(pos[1],inst_replace)
	(ditcioary[pos[0]+1]).pop(pos[1])
	(ditcioary[pos[0]+1]).insert(pos[1],inst_player)


def left(ditcioary,inst_replace,inst_player):
	(ditcioary[pos[0]]).pop(pos[1])
	(ditcioary[pos[0]]).insert(pos[1],inst_replace)
	(ditcioary[pos[0]]).pop(pos[1]-1)
	(ditcioary[pos[0]]).insert(pos[1]-1,inst_player)


def right(ditcioary,inst_replace,inst_player):
	(ditcioary[pos[0]]).pop(pos[1])
	(ditcioary[pos[0]]).insert(pos[1],inst_replace)
	(ditcioary[pos[0]]).pop(pos[1]+1)
	(ditcioary[pos[0]]).insert(pos[1]+1,inst_player)



#updater()
gamemap()
player_pos()




while True:
	pressedkey = getch()
	if pressedkey is 'w' or pressedkey is 'W':
		if room[pos[0]-1][pos[1]] is not stuff['wall']:
			up(room, stuff['empty'], stuff['player'])
			updater()
			print(pos)
	elif pressedkey is 's' or pressedkey is 'S':
		if room[pos[0]+1][pos[1]] is not stuff['wall']:
			down(room,stuff['empty'],stuff['player'])
			updater()
			print(pos)
	elif pressedkey is 'a' or pressedkey is 'A':
		if room[pos[0]][pos[1]-1] is not stuff['wall']:
			left(room,stuff['empty'], stuff['player'])
			updater()
			print(pos)
	elif pressedkey is 'd' or pressedkey is 'D':
		if room[pos[0]][pos[1]+1] is not stuff['wall']:
			right(room,stuff['empty'], stuff['player'])
			updater()
			print(pos)
##############################################################################################
##############################################################################################


def get_string_input(question):
    answer = input(question)

    return answer

def create_characterdef():
    points = 5
    while points > 0:
        #while not is_answer_correct:
        stat_to_add = get_string_input("Enter 'H', 'h', 'D', 'd' or 'A', 'a' to add statistic: ")
        if stat_to_add in ["h", "H"]:
            potion["hp"] += 2
        elif stat_to_add in ["D", "d"]:
            potion["def"] += 1
        elif stat_to_add in ["A", "a"]:
            potion["atc"] += 1
        points -= 1
    print('x')


#create_characterdef()
#print(potion)