from tkinter import *
from random import randint  # Import randint from random library
import time

main = Tk()
screen = Canvas(main, width=400, height=500, bg='white')
screen.pack()

screen.create_text(200, 50, text="Ghosted", font=("Arial", 20, "bold"), fill="black")

start_button = Button(screen, text="Sākt spēli", command=lambda: start_game(), width=14, height=1, bg='yellow')
start_button.place(x=200, y=250, anchor="center")

picked_door = 0  # Initialize picked_door variable

 #i am nigga

def start_game():
    global spoka_durvis, door1, door2, door3

    spoka_durvis = randint(1, 3)
    start_button.destroy()  # Remove the start button
    
    door1 = Button(main, command=lambda: pick(1), width=10, height=8, bg='brown')
    door1.place(x=80, y=315, anchor="center")
    door1.config(bd=0)
    door1.bind("<Enter>", lambda event: on_hover(event, door1))
    door1.bind("<Leave>", lambda event: on_leave(event, door1))

    door2 = Button(main, command=lambda: pick(2), width=10, height=8, bg='brown')
    door2.place(x=200, y=315, anchor="center")
    door2.config(bd=0)
    door2.bind("<Enter>", lambda event: on_hover(event, door2))
    door2.bind("<Leave>", lambda event: on_leave(event, door2))

    door3 = Button(main, command=lambda: pick(3), width=10, height=8, bg='brown')
    door3.place(x=320, y=315, anchor="center")
    door3.config(bd=0)
    door3.bind("<Enter>", lambda event: on_hover(event, door3))
    door3.bind("<Leave>", lambda event: on_leave(event, door3))

    screen.create_text(200, 50, text="Ghosted", font=("Arial", 20, "bold"), fill="black")

"""Reset the game by clearing only the relevant canvas elements and setting up the game again."""
def reset_game():
    global spoka_durvis, door1, door2, door3
    
    screen.delete("open-door")
    screen.delete("ghost")
    screen.delete("text")
    # Randomly select a new door for the ghost
    spoka_durvis = randint(1, 3)

    if (picked_door == 1):
        door1 = Button(screen, command=lambda: pick(1), width=10, height=8, bg='brown')
        door1.place(x=80, y=315, anchor="center")
        door1.config(bd=0)
        door1.bind("<Enter>", lambda event: on_hover(event, door1))
        door1.bind("<Leave>", lambda event: on_leave(event, door1))

    if (picked_door == 2):
        door2 = Button(screen, command=lambda: pick(2), width=10, height=8, bg='brown')
        door2.place(x=200, y=315, anchor="center")
        door2.config(bd=0)
        door2.bind("<Enter>", lambda event: on_hover(event, door2))
        door2.bind("<Leave>", lambda event: on_leave(event, door2))

    if (picked_door == 3):
        door3 = Button(screen, command=lambda:pick(3), width=10, height=8, bg='brown')
        door3.place(x=320, y=315, anchor="center")
        door3.config(bd=0)
        door3.bind("<Enter>", lambda event: on_hover(event, door3))
        door3.bind("<Leave>", lambda event: on_leave(event, door3))

    door1.config(state=NORMAL)
    door2.config(state=NORMAL)
    door3.config(state=NORMAL)

def freeze_buttons():
    if (picked_door == 1):
        door2.config(state=DISABLED)
        door3.config(state=DISABLED)
    elif (picked_door == 2):
        door1.config(state=DISABLED)
        door3.config(state=DISABLED)
    elif (picked_door == 3):
        door1.config(state=DISABLED)
        door2.config(state=DISABLED)
    

"""Creates the three doors and assigns actions."""
def door1_safe():
    door1.destroy()
    screen.create_rectangle(45, 252.5, 65, 377.5, fill="brown", tags="open-door")
    screen.create_text(200, 430, text="Spoka nav!", font=("Arial", 10), fill="black", tags='text')
    screen.create_text(200, 450, text="Tev ir _ dzīvības", font=("Arial", 10), fill="black", tags='text')
    
    freeze_buttons()
    main.after(2000, reset_game)

def door2_safe():
    door2.destroy()
    screen.create_rectangle(165, 252.5, 185, 377.5, fill="brown", tags="open-door")
    screen.create_text(200, 430, text="Spoka nav!", font=("Arial", 10), fill="black", tags='text')
    screen.create_text(200, 450, text="Tev ir _ dzīvības", font=("Arial", 10), fill="black", tags='text')
    
    freeze_buttons()
    main.after(2000, reset_game)

def door3_safe():
    door3.destroy()
    screen.create_rectangle(285, 252.5, 305, 377.5, fill="brown", tags="open-door") 
    screen.create_text(200, 430, text="Spoka nav!", font=("Arial", 10), fill="black", tags='text')
    screen.create_text(200, 450, text="Tev ir _ dzīvības", font=("Arial", 10), fill="black", tags='text')
    
    freeze_buttons()
    main.after(2000, reset_game)

def door1_ghost():
    door1.destroy()
    head = screen.create_oval(60, 280, 100, 320, fill="gray87", width=2, outline="gray87", tags="ghost")
    body = screen.create_polygon(100, 300, 60, 300, 50, 350, 110, 350, fill="gray87", width=2, tags="ghost")
    
    # Creating triangles for the ghost's flowing bottom
    triangles = [
        screen.create_polygon(50, 350, 60, 350, 55, 360, fill="gray87", width=2, tags="ghost"),
        screen.create_polygon(60, 350, 70, 350, 65, 360, fill="gray87", width=2, tags="ghost"),
        screen.create_polygon(70, 350, 80, 350, 75, 360, fill="gray87", width=2, tags="ghost"),
        screen.create_polygon(80, 350, 90, 350, 85, 360, fill="gray87", width=2, tags="ghost"),
        screen.create_polygon(90, 350, 100, 350, 95, 360, fill="gray87", width=2, tags="ghost"),
        screen.create_polygon(100, 350, 110, 350, 105, 360, fill="gray87", width=2, tags="ghost")
    ]
    
    # Creating eyes
    eye1 = screen.create_oval(68, 290, 75, 305, fill="black", width=2, tags="ghost")
    eye2 = screen.create_oval(85, 290, 92, 305, fill="black", width=2, tags="ghost")
    
    # Adding text
    screen.create_text(200, 430, text="Spoks!", font=("Arial", 10), fill="black", tags='text')
    screen.create_text(200, 450, text="Tev ir _ dzīvības", font=("Arial", 10), fill="black", tags='text')
    
    freeze_buttons()
    main.after(2000, reset_game)
    
def door2_ghost():
    door2.destroy()
    # Create a ghost at door2
    head = screen.create_oval(180, 280, 220, 320, fill="gray87", width=2, outline="gray87", tags="ghost")
    body = screen.create_polygon(220, 300, 180, 300, 170, 350, 230, 350, fill="gray87", width=2, tags="ghost")
    
    # Creating triangles for the ghost's flowing bottom
    triangles = [
        screen.create_polygon(170, 350, 180, 350, 175, 360, fill="gray87", width=2, tags="ghost"),
        screen.create_polygon(180, 350, 190, 350, 185, 360, fill="gray87", width=2, tags="ghost"),
        screen.create_polygon(190, 350, 200, 350, 195, 360, fill="gray87", width=2, tags="ghost"),
        screen.create_polygon(200, 350, 210, 350, 205, 360, fill="gray87", width=2, tags="ghost"),
        screen.create_polygon(210, 350, 220, 350, 215, 360, fill="gray87", width=2, tags="ghost"),
        screen.create_polygon(220, 350, 230, 350, 225, 360, fill="gray87", width=2, tags="ghost")
    ]
    
    # Creating eyes
    eye1 = screen.create_oval(188, 290, 195, 305, fill="black", width=2, tags="ghost")
    eye2 = screen.create_oval(205, 290, 212, 305, fill="black", width=2, tags="ghost")
    
    # Adding text
    screen.create_text(200, 430, text="Spoks!", font=("Arial", 10), fill="black", tags='text')
    screen.create_text(200, 450, text="Tev ir _ dzīvības", font=("Arial", 10), fill="black", tags='text')
    
    freeze_buttons()
    main.after(2000, reset_game)
    
def door3_ghost():
    door3.destroy()
    # Create a ghost at door3
    head = screen.create_oval(300, 280, 340, 320, fill="gray87", width=2, outline="gray87", tags='ghost')
    body = screen.create_polygon(340, 300, 300, 300, 290, 350, 350, 350, fill="gray87", width=2, tags='ghost')
    
    # Creating triangles for the ghost's flowing bottom
    triangles = [
        screen.create_polygon(290, 350, 300, 350, 295, 360, fill="gray87", width=2, tags="ghost"),
        screen.create_polygon(300, 350, 310, 350, 305, 360, fill="gray87", width=2, tags="ghost"),
        screen.create_polygon(310, 350, 320, 350, 315, 360, fill="gray87", width=2, tags="ghost"),
        screen.create_polygon(320, 350, 330, 350, 325, 360, fill="gray87", width=2, tags="ghost"),
        screen.create_polygon(330, 350, 340, 350, 335, 360, fill="gray87", width=2, tags="ghost"),
        screen.create_polygon(340, 350, 350, 350, 345, 360, fill="gray87", width=2, tags="ghost")
    ]
    
       # Creating eyes
    eye1 = screen.create_oval(308, 290, 315, 305, fill="black", width=2, tags="ghost")
    eye2 = screen.create_oval(325, 290, 332, 305, fill="black", width=2, tags="ghost")
    
    # Adding text
    screen.create_text(200, 430, text="Spoks!", font=("Arial", 10), fill="black", tags='text')
    screen.create_text(200, 450, text="Tev ir _ dzīvības", font=("Arial", 10), fill="black", tags='text')
    
    freeze_buttons()
    main.after(2000, reset_game)



'''
def create_doors():
    global door1, door2, door3
    door1 = Button(main, command=lambda: pick(1), width=10, height=8, bg='brown')
    door1_id = screen.create_window(80, 315, window=door1)
    door1.config(bd=0)
    door1.bind("<Enter>", lambda event: on_hover(event, door1))
    door1.bind("<Leave>", lambda event: on_leave(event, door1))

    door2 = Button(main, command=lambda: pick(2), width=10, height=8, bg='brown')
    door2_id = screen.create_window(200, 315, window=door2)
    door2.config(bd=0)
    door2.bind("<Enter>", lambda event: on_hover(event, door2))
    door2.bind("<Leave>", lambda event: on_leave(event, door2))

    door3 = Button(main, command=lambda: pick(3), width=10, height=8, bg='brown')
    door3_id = screen.create_window(320, 315, window=door3)
    door3.config(bd=0)
    door3.bind("<Enter>", lambda event: on_hover(event, door3))
    door3.bind("<Leave>", lambda event: on_leave(event, door3))

'''

def pick(door_number):
    global picked_door
    picked_door = door_number  # Store the picked door number
    if door_number == spoka_durvis:
        if door_number == 1:
            door1_ghost()
        elif door_number == 2:
            door2_ghost()
        elif door_number == 3:
            door3_ghost()
    else:
        if door_number == 1:
            door1_safe()
        elif door_number == 2:
            door2_safe()
        elif door_number == 3:
            door3_safe()

# Hover Effects for Buttons
def on_hover(event, btn):
    """Makes button border visible on hover"""
    btn.config(bd=2)

def on_leave(event, btn):
    """Removes button border when not hovered"""
    btn.config(bd=0)

main.mainloop()