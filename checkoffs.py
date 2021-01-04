# ***Checkoffs Version 1.1***
#
# UPDATE HISTORY
#
# 1.1
# Fixes
# - Fixed duplication bug
# - Made code more compact
# Known Issues
# - Remove task function not developed
# - Remove task function executed every time showtasks() is used
#
# 1.0
# Known Issues
# - All tasks duplicate when a new one is created (fixed in 1.1)
# - Remove task function not debeloped

#Imports
from guizero import App, Text, PushButton, Box, MenuBar
import time
import sys

#Tasks
t1= "Give feedback to Checkoffs"
t1p= 0
t2= ""
t2p= 0
t3= ""
t3p= 0
t4= ""
t4p= 0
t5= ""
t5p= 0
t6= ""
t6p= 0
t7= ""
t7p= 0
t8= ""
t8p= 0
t9= ""
t9p= 0
t10= ""
t10p= 0

#Other Predifined Variables
bt1 = ""
bt2 = ""
bt3 = ""
bt4 = ""
bt5 = ""
bt6 = ""
bt7 = ""
bt8 = ""
bt9 = ""
bt10 = ""
ct1 = ""
ct2 = ""
ct3 = ""
ct4 = ""
ct5 = ""
ct6 = ""
ct7 = ""
ct8 = ""
ct9 = ""
ct10 = ""
tt1 = ""
tt2 = ""
tt3 = ""
tt4 = ""
tt5 = ""
tt6 = ""
tt7 = ""
tt8 = ""
tt9 = ""
tt10 = ""

#Functions
def export_function():
    global t1
    global t2
    global t3
    global t4
    global t5
    global t6
    global t7
    global t8
    global t9
    global t10
    global t1p
    global t2p
    global t3p
    global t4p
    global t5p
    global t6p
    global t7p
    global t8p
    global t9p
    global t10p
    export=open("checkoffs_exports.txt", "a")
    elines=[t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]
    export.writelines(elines)
    export.close()
    app.info("Suscessful", "Your tasks have suscessfuly been exported into a '.txt' file in this program's directory.")
def todoist_function():
    app.error("Todoist Integration", "Coming soon!")
def quit_function():
    exit()
def add_function():
    addtask()
def sort_function():
    print("sort")
def about_function():
    app.info("About", "Checkoffs is a free and open scource python program. It was buit with the guizero moudle and designed to be lightwieght and optomised for the Raspberry Pi.")
def feedback_function():
    print("feedback")
def addtask():
    global t1
    global t2
    global t3
    global t4
    global t5
    global t6
    global t7
    global t8
    global t9
    global t10
    global t1p
    global t2p
    global t3p
    global t4p
    global t5p
    global t6p
    global t7p
    global t8p
    global t9p
    global t10p
    global bt1
    global bt2
    global bt3
    global bt4
    global bt5
    global bt6
    global bt7
    global bt8
    global bt9
    global bt10
    global ct1
    global ct2
    global ct3
    global ct4
    global ct5
    global ct6
    global ct7
    global ct8
    global ct9
    global ct10
    global tt1
    global tt2
    global tt3
    global tt4
    global tt5
    global tt6
    global tt7
    global tt8
    global tt9
    global tt10
    taskname = app.question("Add Task", "What task would you like to add?")
    tasknumber = app.question("Add Task", "Which task should this be? You can choose tasks 1-10.")
    taskpriority = app.yesno("Add Task", "Would you like this task to be priority?")
    if taskpriority == True:
        if tasknumber == "1":
            t1 = taskname
            t1p = 1
        elif tasknumber == "2":
            t2 = taskname
            t2p = 1
        elif tasknumber == "3":
            t3 = taskname
            t3p = 1
        elif tasknumber == "4":
            t4 = taskname
            t4p = 1
        elif tasknumber == "5":
            t5 = taskname
            t5p = 1
        elif tasknumber == "6":
            t6 = taskname
            t6p = 1
        elif tasknumber == "7":
            t7 = taskname
            t7p = 1
        elif tasknumber == "8":
            t8 = taskname
            t8p = 1
        elif tasknumber == "9":
            t9 = taskname
            t9p = 1
        elif tasknumber == "10":
            t10 = taskname
            t10p = 1
        else:
            app.error("Error", "Invalid Input")
    else:
        if tasknumber == "1":
            t1 = taskname
            t1p = 0
        elif tasknumber == "2":
            t2 = taskname
            t2p = 0
        elif tasknumber == "3":
            t3 = taskname
            t3p = 0
        elif tasknumber == "4":
            t4 = taskname
            t4p = 0
        elif tasknumber == "5":
            t5 = taskname
            t5p = 0
        elif tasknumber == "6":
            t6 = taskname
            t6p = 0
        elif tasknumber == "7":
            t7 = taskname
            t7p = 0
        elif tasknumber == "8":
            t8 = taskname
            t8p = 0
        elif tasknumber == "9":
            t9 = taskname
            t9p = 0
        elif tasknumber == "10":
            t10 = taskname
            t10p = 0
        else:
            app.error("Error", "Invalid Input")
    showtasks()

def remove_function():
    print("Tasks removed")
def removetask1():
    print("Remove Task 1")
def removetask2():
    print("Remove Task")
def removetask3():
    print("Remove Task")
def removetask4():
    print("Remove Task")
def removetask5():
    print("Remove Task")
def removetask6():
    print("Remove Task")
def removetask7():
    print("Remove Task")
def removetask8():
    print("Remove Task")
def removetask9():
    print("Remove Task")
def removetask10():
    print("Remove Task")
def showtasks():
#tfilter = [number of tasks, priority of tasks]
#priority of tasks = pall (all priorities), p1 (priority 1), or p0 (priority 0)
    global app
    global titletext
    global menubar
    global tfilter
    global buttonbox
    global t1
    global t2
    global t3
    global t4
    global t5
    global t6
    global t7
    global t8
    global t9
    global t10
    global t1p
    global t2p
    global t3p
    global t4p
    global t5p
    global t6p
    global t7p
    global t8p
    global t9p
    global t10p
    global bt1
    global bt2
    global bt3
    global bt4
    global bt5
    global bt6
    global bt7
    global bt8
    global bt9
    global bt10
    global ct1
    global ct2
    global ct3
    global ct4
    global ct5
    global ct6
    global ct7
    global ct8
    global ct9
    global ct10
    global tt1
    global tt2
    global tt3
    global tt4
    global tt5
    global tt6
    global tt7
    global tt8
    global tt9
    global tt10
    app.destroy()
    app=App("Checkoffs")
    app.bg = "#85C1E9"
    titletext = Text(app, text="Tasks")
    menubar = MenuBar(app,
                  toplevel=["File", "Edit", "View", "Help"],
                  options=[
                      [ ["Export Tasks", export_function], ["Todoist", todoist_function], ["Quit", quit_function]],
                      [ ["Add Task", add_function], ["Remove Task", remove_function] ],
                      [ ["Sort Taks", sort_function] ],
                      [ ["About", about_function], ["Feedback", feedback_function] ],
                  ])
    buttonbox = Box(app, layout = "grid")
    tfilter = [10, "pall"]
    titletext.text_size = 25
    
    if tfilter == [10, "pall"]:
        bt1 = Box(app, layout = "grid")
        if t1 != "":
            tt1 = Text(bt1, text = t1, grid = [1,0])
            if t1p == 0:
                ct1 = PushButton(bt1, text = "✓", grid = [0,0], command=removetask1())
            else:
                ct1 = PushButton(bt1, text = "P", grid = [0,0], command=removetask1())
        bt2 = Box(app, layout = "grid")
        if t2 != "":
            tt2 = Text(bt2, text = t2, grid = [1,0])
            if t2p == 0:
                ct2 = PushButton(bt2, text = "✓", grid = [0,0], command=removetask2())
            else:
                ct2 = PushButton(bt2, text = "P", grid = [0,0], command=removetask2())
        bt3 = Box(app, layout = "grid")
        if t3 != "":
            tt3 = Text(bt3, text = t3, grid = [1,0])
            if t3p == 0:
                ct3 = PushButton(bt3, text = "✓", grid = [0,0], command=removetask3())
            else:
                ct3 = PushButton(bt3, text = "P", grid = [0,0], command=removetask3())
        bt4 = Box(app, layout = "grid")
        if t4 != "":
            tt4 = Text(bt4, text = t4, grid = [1,0])
            if t4p == 0:
                ct4 = PushButton(bt4, text = "✓", grid = [0,0], command=removetask4())
            else:
                ct4 = PushButton(bt4, text = "P", grid = [0,0], command=removetask4())
        bt5 = Box(app, layout = "grid")
        if t5 != "":
            tt5 = Text(bt5, text = t5, grid = [1,0])
            if t5p == 0:
                ct5 = PushButton(bt5, text = "✓", grid = [0,0], command=removetask5())
            else:
                ct5 = PushButton(bt5, text = "P", grid = [0,0], command=removetask5())
        bt6 = Box(app, layout = "grid")
        if t6 != "":
            tt6 = Text(bt6, text = t6, grid = [1,0])
            if t6p == 0:
                ct6 = PushButton(bt6, text = "✓", grid = [0,0], command=removetask6())
            else:
                ct6 = PushButton(bt6, text = "P", grid = [0,0], command=removetask6())
        bt7 = Box(app, layout = "grid")
        if t7 != "":
            tt7 = Text(bt7, text = t7, grid = [1,0])
            if t7p == 0:
                ct7 = PushButton(bt7, text = "✓", grid = [0,0], command=removetask7())
            else:
                ct7 = PushButton(bt7, text = "P", grid = [0,0], command=removetask7())
        bt8 = Box(app, layout = "grid")
        if t8 != "":
            tt8 = Text(bt8, text = t8, grid = [1,0])
            if t8p == 0:
                ct8 = PushButton(bt8, text = "✓", grid = [0,0], command=removetask8())
            else:
                ct8 = PushButton(bt8, text = "P", grid = [0,0], command=removetask8())
        bt9 = Box(app, layout = "grid")
        if t9 != "":
            tt9 = Text(bt9, text = t9, grid = [1,0])
            if t9p == 0:
                ct9 = PushButton(bt9, text = "✓", grid = [0,0], command=removetask9())
            else:
                ct9 = PushButton(bt9, text = "P", grid = [0,0], command=removetask9())
        bt10 = Box(app, layout = "grid")
        if t10 != "":
            tt10 = Text(bt10, text = t10, grid = [1,0])
            if t10p == 0:
                ct10 = PushButton(bt10, text = "✓", grid = [0,0], command=removetask10())
            else:
                ct10 = PushButton(bt10, text = "P", grid = [0,0], command=removetask10())

#Load App
app= App("Checkoffs")
app.bg = "#85C1E9"
showtasks()
app.display()
