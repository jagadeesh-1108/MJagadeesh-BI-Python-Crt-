#Stack project
# #write a py program to stimulate the behaviour of a web page or web browsers back botton 
# when a user visits a new page push it to the stack 
# when the user clicks back pop the top page and go back to the previous page 
class Browser:
    def __init__(self):
        self.history=[]
    def visit(self,page):
        self.history.append(page)
        print(f"visited {page}")
    def Undo(self):
        if len(self.history)>1:
            self.history.pop()
            print(f"back to {self.history[-1]}")
        else:
            print("No pages to comeback")
browser=Browser()
browser.visit('google.com')          
browser.visit('linkdin.com')
browser.visit('github.com')   
browser.Undo()
browser.Undo()
browser.Undo()


 