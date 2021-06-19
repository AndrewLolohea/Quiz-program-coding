from tkinter import *
from tkinter import messagebox
import random

# Variables
background_color = "Lightgreen"
foreground_color = "Black"
btn_color = "mediumseagreen"
names_list = [] 
asked = []

question_num = 1

mechanics_score = 0 
nuclear_physics_score = 0
waves_score = 0

python_score = 0
heuristics_score = 0
algorithims_score = 0 

#physics_categories = [mechanics_score,nuclear_physics_score,waves_score]
#cs_categories = [python_score,heuristics_score,algorithims_score]



def randomiser(): 
  global qnum 

  qnum = random.randint(1,15)

  if qnum not in asked: 
    asked.append(qnum)
  elif qnum in asked: 
    randomiser()

randomiser()

# Questions and Answers 
# Physics
# Question number: Question, Answer 1, Answer 2, Answer 3, Answer 4, Correct Answer placement, Category 
phy_qanda = {
  1: [
        "What is Tkinter?",
        "Module", "Graphical user interface",
        "Program", "String",2
    ],
    2: [
        "What is the 'Monitor'?", "Display that shows program",
        "", "300 episodes",
        "600 episodes", "500 episodes", 1
    ],
    3: [
        "What power does thi person have",
        "Fire powers",
        "Water powers",
        "No powers",
        "Physic powers",
        "No powers", 3
    ],
    4: [
        "What anime is this",
        "HunterXHunter", "One piece",
        "Walking dead", "4 lives",
        "One piece", 2
    ],
    5: [
        "When did one piece come out",
        "13/07/1999", "06/10/1999",
        "20/10/1999",
        "19/12/1999",
        "20/10/1999", 3
    ],
    6: [
        "Is this person a girl or boy",
        "a girl", "A boy",
        "A Slime", "a child",
        "A slime", 2
    ],
    7: [
        "What does DBZ MEAN",
        "Double ball z", "Done back z", "Don't bully zack",
        "Dragon ball z", "Dragon ball z", 4
    ],
    8: [
        "Who killed the most?",
        "Truck-kun", "Naruto", "Goku", "Luffy", "Truck-kun", 1
    ],
    9: [
        "What is the strongest jutsu?",
        "Shadow clone jutsu",
        "Resangun",
        "Talk no jutsu",
        "Chidori",
        "Talk no jutsu", 3
    ],
    10: [
        "When hit by truck-kun what happends?",
        "A Isekai", "Go to heaven",
        "Got to hell",
        "Survive", 1
    ],
}

cs_qanda = {
  1: [
        "Which one is a anime",
        "Dragon Bleack", "Goku namikaze",
        "The time i got reincaarnated as a slime", "Dark knight", "Sleeping beuty", 3
    ],
    2: [
        "How many seasons are in one piece", "900+ episodes",
        "800 episodes", "300 episodes",
        "600 episodes", "500 episodes", 1
    ],
    3: [
        "What power does thi person have",
        "Fire powers",
        "Water powers",
        "No powers",
        "Physic powers",
        "No powers", 3
    ],
    4: [
        "What anime is this",
        "HunterXHunter", "One piece",
        "Walking dead", "4 lives",
        "One piece", 2
    ],
    5: [
        "When did one piece come out",
        "13/07/1999", "06/10/1999",
        "20/10/1999",
        "19/12/1999",
        "20/10/1999", 3
    ],
    6: [
        "Is this person a girl or boy",
        "a girl", "A boy",
        "A Slime", "a child",
        "A slime", 2
    ],
    7: [
        "What does DBZ MEAN",
        "Double ball z", "Done back z", "Don't bully zack",
        "Dragon ball z", "Dragon ball z", 4
    ],
    8: [
        "Who killed the most?",
        "Truck-kun", "Naruto", "Goku", "Luffy", "Truck-kun", 1
    ],
    9: [
        "What is the strongest jutsu?",
        "Shadow clone jutsu",
        "Resangun",
        "Talk no jutsu",
        "Chidori",
        "Talk no jutsu", 3
    ],
    10: [
        "When hit by truck-kun what happends?",
        "A Isekai", "Go to heaven",
        "Got to hell",
        "Survive", 1
    ],
}


class QuizStarter: # Class for the UI, the main menu and username 
    def __init__(self, parent):    
        # Frame of the UI
        self.quiz_frame = Frame(parent, bg=background_color, padx=100, pady=100)
        # Geometry and placement of the UI
        self.quiz_frame.grid()

        #Widgets
        # Main header
        self.heading_label = Label(self.quiz_frame, text="Python Quiz",font=("Tw Cen MT","15","bold"),bg=background_color,fg=foreground_color)
        self.heading_label.grid(row=0, padx=10)

        # Username Label
        self.user_label = Label(self.quiz_frame, text="Please Enter Your name below:", font=("Tw Cen MT","14"),bg=background_color, fg=foreground_color)
        self.user_label.grid(row=1,pady=20,padx=100)
        
        #entry box
        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2,padx=100, pady=20)
        self.entry_box.configure(width=30)
      
        #continue button
        self.continue_button = Button(self.quiz_frame, text="Start", font=("Tw Cen MT", "13", "bold"), bg="lightblue", command=self.continue_process)
        self.continue_button.grid(row=3,  padx=50, pady=30, sticky=E)  
        self.continue_button.config(width = 5) # button same size as the exit button

        #Exit button 
        self.exit_button = Button(self.quiz_frame, text="Exit", font=("Tw Cen MT", "13", "bold"), bg="lightblue", command=self.end_screen)
        self.exit_button.grid(row=3, padx=30 ,pady=30, sticky=W)
        self.exit_button.config(width = 5) # make the button the same size as the continue button

        #Error correction
        self.error_label = Label(self.quiz_frame, text="", font=("Tw Cen MT", "10", "bold"), bg=background_color, fg="indianred")
        self.error_label.grid(row=4,padx=20,pady=10)

   # Method for clicking the continue butoon 
    def continue_process(self): 
      name = self.entry_box.get()
      if str.isalpha(name) == True and int(len(name)) <= 15: 
          names_list.append(name)
          self.quiz_frame.destroy()
          Selection(root)
          print(names_list)
      else:
         self.error_label.configure(text = "")
         self.error_label.configure(text = "You left the feild above Empty!")
    # Code for closing the program 
    def end_screen(self): 
      root.withdraw()
    
class Selection: # Class for the quiz selection interface
  def __init__(self, parent): 
     self.quiz_frame = Frame(parent, bg=background_color, padx=100, pady=100)
     # Geometry and placement of the UI
     self.quiz_frame.grid()
     # Heading for the Quiz Selection
     self.heading_label = Label(self.quiz_frame, text="Lets Begin", font=("Tw Cen MT", "12", "bold"), bg=background_color, fg=foreground_color)
     self.heading_label.grid(row=0, column = 0, columnspan = 2, pady=20, padx=50)

     self.var1 = IntVar()
     # Computer Science Radio Button
     self.CS_button = Radiobutton(self.quiz_frame, text="Python Quiz", font=("Tw Cen MT", "13", "bold"), bg=foreground_color, fg=background_color,value=1, variable=self.var1)
     self.CS_button.grid(row=1, column = 0, padx=15, pady=30)
     self.CS_button.config(width = 17, height = 4)

    
     # Go back to the main menu interface 
     self.back_button = Button(self.quiz_frame, text="Back", font=("Tw Cen MT", "13", "bold"),  bg="indianred", fg=background_color, command=self.return_func)
     self.back_button.grid(row=2, column = 0, pady=40)
     self.back_button.configure(width = 8)
     
     # Submit the answer 
     self.submit_button = Button(self.quiz_frame, text="Submit", font=("Tw Cen MT", "13", "bold"),  bg=btn_color, fg=background_color, command=self.test_setup)
     self.submit_button.grid(row=2, column = 1, pady=40)
     self.submit_button.configure(width = 8)
     
     # Error correction label 
     self.error_show = Label(self.quiz_frame, text="", font=("Tw Cen MT", "10", "bold"), bg=background_color, fg="indianred")
     self.error_show.grid(row=3,column=0,pady=10,columnspan=2)

  # Start the questions 
  def test_setup(self):
    global chosen_quiz
    quiz_choice = self.var1.get()
    
    if quiz_choice == 2: 
       chosen_quiz = phy_qanda
       print(chosen_quiz[1][0])
       self.quiz_frame.destroy()
       Quiz(root)
    elif quiz_choice == 1: 
       chosen_quiz = cs_qanda
       print(chosen_quiz[1][0])
       self.quiz_frame.destroy()
       Quiz(root)
    else: 
       self.error_show.configure(text="")
       self.error_show.configure(text="Please select an option before continuing!")
  
  # Return to the first screen function 
  def return_func(self): 
    names_list.clear()
    self.quiz_frame.destroy()
    QuizStarter(root)
    print(names_list)

class Quiz: # Actual quiz 
  def __init__(self, parent):
    self.quiz_frame = Frame(parent, bg=background_color, padx=100, pady=100)
    # Geometry and placement of the UI
    self.quiz_frame.grid()

    self.question_label = Label(self.quiz_frame, text=(str(question_num) + '/15) ' + chosen_quiz[qnum][0]), font=("Tw Cen MT", "17", "bold"), bg=background_color, fg=foreground_color)
    self.question_label.grid(row=1,padx=10,pady=30)
    self.var1 = IntVar()

    self.rb1 = Radiobutton(self.quiz_frame, text=chosen_quiz[qnum][1],font=("Tw Cen MT", "11", "bold"),bg=foreground_color, fg=background_color,value=1,padx=10,pady=10,variable=self.var1)
    self.rb1.grid(row=2,sticky=W)

    self.rb2 = Radiobutton(self.quiz_frame, text=chosen_quiz[qnum][2],font=("Tw Cen MT", "11", "bold"),bg=foreground_color, fg=background_color,value=2,padx=10,pady=10,variable=self.var1)
    self.rb2.grid(row=3,sticky=W)

    self.rb3 = Radiobutton(self.quiz_frame, text=chosen_quiz[qnum][3],font=("Tw Cen MT", "11", "bold"),bg=foreground_color, fg=background_color,value=3,padx=10,pady=10,variable=self.var1)
    self.rb3.grid(row=4,sticky=W)

    self.rb4 = Radiobutton(self.quiz_frame, text=chosen_quiz[qnum][4],font=("Tw Cen MT", "11", "bold"),bg=foreground_color, fg=background_color,value=4,padx=10,pady=10,variable=self.var1)
    self.rb4.grid(row=5,sticky=W)

    self.confirm_button = Button(self.quiz_frame, text='Confrim', font=("Tw Cen MT", "13", "bold"), bg=background_color, fg=foreground_color, command=self.quiz_progress)
    self.confirm_button.grid(row=6,sticky=E)

    self.back_button = Button(self.quiz_frame, text='Back',font=("Tw Cen MT", '13', 'bold'), bg=background_color, fg=foreground_color, command=self.exit_button)
    self.back_button.grid(row=6, sticky=W)

    self.error_label = Label(self.quiz_frame, text = '', font=("Tw Cen MT", "11", "bold"), bg=background_color, fg=foreground_color)
    self.error_label.grid(row=7)

    self.change_num = 1



  def exit_button(self):
    msg_box = messagebox.askokcancel(title='Are you sure?', message='Are you sure you want to coninue? press okay to go back to menu')
    if msg_box == True:
      asked.clear()
      self.quiz_frame.destroy()
      Selection(root)
      asked.clear()
      
    
    
  
  def questions_setup(self):
    randomiser()
    self.change_num +=1
    print(self.change_num)
    self.var1.set(0)
    self.question_label.config(text = str(self.change_num)+ '/15) ' +chosen_quiz[qnum][0])
    self.rb1.config(text = chosen_quiz[qnum][1])
    self.rb2.config(text = chosen_quiz[qnum][2])
    self.rb3.config(text = chosen_quiz[qnum][3])
    self.rb4.config(text = chosen_quiz[qnum][4])
    self.error_label.config(text = '')
  
  def quiz_progress(self):
    global mechanics_score
    global nuclear_physics_score
    global waves_score
    global python_score
    global heuristics_score
    global algorithms_score
    choice = self.var1.get()
    score = chosen_quiz[qnum][6]
    if len(asked)>14: # For the final question 
      if choice == chosen_quiz[qnum][5]: # Correct 
        self.confirm_button.config(text='Confirm')
        score += 1
        print('Finished')
      else: # Wrong 
        self.confirm_button.config(text='Confirm')
        print('Finished')
    else: # If it isn't the final question 
      if choice == 0: # If the person hasn't selected anything 
        self.error_label.config(text = 'You havent answered anything!')
        choice = self.var1.get()
      else: 
        if choice == chosen_quiz[qnum][5]: # Correct
          if chosen_quiz == phy_qanda:
            if chosen_quiz[qnum][7] == 'Mechanics':
              mechanics_score += 1
              print(mechanics_score)
            elif chosen_quiz[qnum][7] == 'Waves':
              waves_score += 1
              print(waves_score)
            else:
              nuclear_physics_score += 1
              print(nuclear_physics_score)
            print('Correct')
            self.questions_setup()
          else:
            if chosen_quiz[qnum][7] == 'Python':
              python_score += 1
              print(python_score)
            elif chosen_quiz[qnum][7] == 'Algorithms':
              algorithms_score += 1
              print(algorithms_score)
            else:
              heuristics_score += 1
              print(heuristics_score)
            print('Correct')
            self.questions_setup()
        else: # Wrong 
          print(chosen_quiz[qnum][5])
          print('Wrong')
          self.questions_setup()
        
        
     
if __name__ == "__main__":
  root = Tk()
  root.title("Python Quiz")
  quiz_instance = QuizStarter(root) #instantiation, making an instance of the class Quiz
  root.mainloop()#so the frame doesnt dissapear