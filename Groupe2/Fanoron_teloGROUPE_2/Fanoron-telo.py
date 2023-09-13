import tkinter as tk

def draw_fanoron_telo(canvas):
    width = canvas.winfo_reqwidth()
    height = canvas.winfo_reqheight()

    # Dessiner le carré
    canvas.create_rectangle(width / 4, height / 4, 3 * width / 4, 3 * height / 4, width=2)

    # Dessiner les deux diagonales
    canvas.create_line(width / 4, height / 4, 3 * width / 4, 3 * height / 4, width=2)
    canvas.create_line(width / 4, 3 * height / 4, 3 * width / 4, height / 4, width=2)

    # Dessiner les deux bissectrices
    canvas.create_line(0, height / 2, width, height / 2, width=2)
    canvas.create_line(width / 2, 0, width / 2, height, width=2)

def main():
    root = tk.Tk()
    root.title("Fanoron-telo")

    canvas = tk.Canvas(root, width=300, height=300)
    canvas.pack()

    draw_fanoron_telo(canvas)

    root.mainloop()

if __name__ == "__main__":
    main()
