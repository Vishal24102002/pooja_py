import os
import customtkinter as ctk
import openai
#from api_key import API_KEY
import pyttsx3 as pt

wf=275
hf=400

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def speak(event):
    print("value=",value.get())
    print("name=",ainame.get())
    engine=pt.init()
    Voices = engine.getProperty('voices')
    volu = engine.getProperty('volume')
    print(Voices)
    print(volu)
    if value.get()=="male" and len(ainame.get())!=0:
        engine.setProperty('voice', Voices[0].id)
        text="hello my name is "+ainame.get()
    elif value.get()=="female" and len(ainame.get())!=0:
        engine.setProperty('voice', Voices[1].id)
        text = "hello my name is " + ainame.get()
    else:
        text="your friend is added"
        pass
    engine.setProperty('rate', 100)
    engine.setProperty('volume', 1)
    spend = engine.getProperty('rate')
    print("speed=", spend)
    engine.say(text)
    engine.runAndWait()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def appearai():
    try:
        content_frame.place_forget()
    except:
        pass
    priya_naming.place(x=0,y=5)

def appearct():
    try:
        priya_naming.place_forget()
    except:
        pass
    content_frame.place(x=0, y=5)

def content_frame_cancel_click():
    content_frame.place_forget()


def save_contact(TYPE):
    top_head.place(x=0, y=0)
    top_head.configure(text="CHATS", font=('calibre', 18, 'normal'))
    frame_man.place(x=0, y=50)
    if TYPE=="AI":
        if len(ainame.get()) != 0:
            priya_naming.place_forget()
            print("deleted frame")
            contact1.append("AI-"+ainame.get())
            print()
            chat_update()
        else:
            pass

    elif TYPE=="friends":
        contact.append(contact_name.get())
        phone = []
        print("contact",contact_phone.get())
        phone.append(contact_phone.get())
        global dictanry
        dictanry=dict.fromkeys(contact,phone)
        print(dictanry)
        chat_update()


    else:
        print("data not entered")


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def response_generated(prompt):

    openai.api_key = "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"

    query = input("enter the question")
    start_sequence = "AI:"
    restart_sequence = "Human: "
    prompt = query
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    mesg = response.choices[0].text
    print(mesg)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

pooja=ctk.CTk()
pooja.title("DEEP-CHAT")
pooja.geometry("275x400")
pooja.maxsize(275,400)
pooja.minsize(275,400)

priya_start=ctk.CTkFrame(pooja,fg_color="black")
priya_start.pack(expand=True,fill='both')

priya_nam = ctk.CTkFrame(priya_start,fg_color="black",width=275,height=hf)
priya_nam.place(x=0,y=0)

top_head=ctk.CTkLabel(priya_nam,font=('calibre',12,'normal'),fg_color="black",text_color="white",width=275,height=35)
#top_head.place()

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

frame_man=ctk.CTkFrame(priya_nam,fg_color="black",width=wf,height=400)
contact1 = []
contact= []
dictanry={}
data= []

def chat_update():
    data = dictanry.keys()
    try:
        if len(contact1)!=0 and len(data)==0:
            for cont in contact1:
                print(cont)
                button_ai = ctk.CTkButton(frame_man, text=cont, text_color='white', font=('calibre', 12, 'normal'),
                                          fg_color='black', hover_color='orange', width=wf, height=30)
                button_ai.pack()
                contact1.remove(cont)
                if len(contact1) == 0:
                    print("deleted ")
        elif len(contact1)==0 and len(data)!=0:
            data = dictanry.keys()
            for dic in data:
                print("dic= ", dic)
                button_human = ctk.CTkButton(frame_man, text=dic,hover_color='green', text_color='white',
                                             font=('calire', 12, 'normal'), fg_color='black', width=wf, height=30)
                button_human.pack()

    except:
        print("error occured")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

priya_naming=ctk.CTkFrame(priya_nam,fg_color="black",width=270,height=50)

ainame = ctk.StringVar()

ai_label = ctk.CTkLabel(priya_naming, text="name your AI friend", text_color="white", font=('calibre', 12, 'normal'))
ai_name = ctk.CTkEntry(priya_naming, textvariable=ainame, font=('calibre', 12, 'normal'))
value = ctk.StringVar()
value.set("select")
ai='AI'
save_button=ctk.CTkButton(priya_naming,text="save",hover_color="lime",command=lambda:save_contact(ai))
option = ctk.CTkOptionMenu(priya_naming, values=['male', 'female'],dropdown_hover_color="orange",variable=value, command=speak)
option.grid(columnspan=1, row=1,column=0)

save_button.grid(row=1,column=1)
ai_label.grid(row=0,column=0)
ai_name.grid(row=0,column=1)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#friend list
content_frame=ctk.CTkFrame(priya_start,fg_color="black")

contact_phone=ctk.StringVar()
contact_name=ctk.StringVar()
name_detail=ctk.CTkEntry(content_frame,textvariable=contact_name)
phone_number=ctk.CTkEntry(content_frame,textvariable=contact_phone)
name_detail_label=ctk.CTkLabel(content_frame,text="NAME",text_color="white",width=hf//3,font=('calibre',12,'normal'))
phone_number_label=ctk.CTkLabel(content_frame,text="mobile-number",text_color="white",width=hf//3,font=('calibre',12,'normal'))
content_frame_save=ctk.CTkButton(content_frame,text="SAVE",hover_color='olive',command=lambda:save_contact("friends"))
content_frame_cancel=ctk.CTkButton(content_frame,text="CANCEL",hover_color='red',command=content_frame_cancel_click)

#packing
content_frame_save.grid(row=2,column=1)
content_frame_cancel.grid(row=2,column=0)
name_detail_label.grid(row=0,column=0)
name_detail.grid(row=0,column=1)
phone_number_label.grid(row=1,column=0)
phone_number.grid(row=1,column=1)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

chat_AI_button=ctk.CTkButton(priya_nam,text="AI friend",hover_color=("green","blue"),fg_color="black",width=137.5,height=25,command=appearai)
chat_FRI_button=ctk.CTkButton(priya_nam,text="Friends",hover_color=("green","blue"),fg_color="black",width=137.5,height=25,command=appearct)
chat_clear=ctk.CTkButton(priya_nam,text="CLEAR Chats",hover_color="red",fg_color="black",width=275,height=50)

chat_AI_button.place(x=0,y=375)
chat_FRI_button.place(x=137.5,y=375)
chat_clear.place(x=0,y=325)


pooja.mainloop()
