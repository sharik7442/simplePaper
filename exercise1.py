from  tkinter import  *
from  PIL import  Image,ImageTk
import imutils


root=Tk()

root.title("Latest News - Aaj ki Taza Khabar")
root.geometry("1200x800")

photos=[]
texts = []
for i in range(0,3):
    with open(f"{i+1}.txt") as f:
        text=f.read()
        texts.append(text)

    image=Image.open(f"{i+1}.jpg")



    photos.append(ImageTk.PhotoImage(image))


f0=Frame(root, width=800,height=70)
Label(f0,text="Todays Latest News", font="lucida 33 bold").pack()
f0.pack()
Label(f0,text="1st May 2021", font="lucida 18 bold").pack()
f0.pack()


f1=Frame(root,width=1000, height=200)
Label(f1,text=texts[0], padx=22,pady=22).pack(side=LEFT)
Label(f1,image=photos[0],anchor="e" ).pack()
f1.pack(anchor="w")


f2=Frame(root,width=1000, height=200)
Label(f2,text=texts[1], padx=22,pady=22).pack(side=RIGHT)
Label(f2,image=photos[1],anchor="w" ).pack()
f2.pack(anchor="w")

f3=Frame(root,width=1000, height=200)
Label(f3,text=texts[2], padx=22,pady=22).pack(side=LEFT)
Label(f3,image=photos[2],anchor="e" ).pack()
f3.pack(anchor="w")

root.mainloop()