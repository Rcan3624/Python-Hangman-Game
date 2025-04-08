# Ryan Cannon
# SDEV 220 Final Project
# Create a hangman game
# May 19, 2022

''' Changes made to the original code listed below

Adjusted the height for the letter buttons in line 65

Moved the blank line spaces to the left for more room for longer words in line 46

Moved the exit button further to the right in line 89

Added more words to the list in line 40

'''



#Hangman - Project
#Import modules
import random
from tkinter import *
from tkinter import messagebox

score = 0
run = True

#Main loop
while run:
    root = Tk()
    root.geometry('1000x2500')
    root.title('HANGMAN BY PYTHON')
    root.config(bg = '#ffffe7')
    count = 0
    win_count = 0
    #choosing word
    # words = ['programming', 'data', 'python', 'code', 'geeks', 'computer', 'engineer', 'word', 'science', 
    #          'machine', 'java', 'college', 'player', 'mobile', 'image'] 
    words = ['programming', 'data', 'python', 'code', 'geeks', 'computer', 'engineer', 'word', 'science',
             'machine', 'java', 'college', 'player', 'mobile', 'image']
    word = random.choice(words)
   
 
    #creation a dashes of secret word
    x = 150
    for i in range(0,len(word)):
        x += 60
        exec('d{}=Label(root,text="_",bg="#ffffe7",font=("arial",40))'.format(i))
        exec('d{}.place(x={},y={})'.format(i,x,450))
        
    #Creating letters icon and Hangman images.
    # letters icon
    icon = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for let in icon:
        exec('{}=PhotoImage(file="{}.png")'.format(let,let))
        
    #hangman images
    hangman_img = ['h1','h2','h3','h4','h5','h6','h7']
    for hangman in hangman_img:
        exec('{}=PhotoImage(file="{}.png")'.format(hangman,hangman))
        
    #Placing letters icon and hangman img on the screen
    #Buttons placement
    button = [['b1','a',0,555],['b2','b',70,555],['b3','c',140,555],['b4','d',210,555],['b5','e',280,555],['b6','f',350,555],['b7','g',420,555],['b8','h',490,555],['b9','i',560,555],['b10','j',630,555],['b11','k',700,555],['b12','l',770,555],['b13','m',840,555],['b14','n',0,608],['b15','o',70,608],['b16','p',140,608],['b17','q',210,608],['b18','r',280,608],['b19','s',350,608],['b20','t',420,608],['b21','u',490,608],['b22','v',560,608],['b23','w',630,608],['b24','x',700,608],['b25','y',770,608],['b26','z',840,608]]

    for q1 in button:
        exec('{}=Button(root,bd=0,command=lambda:check("{}","{}"),bg="#ffffe7",activebackground="#ffffe7",font=10,image={})'.format(q1[0],q1[1],q1[0],q1[1]))
        exec('{}.place(x={},y={})'.format(q1[0],q1[2],q1[3]))
        
    #hangman placement
    hang = [['c1','h1'],['c2','h2'],['c3','h3'],['c4','h4'],['c5','h5'],['c6','h6'],['c7','h7']]
    for p1 in hang:
        exec('{}=Label(root,bg="#ffffe7",image={})'.format(p1[0],p1[1]))

    # placement of first hangman image
    c1.place(x = 300,y =- 50)
    
    #exit button
    def close():
        global run
        answer = messagebox.askyesno('ALERT','YOU WANT TO EXIT THE GAME?')
        if answer == True:
            run = False
            root.destroy()
            
    e1 = PhotoImage(file = 'exit.png')
    ex = Button(root,bd = 0,command = close,bg="#ffffe7",activebackground = "#ffffe7",font = 10,image = e1)
    ex.place(x=870,y=10)
    s2 = 'SCORE:'+str(score)
    s1 = Label(root,text = s2,bg = "#ffffe7",font = ("arial",25))
    s1.place(x = 10,y = 10)

    #check function
    def check(letter,button):
        global count,win_count,run,score
        exec('{}.destroy()'.format(button))
        if letter in word:
            for i in range(0,len(word)):
                if word[i] == letter:
                    win_count += 1
                    exec('d{}.config(text="{}")'.format(i,letter.upper()))
            if win_count == len(word):
                score += 1
                answer = messagebox.askyesno('GAME OVER','YOU WON!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    root.destroy()   
                else:
                    run = False
                    root.destroy()
        else:
            count += 1
            exec('c{}.destroy()'.format(count))
            exec('c{}.place(x={},y={})'.format(count+1,300,-50))
            if count == 6:
                answer = messagebox.askyesno('GAME OVER','YOU LOST!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    score = 0
                    root.destroy()
                else:
                    run = False
                    root.destroy()         
    root.mainloop()
