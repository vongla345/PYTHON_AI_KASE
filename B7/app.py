from tkinter import *
from tkinter import messagebox as mb
import PyPDF2
import pyttsx3

class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.title('Voice PDF Reader')
        self.geometry('400x250')
        
        # show a label
        label = Label(self, text='Voice PDF Reader Application', font = ('Arial', 20), foreground='white').place(x=0, y = 0)
        #label.pack(ipadx=10, ipady=10)

        # show a button
        button = Button(self,text='Convert PDF to Audio', foreground='red',command=self.pdf_to_audio).place(x=40, y=80)

        button = Button(self,text='Convert Audio to PDF', foreground='red', command=self.audio_to_pdf).place(x=40, y=150)
    def pdf_to_audio(self):
        pta = Toplevel(self)
        pta.title('PDF to Audio')
        pta.geometry('400x250')
        
        Label(pta, text = 'PDF to Audio').place(x=3, y = 0)
        Label(pta, text = 'Enter the PDF file path:').place(x=10, y=60)
        
        filename = Entry(pta)
        filename.place(x=10, y=80)
        
        Label(pta,text = 'Enter the page to read from pdf').place(x = 10, y = 120)
        page = Entry(pta)
        page.place(x=10, y=140)
        
        Button(pta, text='Speak the text',command = lambda:self.speak_text(filename.get(), page.get())).place(x=10, y=180)
    def speak_text(self, filename, page):
        if not filename or not page:
            mb.showerror('Error', 'Please enter the filename and page number')
            return
        mb.showinfo('Info', 'Please wait for a moment')
        book = open(filename, 'rb')
        pdfReader = PyPDF2.PdfReader(book)
        #Khai báo reader
        reader = pyttsx3.init()
        #Chỉnh giọng nói
        voice = reader.getProperty('voices')
        reader.setProperty('voice', voice[2].id)

        #Chỉnh âm lượng
        volum = reader.getProperty('volume')
        
        with open(filename, 'rb') as book:
            pdfReader = PyPDF2.PdfReader(book)
            pageObj = pdfReader.pages[int(page)]
            text = pageObj.extract_text()
            reader.say(text)
            reader.runAndWait()
    def audio_to_pdf(self):
        pass
    
    
app = Window()
app.update()
app.mainloop()