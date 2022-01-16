import tkinter as tk
from tkinter import *
from tkinter import ttk
import random 
from PIL import ImageTk, Image

import sent
 
LARGEFONT =("Verdana", 35)
buttonPressed=0

  
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        # self.geometry("1000x1000")
        self.configure(bg="#9ab3db")



        # myImg = ImageTk.PhotoImage(Image.open("twtlogo.png"))
        # twtPic = tk.Label(image=myImg,bg="#9ab3db")
        # twtPic.pack()
      
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
        self.wm_title("nwHACKS 2022 Swagalicious")
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
  
class StartPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        def update(data):
          #clear Listbox
          myList.delete(0, END)

          for item in data:
            myList.insert(END, item)

        #update entry box with listbox clicked
        def fillout(e):
          #delete whatever is in entry box
          myEntry.delete(0, END)

          myEntry.insert(0, myList.get(ANCHOR))

        def check(e):
          typed = myEntry.get()
          if typed == '':
            data = suggestedWords
          else:
            data = []
            for item in suggestedWords:
              if typed.lower() in item.lower():
                data.append(item)

          update(data)

        def buttonClick(words):
          # sent.runSentimentAnalysis(words)
          controller.show_frame(Page1)
          keyword = myEntry.get()
          print(keyword)
          buttonPressed=1


        words = []
        wordData=open('test.csv', encoding = "ISO-8859-1")
        for i in wordData:
            words.append(i)



        #create myLabel widget
        myLabel = tk.Label(self, text="Public Opinion Vibe Checker", bg="#9ab3db", font=("comic sans", 25))
        myLabel2 = tk.Label(self, text="What does the court of public opinon (Twitter) think about.... anything?",bg="#9ab3db")




        #Shove onto screen
        myLabel.pack(pady=5)
        myLabel2.pack(pady=5)
        #Create an entry 
        myEntry = tk.Entry(self, font=("Helvetica", 20))
        myEntry.pack()

        #Create a list
        myList = tk.Listbox(self, width=50)
        myList.pack(pady = 30)

        suggestedWords = []
        suggestedFiles = open('suggest.csv', encoding = "ISO-8859-1")
        for i in suggestedFiles:
          

          suggestedWords.append(i.encode('utf-8').strip())
          #i..strip()

        myButton = tk.Button(self, text="Check Twitter!", command=lambda : buttonClick(words))  #command=submit())
        myButton.pack()



        # myImg = ImageTk.PhotoImage(Image.open("twtlogo.png"))
        # twtPic = tk.Label(image=myImg,bg="#9ab3db")
        # twtPic.pack()



        update(suggestedWords)

        #create binding on listbox onclick
        myList.bind("<<ListboxSelect>>", fillout)
        myEntry.bind("<KeyRelease>", check)






          

  
# second window frame page1
class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 1", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
  
  


def update():
    app.after(1000, update)


  
  
# Driver Code
app = tkinterApp()

app.after(1000, update)
app.mainloop()




"""
root = Tk()
root.title("nwHACKS 2022 Swagalicious")
#root.iconbitmap(.ico)
root.geometry("1000x1000")
root.configure(bg="#9ab3db")


results = Tk()
results.title("Analysis Results")
#root.iconbitmap(.ico)
results.geometry("1000x1000")
results.configure(bg="#9ab3db")

def update(data):
  #clear Listbox
  myList.delete(0, END)

  for item in data:
    myList.insert(END, item)

#update entry box with listbox clicked
def fillout(e):
  #delete whatever is in entry box
  myEntry.delete(0, END)

  myEntry.insert(0, myList.get(ANCHOR))

def check(e):
  typed = myEntry.get()
  if typed == '':
    data = suggestedWords
  else:
    data = []
    for item in suggestedWords:
      if typed.lower() in item.lower():
        data.append(item)

  update(data)

def buttonClick(words):
  # sent.runSentimentAnalysis(words)

  keyword = myEntry.get()
  print(keyword);



words = []

wordData=open('test.csv', encoding = "ISO-8859-1")
for i in wordData:
    words.append(i)

# sent.runSentimentAnalysis(words)

#create myLabel widget
myLabel = Label(root, text="Public Opinion Vibe Checker", bg="#9ab3db", font=("comic sans", 25))
myLabel2 = Label(root, text="What does the court of public opinon (Twitter) think about.... anything?",bg="#9ab3db")


#sampleText = tkinter.Text(root, )

#Shove onto screen
myLabel.pack(pady=5)
myLabel2.pack(pady=5)

#myLabel.grid(row=0, column=0)
#myLabel2.grid(row=1, column = 0)



#Create an entry 
myEntry = Entry(root, font=("Helvetica", 20))
myEntry.pack()

#Create a list
myList = Listbox(root, width=50)
myList.pack(pady = 30)

suggestedWords = []
suggestedFiles = open('suggested.csv')
for i in suggestedFiles:
  
  suggestedWords.append(i.strip())



myButton = Button(root, text="Check Twitter!", command=lambda : buttonClick(words))  #command=submit())
myButton.pack()

myImg = ImageTk.PhotoImage(Image.open("twtlogo.png"))
twtPic = Label(image=myImg,bg="#9ab3db")
twtPic.pack()


update(suggestedWords)

#create binding on listbox onclick
myList.bind("<<ListboxSelect>>", fillout)
myEntry.bind("<KeyRelease>", check)

#Event Loop 
root.mainloop()

"""
