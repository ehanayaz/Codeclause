import tkinter as tk
from tkinter import filedialog
from pygame import mixer
from PIL import Image, ImageTk


def set_volume(volume):
    mixer.music.set_volume(float(volume) / 100)


def mixer_init():
    mixer.init()


class MusicPlayer:
    def __init__(self, root):
        self.seekbar = None
        self.volume_slider = None
        self.pause_icon = None
        self.play_button = None
        self.play_icon = None
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x200")

        self.current_file = None
        self.file_length = 0
        self.paused = False
        self.loaded = False
        self.update = False

        mixer_init()
        self.create_widgets()

    def create_widgets(self):
        # Load play and pause images
        play_image = Image.open("images/play.png")
        play_image = play_image.resize((50, 50))
        self.play_icon = ImageTk.PhotoImage(play_image)

        pause_image = Image.open("images/pause.png")
        pause_image = pause_image.resize((50, 50))
        self.pause_icon = ImageTk.PhotoImage(pause_image)

        # Create play button
        self.play_button = tk.Button(self.root, image=self.play_icon, command=self.toggle_play)
        self.play_button.grid(row=0, column=1, padx=10, pady=10)

        # Create open button
        open_button = tk.Button(self.root, text="Open", command=self.open_file)
        open_button.grid(row=0, column=2, padx=10, pady=10)

        # Create volume slider
        self.volume_slider = tk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL, label="Volume"
                                      , command=set_volume)
        self.volume_slider.set(50)  # Set initial volume to 50
        self.volume_slider.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Create seekbar/slider
        self.seekbar = tk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL, label="Playback")

        self.seekbar.grid(row=1, column=3, columnspan=2, padx=10, pady=10)
        self.seekbar.bind("<ButtonRelease-1>", self.set_seek)

    def toggle_play(self):
        if self.current_file:
            if self.loaded:
                if self.paused:
                    mixer.music.unpause()
                    self.paused = False
                else:
                    mixer.music.pause()
                    self.paused = True
                self.update_play_button_icon()
                self.update_seekbar()
            else:
                mixer.music.load(self.current_file)
                mixer.music.play()

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            self.current_file = file_path
            mixer.music.load(self.current_file)
            sound = mixer.Sound(self.current_file)
            length = sound.get_length()
            self.file_length = length
            mixer.music.play()
            self.update_play_button_icon()
            self.update_seekbar()
            self.loaded = True

    def update_play_button_icon(self):
        if self.paused:
            self.play_button.config(image=self.play_icon)
        else:
            self.play_button.config(image=self.pause_icon)

    def set_seek(self, event):
        position = float(self.seekbar.get()) / 100 * self.file_length
        mixer.music.set_pos(position)

    def update_seekbar(self):
        if not self.paused:
            self.seekbar.set(((mixer.music.get_pos() / 1000) / self.file_length) * 100)
            self.seekbar.after(1000, self.update_seekbar)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    music_player.run()
