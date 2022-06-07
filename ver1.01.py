from tkinter import *
import snake_hard
import snake_easy
import tkinter.font
import snake_deathmatch
import option
from PIL import Image

def openFrame(frame): #프레임 변경
    frame.tkraise()

def easystart():
    end()
    snake_easy.start()
    
def hardstart():
    end()
    snake_hard.start()
    
def vsstart():
    end()
    snake_deathmatch.start()  

def end():
    win.destroy()

def ranklist():
    ranking = {}
    font = tkinter.font.Font(family="맑은 고딕", size=15)
    font2 = tkinter.font.Font(family="Courier", size=15, weight='bold' )
    with open("Ranking.txt", 'r') as f:
        for line in f.readlines():
            ranking[line.split(',')[0]] = int(line.split(',')[1].strip())

    sorted(ranking.items(), key=lambda x: x[1], reverse=True)
    result = ""

    rank = 1
    for value in sorted(ranking.items(), key=lambda x: x[1], reverse=True):
        result += (str(rank)+". "+value[0]+" - "+str(value[1])) + "\n"
        rank += 1
        if rank > 10:
            break;
        
    Rank1lb = tkinter.Label(rankingframe,width=33,height = 2,text = "Snake Game Ranking", font=font2, bg='lightblue')
    Rank1lb.grid(row=0, column =1, columnspan=2, padx=(0,0))
    Rank2lb = tkinter.Label(rankingframe,width=35, height=10,text = result, font= font, bg='lightgray')
    Rank2lb.grid(row=1, column =0, columnspan=2, ipady=2)
    back3 = tkinter.Button(rankingframe,width=34, text="BACK", command=lambda:[openFrame(mainframe)],bg="#99ff99")
    back3.grid(row=2, column = 0,columnspan = 5,sticky="nsew", padx=(0,17))

win = tkinter.Tk();
win.title('Welcome to Snake Game!!')
win.geometry('385x368')

win.resizable(width=False, height=False)

mainframe = tkinter.Frame(win)
modeframe = tkinter.Frame(win)
settingframe = tkinter.Frame(win)
rankingframe = tkinter.Frame(win)

 




imagemain = Image.open('./img/snake1.png')
resize_image = imagemain.resize((385,368))
resize_image.save('./img/mainsnake.png')

mainsnake = PhotoImage(file="./img/mainsnake.png")
mainimg = tkinter.Label(mainframe, text="배경색",image=mainsnake)
mainimg.grid()

mainframe.grid(row=0, column=0, sticky="nsew")
modeframe.grid(row=0, column=0, sticky="nsew")
settingframe.grid(row=0, column=0, sticky="nsew")
rankingframe.grid(row=0, column=0, sticky="nsew")

backlb1 = tkinter.Label(settingframe, text="배경색", width=11, height=2, bg = 'lightblue')
backlb1.grid(row=0, column=0,columnspan=2, pady=(5,2))

backgc1 = tkinter.Button(settingframe,width =4, height =2, bg ='aqua', command=lambda:[option.changeBackgroundColor('aqua')])
backgc1.grid(row=1, column=0,padx=2)
backgc2 = tkinter.Button(settingframe,width =4, height =2, bg ='beige', command=lambda:[option.changeBackgroundColor('beige')])
backgc2.grid(row=1, column=1,padx=2)
backgc3 = tkinter.Button(settingframe,width =4, height =2, bg ='lightgreen', command=lambda:[option.changeBackgroundColor('lightgreen')])
backgc3.grid(row=1, column=2,padx=2)
backgc4 = tkinter.Button(settingframe,width =4, height =2, bg ='aquamarine', command=lambda:[option.changeBackgroundColor('aquamarine')])
backgc4.grid(row=1, column=3,padx=2)
backgc5 = tkinter.Button(settingframe,width =4, height =2, bg ='darksalmon', command=lambda:[option.changeBackgroundColor('darksalmon')])
backgc5.grid(row=1, column=4,padx=2)
backgc5 = tkinter.Label(settingframe,width =5, height =2)
backgc5.grid(row=1, column=8,padx=2)


backlb2 = tkinter.Label(settingframe, text="뱀 색", width=11, height=2, bg = 'lightblue')
backlb2.grid(row=2, column=0,columnspan=2, pady=(5,2))

backgc2_1 = tkinter.Button(settingframe,width =4, height =2, bg ='black', command=lambda:[option.changeSnakeColor('black')])
backgc2_1.grid(row=3, column=0,padx=2)
backgc2_2 = tkinter.Button(settingframe,width =4, height =2, bg ='blue', command=lambda:[option.changeSnakeColor('blue')])
backgc2_2.grid(row=3, column=1,padx=2)
backgc2_3 = tkinter.Button(settingframe,width =4, height =2, bg ='green', command=lambda:[option.changeSnakeColor('green')])
backgc2_3.grid(row=3, column=2,padx=2)
backgc2_4 = tkinter.Button(settingframe,width =4, height =2, bg ='deeppink', command=lambda:[option.changeSnakeColor('deeppink')])
backgc2_4.grid(row=3, column=3,padx=2)
backgc2_5 = tkinter.Button(settingframe,width =4, height =2, bg ='yellow', command=lambda:[option.changeSnakeColor('yellow')])
backgc2_5.grid(row=3, column=4,padx=2)

backlb3 = tkinter.Label(settingframe, text="먹이 색", width=11, height=2, bg = 'lightblue')
backlb3.grid(row=4, column=0,columnspan=2, padx=(0,0),pady=(5,2))

backgc3_1 = tkinter.Button(settingframe,width =4, height =2, bg ='yellow', command=lambda:[option.changeFoodColor('yellow')])
backgc3_1.grid(row=5, column=0,padx=2)
backgc3_2 = tkinter.Button(settingframe,width =4, height =2, bg ='teal', command=lambda:[option.changeFoodColor('teal')])
backgc3_2.grid(row=5, column=1,padx=2)
backgc3_3 = tkinter.Button(settingframe,width =4, height =2, bg ='navy', command=lambda:[option.changeFoodColor('navy')])
backgc3_3.grid(row=5, column=2,padx=2)
backgc3_4 = tkinter.Button(settingframe,width =4, height =2, bg ='black', command=lambda:[option.changeFoodColor('black')])
backgc3_4.grid(row=5, column=3,padx=2)
backgc3_5 = tkinter.Button(settingframe,width =4, height =2, bg ='green', command=lambda:[option.changeFoodColor('green')])
backgc3_5.grid(row=5, column=4,padx=2)

backlb4 = tkinter.Label(settingframe, text="뱀 형태", width=11, height=2, bg = 'lightblue')
backlb4.grid(row=6, column=0,columnspan=2, pady=(5,2))

triimg = PhotoImage(file="./img/tri.png")
squimg = PhotoImage(file="./img/squ.png")
cirimg = PhotoImage(file="./img/cir.png")
turimg = PhotoImage(file="./img/tur.png")


backgc4_1 = tkinter.Button(settingframe,width =35, height =35,image=squimg, command=lambda:[option.changeSnake_shape('square')])
backgc4_1.grid(row=7, column=0,padx=2)
backgc4_2 = tkinter.Button(settingframe,width =35, height =35,image=triimg, command=lambda:[option.changeSnake_shape('triangle')])
backgc4_2.grid(row=7, column=1,padx=2)
backgc4_3 = tkinter.Button(settingframe,width =35, height =35,image=cirimg, command=lambda:[option.changeSnake_shape('circle')])
backgc4_3.grid(row=7, column=2,padx=2)
backgc4_4 = tkinter.Button(settingframe,width =35, height =35,image=turimg, command=lambda:[option.changeSnake_shape('turtle')])
backgc4_4.grid(row=7, column=3,padx=2)


gotomode = tkinter.Button(mainimg, text="START",width =15, height =2,command=lambda:[openFrame(modeframe)], bg ='skyblue')
gotoset = tkinter.Button(mainimg, text="SETTING",width=15,height =2,command=lambda:[openFrame(settingframe)], bg = 'gray')
gotorank = tkinter.Button(mainimg, text="RANKING",width=15,height =2,command=lambda:[openFrame(rankingframe),ranklist()], bg = 'orange')

easybtn = tkinter.Button(modeframe, text = 'EASY',width=25,height = 10,bg="#00ffff",command=lambda:[easystart()])
hardbtn = tkinter.Button(modeframe, text = 'HARD',width=25,height = 10,bg="#ff9999",command=lambda:[hardstart()])
vsbtn = tkinter.Button(modeframe, text = 'VS MODE',width=52,height = 10,bg="#ffc000",command=lambda:[vsstart()])


back = tkinter.Button(modeframe, text="BACK", command=lambda:[openFrame(mainframe)],bg="#99ff99")
back2 = tkinter.Button(settingframe, width=53 ,text="BACK", command=lambda:[openFrame(mainframe)],bg="#99ff99")


gotomode.place(x=10, y=220)
gotoset.place(x=10, y=265)
gotorank.place(x=10, y=310)
easybtn.grid(row=0, column=0,padx=(5,0), pady=5)
hardbtn.grid(row=0, column=1,padx=(5,5), pady=5)
vsbtn.grid(row=1, column=0,padx=(5,0), pady=(0,5), columnspan=2, sticky="w" )

back.grid(row= 2,columnspan = 2,sticky="nsew",padx=5)
back2.grid(row= 8,columnspan = 10,padx=(2,0),pady=(4,0),sticky="sew")



option.setDefaultSetting()




openFrame(mainframe) #기본메인화면



win.mainloop();




