from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import Tk, Canvas, Frame, BOTH, NW
import json

from threading import Thread
import threading

import cv2
from utils.pokemon_detector import PokemonDetector


class MainWindow:

    def browseFiles(self):
        file_name = filedialog.askopenfilename(initialdir="./",
                                               title="Select a File",
                                               filetypes=(("Video File",
                                                           "*.mp4*"),
                                                          ("Image Files",
                                                           "*.png*"),
                                                          ("All Files", "*.*")))
        self.path_text.delete("1.0", END)
        self.path_text.insert("1.0", file_name)

    def deal_with_video(self):
        video_path = self.path_text.get("1.0", END).replace("\n", "")
        if not video_path == "":
            print(video_path)
            cap = cv2.VideoCapture(video_path)
        else:
            cap = cv2.VideoCapture(0)

        pokemon_detector = PokemonDetector()
        while (True):
            
            if threading.activeCount() > 2:
                break

            ret, frame = cap.read()
            if ret:
                frame = cv2.resize(frame, (600, 400))
                pokemon_detector.detect_pokemons(frame)
                im = Image.fromarray(frame)
                b, g, r = im.split()
                im = Image.merge("RGB", (r, g, b))
                video_image = ImageTk.PhotoImage(image=im)
                self.video_image_label.configure(image=video_image)
                self.video_image_label.image = video_image
                self.video_image_label.place_configure(relx=0.35, rely=0.1)
            if not ret:
                break

    def start(self):
        global start_locked
        self.thread = Thread(
            target=MainWindow.deal_with_video, kwargs={"self": self})
        self.thread.start()
        start_locked = True

    def __init__(self, win):
        font_style = Font(root=win.master, size=12,
                          weight="bold", family="Arial")

        pokeball_image = Image.open("assets/dd-red.png")
        pokeball_image = pokeball_image.resize((960, 540), Image.ANTIALIAS)
        pokeball_image_tk = ImageTk.PhotoImage(pokeball_image)
        self.video_image_label = Label(win, image=pokeball_image_tk)
        self.video_image_label.image = pokeball_image_tk
        self.video_image_label.place_configure(relx=0.0, rely=0.0)

        pokedex_logo = Image.open("assets/pokedex.png")
        pokedex_logo = pokedex_logo.resize((400, 72), Image.ANTIALIAS)
        pokedex_logo_tk = ImageTk.PhotoImage(pokedex_logo)
        self.pokedex_logo_label = Label(win, image=pokedex_logo_tk)
        self.pokedex_logo_label.image = pokedex_logo_tk
        self.pokedex_logo_label.pack(side="right", anchor="se")

        self.button_explore = Button(win,
                                     text="...",
                                     command=self.browseFiles)
        self.button_explore.place(
            relx=.29, rely=.198, width=25, height=25, bordermode="inside")

        start_pokedex = Image.open("assets/pokemon-icons-png-15.png")
        start_pokedex = start_pokedex.resize((35, 35), Image.ANTIALIAS)
        start_pokedex_tk = ImageTk.PhotoImage(start_pokedex)
        self.button_start = Button(win,
                                   text="Choose your file!", image=start_pokedex_tk,
                                   command=self.start)
        self.button_start.image = start_pokedex_tk
        self.button_start.place(relx=.135, rely=.25, bordermode="inside")

        self.path_text = Text(win, font="Times32", width=25, height=1.4)
        # self.path_text.insert(END,"path to input file")
        self.path_text.place(relx=.15, rely=.22, anchor="center")

        pokeball_image = Image.open("assets/pokeball.png")
        pokeball_image = pokeball_image.resize((400, 400), Image.ANTIALIAS)
        pokeball_image_tk = ImageTk.PhotoImage(pokeball_image)
        self.video_image_label = Label(win, image=pokeball_image_tk)
        self.video_image_label.image = pokeball_image_tk
        self.video_image_label.place_configure(relx=0.45, rely=0.1)