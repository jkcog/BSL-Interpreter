from tkinter import *
import sign as sign
#


def start_cam():
    main_label.config(text="Type Q to quit")
    sign.start_signing()

# GUI

root = Tk()
var = IntVar()
root.title("BSL Interpreter")
root.config(padx=100, pady=100, bg="#364f6b")

start_button = Button(text="Start Interpreter", command=start_cam, relief=FLAT, bg="white", fg="black", highlightthickness=0)
start_button.grid(column=1, row=1)

class NewWindow(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Help")
        self.geometry("700x500")
        start_title = Label(self, text="Getting Started\n", justify=LEFT, font=("Arial", 10, "bold"))
        start_title.grid(column=0, row=0, sticky="W")
        start_content = Label(self, text="Click the 'Start Interpreter' button to begin.\n"
                                         "Type 'Q' to quit.\n\n", justify=LEFT, font=("Arial", 10))
        start_content.grid(column=0, row=1, sticky="W")
        improve_title = Label(self, text="Improving the Interpreter\n", justify=LEFT, font=("Arial", 10, "bold"))
        improve_title.grid(column=0, row=2, sticky="W")
        improve_content = Label(self, text="This model uses Tensorflow's Object Detection API\n"
                                         "It has been trained on BSL signs but it is still very limited.\n"
                                         "To improve the model's accuracy/vocabulary you may want to train it yourself.\n"
                                         "To find out more about how to do this visit:\n"
                                         "https://tensorflow-object-detection-api-tutorial.readthedocs.io/"
                                         "en/latest/training.html\n\n",
                              justify=LEFT, font=("Arial", 10))
        improve_content.grid(column=0, row=3, sticky="W")
        video_call_title = Label(self, text="Video Call Integration\n", justify=LEFT, font=("Arial", 10, "bold"))
        video_call_title.grid(column=0, row=4, sticky="W")
        video_call_content = Label(self, text="To use this interpreter within a video conferencing application such as Zoom, Skype or Google Duo,\n"
                                              "You must first create a virtual webcam.\n"
                                              "One of the easiest ways to do this is with OBS Studio:\n\n"
                                              "With OBS Studio installed and open, start the sign interpreter\n"
                                              "In sources click '+' and select 'Window Capture'\n"
                                              "You should be able to select 'object detection from the list of window options\n"
                                              "Click 'Start Virtual Camera'. The virtual camera should now start.\n"
                                              "You can then choose this virtual camera in your video conferencing application settings.",
                                justify=LEFT, font=("Arial", 10))
        video_call_content.grid(column=0, row=5, sticky="W")


help_button = Button(root, text="Help", relief=FLAT, bg="white", fg="black", highlightthickness=0, width=4)
help_button.bind("<Button>", lambda e: NewWindow(root))
help_button.grid(column=1, row=2, pady=50)

main_label = Label(text="Type 'Q' to quit", bg="#364f6b", fg="#eeeeee")
main_label.grid(column=1, row=3)



root.mainloop()
