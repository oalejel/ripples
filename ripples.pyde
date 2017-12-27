"""
Omar Al-Ejel

Click to summon a new ripple or use arrow keys

"""



# contains tuples ((x,y), radius, (topleft, topright, bottomleft, bottomright))
# the tuple at the end is used to check if circle still in box
circles = []
lastMillis = 0
playerX = 0
playerY = 0

def setup():
    pixelDensity(2)
    background(0)
    size(500, 500)
    # fullScreen()
    global playerX, playerY
    playerX = width / 2
    playerY = height / 2

def draw():
    global lastMillis
    m = millis() // 600
    # print(m)
    # print(lastMillis)
    if lastMillis != m:
        lastMillis = m
        newRipple()
    
    # println("here1")
    fill(0)
    # must use a static definition of length since size can change in draw
    # function
    startLen = len(circles)
    indicesToRemove = []
    stroke(255)
    for i in range(0, startLen):
        c = circles[i]
        x = c[0][0]
        y = c[0][1]
        r = c[1]
        distanceCheck = c[2]

        if distanceCheck[0] < r and distanceCheck[1] < r and distanceCheck[2] < r and distanceCheck[3] < r:
            # print("time to remove")
            indicesToRemove.append(i)
            continue
        ellipse(x, y, 2 * r, 2 * r)
        circles[i][1] = r + 1
    # must traverse backwards to avoid removing wanted circles
    # print(range(len(indicesToRemove), 0))
    if len(indicesToRemove):
        for index in indicesToRemove[::-1]:
            del circles[index]
            # print("removing circle")
            # print(circles)


def newRipple():
    x = playerX
    y = playerY

    topLeft = sqrt(pow(x, 2) + pow(y, 2))
    topRight = sqrt(pow(x - width, 2) + pow(y, 2))
    bottomLeft = sqrt(pow(x, 2) + pow(y - height, 2))
    bottomRight = sqrt(pow(x - width, 2) + pow(y - height, 2))

    distanceChecklist = (topLeft, topRight, bottomLeft, bottomRight)

    newCircle = [(x, y), 0, distanceChecklist]
    circles.append(newCircle)
    # print(circles)

def keyPressed():
    global playerY, playerX
    print(keyCode)
    if keyCode == 38:
        playerY -= 3
    elif keyCode == 40:
        playerY += 3
    elif keyCode == 37:
        playerX -= 3
    elif keyCode == 39:
        playerX += 3

def mousePressed():
    x = mouseX
    y = mouseY

    topLeft = sqrt(pow(x, 2) + pow(y, 2))
    topRight = sqrt(pow(x - width, 2) + pow(y, 2))
    bottomLeft = sqrt(pow(x, 2) + pow(y - height, 2))
    bottomRight = sqrt(pow(x - width, 2) + pow(y - height, 2))

    distanceChecklist = (topLeft, topRight, bottomLeft, bottomRight)

    newCircle = [(x, y), 0, distanceChecklist]
    circles.append(newCircle)
    print(circles)