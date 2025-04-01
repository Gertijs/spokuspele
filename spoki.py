from tkinter import *
from random import randint  # Import randint from random library
import time

main = Tk()
screen = Canvas(main, width=400, height=500, bg='white')
screen.pack()

screen.create_text(200, 50, text="Ghosted", font=("Arial", 20, "bold"), fill="black")

start_button = Button(main, text="Sākt spēli", command=lambda: reset_game(), width=14, height=1, bg='yellow')
screen.create_window(200, 250, window=start_button)


# Global variable to track the chosen door and the ghost door
choice = 0
spoka_durvis = randint(1, 3)  # Randomly select which door has the ghost (1 for door1, 2 for door2, 3 for door3)

def reset_game():
    """Reset the game by clearing only the relevant canvas elements and setting up the game again."""
    global choice, spoka_durvis
    screen.delete("ghost")  # Clear only the ghost and any previous text

    # Recreate the title (it stays visible)
    screen.create_text(200, 50, text="Ghosted", font=("Arial", 20, "bold"), fill="black")

    # Randomly select a new door for the ghost
    spoka_durvis = randint(1, 3)

    # Recreate the doors
    create_doors()


def create_doors():
    """Creates the three doors and assigns actions."""
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

def pick(door_number):
    global choice
    choice = door_number
    if choice == spoka_durvis:
        if choice == 1:
            door1_ghost()
        elif choice == 2:
            door2_ghost()
        elif choice == 3:
            door3_ghost()
    else:
        if choice == 1:
            door1_safe()
        elif choice == 2:
            door2_safe()
        elif choice == 3:
            door3_safe()

def door1_safe():
    screen.create_rectangle(45, 252.5, 65, 377.5, fill="brown")
    screen.create_text(200, 430, text="Spoka nav!", font=("Arial", 10), fill="black")
    screen.create_text(200, 450, text="Tev ir _ dzīvības", font=("Arial", 10), fill="black")
    time.sleep(2)
    reset_game

def door2_safe():
    screen.create_rectangle(165, 252.5, 185, 377.5, fill="brown")
    screen.create_text(200, 430, text="Spoka nav!", font=("Arial", 10), fill="black")
    screen.create_text(200, 450, text="Tev ir _ dzīvības", font=("Arial", 10), fill="black")
    time.sleep(2)
    reset_game

def door3_safe():
    screen.create_rectangle(285, 252.5, 305, 377.5, fill="brown")  # Simulating an open door
    screen.create_text(200, 430, text="Spoka nav!", font=("Arial", 10), fill="black")
    screen.create_text(200, 450, text="Tev ir _ dzīvības", font=("Arial", 10), fill="black")
    time.sleep(2)
    reset_game

def door1_ghost():
    # Create a ghost at door1
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
    screen.create_text(200, 430, text="Spoks!", font=("Arial", 10), fill="black", tags="ghost")
    screen.create_text(200, 450, text="Tev ir _ dzīvības", font=("Arial", 10), fill="black", tags="ghost")
    time.sleep(2)
    reset_game
    
def door2_ghost():
    # Create a ghost at door2
    head = screen.create_oval(160, 280, 200, 320, fill="gray87", width=2, outline="gray87", tags="ghost")
    body = screen.create_polygon(200, 300, 160, 300, 150, 350, 210, 350, fill="gray87", width=2, tags="ghost")
    
    # Creating triangles for the ghost's flowing bottom
    triangles = [
        screen.create_polygon(150, 350, 160, 350, 155, 360, fill="gray87", width=2, tags="ghost"),
        screen.create_polygon(160, 350, 170, 350, 165, 360, fill="gray87", width=2, tags="ghost"),
        screen.create_polygon(170, 350, 180, 350, 175, 360, fill="gray87", width=2, tags="ghost"),
        screen.create_polygon(180, 350, 190, 350, 185, 360, fill="gray87", width=2, tags="ghost"),
        screen.create_polygon(190, 350, 200, 350, 195, 360, fill="gray87", width=2, tags="ghost"),
        screen.create_polygon(200, 350, 210, 350, 205, 360, fill="gray87", width=2, tags="ghost")
    ]
    
    # Creating eyes
    eye1 = screen.create_oval(168, 290, 175, 305, fill="black", width=2, tags="ghost")
    eye2 = screen.create_oval(185, 290, 192, 305, fill="black", width=2, tags="ghost")
    
    # Adding text
    screen.create_text(200, 430, text="Spoks!", font=("Arial", 10), fill="black", tags="ghost")
    screen.create_text(200, 450, text="Tev ir _ dzīvības", font=("Arial", 10), fill="black", tags="ghost")
    time.sleep(2)
    reset_game
    

def door3_ghost():
    # Create a ghost at door3
    head = screen.create_oval(260, 280, 300, 320, fill="gray87", width=2, outline="gray87", tags="ghost")
    body = screen.create_polygon(300, 300, 260, 300, 250, 350, 310, 350, fill="gray87", width=2, tags="ghost")
    
    # Creating triangles for the ghost's flowing bottom
    triangles = [
        screen.create_polygon(250, 350, 260, 350, 255, 360, fill="gray87", width=2, tags="ghost"),
        screen.create_polygon(260, 350, 270, 350, 265, 360, fill="gray87", width=2, tags="ghost"),
        screen.create_polygon(270, 350, 280, 350, 275, 360, fill="gray87", width=2, tags="ghost"),
        screen.create_polygon(280, 350, 290, 350, 285, 360, fill="gray87", width=2, tags="ghost"),
        screen.create_polygon(290, 350, 300, 350, 295, 360, fill="gray87", width=2, tags="ghost"),
        screen.create_polygon(300, 350, 310, 350, 305, 360, fill="gray87", width=2, tags="ghost")
    ]
    
    # Creating eyes
    eye1 = screen.create_oval(268, 290, 275, 305, fill="black", width=2, tags="ghost")
    eye2 = screen.create_oval(285, 290, 292, 305, fill="black", width=2, tags="ghost")
    
    # Adding text
    screen.create_text(200, 430, text="Spoks!", font=("Arial", 10), fill="black", tags="ghost")
    screen.create_text(200, 450, text="Tev ir _ dzīvības", font=("Arial", 10), fill="black", tags="ghost")
    time.sleep(2)
    command=reset_game
    

# Hover Effects for Buttons
def on_hover(event, btn):
    """Makes button border visible on hover"""
    btn.config(bd=2)

def on_leave(event, btn):
    """Removes button border when not hovered"""
    btn.config(bd=0)

    


main.mainloop()