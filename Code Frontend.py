window = tkinter.Tk()
window.title("Sistem Penjadwalan")

frame = tkinter.Frame(window)
frame.pack()

# Saving Job Specification
job_info_frame =tkinter.LabelFrame(frame, text="Job Specification")
job_info_frame.grid(row= 0, column=0, padx=20, pady=10)

banyak_job_label = tkinter.Label(job_info_frame, text="Banyak Job")
banyak_job_label.grid(row=0, column=0)

banyak_job_entry = tkinter.Entry(job_info_frame, textvariable=tkinter.IntVar())
banyak_job_entry.grid(row=1, column=0)

button_1 = tkinter.Button(job_info_frame, text="Next", command= lambda: enter_data(entry_box_manager))
button_1.grid(row=3, column=0, sticky="news", padx=20, pady=10)


for widget in job_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Detail Job
courses_frame = tkinter.LabelFrame(frame, text="Detail Job")
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Min Processing Time
terms_frame = tkinter.LabelFrame(frame, text="Cek Spesifikasi Temperatur Tangki")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)


for widget in terms_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Max Processing Time
terms_1_frame = tkinter.LabelFrame(frame, text="Cek Spesifikasi Level Air Tangki")
terms_1_frame.grid(row=3, column=0, sticky="news", padx=20, pady=10)

entry_box_manager = EntryBoxManager(courses_frame, terms_frame, terms_1_frame)

for widget in terms_1_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Button Final
button = tkinter.Button(frame, text="Buat Jadwal!", command= lambda: proses_data(entry_box_manager))
button.grid(row=4, column=0, sticky="news", padx=20, pady=10)

#Display Final
Final_Frame = tkinter.LabelFrame(frame, text="Waktu Selesai")
Final_Frame.grid(row=5, column=0, sticky="news", padx=20, pady=10)

#Display Waktu Pemrosesan Tiap Tangki
Proses_Frame = tkinter.LabelFrame(frame, text="Detail Waktu Pencelupan")
Proses_Frame.grid(row=6, column=0, sticky="news", padx=20, pady=10)


window.mainloop()
