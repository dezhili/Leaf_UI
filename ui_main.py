from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askdirectory
import os
from UI_funcs_summary import leaves_general, per_serration_general, \
    boundary_curvature, boundary_evenly_segment_coordinate, \
    vein_general, vein_curvature

root = Tk()  # top level  root 窗口
root.title('LFEP')
root.config(bg="SteelBlue")
root.geometry('610x400')


# UI 1
image1 = Image.open('umu_logo_eng.jpg')
img1= ImageTk.PhotoImage(image1)

label_1 = Label(root, image=img1)
label_1.grid(row=0, column=2, pady=15)

label_2 = Label(root, text="Leaves features\nextraction platform", bg="SteelBlue", font=15)
label_2.grid(row=0, column=0)


# 选择路径
def selectPath():
    global path_
    path_ = askdirectory()
    path.set(path_)
path = StringVar()
e = Entry(root, textvariable = path, width=30, borderwidth=10)
e.grid(row = 1, column=1, pady=100)
e.insert(0, "Select leaf images path")
Button(root, text = "select", command = selectPath).grid(row=1, column=2)


sure1 = sure2 = sure3 = sure4 = sure5 = sure6 = 0
def sure_button1(event):
    global sure1
    sure1 = 1
def sure_button2(event):
    global sure2
    global text
    text = int(ee.get())
    sure2 = 1
def sure_button3(event):
    global sure3
    sure3 = 1
def sure_button4(event):
    global sure4
    sure4 = 1
def sure_button5(event):
    global sure5
    sure5 = 1
def sure_button6(event):
    global sure6
    sure6 = 1
    
# 根据sure1、sure2、sure3、sure4、sure5、sure6的值选择函数执行
def ui_funcs_summary():
    if sure1 == 1:
        leaves_general()
    if sure2 == 1:
        boundary_evenly_segment_coordinate(text)
    if sure3 == 1:
        per_serration_general()
    if sure4 == 1:
        boundary_curvature()
    if sure5 == 1:
        vein_general()
    if sure6 == 1:
        vein_curvature()

        
    
    
# listbox  select1 -> button1
def button1_select1():
    features = ["round or not", "serration_number", "serration_depth_mean", "serration_depth_median",
                "serration_width_mean", "serration_width_median", "serration_width_std",
                "serration_area_mean", "serration_area_median", "serration_area_std",
                "boundary_curvature_mean", "boundary_curvature_median", "boundary_curvature_std",
                "leaf_entire_area", "leaf_area_without_holes", "leaf perimeter", "length_left",
                "length_middle", "length_right", "width_top", "width_middle", "width_bottom",
                "L:W(ratio=length_middle/width_middle)"]
    master1 = Tk()
    master1.title("leaves general")
    master1.config(width=40)
    sb = Scrollbar(master1)
    sb.pack(side=RIGHT, fill=Y)
    lb = Listbox(master1, yscrollcommand=sb.set, width=30, height=20)  # 互联互通，会改变 滚动条位置
    for item in features:
        lb.insert(END, item)

    lb.pack(side=LEFT, fill=BOTH)
    sb.config(command=lb.yview)  # 通过改变滚动条位置，看到yview
    
    theButton1 = Button(master1, text="select all", command=lambda x=lb: lb.selection_set(0, END), width=6)
    theButton2 = Button(master1, text="confirm", command=master1.destroy, width=6)
    theButton2.bind("<Button-1>", sure_button1)
    theButton3 = Button(master1, text="quit", command=master1.destroy, width=6)
    theButton1.pack(side=TOP)
    theButton2.pack(side=TOP)
    theButton3.pack(side=BOTTOM)
    


# Entry button2
def button2_select2():
    master = Tk()
    master.title("boundary evenly segment coordinate")
    Label(master, text="please enter a number: ").grid(row=0, column=0, padx=10, pady=10)
    ee = Entry(master)
    global ee
    ee.grid(row=0, column=1, padx=10, pady=10)
    theButton = Button(master, text="confirm", command=master.destroy)
    theButton.grid(row=1, column=0,sticky=W, padx=10)
    theButton.bind("<Button-1>", sure_button2)
    Button(master, text="quit", command=master.destroy).grid(row=1, column=1,
            sticky=E, padx=10)
    
# listbox  select3 -> button3
def button3_select3():
    features = ["serration_depth(mm)", "serration_width(mm)", "serration_area(mm2)",
                "serration_curvature_mean", "serration_curvature_median", "serration_curvature_std"]
    master = Tk()
    master.title("per serration general")
    master.config(width=40)
    sb = Scrollbar(master)
    sb.pack(side=RIGHT, fill=Y)
    lb = Listbox(master, yscrollcommand=sb.set, selectmode=EXTENDED, width=30, height=10)  # 互联互通，会改变 滚动条位置
    for item in features:
        lb.insert(END, item)
    lb.pack(side=LEFT, fill=BOTH)
    sb.config(command=lb.yview)  # 通过改变滚动条位置，看到yview

    theButton1 = Button(master, text="select all", command=lambda x=lb: lb.selection_set(0, END), width=6)
    theButton2 = Button(master, text="confirm", command=master.destroy, width=6)
    theButton2.bind("<Button-1>", sure_button3)
    theButton3 = Button(master, text="quit", command=master.destroy, width=6)
    theButton1.pack(side=TOP)
    theButton2.pack(side=TOP)
    theButton3.pack(side=BOTTOM)

# listbox  select4 -> button4
def button4_select4():
    features = ["serrations_curvature", "boundary_curvature"]
    master = Tk()
    master.title("boundary curvature")
    master.config(width=40)
    sb = Scrollbar(master)
    sb.pack(side=RIGHT, fill=Y)
    lb = Listbox(master, yscrollcommand=sb.set, selectmode=EXTENDED, width=30, height=5)  # 互联互通，会改变 滚动条位置
    for item in features:
        lb.insert(END, item)
    lb.pack(side=LEFT, fill=BOTH)
    sb.config(command=lb.yview)  # 通过改变滚动条位置，看到yview

    theButton1 = Button(master, text="select all", command=lambda x=lb: lb.selection_set(0, END), width=6)
    theButton2 = Button(master, text="confirm", command=master.destroy, width=6)
    theButton2.bind("<Button-1>", sure_button4)        
    theButton3 = Button(master, text="quit", command=master.quit, width=6)
    theButton1.pack(side=TOP)
    theButton2.pack(side=TOP)
    theButton3.pack(side=BOTTOM)

# listbox  select5 -> button5
def button5_select5():
    features = ["vein_angle_mean", "vein_angle_median", "vein_angle_std", "top_left_angle",
                "top_right_angle", "bottom_left_angle", "bottom_right_angle",
                "main_vein_curvature_mean", "main_vein_curvature_median",
                "main_vein_curvature_std", "sub_vein_curvature_mean",
                "sub_vein_curvature_median", "sub_vein_curvature_std", "sub_vein_number",
                "vein_cross_angle_number", "vein_cross_angle(multi)"]
    master = Tk()
    master.title("vein general")
    master.config(width=40)
    sb = Scrollbar(master)
    sb.pack(side=RIGHT, fill=Y)
    lb = Listbox(master, yscrollcommand=sb.set, selectmode=EXTENDED, width=30, height=20)  # 互联互通，会改变 滚动条位置
    for item in features:
        lb.insert(END, item)
    lb.pack(side=LEFT, fill=BOTH)
    sb.config(command=lb.yview)  # 通过改变滚动条位置，看到yview

    theButton1 = Button(master, text="select all", command=lambda x=lb: lb.selection_set(0, END), width=6)
    theButton2 = Button(master, text="confirm", command=master.destroy, width=6)
    theButton2.bind("<Button-1>", sure_button5)        
    theButton3 = Button(master, text="quit", command=master.destroy, width=6)
    theButton1.pack(side=TOP)
    theButton2.pack(side=TOP)
    theButton3.pack(side=BOTTOM)

# listbox  select6 -> button6
def button6_select6():
    features = ["main_vein_curvature", "sub_vein_curvature"]
    master = Tk()
    master.title("vein curvature")
    master.config(width=40)
    sb = Scrollbar(master)
    sb.pack(side=RIGHT, fill=Y)
    lb = Listbox(master, yscrollcommand=sb.set, selectmode=EXTENDED, width=30, height=5)  # 互联互通，会改变 滚动条位置
    for item in features:
        lb.insert(END, item)
    lb.pack(side=LEFT, fill=BOTH)
    sb.config(command=lb.yview)  # 通过改变滚动条位置，看到yview

    theButton1 = Button(master, text="select all", command=lambda x=lb: lb.selection_set(0, END), width=6)
    theButton2 = Button(master, text="confirm", command=master.destroy, width=6)
    theButton2.bind("<Button-1>", sure_button6)        
    theButton3 = Button(master, text="quit", command=master.destroy, width=6)
    theButton1.pack(side=TOP)
    theButton2.pack(side=TOP)
    theButton3.pack(side=BOTTOM)
    
# UI 2
def show_ui_2():
    # UI 2
    # 画布 背景
    root1 = Toplevel()  # top level 窗口
    root1.title('LFEP')
    root1.geometry('750x500')

    canvas = Canvas(root1, bg="SteelBlue")
    canvas.pack(expand=YES, fill=BOTH)
#    canvas.pack()
    print(path_)
    leaf_name = os.listdir(path_)[0]
    leaves_path = path_ +'/' + leaf_name
    
    # 图片通过Label放入canvas
    image2 = Image.open(leaves_path)
    img2 = image2.resize((355, 280))
    img2 = ImageTk.PhotoImage(img2)
#    canvas.create_image(350, 150, image=img2)
    Label(canvas, image=img2).grid(row=2, column=1, pady=10)
    

    # button
    button1 = Button(canvas, text="1. Leaves general", bg="white",fg='black', 
                     width=20, height=2, command=button1_select1)
    button1.grid(row=0, column=0, padx=23, pady=10)

    button2 = Button(canvas, text="2. Boundary evenly \n segment coordinate",
                     bg="white",fg='black', width=20, height=2, 
                     command=button2_select2)
    button2.grid(row=1, column=0, padx=23, pady=10)

    button3 = Button(canvas, text="3. Per serration general", bg="white",fg='black', 
                     width=20, height=2, command=button3_select3)
    button3.grid(row=0, column=1, padx=23, pady=10)

    button4 = Button(canvas, text="4. Boundary curvature", bg="white",fg='black', 
                     width=20, height=2, command=button4_select4)
    button4.grid(row=1, column=1, padx=23, pady=10)

    button5 = Button(canvas, text="5. Vein general", bg="white",fg='black', 
                     width=20, height=2, command=button5_select5)
    button5.grid(row=0, column=2, padx=23, pady=10)

    button6 = Button(canvas, text="6. Vein curvature", bg="white",fg='black', 
                     width=20, height=2, command=button6_select6)
    button6.grid(row=1, column=2, padx=23, pady=10)

    # 确定选择好了路径
    button7 = Button(canvas, text="confirm", fg="red", bg="green", width=15, height=1, command=ui_funcs_summary)
    button7.grid(row=13, column=2, pady=15)

    root1.config(background="SteelBlue")
    mainloop()


# 确定选择好了路径
button1 = Button(root, text="confirm", fg="red", bg="green", width=15, height=1, command=show_ui_2)
button1.grid(row=2, column=2, pady=40)
root.config(background="SteelBlue")

mainloop()





















