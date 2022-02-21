import tkinter as tk

main_window = tk.Tk()

label1 = tk.Label(main_window, text ="Text")
label2 = tk.Label(main_window, text ="Text")
tombol1 = tk.Button(main_window, text ="Button")
tombol2 = tk.Button(main_window, text ="Button")
check = tk.Checkbutton(main_window, text="Check")

# Method/fungsi Positioning
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()
check.pack()

# Method menampilkan GUI
main_window.mainloop()


