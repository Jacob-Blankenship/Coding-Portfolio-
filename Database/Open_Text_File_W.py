import os , pyodbc

files = os.listdir("E:\College\Geodatabases_project\ASCII and SED files")
print(files)
for filename in files:                             #going through each file in the flolder given from above
    if filename.endswith(".sed"):
        MList = []                                 # master list for everything
        file = open("E:\College\Geodatabases_project\ASCII and SED files\{}".format(filename),"r")# opening the file up
        row = file.readlines()                     # reading text row by row

        for i in row:
            Clean1 = i.strip()                     # taking away the \n
            for words in Clean1.split("\t"):       # taking away the \t
                F = words.strip()                  # taking away white space in the strings
                MList.append(F)                    # putting it into a master List Note: has 3154 items in it


        print("Clean Data")


        Date_Scan = []                             # Date_Scan list for date and scan numb

        Data = []                                  # Data for the information Wvl Rad. (Ref.) Rad. (Target) Reflect
        count=0
        while count < 3154:                        # Note MList has 3154 items in it
            if count == 0:                         # index 0 is scan number
                Date_Scan.append(MList[count])
            elif count == 6:                       # index 6 is Date
                Date_Scan.append(MList[count])
            elif count >= 30:                      # index 30 and on are the Wvl, Rad.(Ref.), Rad.(Target), Reflect
                Data.append(MList[count])
            count += 1

        print("Data List Made")


        Cdate = Date_Scan[0][22:26:1]
        Cscan = Date_Scan[1][6:16:1]
        Scan_ID = Cdate + "_" + Cscan              # putting the scan and date together

        print("Scan_ID Made: {}".format(Scan_ID))


        num = 0
        num_1= 1
        num1 = 0
        num2 = 1
        num3 = 2
        num4 = 3
        Wvl_ID = []
        Wvl = []
        Rad_ref = []
        Rad_target = []
        Reflect = []
        Masterl = []

        while num < 781:                           # 3124 total amount items in Data the 3124/4 to get 781 because we are going up by 4
            Wvl.append(Data[num1])                 # Taking the Data list and making 4 list out of it Wvl,Rad_ref,Rad_Target,Reflect
            Rad_ref.append(Data[num2])
            Rad_target.append(Data[num3])
            Reflect.append(Data[num4])
            Wvl_ID.append((num_1))
            num += 1
            num_1 += 1
            num1 += 4
            num2 += 4
            num3 += 4
            num4 += 4

        print("Four Data lists Made")



        N1 = 0
        while N1 < 781:
            Masterl.append([Scan_ID,Wvl[N1],Rad_ref[N1],Rad_target[N1],Reflect[N1]])  # making a master list with the data in order Scan_ID,Wvl,Rad_ref,Rad_Target,Reflect
            N1 += 1


        curpath = os.path.abspath(os.curdir)
        output = 'E:\College\Geodatabases_project\Text_file\Scan_ID_{}.txt'.format(Scan_ID)  # this creates a new text file name for each scan
        output = output.replace('/', '')


        file_object = open(output,'w') # this creates the text file for each scan
        for value in Masterl:
            file_object.write(str(value[0])+","+str(value[1])+","+str(value[2])+","+str(value[3])+","+str(value[4])+'\n')  # putting it into a txt file in the order I want
        file_object.close()

        print("Finshed with Scan_ID_{}.txt\n".format(Scan_ID))

print("-----------------------------------------------")
print("Starting to combine all the Text Files Together")
print("-----------------------------------------------")

Folder = r"E:\College\Geodatabases_project\Text_file"               # Location of all the formated text file made
Text_Files = os.listdir(Folder)
Location = r"E:\College\Geodatabases_project\Master_Text_File.txt"
Location = Location.replace('/', '')

Master_Text_File = open(Location,'w')                              # Making the Master_Text_File

for File in Text_Files:                                            # Running through all the formated text file
    with open(Folder + "\\" + File,'r') as infile:                 # Reading one file
        for line1 in infile:
            Master_Text_File.write(line1)                          # In putting each line into the Master_Text_File
Master_Text_File.close()

Master_Text_File = open(Location,'r') #reading the Master_Text_File
row = Master_Text_File.read()

All_lines = row.split("\n")                                        # makeing a list of the file to be inputed into the databases

Master2 = []                                                       # List to be used to input it into the databases
for i in All_lines:                                                # Running through each row and makeing it a list
    i = i.strip()
    s_list = i.split(",")
    Master2.append(s_list)
#this deletes the last list that is emtpy in the file created by the last \n charter in the last Text Files inputed
del Master2[-1]

print("----------------------------------")
print("Connecting to the Databases Server")
print("----------------------------------")

print(" ")
#information for acces into the Server for the database
cnxn = pyodbc.connect("DRIVER={SQL Server};server=GEOG-VS-2653.geonet.tamu.edu;database=Test_code;uid=Jeremy;pwd=password")
cursor = cnxn.cursor()
print("-------------------")
print("Connected to Server")
print("-------------------")

print(" ")

print("--------------------")
print("About to insert data")
print("--------------------")
Count = 1
print(Master2)
for value in Master2:    # Running through the list for each list of rows
    Count += 1
    print("Inserting line {}".format(Count))
    # This is the table name,1 column name,2 column name,3 column name,4 column name,5 column name and the values to be inputed
    SQLCommand = "INSERT INTO [dbo].[Scan_WL] ([ScanID], [Wavelength], [RadRef], [RadTarget], [Reflectance]) VALUES (?, ?, ?, ?, ?)"
    #The values to be inputed into the databases bases off on the index of the list per row/line of the Master_Text_File
    Values = [str(value[0]), str(value[1]), str(value[2]), str(value[3]), float(value[4])]
    cursor.execute(SQLCommand,Values)

cnxn.commit()
cnxn.close()

print("-------------------------------")
print("Finished: Go check the Database")
print("-------------------------------")
