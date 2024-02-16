#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Tower of hanoi using tkinter GUI
# ---------------------------------------------------------------------------
# desc:
#   。can set speed
#   。can set discs numbers
#   。step reset, run and resume run
#
##############################################################################

from tkinter import *
from turtle import TurtleScreen, RawTurtle

#==========================================================================================
#  Hanoi disc, a RawTurtle object on a TurtleScreen.
#==========================================================================================
class Disc(RawTurtle):
    def __init__(self, cv):
        RawTurtle.__init__(self, cv, shape="square", visible=False)
        self.pu()
        self.goto(-140,200)

    def config(self, k, n):
        self.hideturtle()
        f = float(k+1)/n
        self.shapesize(0.5, 1.5+5*f) # square-->rectangle
        self.fillcolor(f, 0, 1-f)
        self.showturtle()

#==========================================================================================
#  "Hanoi tower, a subclass of built-in type list"
#==========================================================================================
class Tower(list):
    """create an empty tower. x is x-position of peg"""
    def __init__(self, x):
        self.x = x

    def push(self, d):
        d.setx(self.x)
        d.sety(-70+10*len(self))
        self.append(d)

    def pop(self, y=90):
        d = list.pop(self)
        d.sety(y)
        return d


#==========================================================================================
#   """Play the Hanoi-game on a given TurtleScreen."""
#==========================================================================================
class HanoiEngine:
    def __init__(self, canvas, nrOfDiscs, speed, moveCntDisplay=None):
        """Sets Canvas to play on as well as default values for number of discs and animation-speed.
        moveCntDisplay is a function with 1 parameter, which communicates
        the count of the actual move to the GUI containing the Hanoi-engine-canvas."""
        self.ts = canvas
        self.ts.tracer(False)
        # setup scene
        self.designer = RawTurtle(canvas, shape="square")
        self.designer.penup()
        self.designer.shapesize(0.5, 21)
        self.designer.goto(0,-80); self.designer.stamp()
        self.designer.shapesize(7, 0.5)
        self.designer.fillcolor('darkgreen')
        for x in -140, 0, 140:
            self.designer.goto(x,-5); self.designer.stamp()

        self.nrOfDiscs = nrOfDiscs
        self.speed = speed
        self.moveDisplay = moveCntDisplay
        self.running = False
        self.moveCnt = 0
        self.discs = [Disc(canvas) for i in range(10)]
        self.towerA = Tower(-140)
        self.towerB = Tower(0)
        self.towerC = Tower(140)
        self.ts.tracer(True)

    def setspeed(self):
        for disc in self.discs: disc.speed(self.speed)

    """The classical recursive Towers-Of-Hanoi algorithm,
        implemented as a recursive generator, yielding always None
        plus an 'important' side effect - the next Hanoi move."""
    def hanoi(self, n, src, dest, temp):
        if n > 0:
            for x in self.hanoi(n-1, src, temp, dest): yield None
            yield self.move(src, dest)
            for x in self.hanoi(n-1, temp, dest, src): yield None

    """move uppermost disc of source tower to top of destination tower."""
    def move(self, src_tower, dest_tower):
        dest_tower.push(src_tower.pop())
        self.moveCnt += 1
        self.moveDisplay(self.moveCnt)

    """Setup of (a new) game."""
    def reset(self):
        self.ts.tracer(False)
        self.moveCnt = 0
        self.moveDisplay(0)
        for t in self.towerA, self.towerB, self.towerC:
            while t != []: t.pop(200)
        for k in range(self.nrOfDiscs-1,-1,-1):
            self.discs[k].config(k, self.nrOfDiscs)
            self.towerA.push(self.discs[k])
        self.ts.tracer(True)
        self.HG = self.hanoi(self.nrOfDiscs, self.towerA, self.towerC, self.towerB)

    """run game ;-) return True if game is over, else False"""
    def run(self):
        self.running = True
        try:
            while self.running:
                result = self.step()
            return result      # True iff done
        except StopIteration:  # game over
            return True

    """perform one single step of the game, returns True if finished, else False"""
    def step(self):
        try:
            next(self.HG)
            return 2**self.nrOfDiscs-1 == self.moveCnt
        except TclError: 
            return False

    """ ;-) """
    def stop(self):
        self.running = False


#==========================================================================================
#  """GUI for animated towers-of-Hanoi-game with up to 10 discs:"""
#==========================================================================================
class Hanoi:
    """method to be passed to the Hanoi-engine as a callback to report move-count"""
    def displayMove(self, move):
        self.moveCntLbl.configure(text = "move:\n%d" % move)

    """callback function for nr-of-discs-scale-widget"""
    def adjust_nr_of_discs(self, e):
        self.hEngine.nrOfDiscs = self.discs.get()
        self.reset()

    """callback function for speeds-scale-widget"""
    def adjust_speed(self, e):
        self.hEngine.speed = self.tempo.get() % 10
        self.hEngine.setspeed()

    """most simple implementation of a finite state machine"""
    def setState(self, STATE):
        self.state = STATE
        try:
            if STATE == "START":
                self.discs.configure(state=NORMAL)
                self.discs.configure(fg="black")
                self.discsLbl.configure(fg="black")
                self.resetBtn.configure(state=DISABLED)
                self.startBtn.configure(text="start", state=NORMAL)
                self.stepBtn.configure(state=NORMAL)
            elif STATE == "RUNNING":
                self.discs.configure(state=DISABLED)
                self.discs.configure(fg="gray70")
                self.discsLbl.configure(fg="gray70")
                self.resetBtn.configure(state=DISABLED)
                self.startBtn.configure(text="pause", state=NORMAL)
                self.stepBtn.configure(state=DISABLED)
            elif STATE == "PAUSE":
                self.discs.configure(state=NORMAL)
                self.discs.configure(fg="black")
                self.discsLbl.configure(fg="black")
                self.resetBtn.configure(state=NORMAL)
                self.startBtn.configure(text="resume", state=NORMAL)
                self.stepBtn.configure(state=NORMAL)
            elif STATE == "DONE":
                self.discs.configure(state=NORMAL)
                self.discs.configure(fg="black")
                self.discsLbl.configure(fg="black")
                self.resetBtn.configure(state=NORMAL)
                self.startBtn.configure(text="start", state=DISABLED)
                self.stepBtn.configure(state=DISABLED)
            elif STATE == "TIMEOUT":
                self.discs.configure(state=DISABLED)
                self.discs.configure(fg="gray70")
                self.discsLbl.configure(fg="gray70")
                self.resetBtn.configure(state=DISABLED)
                self.startBtn.configure(state=DISABLED)
                self.stepBtn.configure(state=DISABLED)
        except TclError:
            pass

    """restore state "START" for a new game"""
    def reset(self):
        self.hEngine.reset()
        self.setState("START")

    """callback function for start button, which also serves as pause button. Makes hEngine running until done or interrupted"""
    def start(self):
        if self.state in ["START", "PAUSE"]:
            self.setState("RUNNING")
            if self.hEngine.run():
                self.setState("DONE")
            else:
                self.setState("PAUSE")
        elif self.state == "RUNNING":
            self.setState("TIMEOUT")
            self.hEngine.stop()

    """callback function for step button. makes hEngine perform a single step"""
    def step(self):
        self.setState("TIMEOUT")
        if self.hEngine.step():
            self.setState("DONE")
        else:
            self.setState("PAUSE")

    """ construct Hanoi-engine, build GUI and set STATE to "START" then launch mainloop() """
    def __init__(self, nrOfDiscs, speed):
        root = Tk()
        root.title("Towers Of Hanoi:")
        cv = Canvas(root,width=440,height=210, bg="gray90")
        cv.pack()
        cv = TurtleScreen(cv)
        self.hEngine = HanoiEngine(cv, nrOfDiscs, speed, self.displayMove)
        fnt = ("Arial", 12, "bold")

        # set tower of hanios attributes: 
        attrFrame = Frame(root) # contains scales to adjust game's attributes

        # 1) display number of discs
        self.discsLbl = Label(attrFrame, width=7, height=2, font=fnt, text="discs:\n")
        self.discs = Scale(attrFrame, from_=1, to_=10, orient=HORIZONTAL,font=fnt, length=75, showvalue=1, repeatinterval=10, command=self.adjust_nr_of_discs)
        self.discs.set(nrOfDiscs)

        # 2) display speed
        self.tempoLbl = Label(attrFrame, width=8,  height=2, font=fnt, text = "   speed:\n")
        self.tempo = Scale(attrFrame, from_=1, to_=10, orient=HORIZONTAL, font=fnt, length=100, showvalue=1,repeatinterval=10, command = self.adjust_speed)
        self.tempo.set(speed)

        # 3) display move count
        self.moveCntLbl= Label(attrFrame, width=5, height=2, font=fnt, padx=20, text=" move:\n0", anchor=CENTER)
        for widget in ( self.discsLbl, self.discs, self.tempoLbl, self.tempo, self.moveCntLbl ):
            widget.pack(side=LEFT)
        attrFrame.pack(side=TOP)

        # 4) control buttons: reset, step, start/pause/resume    
        ctrlFrame = Frame(root) # contains Buttons to control the game 
        self.resetBtn = Button(ctrlFrame, width=11, text="reset", font=fnt, state = DISABLED, padx=15, command = self.reset)
        self.stepBtn  = Button(ctrlFrame, width=11, text="step",  font=fnt, state = NORMAL, padx=15, command = self.step)
        self.startBtn = Button(ctrlFrame, width=11, text="start", font=fnt, state = NORMAL,  padx=15, command = self.start)
        for widget in self.resetBtn, self.stepBtn, self.startBtn:
            widget.pack(side=LEFT)
        ctrlFrame.pack(side=TOP)

        # init stat and run mainloop
        self.state = "START"
        root.mainloop()

#==========================================================================================
if __name__  == "__main__":
    # init set 7 discs and speed 3
    Hanoi(7,3)
