from tkinter import *
import random
from PIL import ImageTk, Image



names_list =[]
global questions_answers
asked = []
score = 0


questions_answers = {
  
  1: [ "What is a correct syntax to output Hello World in Python?", # item 1 index 0 will be the question
  'echo "Hello World"', # item 2 index 1 will be the first choice
  'echo (Hello World)' , # item 3 index 2 will be the second choice
  'print("Hello World")', # item 4 index 3 will be the third choice
  'print(hello World)', # item 5 index 4 will be the fourth choice
  'print("Hello World")' # item 6 index 5 will be the write statement  we need to display the right statement if the user enters wrong choice
  ,3], # item 7 index 6 will be the position of the right answer (index were right answer sits), this will be our check if answer is correct or not
  2: [ "What is Tkinter?" , 'module','*program', 'List', 1],
  3: [ "How do you create a variable with the numeric value 5?" , 'x = 5', 'Both the 1 and 3 are correct', 'x = int(5)', 'x = def(5)', 'Both the 1 and 3 are correct', 2],
  4: ["What is the correct file extension for Python files?", '.pyth', '.py', '.ph', '.pyt', '.py', 2],
  5: ["How do you create a variable with the floating number 2.8?", 'x = float(2.8)', 'x = 2.8', 'Both 1 and 2 are correct', 'x = def(2.8)', 'Both 1 and 2 are correct', 3],
  6: ["What is the correct way to create a function in Python?", 'function myfunction():', 'create myFunction():', 'def myFunction():', 'make myfunction():', 'def myFunction():', 3],
  7: ["Which method can be used to remove any whitespace from both the beginning and the end of a string?", 'trim()', 'ptrim()', 'len()', 'strip()', 'strip()', 4],
  8: ["Which method can be used to return a string in upper case letters?", 'upper()', 'toUpperCase()', 'uppercase()', 'Caseupper()', 'upper()', 1],
  9: ["Which method can be used to replace parts of a string?", 'replaceString()', 'switch()', 'replace()', 'repl()', 'replace()', 3],
  10: ["Which collection is ordered, changeable, and allows duplicate members?", 'LIST', 'DICTIONARY', 'TUPLE' , 'SET', 'LIST', 1]
}


#adding a randomsier so users can get question randomly
def randomiser():
  global qnum
  qnum = random.randint(1,10)
  if qnum not in asked:
    asked.append(qnum)
  elif qnum in asked:
    randomiser()


class Quiz:
  
  def __init__(self, parent):
    
    background_color = "Light Grey" #background color of python code quiz.
    
    #frame setup for quiz
    self.quiz_frame = Frame(parent, bg = background_color, padx = 70, pady = 70)
    self.quiz_frame.grid()

    #label widget for quiz heading
    self.heading_label = Label(self.quiz_frame, text = "Python Quiz", font = ("Anton", "16", "bold"), bg = background_color)
    self.heading_label.grid(row = 0, padx = 20,)

    #Username Label for quiz
    self.user_label = Label(self.quiz_frame, text = "Please enter your name! ", font = ("Noto Sans JP", "16"),bg = background_color)
    self.user_label.grid(row = 1, padx = 20, pady = 20)

    # Creating entry box for the quiz
    self.entry_box = Entry(self.quiz_frame)
    self.entry_box.grid(row = 2, padx = 20, pady = 20)

    #start button for quiz
    self.continue_button = Button(self.quiz_frame, text = "Start", font = ("Anton", "16"), bg = "Lightblue", command = self.name_collection)
    self.continue_button.grid(row = 3, padx = 20, pady=20)

    self.picture_image = Image.open('python.png')
    self.picture_image = self.picture_image.resize((200,150), Image.ANTIALIAS)
    self.picture_image = ImageTk.PhotoImage(self.picture_image)
    self.image_label = Label(self.quiz_frame,
                                image=self.picture_image)
    self.image_label.grid(row=4, pady=5, padx=5)


  #creating a name collection method so it can store username data
  def name_collection(self):
    name = self.entry_box.get()
    names_list.append(name) #add name to names list declared at the beginning
    print(names_list)#print names list
    self.quiz_frame.destroy()#destory class quiz so question class can run
    Question(root) # start class Quiz


#creating a question class
class Question:
  def __init__(self, parent):
    
    background_color = "lightgrey" #background color of python code quiz.
    
    #frame setup for quiz
    self.quiz_frame = Frame(parent, bg = background_color, padx = 100, pady = 100)
    self.quiz_frame.grid()

    #label widget for random question
    self.question_label = Label(self.quiz_frame, text = questions_answers[qnum][0], font = ("Anton", "10", "bold"), bg = background_color)
    self.question_label.grid(row = 0, padx = 20,)

    self.var1 = IntVar()# slef.var1 holds value of radio button

    #rb1 is the answer choice buttom 1
    self.rb1 = Radiobutton(self.quiz_frame, text = questions_answers[qnum][1], font = ("Anton", "10"), bg = background_color, value = 1, padx = 10, pady = 10, variable = self.var1, background = background_color)
    self.rb1.grid(row = 1, sticky = W)

    #rb2 is the answer choice buttom 2
    self.rb2 = Radiobutton(self.quiz_frame, text = questions_answers[qnum][2], font = ("Anton", "10"), bg = background_color, value = 2, padx = 10, pady = 10, variable = self.var1, background = background_color)
    self.rb2.grid(row = 2, sticky = W)

    #rb3 is the answer choice buttom 3
    self.rb3 = Radiobutton(self.quiz_frame, text = questions_answers[qnum][3], font = ("Anton", "10"), bg = background_color, value = 3, padx = 10, pady = 10, variable = self.var1, background = background_color)
    self.rb3.grid(row = 3, sticky = W)


    #rb4 is the answer choice buttom 4
    self.rb4 = Radiobutton(self.quiz_frame, text = questions_answers[qnum][4], font = ("Anton", "10"), bg = background_color, value = 4, padx = 10, pady = 10, variable = self.var1, background = background_color)
    self.rb4.grid(row = 4, sticky = W)

    #aconfirm button when user choose his/her answer
    self.confirm_button = Button(self.quiz_frame, text = "Submit", bg= "Lightblue", command = self.test_progress)
    self.confirm_button.grid(row = 5)




  #creating a question set up so users can get different question  
  def questions_setup(self):
    randomiser()
    self.var1.set(0)
    self.question_label.config(text = questions_answers[qnum][0])
    self.rb1.config(text = questions_answers[qnum][1])
    self.rb2.config(text = questions_answers[qnum][2])
    self.rb3.config(text = questions_answers[qnum][3])
    self.rb4.config(text = questions_answers[qnum][4])

  # steup test progress so user can get his score
  def test_progress(self):
    global score
    choice = self.var1.get()
    if len(asked)>9:
      if choice == questions_answers[qnum][6]:
        score += 1 #user can get 1 point if their answer is correct
        scr_label.configure(text = score)
        self.confirm_button.submit(text = "Submit")
        
      else:
        score += 0 #users get 0 point if answer is wrong
        scr_label.configure(text = "The correct answer is " +  questions_answers[qnum][5]) # tells the correct answer to the user
        self.confirm_button.submit(text = "Confirm")
        
    else:
      if choice == 0: #users get 0 point if user can't select answer
        self.confirm_button.submit(text = "Try Again") #tells user to try again
        choice = self.var1.get()
        
      else:
        if choice == questions_answers[qnum][6]:
          self.confirm_button.submit(text = "Confirm")
          self.questions_setup()
        
        else:
          self.confirm_button.submit(text = "Confirm")
          self.questions_setup()



randomiser()
#starting point of Python Quiz
if __name__ == "__main__":
  root = Tk()
  root.title("Python quiz")
  quiz_object = Quiz(root)
  root.mainloop()
