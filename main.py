from tkinter import *

import sent

root = Tk()
root.title("nwHACKS 2022 Swagalicious")
#root.iconbitmap(.ico)
root.geometry("500x500")

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
myLabel = Label(root, text="Public Opinion Vibe Checker", font=("Helvetica", 25))
myLabel2 = Label(root, text="What does the court of public opinon (Twitter) think about.... anything?")

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





update(suggestedWords)

#create binding on listbox onclick
myList.bind("<<ListboxSelect>>", fillout)
myEntry.bind("<KeyRelease>", check)

#Event Loop 
root.mainloop()
