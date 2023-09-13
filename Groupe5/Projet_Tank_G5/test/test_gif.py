# import tkinter as tk
# from PIL import Image, ImageTk
#
#
# def animate_gif(frame_number):
#     # Afficher l'image courante du GIF
#     gif_image = gif_frames[frame_number]
#     canvas.itemconfig(gif_item, image=gif_image)
#
#     # Appeler la fonction à nouveau après un certain délai (en millisecondes)
#     root.after(delay, animate_gif, (frame_number + 1) % num_frames)
#
#
# # Créer la fenêtre principale
# root = tk.Tk()
#
# # Charger le GIF en utilisant la bibliothèque Pillow
# gif = Image.open("rocket11.gif")
#
# # Extraire chaque image du GIF
# gif_frames = []
# num_frames = gif.n_frames
# for frame_number in range(num_frames):
#     gif.seek(frame_number)
#     gif_frames.append(ImageTk.PhotoImage(gif.copy()))
#
# # Créer un canevas pour afficher le GIF
# canvas = tk.Canvas(root, width=gif.width, height=gif.height)
# canvas.pack()
#
# # Afficher la première image du GIF
# gif_item = canvas.create_image(0, 0, anchor=tk.NW, image=gif_frames[0])
#
# # Définir le délai entre chaque image du GIF (en millisecondes)
# delay = gif.info["duration"]
#
# # Lancer l'animation du GIF en appelant la fonction animate_gif
# root.after(delay, animate_gif, 1)
#
# # Démarrer la boucle principale Tkinter
# root.mainloop()



from tkinter import ttk
import tkinter as tk

root = tk.Tk()

# config the root window
root.geometry('600x400')
root.resizable(False, False)
root.title('Tkinter Cursors')

frame = ttk.Frame(root)


# label
label = ttk.Label(frame, text="Cursor:")
label.pack(fill=tk.X, padx=5, pady=5)

# cursor list
selected_cursor = tk.StringVar()
cursor_list = ttk.Combobox(frame, textvariable=selected_cursor, cursor='arrow')
cursors = ['arrow', 'man', 'based_arrow_down', 'middlebutton', 'based_arrow_up', 'mouse', 'boat', 'pencil', 'bogosity', 'pirate', 'bottom_left_corner', 'plus', 'bottom_right_corner', 'question_arrow', 'bottom_side', 'right_ptr', 'bottom_tee', 'right_side', 'box_spiral', 'right_tee', 'center_ptr', 'rightbutton', 'circle', 'rtl_logo', 'clock', 'sailboat', 'coffee_mug', 'sb_down_arrow', 'cross', 'sb_h_double_arrow', 'cross_reverse', 'sb_left_arrow', 'crosshair', 'sb_right_arrow', 'diamond_cross',
           'sb_up_arrow', 'dot', 'sb_v_double_arrow', 'dotbox', 'shuttle', 'double_arrow', 'sizing', 'draft_large', 'spider', 'draft_small', 'spraycan', 'draped_box', 'star', 'exchange', 'target', 'fleur', 'tcross', 'gobbler', 'top_left_arrow', 'gumby', 'top_left_corner', 'hand1', 'top_right_corner', 'hand2', 'top_side', 'heart', 'top_tee', 'icon', 'trek', 'iron_cross', 'ul_angle', 'left_ptr', 'umbrella', 'left_side', 'ur_angle', 'left_tee', 'watch', 'leftbutton', 'xterm', 'll_angle', 'X_cursor', 'lr_angle']
cursor_list['values'] = cursors
cursor_list['state'] = 'readonly'


cursor_list.pack(fill=tk.X, padx=5, pady=5)

frame.pack(expand=True, fill=tk.BOTH)


# bind the selected value changes
def cursor_changed(event):
    frame.config(cursor=selected_cursor.get())


cursor_list.bind('<<ComboboxSelected>>', cursor_changed)

root.mainloop()