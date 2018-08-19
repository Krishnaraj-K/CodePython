# TRANSLATOR
import bs4
import requests
from tkinter import *


def translator(tran):
    res = requests.get('https://www.collinsdictionary.com/dictionary/english/%s' % tran)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    try:
            meaning = soup.find('div', class_='content-box content-box-definition ced')
            result = meaning.find('div', class_='hom')
            t1.delete(1.0, END)
            t1.insert(END, result.text)
    except AttributeError:
        t1.delete(1.0, END)
        t1.insert(END, 'Try something different.....\nContact:admin@weareawesome.tk')


# translator('CEASE')
##
##GUI
##
##
window = Tk()
window.geometry("500x800")
window.configure(background='khaki3')
window.title("Go Translate")
l1 = Label(text='An Awesome Translator\nBy Krishnaraj', font=('Times', 18), fg='white', bg='purple')
l1.pack(fill=X)
l2 = Label(window, text='Enter word here :', font=('Century gothic', 17), background='khaki2')
l2.pack()
e1 = Entry(window, font=('Lucida calligraphy', 10))
e1.pack()
b1 = Button(window, text="Go", font=('Times', 16), background='khaki4', fg='white',command=lambda: translator(e1.get()))
b1.pack()
t1 = Text(height=90, font=('Comic sans ms', 18), bg='sienna4', fg='white')
t1.pack(fill=X)
window.mainloop()