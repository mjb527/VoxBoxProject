Counter = 0
class Button:
    Title = ""
    Img = ""
    Ttv = ""
    ID = 0
    def createButton(self, title, img, ttv): #will create the object of button, need title, image, and text to voice
        self.Title = title
        self.Img = img
        self.Ttv = ttv
        self.ID = Counter
        Counter+1

    def getTitle(self):
        return self.Title
    def setTitle(self, title):
        self.Title = title
    def getImg(self):
        return self.Img
    def setImg(self, img):
        self.Img = img
    def getTtv(self):
        return self.Ttv
    def setTtv(self, ttv):
        self.Ttv = ttv
    def getID(self):
        return self.ID

def yesOrNo():
    bool = False
    YN = False
    print('Please enter \"yes\" or \"no\"')
    while bool == False:
        string = str(input())
        if string.lower() == 'yes':
            YN = True; bool = True
        elif string.lower() == 'no':
            YN = False; bool = True
        else:
            print('Please enter either \"yes\" or \"no\"')
    return YN

buttons = []

def createButt():
    buttonName = str(input('Please enter the button name'))
    print('Would you like to upload an image?')
    hasImg = yesOrNo()
    image = ''
    if hasImg == True: # need to upload image here as variable 'img'
        print('this is just to stop the red underline')
    print('Is the title the same as the phrase you would like the device to say?')
    same = yesOrNo()
    voice = ''
    if same == True:
        voice = buttonName
    else:
        print("Please enter the phrase you would like to hear when the button is pressed")
        voice = str(input())
    buttons.append(Button.createButton(buttonName, image, voice))
def editButton():
    for i in range(0, len(buttons)):
        print(i+1, ': ', buttons[i])
    print('Please select a number of the button you would like to change or enter \"back\" to return to the main menu')
    problem = True
    while problem:
        try:
            myString = str(input())
            if myString.lower() == 'back':
                #go to main menu
                problem = False
                print('pretend we go to main menu for now')
            else:
                myInt = int(myString)
                if myInt > 0 and myInt < len(buttons):
                    problem = False
        except ValueError:
            print('Please enter a number between 1 and ', len(buttons), 'or \"back\" to return to main menu')
            problem = True
    print('You have selected ',  buttons[myInt], ', is this correct?')
    bool = yesOrNo()
    if bool == False:
        editButton()
    else:
        print('What would you like to edit? \n  1) Button Title \n  2) Image \n  3) Spoken Phrase')
        problem = True
        decision = 0
        while problem:
            try:
                decision = int(input())
                if decision > 0 and decision < 4:
                    problem = False
            except ValueError:
                print('Please enter a number listed (1, 2, 3)')
                problem = True
        newString = ''
        if decision == 1:
            newString = str(input('Please enter the new Button Title: '))
            Button.setTitle(buttons[myInt], newString)
            print('The new Title of ', buttons[myInt], ' is ', newString)
        elif decision == 2:
            newString = str(input('Please enter the new Image: '))
            Button.setImg(buttons[myInt], newString)
            print(newString, ' is now the image for ', buttons[myInt])
        elif decision == 3:
            newString == str(input('Pleae enter the new Spoken Phrase: '))
            Button.setTtv(buttons[myInt], newString)
            print('This button will now read \"', newString, '\" when pressed')
def saveButtons():
    toSave = ''
    for i in range (0,len(buttons)):
        title = Button.getTitle(buttons[i])
        image = Button.getImg(buttons[i])
        ttv = Button.getTtv(buttons[i])
        toSave = toSave + title + '|' + image + '|' + ttv + '\n'
    #save to file here
def loadButtons():
    file = open('buttons.txt', 'w+')
    nextLine = True
    fileLine = ''
    fileLines = []
    file = file.read()
    while nextLine:
        fileLines.append(file.split('\n'))
        if fileLine == '':
            nextLine = False
            break
    for i in range (len(fileLines)):
        theLine = fileLines[i]
        b = 0
        e = 0
        parts = []
        for j in range (len(theLine)):
            if theLine.index(j)=='|':
                e = j
                parts.append(theLine[b,e])
                b = e
            if theLine.index(j)=='\n':
                buttons.append(Button.createButton(parts[0],parts[1],parts[2],parts[3]))
