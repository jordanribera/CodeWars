import random

def interpret(code):
    print "<pre>" + code + "</pre>"
    output = ""
    direction = "right"
    directions = ["up", "down", "left", "right"]
    code = code.split("\n")
    print code
    for x in range(0, len(code)):
        code[x] = list(code[x])
    running = True
    safeCounter = 0
    pointerX = 0
    pointerY = 0
    stack = []
    stringMode = False
    while (running):
        #read pointer location
        value = code[pointerY][pointerX]
        print value
        
        if (value == "\""):
            stringMode = not stringMode
        else:
            
            if (stringMode):
                stack.append(ord(value))
            
            if (stringMode == False):
                #simple flow
                if (value == "^"):
                    direction = "up"
                if (value == "v"):
                    direction = "down"
                if (value == "<"):
                    direction = "left"
                if (value == ">"):
                    direction = "right"
                    
                #advanced flow
                if (value == "?"):
                    direction = directions[random.randint(0,3)]
                if (value == "_"):
                    a = stack.pop()
                    if (a == 0):
                        direction = "right"
                    else:
                        direction = "left"
                if (value == "|"):
                    a = stack.pop()
                    if (a == 0):
                        direction = "down"
                    else:
                        direction = "up"
                if (value == "#"):
                    #move the pointer
                    if (direction == "up"):
                        pointerY = (pointerY - 1) % len(code)
                    if (direction == "down"):
                        pointerY = (pointerY + 1) % len(code)
                    if (direction == "left"):
                        pointerX = (pointerX - 1) % (len(code[0]) + 1)
                    if (direction == "right"):
                        pointerX = (pointerX + 1) % (len(code[0]) + 1)
                if (value == "@"):
                    running = False
                    return output
                        
                #misc stack manipulation
                if (value == ":"):
                    if (len(stack) == 0):
                        stack.append(0)
                    else:
                        a = stack.pop()
                        stack.append(a)
                        stack.append(a)
                if (value == "\\"):
                    if (len(stack) < 2):
                        stack.append(0)
                    else:
                        a = stack.pop()
                        b = stack.pop()
                        stack.append(a)
                        stack.append(b)
                if (value == "$"):
                    a = stack.pop()
                
                #output
                if (value == "."):
                    output = output + str(stack.pop())
                    print "output: " + output
                if (value == ","):
                    output = output + chr(stack.pop())
                    print "output: " + output
                    
                #numbers onto stack
                if representsInt(value):
                    stack.append(int(value))
                    
                #addition
                if (value == "+"):
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a+b)
                    
                #subtraction
                if (value == "-"):
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b-a)
                
                #multiplication
                if (value == "*"):
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a*b)
                    
                #integer division
                if (value == "/"):
                    a = stack.pop()
                    b = stack.pop()
                    if (a == 0):
                        stack.append(0)
                    else:
                        stack.append(b//a)
                        
                #modulus
                if (value == "%"):
                    a = stack.pop()
                    b = stack.pop()
                    if (a == 0):
                        stack.append(0)
                    else:
                        stack.append(b%a)
                        
                #logical not
                if (value == "!"):
                    a = stack.pop()
                    if (a == 0):
                        stack.append(1)
                    else:
                        stack.append(0)
                        
                #greater than
                if (value == "`"):
                    a = stack.pop()
                    b = stack.pop()
                    if (b > a):
                        stack.append(1)
                    else:
                        stack.append(0)
                        
                #p and g
                if (value == "p"):
                    y = stack.pop()
                    x = stack.pop()
                    v = stack.pop()
                    
                    v = chr(v)
                    code[y][x] = v
                if (value == "g"):
                    y = stack.pop()
                    x = stack.pop()
                    v = code[y][x]
                    v = ord(v)
                    
                    stack.append(v)
                        
        print stack
        
        #move the pointer
        if (direction == "up"):
            pointerY = (pointerY - 1) % len(code)
        if (direction == "down"):
            pointerY = (pointerY + 1) % len(code)
        if (direction == "left"):
            pointerX = (pointerX - 1) % (len(code[0]) + 1)
        if (direction == "right"):
            pointerX = (pointerX + 1) % (len(code[0]) + 1)
        #safeCounter = safeCounter + 1
        if (safeCounter > 1000):
            running = False
    return output
    
def representsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False