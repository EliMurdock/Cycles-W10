import turtle
import time


#create the window, with no auto refreshing
class Main_Window():
    def __init__():
        turtle.tracer(0,0) 
        main_window = turtle.Screen()
        main_window.title("Cycle")
        main_window.bgcolor("black")
        main_window.setup(width = 1000, height = 700)
        return main_window

#create player 1
class Player_One():
    def create():
        player1 = turtle.Turtle()
        player1.color("#228B22")
        player1.shape("square")
        player1.penup()
        player1.speed(0)
        player1.setposition(-210, 0)
        return player1

#create player 2
class Player_Two():
    def create():
        player2 = turtle.Turtle()
        player2.color("#0000FF")
        player2.shape("square")
        player2.penup()
        player2.speed(0)
        player2.setposition(189, 0)
        return player2

#create writing bot
class Writing_Bot():
    def create():
        writebot = turtle.Turtle()
        writebot.color("white")
        writebot.penup()
        writebot.hideturtle()
        return writebot

#set player variables
playerspeed = 21
gamespeed = 1
taillength = 10
growth = 0.2
playerinput1 = 'w'
playerinput2 = 'i'



#changes cycle direction, won't change if it is reverse

keyid = {'w':1,'a':2,'s':4,'d':3,'i':1,'j':2,'k':4,'l':3}
def set_input(key):
    global playerinput1, playerinput2
    if key in ['w','a','s','d'] and keyid[key] + keyid[playerinput1] != 5:
        playerinput1 = key
    elif key in ['i','j','k','l'] and keyid[key] + keyid[playerinput2] != 5:
        playerinput2 = key
    else:
        pass

#detects when the specified keys are pressed and updates the saved key
for keypress in ['w','a','s','d','i','j','k','l']:
    turtle.onkeypress(lambda key=keypress: set_input(key), str(keypress))
turtle.listen()

# empty lists to save coords and the associated turtles
tailcoords1 = []
tailcoords2 = []
playerturtles1 = []
playerturtles2 = []
gameover = False


# main game loop to move all turtles
main_window = Main_Window.__init__()
player1 = Player_One.create()
player2 = Player_Two.create()
writebot = Writing_Bot.create()
while True:

    time.sleep(0.1/gamespeed)
    #save the coordinates for the first player
    y = player1.ycor()
    x = player1.xcor()
    location1 = [x,y]
    tailcoords1.append(location1)

    #movement for the first player
    if playerinput1 == "w":
        y += playerspeed
    elif playerinput1 == "a":
        x -= playerspeed
    elif playerinput1 == "s":
        y -= playerspeed
    elif playerinput1 == "d":
        x += playerspeed
    player1.sety(y)
    player1.setx(x)

    #movement for the first player's tail
    if len(tailcoords1) > taillength:
        tailcoords1.pop(0)
        for i in range(len(playerturtles1)):
            playerturtles1[i].setposition(tailcoords1[i])
    else:
        playerturtle1 = turtle.Turtle()
        playerturtle1.color("#32CD32")
        playerturtle1.shape("square")
        playerturtle1.penup()
        playerturtle1.speed(0)
        playerturtle1.setposition(location1)
        playerturtles1.append(playerturtle1)



    #save the coordinates for the second player
    y = player2.ycor()
    x = player2.xcor()
    location2 = [x,y]
    tailcoords2.append(location2)

    #movement for the second player
    if playerinput2 == "i":
        y += playerspeed
    elif playerinput2 == "j":
        x -= playerspeed
    elif playerinput2 == "k":
        y -= playerspeed
    elif playerinput2 == "l":
        x += playerspeed
    player2.sety(y)
    player2.setx(x)

    #movement for the second player's tail
    if len(tailcoords2) > taillength:
        tailcoords2.pop(0)
        for i in range(len(playerturtles2)):
            playerturtles2[i].setposition(tailcoords2[i])
    else:
        playerturtle2 = turtle.Turtle()
        playerturtle2.color("#1F51FF")
        playerturtle2.shape("square")
        playerturtle2.penup()
        playerturtle2.speed(0)
        playerturtle2.setposition(location2)
        playerturtles2.append(playerturtle2)
    


    # check for game end
    for player in [player1, player2]:
        if (player1.pos() == player2.pos() or
            [player.xcor(),player.ycor()] in tailcoords1 or 
            [player.xcor(),player.ycor()] in tailcoords2 or 
            player.xcor() < -500 or 
            player.xcor() > 500 or
            player.ycor() < -350 or
            player.ycor() > 350):
            gameover = True
    
    #when game is over, turns cycles white and writes game over
    if gameover == True:
        growth = 0
        for player in [player1, player2]:
            player.color("#D3D3D3")
        for tailturtle in playerturtles1:
            tailturtle.color("#C0C0C0")
        for tailturtle in playerturtles2:
            tailturtle.color("#C0C0C0")
        writebot.goto(0,0)
        writebot.write("GAME OVER", align="center", font=("Courier", 60, "bold"))

    #updates screen manually, increases tail length
    turtle.update()
    taillength += growth