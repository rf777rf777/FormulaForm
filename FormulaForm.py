from tkinter import *
from sympy import *

class Window(Frame):
  
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master
        self.grid()
        self.createWidgets()
        #self.click()
        #self.calculate()

    def createWidgets(self):
        self.label1 = Label(self,text = 'y = ax + b')
        self.label1.grid(row=0, column=0,columnspan=1)

        self.label2 = Label(self,text = 'When  x  =  ')
        self.label2.grid(row=1, column=0,columnspan=1)
        self.inputField1 = Entry(self,width = 15)
        self.inputField1.grid(row=1, column=1, columnspan=1)
        self.label3 = Label(self,text = 'y = ')
        self.label3.grid(row=1,column=2,columnspan=1)
        self.inputField2 = Entry(self,width = 15)
        self.inputField2.grid(row=1, column=3, columnspan=1)

        self.label3 = Label(self,text = 'When  x  =  ')
        self.label3.grid(row=2, column=0,columnspan=1)
        self.inputField3 = Entry(self,width = 15)
        self.inputField3.grid(row=2, column=1, columnspan=1)
        self.label4 = Label(self,text = 'y = ')
        self.label4.grid(row=2,column=2,columnspan=1)
        self.inputField4 = Entry(self,width = 15)
        self.inputField4.grid(row=2, column=3, columnspan=1)


        self.label6 = Label(self,text = '')
        self.label6.grid(row=2,column=0,columnspan=1)
        self.start = Button(self,text = '計算',width=10,command=self.click)
        self.start.grid(row=3, column=0,columnspan=1)

        self.label7 = Label(self,text = '')
        self.label7.grid(row=4,column=0,columnspan=1)
        self.label8 = Label(self,text = '計算結果:')
        self.label8.grid(row=5,column=0,columnspan=1)

        self.outputField = Entry(self,width = 45,text='')
        self.outputField.grid(row=5,column=1,columnspan=3)

    def click(self):
        string_formula1 = '({})*a+b-({})'.format(self.inputField1.get(),self.inputField2.get())
        string_formula2 = '({})*a+b-({})'.format(self.inputField3.get(),self.inputField4.get())
        
        #print(string_H)
        #print(self.calculate(string_Q))

        self.outputField.delete(0,END)
        string_Error = "發生錯誤，請檢查輸入式！"
        try:
            self.outputField.insert(0,self.calculate(string_formula1,string_formula2)) 
        except:
            self.outputField.insert(0,string_Error)

        print(self.calculate(string_formula1,string_formula2))

    def calculate(self,formula1,formula2):
        #Symbol('x')
        return solve([formula1,formula2],['a','b'])
        

root = Tk()
root.title('二元一次方程求係數')
root.geometry("420x150")
Window(root)
root.mainloop()