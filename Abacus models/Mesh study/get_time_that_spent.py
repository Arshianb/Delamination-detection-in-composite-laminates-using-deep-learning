import glob

for i in glob.glob("C:\\Users\\795593\\OneDrive\\Desktop\\Delamination-detection-in-composite-laminates-using-deep-learning\\Abacus models\\Mesh study/*"):
    if ".log" in i:
        # print(i)
        num_job = int(i[i.find("Job-")+len("Job-"):i.find(".log")])
        # print("num_job = ", num_job)
        with open(i, "r") as txt_file:
            # print(txt_file)
            whole = []
            for row in txt_file:
                whole.append(row)
            for index in range(len(whole)):
                if "Begin Analysis Input File Processor" in whole[index]:
                    text = whole[index+1].split(" ")
                    begin = text[1]
                    begin = begin.split(":")
                    begin = int(begin[1])*60 + int(begin[2])
                if "Run SMASimUtility.exe" in whole[index]:
                    text = whole[index+1].split(" ")
                    end = text[1]
                    end = end.split(":")
                    end = int(end[1])*60 + int(end[2])
            whole_time = end-begin
            print(whole_time)
        # exit()