import tkinter as tk

def draw_fanoron_telo(canvas):
    width = canvas.winfo_reqwidth()
    height = canvas.winfo_reqheight()

    # Dessiner le carré
    canvas.create_rectangle(width / 4, height / 4, 3 * width / 4, 3 * height / 4, width=2)

    # Dessiner les deux diagonales
    canvas.create_line(width / 4, height / 4, 3 * width / 4, 3 * height / 4, width=2)
    canvas.create_line(width / 4, 3 * height / 4, 3 * width / 4, height / 4, width=2)

    # Dessiner les deux bissectrices du carré
    mid_x = width / 2
    mid_y = height / 2
    canvas.create_line(width / 4, mid_y, 3 * width / 4, mid_y, width=2)
    canvas.create_line(mid_x, height / 4, mid_x, 3 * height / 4, width=2)

def main():
    root = tk.Tk()
    root.title("Fanoron-telo")

    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()

    draw_fanoron_telo(canvas)

    root.mainloop()

if __name__ == "__main__":
    main()
