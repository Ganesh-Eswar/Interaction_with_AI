from tkinter import ttk
from tkinter import * 
from PIL import Image,ImageTk
import ai_connection as AI

class InteractWithAI(Tk):
    def __init__(self,user_img,robot_img):
        super().__init__()
        self.geometry("1400x700")
        self.title("Interact with AI")
        self.user_img = user_img
        self.robot_img = robot_img 
        interact = InteractionContainer(self)
        UserEnterContainer(self,interact)

class InteractionContainer():
    def __init__(self,root):
        self.interaction_container = Frame(root)
        self.interaction_container.pack(side="top",fill="both",expand=True)
        self.canvas = Canvas(self.interaction_container)
        self.scrollbar = Scrollbar(self.interaction_container,
                                    orient='vertical',
                                    command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
            scrollregion=self.canvas.bbox("all")
            ))
        self.scrollable_frame.pack(side='left',fill='x',expand=True)
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.AI_image = Image.open(root.robot_img)
        self.AI_image = self.AI_image.resize((40,60))
        self.AIimage = ImageTk.PhotoImage(image=self.AI_image)
        self.developer_image = Image.open(root.user_img)
        self.developer_image = self.developer_image.resize((50,60))
        self.dimage = ImageTk.PhotoImage(image=self.developer_image)
        self.robot_type = "Hello, How can I assist you today?"
        self.initial_robot_message()
           
    def initial_robot_message(self):
        self.init_container = Frame(self.scrollable_frame)
        self.init_container.pack(side="top",fill="x")
        self.robot_avatar = Label(self.init_container,image=self.AIimage)
        self.robot_avatar.image = self.AIimage
        self.robot_avatar.grid(row=0,column=0,sticky="W")
        space1 = "                                                       "        
        self.robot_initial_msg = Label(self.init_container,text=self.robot_type+(space1*5),
                                       font=("Helvetica",10),
                                       padx=5,pady=10)
        self.robot_initial_msg.grid(row=0,column=1,sticky="W",padx=15,pady=5)
        
    def interaction(self,user_entry,controller):
        self.user_type = user_entry
        self.ai_reply = (AI.AIConnection.connect_ai(self.user_type,self.robot_type))
        self.setting_component()
    
    def setting_component(self):
        self.right_container = Frame(self.scrollable_frame)
        self.right_container.pack(side="top",fill="x")
        self.robot_type = self.ai_reply
        self.user_avatar = Label(self.right_container,image=self.dimage)
        self.user_avatar.image = self.dimage
        self.user_avatar.pack(side="right",padx=15,pady=5)
        self.user_msg = Label(self.right_container,text=self.user_type,
                                       font=("Helvetica",10),background="yellow",
                                       padx=5,pady=5,wraplength=400)
        self.user_msg.pack(side="right",padx=15,pady=5)
        self.left_container = Frame(self.scrollable_frame)
        self.left_container.pack(side="top",fill="x")
        self.robot_avatar = Label(self.left_container,image=self.AIimage)
        self.robot_avatar.image = self.AIimage
        self.robot_avatar.grid(row=0,column=0,sticky="W",padx=15,pady=5)
        self.robot_initial_msg = Label(self.left_container,text=self.robot_type,
                                       font=("Helvetica",10),background="pink",
                                       padx=5,pady=10,wraplength=400)
        self.robot_initial_msg.grid(row=0,column=1,sticky="W",padx=15,pady=5)
        self.canvas.after(150,lambda: self.canvas.yview_moveto(1.0))

class UserEnterContainer():
    def __init__(self,root,interactionController) -> None:
        self.root = root  
        self.control = interactionController
        self.bottom_container = Frame(self.root)
        self.bottom_container.pack(side="bottom",pady=40)
        self.developer_image = Image.open(self.root.user_img)
        self.developer_image = self.developer_image.resize((60,60))
        self.dimage = ImageTk.PhotoImage(image=self.developer_image)
        self.user_avatar = Label(self.bottom_container,image=self.dimage)
        self.user_avatar.image = self.dimage
        self.user_avatar.pack(side="left",padx=20)
        self.user_text = Text(self.bottom_container,
                              height=2,width=170,
                              background="white",                   
                              font=("Helvetica",10,'bold'),padx=5,pady=5)
        self.user_text.insert(INSERT,"Hello AI")
        self.user_text.pack(side="left")
        self.send_button = Button(self.bottom_container,text="Send",
                                  background="blue",foreground="white",
                                  font=("Helvetica",10),padx=10,
                                  command=self.user_entry)
        self.send_button.pack(side="left",padx=20)
        
    def user_entry(self):
        entry = self.user_text.get(1.0,'end')
        self.user_text.delete(1.0,'end')
        self.control.interaction(entry,self.root)

if __name__ == "__main__":
    user_img = r"chatApp\user_img.png"
    robot_img = r"chatApp\robot_img.png" 
    app = InteractWithAI(user_img,robot_img)
    app.mainloop()
    

