from sys import exit
from os import path, fork
from random import randint
from time import sleep

from tkinter import *
from PIL import Image, ImageTk


class LeSanaeWindow(Frame):
    """
    Create a window with Le Sanae on a random location on screen.
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.load_lesanae()

    def catch_on_close_event(self):
        pass

    def load_lesanae(self):
        """
        Render window with Le Sanae.
        """
        # Make it more portable by letting the OS utils handle paths
        lesanae = Image.open(path.join(".", "lesanae.png"))
        render = ImageTk.PhotoImage(lesanae)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        # Le Sanae is Le Sanae
        self.master.wm_title("Le Sanae")

        # Place LeSanae in a random location on screen
        # and make window fit Le Sanae's image size
        self.master.geometry(self.random_location(lesanae))

    def render(self):
        self.master.mainloop()

    def random_location(self, lesanae):
        """
        Define a random location on screen for Le Sanae.
        """
        img_w, img_h = lesanae.size
        screen_w = self.master.winfo_screenwidth()
        screen_h = self.master.winfo_screenheight()
        offset_w = randint(0, screen_w - img_w)
        offset_h = randint(0, screen_h - img_h)

        return f"{img_w}x{img_h}+{offset_w}+{offset_h}"


def spawn_lesanae():
    root = Tk()
    app = LeSanaeWindow(root)
    app.render()


def daemon():
    """
    Usually daemons are the granchildren of dead processes.
    The original parent forks and finishes execution.
    The child forks again and finishes execution as well.
    The grandchild(daemon) runs on a infinite loop of some activity.
    """
    pid = fork()
    # Parent
    if pid:
        pass
    # Child
    else:
        while True:
            if fork() == 0:
                spawn_lesanae()
            else:
                fork()
                sleep(1)


def init_daemon():
    pid = fork()
    # Parent
    if pid:
        pass
    # Child
    else:
        daemon()


if __name__ == "__main__":
    init_daemon()
