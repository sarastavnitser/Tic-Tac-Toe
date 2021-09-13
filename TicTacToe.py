class Player:
    name, gamesPlayed, win, draw, loss, percentWin = '', 0, 0, 0, 0, 0.0
    leaderBoard = []

    def __init__(self, owner, games, wins, draws, losses):
        self.name = owner
        self.gamesPlayed = games
        self.win = wins
        self.draw = draws
        self.loss = losses
        if self.gamesPlayed == 0:
            percent = 0
        else:
            percent = round(100 * float(self.win) / self.gamesPlayed, 2)
        self.percentWin = percent

    def __str__(self):
        s = '{:10s}, {:>15d}, {:>7d}, {:>8d}, {:>9d}, {:>11.2f}%'
        return s.format(self.name, self.gamesPlayed, self.win, self.draw, self.loss, float(self.percentWin))

class Board:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    def __init__(self):
        self.coords = []
        self.allPlayers, self.currentplayers = [], []
        self.pointsarray = []
        self.n = 0
        self.playerStats = []

    def run(self):
        while True:
            print()
            print('Please select from one of the following:')
            print('0. Exit Program')
            print('1. Play new game')
            print('2. Change size of board')
            print('3. Add new player')
            print('4. Change two current players')
            print('5. Look up player stats')
            print('6. Display leaderboard')
            print('7. Rules & instructions')
            print('8. Reset all player scores')
            option = -3
            while True:
                try:
                    if -1 < option < 9:
                        break
                    else:
                        option = int(input('Option: '))
                        print()
                except:
                    print('Invalid Option')
                    print()
                    continue
            if option == 0:
                return
            if option == 1:
                self.playGame()
            if option == 2:
                self.dimensions()
            if option == 3:
                self.addPlayer()
            if option == 4:
                self.currentPlayers()
            if option == 5:
                self.playerLookUp()
            if option == 6:
                self.displayLeaderboard()
            if option == 7:
                self.printRules()
            if option == 8:
                self.resetScores()

    def playerLookUp(self):
        while True:
            person = input('Enter Player name to look up: ')
            person = person.strip().capitalize()
            for name in self.playerStats:
                if name.name == person:
                    print(format('Name', '10s'), '    Games Played     Wins     Draws   Losses     Percent Win')
                    print(name)
                    return
            print('name not found')
            return

    def dimensions(self):
        numberlist = []
        self.coords = []
        self.n = 1
        while self.n < 3:
            self.n = int(input('Input size of new board: '))
        for i in range(self.n):
            numberlist.append(i + 1)
        for i in range(self.n):
            self.coords.append([])
        for i in range(self.n):
            for j in range(self.n):
                self.coords[i].append([])
        for i in range(self.n):
            for j in range(self.n):
                self.coords[i][j].append(self.alphabet[j])
                self.coords[i][j].append(str(numberlist[-(i + 1)]))
                self.coords[i][j] = ''.join(self.coords[i][j])
        self.pointsarray = []
        for i in range(self.n):
            self.pointsarray.append([])
        for i in range(self.n):
            for j in range(self.n):
                self.pointsarray[i].append(' ')

    def addPlayer(self):
        while True:
            name = input('Please enter new player name: ')
            name = name.strip().capitalize()
            if name in self.allPlayers:
                print('Name already entered.')
                continue
            else:
                break
        self.allPlayers.append(name)
        playing = Player(name, 0, 0, 0, 0)
        self.playerStats.append(playing)
        return

    def printRules(self):
        print('                 RULES')
        print('---------------------------------------')
        print(' This is a regular game of Tic Tac Toe.')
        print('Board will be shown on a grid. Chose ')
        print('the dimensions of your board. Players')
        print('chose their moves by inputting a letter ')
        print('followed by the number. A player wins ')
        print('once he has a full row, column, or ')
        print('diagonal of only his or her character.')

    def currentPlayers(self):
        while True:
            if len(self.allPlayers) < 2:
                print('Not enough players')
                self.addPlayer()
            else:
                break
        self.currentplayers = []
        print('Please enter two player names to play this game')
        while True:
            player1 = input('please enter registered player1 name: ')
            player1 = player1.strip().capitalize()
            if player1 in self.allPlayers:
                self.currentplayers.append(player1)
                break
            else:
                print('You have not entered a valid player.')
                continue
        while True:
            player2 = input('please enter registered player2 name: ')
            player2 = player2.strip().capitalize()
            if player2 in self.allPlayers and player2 != player1:
                self.currentplayers.append(player2)
                break
            else:
                print('You have not entered a valid player2. ')
                continue

    def displayLeaderboard(self):
        print(format('Name', '10s'), '    Games Played     Wins     Draws   Losses     Percent Win')
        self.playerStats = sorted(self.playerStats, key=lambda x: x.percentWin, reverse=True)
        for player in self.playerStats:
            print(player)

    def resetScores(self):
        for player in self.playerStats:
            player.gamesPlayed = 0
            player.win = 0
            player.draw = 0
            player.loss = 0
            player.percentWin = 0
            print('Scores reset')

    def displayBoard(self):

        x = self.n + 1
        numberlist = []
        rowSeparator = ['  ---']
        for i in range(self.n - 1):
            rowSeparator.append('+')
            rowSeparator.append('---')
        rowSeparator.append('  ')
        for i in range(self.n):
            numberlist.append(i + 1)
        masterBoardArray = []
        for i in range(x + 1):
            masterBoardArray.append([])
        masterBoardArray[0].append('   ')

        for i in range(1, x):
            masterBoardArray[0].append(self.alphabet[i - 1])
            masterBoardArray[0].append('   ')
        masterBoardArray[-1] = masterBoardArray[0]

        for i in range(self.n):
            masterBoardArray[i + 1].append(str(numberlist[-(i + 1)]))
            masterBoardArray[i + 1].append('  ')

        for i in range(self.n):
            for j in range(self.n - 1):
                masterBoardArray[i + 1].append(self.pointsarray[i][j])
                masterBoardArray[i + 1].append(' | ')

        for i in range(self.n):
            masterBoardArray[i + 1].append(self.pointsarray[i][-1])

        for i in range(self.n):
            masterBoardArray[i + 1].append('  ')
            masterBoardArray[i + 1].append(str(numberlist[-(i + 1)]))

        for i in range(self.n - 1):
            masterBoardArray.insert(((i * 2) + 2), rowSeparator)

        for i in range((self.n * 2) + 1):
            print(''.join(masterBoardArray[i]))

    def give_point_index(self, point):
        lister = self.coords
        lstst = [str(self.get_index(lister, point)), str(self.get_index(lister[self.get_index(lister, point)], point))]
        lst2 = ''.join(lstst)
        lst3 = ''.join([lst2[0], lst2[1]])
        return lst3

    def get_index(self, lst, num, index=0):
        index = int(index)
        if str(num) in lst[index]:
            return index
        else:
            return self.get_index(lst, str(num), index + 1)

    def check_list_win(self, alist):
        spc = allx = allo = 0
        for h in alist:
            if h == 'X':
                allx += 1
            elif h == 'O':
                allo += 1
            else:
                spc += 0
        if allx == self.n:
            return 'X'
        elif allo == self.n:
            return 'O'
        else:
            return ''

    def check_win(self):
        # check dim 1
        for a_list in self.pointsarray:
            winner = self.check_list_win(a_list)
            if winner != '':
                return winner
        transposed = map(list, zip(*self.pointsarray))
        for a_list in transposed:
            winner = self.check_list_win(a_list)
            if winner != '':
                return winner
        diag1 = []
        diag2 = []
        for i in range(self.n):
            diag1.append(self.pointsarray[i][i])
            diag2.append(self.pointsarray[i][-(i + 1)])
        for a_list in [diag1, diag2]:
            winner = self.check_list_win(a_list)
            if winner != '':
                return winner
        return ''

    def emptyArray(self):
        self.pointsarray = []
        for i in range(self.n):
            self.pointsarray.append([])
        for i in range(self.n):
            for j in range(self.n):
                self.pointsarray[i].append(' ')

    def playGame(self):
        if len(self.allPlayers) < 2:
            print('Not enough players')
            self.addPlayer()
        if len(self.currentplayers) == 0:
            self.currentPlayers()
        if self.n < 3:
            self.dimensions()
        self.displayBoard()
        charlist = ['X', 'O']
        for i in range(self.n ** 2 - 1):
            for j in range(2):
                while True:
                    try:
                        while True:
                            print(self.currentplayers[j],
                                  ', please enter point coordinates of desired space - letter '
                                  'immediately followed by number - no space in between', sep='')
                            point = input().strip().lower()
                            thisindex = self.give_point_index(point)
                            newindex = str(thisindex)
                            if self.pointsarray[int(newindex[0])][int(newindex[1])] != ' ':
                                continue
                            else:
                                break
                        break
                    except:
                        continue
                self.pointsarray[int(newindex[0])][int(newindex[1])] = charlist[j]
                self.displayBoard()
                the_winner = self.check_win()
                if the_winner != '':
                    if the_winner == 'X':
                        winner = self.currentplayers[0]
                        loser = self.currentplayers[1]
                    if the_winner == 'O':
                        winner = self.currentplayers[1]
                        loser = self.currentplayers[0]
                    print("WE HAVE A WINNER IT IS", winner.upper())
                    for playing in self.playerStats:
                        if winner == playing.name:
                            playing.win += 1
                            playing.gamesPlayed += 1
                            playing.percentWin = round(100 * (playing.win / playing.gamesPlayed), 2)
                        if loser == playing.name:
                            playing.loss += 1
                            playing.gamesPlayed += 1
                            playing.percentWin = round(100 * (playing.win / playing.gamesPlayed), 2)
                    self.emptyArray()
                    return
                isempty = []
                for i in range(self.n):
                    for j in range(self.n):
                        if self.pointsarray[i][j] == ' ':
                            isempty.append(0)
                if len(isempty) == 0:
                    for playing in self.playerStats:
                        if self.currentplayers[1] == playing.name:
                            playing.draw += 1
                            playing.gamesPlayed += 1
                            playing.percentWin = round(100 * (playing.win / playing.gamesPlayed), 2)
                        if self.currentplayers[0] == playing.name:
                            playing.draw += 1
                            playing.gamesPlayed += 1
                            playing.percentWin = round(100 * (playing.win / playing.gamesPlayed), 2)
                    self.emptyArray()
                    return

class ContactItem:  # ContactItem
    lastName, firstName, email, homephone = '', '', '', ''

    def __init__(self, last, first, mail, number1):  # constructor
        self.lastName = last.strip().capitalize()
        self.firstName = first.strip().capitalize()
        self.email = mail.strip().lower()
        self.homephone = number1

    def __str__(self):
        s = '{:12s}, {:>10s}, {:>25s}, {:>12s}'
        return s.format(self.lastName, self.firstName, self.email, self.homephone)

class ContactBook:
    owner = ''
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    def __init__(self, name):
        self.owner = name.strip().capitalize()
        self.contact_list = []

    def __eq__(self, other):
        if self.lastName.lower() == other.lastName.lower() and \
                self.firstName.lower() == other.firstName.lower():
            return True

        else:
            return False

    def addNewContact(self, last_name, first_name, newMail, newPhone):
        if len(last_name) == 0:
            print("Invalid last name")
            return
        if len(first_name) == 0:
            print("Invalid first name")
            return
        for contact in self.contact_list:
            if last_name.strip().capitalize() == contact.lastName:
                if first_name.strip().capitalize() == contact.firstName:
                    print("Contact already exists")
                    print()
                    return
        if newMail.strip() == '':
            print("Invalid Email Address")
            return
        else:
            newMail = newMail.strip().lower()
            end = newMail.strip()[-4:-1], newMail.strip()[-1]
            acceptableEnds = ['.com', '.edu', '.gov', '.net']
            if '@' not in newMail or ''.join(end) not in acceptableEnds or newMail.strip()[0] == '@' or \
                    newMail.count('@') > 1 or (newMail.strip()[-5] == "@" and newMail.strip()[-4] == "."):
                print("Invalid Email Address")
                return
        if newPhone.strip() == '':
            print("Invalid Phone Number")
            return
        else:
            if len(newPhone.strip()) != 12 or newPhone.strip()[3] != '-' or newPhone.strip()[7] != '-':
                print("Invalid Phone Number")
                return

            elif newPhone[0] not in self.numbers or newPhone[1] not in self.numbers or newPhone[2] not in \
                    self.numbers or newPhone[4] not in self.numbers or newPhone[5] not in self.numbers or \
                    newPhone[6] not in self.numbers or newPhone[8] not in self.numbers or newPhone[9] not in \
                    self.numbers or newPhone[10] not in self.numbers or newPhone[11] not in self.numbers:
                print("Invalid Phone Number")
                return
        contact = ContactItem(last_name, first_name, newMail, newPhone)
        self.contact_list.append(contact)
        self.contact_list.sort(key=lambda x: (x.lastName, x.firstName, x.email, x.homephone))
        return

    def updateContact(self, lastName, firstName, newLast, newFirst, newMail, newPhone):
        for contact in self.contact_list:
            if newLast.strip().capitalize() == contact.lastName:
                if newFirst.strip().capitalize() == contact.firstName:
                    print("Contact Already Exists")
                    print()
                    return
        for contact in self.contact_list:
            if newLast.strip().capitalize() == contact.lastName:
                if firstName.strip().capitalize() == contact.firstName:
                    print("Contact Already Exists")
                    print()
                    return
        for contact in self.contact_list:
            if lastName.strip().capitalize() == contact.lastName:
                if newFirst.strip().capitalize() == contact.firstName:
                    print("Contact Already Exists")
                    print()
                    return
        for contact in self.contact_list:
            if lastName.strip().capitalize() == contact.lastName:
                if firstName.strip().capitalize() == contact.firstName:
                    if len(newLast.strip()) == 0:
                        contact.lastName = contact.lastName
                    else:
                        contact.lastName = newLast.strip().capitalize()
                    if len(newFirst.strip()) == 0:
                        contact.firstName = contact.firstName
                    else:
                        contact.firstName = newFirst.strip().capitalize()
                    if len(newMail.strip()) == 0:
                        contact.email = contact.email
                    else:
                        end = newMail.strip()[-4:-1], newMail.strip()[-1]
                        acceptableEnds = ['.com', '.edu', '.gov', '.net']
                        if '@' not in newMail or ''.join(end) not in acceptableEnds or newMail.strip()[0] == '@' or \
                                newMail.count('@') > 1 or (newMail.strip()[-5] == "@" and newMail.strip()[-4] == "."):
                            print("Invalid Email Address")
                            return
                        else:
                            contact.email = newMail.strip().lower()
                    if newPhone.strip() == '':
                        contact.homephone = contact.homephone
                        return
                    else:
                        if len(newPhone.strip()) != 12 or newPhone.strip()[3] != '-' or newPhone.strip()[7] != '-':
                            print("Invalid Phone Number")
                            return
                        elif newPhone.strip()[0] not in self.numbers or newPhone.strip()[1] not in self.numbers or \
                                newPhone.strip()[2] not in self.numbers or newPhone.strip()[4] not in self.numbers or \
                                newPhone.strip()[5] not in self.numbers or newPhone.strip()[6] not in self.numbers or \
                                newPhone.strip()[8] not in self.numbers or newPhone.strip()[9] not in self.numbers or \
                                newPhone.strip()[10] not in self.numbers or newPhone.strip()[11] not in self.numbers:
                            print("Invalid Phone Number")
                            return
                        else:
                            contact.homephone = newPhone.strip()
                            return
                else:
                    continue

            else:
                continue
        print('Contact not found')
        print()

    def removeContact(self, lastName, firstName):
        for contact in self.contact_list:
            if lastName.strip().capitalize() == contact.lastName:
                if firstName.strip().capitalize() == contact.firstName:
                    print(contact.lastName, contact.firstName, 'removed from conatacts')
                    print()
                    self.contact_list.remove(contact)
                    return
        print('Contact not found')
        print()

    def locateContact(self, lastName, firstName):
        for contact in self.contact_list:
            if lastName.strip().capitalize() == contact.lastName:
                if firstName.strip().capitalize() == contact.firstName:
                    print(contact)
                    print()
                    return
        print('Contact not found')
        print()

    def printByName(self):
        if len(self.contact_list) == 0:
            print('sorry, no contacts found')
            print()
            return
        print(self.owner, '\'s contacts:', sep='')
        self.contact_list = sorted(self.contact_list, key=lambda x: (x.lastName, x.firstName, x.email, x.homephone))
        for contact in self.contact_list:
            print(contact)
        print()
        return

    def printByEmail(self):
        if len(self.contact_list) == 0:
            print('sorry, no contacts found')
            print()
            return
        print(self.owner, '\'s contacts:', sep='')
        self.contact_list = sorted(self.contact_list, key=lambda x: (x.email, x.lastName, x.firstName, x.homephone))
        for contact in self.contact_list:
            print(contact)
        print()
        return

    def printByPhone(self):
        if len(self.contact_list) == 0:
            print('sorry, no contacts found')
            print()
            return
        print(self.owner, '\'s contacts:', sep='')
        self.contact_list = sorted(self.contact_list, key=lambda x: (x.homephone, x.lastName, x.firstName, x.email))
        for contact in self.contact_list:
            print(contact)
        print()
        return

a = Board()
a.run()

