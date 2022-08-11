import glob
import csv
# mesh_Class = []
whole_freq = []
for i in glob.glob("C:\\Users\\795593\\OneDrive\\Desktop\\Delamination-detection-in-composite-laminates-using-deep-learning\\Abacus models\\Mesh study/*"):
    if ".dat" in i:
        # print(i)
        num_job = int(i[i.find("Job-")+len("Job-"):i.find(".dat")])
        # print("num_job = ", num_job)
        with open(i, "r") as txt_file:
            show = False
            freqs = []
            freqs.append(num_job)
            for row in txt_file:
                if "E I G E N V A L U E    O U T P U T" in row:
                    show = True
                if " P A R T I C I P A T I O N   F A C T O R S" in row:
                    show = False
                if show:
                    # print(row)
                    row = row.split("         ")
                    # print(row)
                    index = -1
                    for col in row:
                        index+=1
                        if col == "1.0000":
                            # print(row[index-1])
                            freqs.append(float(row[index-1]))
            whole_freq.append(freqs)
            # print(len(freqs))
index = -1
for i in whole_freq:
    index+=1
    last_list = i
    with open('protagonist.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(last_list)