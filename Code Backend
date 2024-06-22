import tkinter
from tkinter import ttk
from tkinter import messagebox
import pulp
from chart_studio import plotly as py
from plotly.offline import plot 
import plotly.figure_factory as ff
import datetime
from datetime import timedelta, date
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import snap7
from snap7.util import *
import tracemalloc
import time

class EntryBoxManager:
    def __init__(self, courses_frame, terms_frame, terms_1_frame):
        self.courses_frame = courses_frame
        self.terms_frame = terms_frame
        self.terms_1_frame = terms_1_frame
        self.entry_boxes = {}
        self.check_boxes = {}

    def create_entry_boxes(self, num_jobs):
        job_list = ["CBP-IP", "CBP-ADS", "CCC", "CAA", "SAA" ]
        list_tangki = ["Alkaline", "Rinsing", "Deoxidizing", "CCC", "CAA"]
        for i in range (1, num_jobs + 1):
            job_label = tkinter.Label(courses_frame, text=f"Job {i}")
            job_label.grid(row=i, column=0)

            for j in range (5):
                prompt = job_list[j]
                prompt_1 = f"{list_tangki[j]}"        
                var = tkinter.StringVar(value="Unchecked")
                var_1 = tkinter.StringVar(value="Unchecked")
                var_2 = tkinter.StringVar(value="Unchecked")


                # Create entry box for user input
                check_box = tkinter.Checkbutton(courses_frame, text=prompt,
                                       variable=var, onvalue="Checked", offvalue="Unchecked")
                check_box.grid(row=i, column=j+1, padx=5, pady=5)
                if (i == 1):
                    prompt_label_1 = tkinter.Label(terms_frame, text=prompt_1)
                    check_box_temp = tkinter.Checkbutton(terms_frame, text="Sesuai?",
                                variable=var_1, onvalue="Checked", offvalue="Unchecked")
                    check_box_temp.grid(row=i+1, column=j+1, padx=5, pady=5)
                    prompt_label_1.grid(row=i, column=j+1)

                    prompt_label_2 = tkinter.Label(terms_1_frame, text=prompt_1)
                    check_box_level = tkinter.Checkbutton(terms_1_frame, text="Sesuai?",
                                variable=var_2, onvalue="Checked", offvalue="Unchecked")
                    check_box_level.grid(row=i+1, column=j+1, padx=5, pady=5)
                    prompt_label_2.grid(row=i, column=j+1)
                    self.check_boxes[(i,j)] = (var_1, var_2)

                self.entry_boxes[(i, j)] = (var)
                

    def get_entry_box_values(self):
        values = {}
        for (i, j), (var) in self.entry_boxes.items():
            values[(i, j)] = (var.get())
        return values
    
    def get_check_box_values(self):
        values = {}
        all_checked = True
        for (i, j), (var_1,var_2) in self.check_boxes.items():
            values[(i, j)] = (var_1.get(), var_2.get())
        return values



def enter_data(entry_box_manager):
    
    num_jobs = int(banyak_job_entry.get())
    
    entry_box_manager.create_entry_boxes(num_jobs)

def proses_data(entry_box_manager):
    job_list = ["CBP-IP", "CBP-ADS", "CCC", "CAA", "SAA" ]
    list_tangki = ["Alkaline", "Rinsing", "Deoxidizing", "CCC", "CAA"]
    R_1 = [0,1,2,3,4,5,6] #Routing job 1
    R_2 = [0,1,2,3,4,5,6] #Routing job 2
    SP = 10.5
    m_c = 5
    n = int(banyak_job_entry.get())
    M = 100000000
    job = []
    lanjut = True
    check_dict = entry_box_manager.get_check_box_values()
    

    all_checked = True

    for key, values in check_dict.items():
        for value in values:
            if value != 'Checked':
                all_checked = False
                break  # Exit the inner loop if an unchecked value is found
        if not all_checked:
            break  # Exit the outer loop if an unchecked value is found

    if not all_checked:
        # Display notification (using messagebox from tkinter)
        from tkinter import messagebox
        print ("Connection Terminated: Parameter Tangki Belum Terverifikasi")
        messagebox.showwarning("Perhatian!", "Mohon Cek Kondisi Semua Tangki Terlebih Dahulu!")
        lanjut = False


    if (lanjut):
        check_dict = entry_box_manager.get_check_box_values()


        job_dict = entry_box_manager.get_entry_box_values()

        for key, value in job_dict.items():
    # If the value is 'Checked', print the first element of the key (the row number)
            if value == 'Checked':
                job.append(key[1])
        
        #Bikin Dict buat seluruh min processing time, travel time, dan max processing time
        a = {0:[0,150,75,60,0,0], 1:[0,150,75,0,0,0], 2:[0,150,75,30,7.5,0], 3:[0,150,75,60,0,615], 4:[0,150,75,60,0,0]} #Min prosesing time
        b = {0:[0,225,90,90,0,0], 1:[0,225,75,0,0,0], 2:[0,225,90,75,45,0], 3:[0,225,90,150,0,825], 4:[0,225,90,150,0,0]} #Maks prosesing time
        d = {0:[68.5,66.5,66.5,0,0,76.5], 1:[68.5,66.5,0,0,0,72.5], 2:[68.5,66.5,66.5,66.5,0,80.5], 3:[68.5,66.5,66.5,0,69,84.5], 4:[68.5,66.5,66.5,0,0,76.5]} #Loaded Move
        routing = {0: [1,2,3], 1:[1,2], 2:[1,2,3,4], 3:[1,2,3,5], 4:[1,2,3]}
        c = {1: {
              0: [0, 8.5, 12.5, 16.5, 20.5, 24.5, 0], 
              1: [8.5, 0, 6.5, 9, 11.5, 14, 8.5], 
              2: [12.5, 6.5, 0, 6.5, 9, 11.5, 12.5], 
              3: [16.5, 9, 6.5, 0, 6.5, 9, 16.5], 
              4: [20.5, 11.5, 9, 6.5, 0, 6.5, 20.5], 
              5: [24.5, 14, 11.5, 9, 6.5, 0, 24.5], 
              6: [0, 6.5, 9.5, 15.5, 18.5, 21.5, 0]}, 
            2: {
              0: [0, 8.5, 12.5, 16.5, 20.5, 24.5, 0], 
              1: [8.5, 0, 6.5, 9, 11.5, 14, 8.5], 
              2: [12.5, 6.5, 0, 6.5, 9, 11.5, 12.5], 
              3: [16.5, 9, 6.5, 0, 6.5, 9, 16.5], 
              4: [20.5, 11.5, 9, 6.5, 0, 6.5, 20.5], 
              5: [24.5, 14, 11.5, 9, 6.5, 0, 24.5], 
              6: [0, 8.5, 12.5, 16.5, 20.5, 24.5, 0]}}
        
        dv = pulp.LpVariable.dicts("ending_time", ((r,i) for r in range (1,n+1) for i in range (m_c+1)), lowBound=0, cat='Continuous') #S ri
        bv = pulp.LpVariable.dicts("Binary_var", ((r,i,u,j) for r in range (1,n+1) for i in range (m_c+1) for u in range (1,n+1) for j in range (m_c+1)), lowBound=0, cat='Binary')

        Cmax = pulp.LpVariable('Cmax', lowBound=0, cat='Continuous')
        model = pulp.LpProblem("MIN_Makespan", pulp.LpMinimize)
        model += Cmax

        #Konstrain 1 Fungsi Objektif
        for r in range (1, n+1):
            model += (Cmax >= dv[r,m_c] + d[job[r-1]][m_c])

        #Konstrain 2 (Prosesing time low bound)
        for r in range (1, n+1):
            for i in range (1, m_c+1):
                model += (dv[r,i] - dv[r,i-1] - d[job[r-1]][i-1] >= a[job[r-1]][i])

        #Konstrain 2 (Prosesing time high bound)
        for r in range (1, n+1):
            for i in range (1, m_c+1):
                model += (dv[r,i] - dv[r,i-1] - d[job[r-1]][i-1] <= b[job[r-1]][i])

        #Konstrain 3 (Movement Hoist Constrain)
        for r in range (1, n+1):
            for u in range (1, n+1):
                for i in range (m_c+1): #Tangki job 1
                    for j in range (m_c+1): #Tangki job 2
                        if (i == j or r == u):
                            continue
                        else:
                            model += (dv[u,j] - dv[r,i] >= d[job[r-1]][i] + c[r][i+1][j] - (M*(1-bv[r,i,u,j])))

        #Konstrain 4 (Binary check)
        for r in range (1, n+1):
            for u in range (1, n+1):
                for i in range (m_c+1):
                    for j in range (m_c+1):
                        if (i==j or r==u):
                            continue
                        else:
                            model += (bv[r,i,u,j] + bv[u,j,r,i] == 1)

        #Konstrain 5 (Tank Constrain)
        for r in range (1, n+1):
            for u in range (r+1, n+1):
                for i in range (1,m_c+1):
                    for j in range (1,m_c+1):
                        if (R_1[i] == R_2[j]):
                            model += (bv[r,i,u,j-1] + bv[u,j,r,i-1] == 1)
                        else:
                            continue

        #Konstrain 6 (Routing constrain)
        for r in range (1, n+1):
            for i in range (m_c+1):
                for j in range (i+1, m_c+1):
                    model += (bv[r,i,r,j] == 1)

        model.solve()
        pulp.LpStatus[model.status]

        df=[]
        kirim = {}

        for var in dv:
            var_value = dv[var].varValue
            #print ( var[0], "-", var[1], var_value)
            kirim[(var[0], var[1])] = var_value


        ''' Persiapan Data Untuk Dikirim ke PLC'''
        seen_values = set()
        unique_data = {}

        for key, value in kirim.items():
            if value not in seen_values:
                seen_values.add(value)
                unique_data[key] = value
        
        sorted_data = dict(sorted(unique_data.items(), key=lambda x: x[1]))
        print (sorted_data)
        # Output 1: Urutan Kerja
        Urutan_Kerja = [key[0] for key in sorted_data.keys()]

        # Output 2: Timing Routing Job 1
        Timing_Job_1 = [value for key, value in sorted_data.items() if key[0] == 1]
        if (Timing_Job_1[0] == 0):
            Timing_Job_1 = [x if i == 0 else x - 10 for i, x in enumerate(Timing_Job_1)]
            Timing_Job_1 = [x if i == 0 or i == 1 else (x - 25 if i == 2 else x - (50+25*(i-3))) for i, x in enumerate(Timing_Job_1)]
            Timing_Job_1 = [x if i == 0 else x - 15*i - 13 for i, x in enumerate(Timing_Job_1)]
        else:
            Timing_Job_1 = [x - 15*i - 13 - 50 - 25*i for i, x in enumerate(Timing_Job_1)]

        # Output 3: Timing Routing Job 2
        Timing_Job_2 = [value for key, value in sorted_data.items() if key[0] == 2]
        if (len(Timing_Job_2) != 0):
            if (Timing_Job_2[0] == 0):
                Timing_Job_2 = [x if i == 0 else x - 10 for i, x in enumerate(Timing_Job_2)]
                Timing_Job_2 = [x if i == 0 or i == 1 else (x - 25 if i == 2 else x - (50+25*(i-3))) for i, x in enumerate(Timing_Job_2)]
                Timing_Job_2 = [x if i == 0 else x - 15*i - 13 for i, x in enumerate(Timing_Job_2)]
            else:
                Timing_Job_2 = [x - 15*i - 13 - 50 - 25*i for i, x in enumerate(Timing_Job_2)]

        # Output 4: Routing Job 1
        Routing_Job_1 = routing[job[0]]
        Routing_Job_1 = [x + 3 for x in Routing_Job_1] + [3]

        # Output 5: Routing Job 2
        if (len(Timing_Job_2) != 0):
            Routing_Job_2 = routing[job[1]]
            Routing_Job_2 = [x + 3 for x in Routing_Job_2] + [2]

        '''----------------------- KIRIM DATA KE PLC -----------------------'''
        
        tracemalloc.start()
        start_time_1 = time.time()
        plc = snap7.client.Client()
        plc.connect('192.168.0.1', rack=0, slot=1)

        offset_urutan_kerja = 0
        offset_timing_job_1 = 44
        offset_timing_job_2 = 56
        offset_routing_job_1 = 24
        offset_routing_job_2 = 34

        #1. Kirim Urutan Kerja
        for i in range (len(Urutan_Kerja)):
            data = bytearray(2)
            set_int(data, 0, Urutan_Kerja[i])            
            plc.db_write(8,offset_urutan_kerja,data)
            offset_urutan_kerja += 2

        #2. Kirim Timing Routing Job 1
        for i in range (len(Timing_Job_1)):
            data = bytearray(2)
            set_int(data, 0, Timing_Job_1[i])            
            plc.db_write(8,offset_timing_job_1,data)
            offset_timing_job_1 += 2

        #3. Kirim Timing Routing Job 2
        for i in range (len(Timing_Job_2)):
            data = bytearray(2)
            set_int(data, 0, Timing_Job_2[i])            
            plc.db_write(8,offset_timing_job_2,data)
            offset_timing_job_2 += 2

        #4. Kirim Routing Job 1
        for i in range (len(Routing_Job_1)):
            data = bytearray(2)
            set_int(data, 0, Routing_Job_1[i])            
            plc.db_write(8,offset_routing_job_1,data)
            offset_routing_job_1 += 2

        #5. Kirim Timing Routing Job 2
        for i in range (len(Routing_Job_2)):
            data = bytearray(2)
            set_int(data, 0, Routing_Job_2[i])            
            plc.db_write(8,offset_routing_job_2,data)
            offset_routing_job_2 += 2

        #6. Kirim Boolean Mulai
        data = bytearray(1)
        set_bool(data,0,0,True)
        plc.db_write(8,78,data)

        #7. Kirim Panjang Array Urutan Kerja
        data = bytearray(2)
        set_int(data,0,len(Urutan_Kerja))
        plc.db_write(8,72,data)

        plc.disconnect()

        end_time_1 = time.time()
        current, peak = tracemalloc.get_traced_memory()

        tracemalloc.stop()
        print(f"Time taken: {end_time_1 - start_time_1} seconds")
        print(f"Current memory usage: {current / 10**6} MB")
        print(f"Peak memory usage: {peak / 10**6} MB")
        
        '''----------------------- KIRIM DATA KE PLC -----------------------'''
        
        print("Urutan Kerja:", Urutan_Kerja)
        print("Timing Job 1:", Timing_Job_1)
        print("Timing Job 2:", Timing_Job_2)
        print("Routing Job 1:", Routing_Job_1)
        if (len(Timing_Job_2) != 0):
            print("Routing Job 2:", Routing_Job_2)

        #print (kirim)
        total_cost = pulp.value(model.objective)
        max_1 = max(Timing_Job_1)
        max_2 = 0
        if (len(Timing_Job_2) != 0):
            max_2 = max(Timing_Job_2)
        print_max = max(max_1,max_2)
        print ("C_Max: ", print_max)
        #print (pulp.LpStatus[model.status])
        j_record = {}
        lama_record = {}
        lama_tangki = {}
        
        
        for i in range (1, len(job)+1):
            k = 0
            l = 0
            p_1 = 1
            m_keys = routing[job[i-1]]
            list_lama_tangki = []
            
            #print (m_keys)

            if (dv[i,0].varValue == 0):
                dummy_start = dv[i,0].varValue
            else:
                dummy_start = dv[i,0].varValue
            for var in m_keys:
                var_value = dv[i,var].varValue - 15*l
                print (var_value)
                end_time = str(timedelta(seconds=var_value))
                dummy = d[job[i-1]][var-1] + dummy_start - 15*k
                print (dummy)
                print ("-----")
                start_time = str(timedelta(seconds= dummy))
                dummy_start = var_value
                j_record[(var,i)] =[start_time, end_time]
                lama_record[(var,i)] = [dummy, var_value]
                l += 1
                k = 1
                p_1 += 1

            today = date.today().strftime('%Y-%m-%d')

            for m in m_keys:
                df.append(dict(Task='Tangki %s'%(list_tangki[m-1]), Start='%s %s' % (today, str(j_record[(m,i)][0])), Finish='%s %s' % (today, str(j_record[(m,i)][1])),Resource='Job %s'%(job_list[job[i-1]])))
                dummy_lama = lama_record[(m,i)][1]-lama_record[(m,i)][0]
                list_lama_tangki.append(dummy_lama)
            
            lama_tangki[i-1] = list_lama_tangki

        fig = ff.create_gantt(df, index_col='Resource', show_colorbar=True, group_tasks=True, showgrid_x=True, title='Surface Treatment Schedule')
        plot(fig, filename='Surface_Treatment_Scheduling')

        prompt = f"Pekerjaan Anda Akan Selesai Pada Detik Ke: {total_cost}"
        prompt_label = tkinter.Label(Final_Frame, text=prompt)
        prompt_label.grid(row=0, column=0)

        for widget in Final_Frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)
        
        for i in range (len(job)):
            a = 1
            prompt_proses = f"Job: {job_list[job[i]]}"
            prompt_proses_label = tkinter.Label(Proses_Frame, text=prompt_proses)
            prompt_proses_label.grid(row=0, column=i)
            for m in lama_tangki[i]:
                dummy_prompt = routing[job[i]][a-1]
                prompt_lama = f"{list_tangki[dummy_prompt-1]} { m} Detik"
                prompt_lama_label = tkinter.Label(Proses_Frame, text=prompt_lama)
                prompt_lama_label.grid(row = a, column=i)
                a += 1
