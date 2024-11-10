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
        button = Button(self,text='Convert PDF to Audio', foreground='red',
                        command=self.pdf_to_audio
                        ).place(x=40, y=80)

        button = Button(self,text='Convert Audio to PDF', foreground='red', 
                        command=self.audio_to_pdf
                        ).place(x=40, y=150)
    
    # Tao giao dien tuong tu giao dien chinh de chuyen doi tu file pdf sang file audio
    def pdf_to_audio(self):
        pass
        '''
        Giao diện này dùng để nhập vào đường dẫn file pdf và số trang cần đọc
        - label(dòng chữ) 
        - entry (ô nhập liệu để nhập đường dẫn file và số trang)
        - button (nút bấm) - bắt đầu việc chuyển đổi -> command sẽ có 1 hàm xử lý lấy đường dẫn file và số trang để làm -> speak_text (link_file, num_page)
        '''

    def speak_text(self, link_file, num_page):
        pass
        '''
        reader = pyttsx3.init()
        #Chỉnh giọng nói
        voice = reader.getProperty('voices')
        reader.setProperty('voice', voice[2].id)

        #Chỉnh âm lượng
        volum = reader.getProperty('volume')
        reader.setProperty('volume', 0.5)
        
        # Đọc file pdf
        book = open(link_file, 'rb')
        pdfReader = PyPDF2.PdfReader(book) #Đọc file pdf

        for num in range(num_page):
            page =  pdfReader.pages[num]
            text = page.extract_text()
            if text != '':
                reader.say(text)
                reader.runAndWait()
                if reader._inLoop:
                    reader.endLoop()
        '''
    
    # Bai tap them 
    def audio_to_pdf(self):
        pass
    
app = Window()
app.mainloop()
app.update()