import arcpy
arcpy.env.workspace = r"E:\College\Web GIS\CodeFiles-\GDB_example\GEOG391_CampusMap.gdb"                        #need to change file path for diffrent computers becauses of the diffrent file structure
Dataset_routes = arcpy.ListDatasets("R*")

Route_L=[]


for route in Dataset_routes:
	arcpy.env.workspace = r"E:\College\Web GIS\CodeFiles-\GDB_example\GEOG391_CampusMap.gdb"+"\\"+route         #need to change file path for diffrent computers becauses of the diffrent file structure
	sub_route = arcpy.ListFeatureClasses("r*")
	for R in sub_route:
		Route_L.append(R)

print(Dataset_routes[1])
Name_file="Merge_route"

Num_routes=len(Route_L)
Num_R= Num_routes/6

count=0

num1=0
num2=1
num3=2
num4=3
num5=4
num6=5		

MList=['115', '114', '113', '112', '111', '102', '121', '123', '125', '124', '120', '122', '119', '118', '110', '103', '104', '136B', '136', '136A', '129B', '133', '129', '129A', '131', '126', '126A', '128', '127', '130', '132', '105', '137', '139', '140', '140A', '143', '144', '146', '147', '100', '106', '106A', '116', '109', '108', '107', '148B', '149', '148', '148C', '145', '148A', '138', '142', '141', '135', '255', '256', '258', '259', '262', '266', '267', '268', '269', '270', '272', '273', '275', '276', '278', '280', '202', '204', '205', '211', '212', '215', '217', '218', '219', '220', '222', '224', '228', '229', '230', '231', '232', '234', '235', '236', '237', '233', '238', '239', '240', '241', '242', '226', '223', '221', '216', '213', '210', '206', '203', '281', '279', '277', '274', '271', '265', '264', '263', '207', '208', '209', '214', '246', '247', '250', '252', '254', '257', '251', '251A', '248', '249', '253', '254', '260', '1', '2', '3', '201A', '227', '360', '362', '364', '367', '368', '376', '377', '378', '379', '380', '381', '383', '384', '386', '387', '390', '391', '302', '304', '305', '311', '312', '314', '316', '317', '318', '319', '321', '322', '330', '332', '335', '337', '338', '339', '336', '334', '333', '331', '329', '323', '324', '320', '315', '313', '310', '306', '303', '392', '389', '388', '385', '382', '375', '374', '373', '372', '393', '370', '371', '1', '2', '3', '309', '307', '308', '326', '325', '327', '348', '349', '347', '334', '340', '341', '342', '343', '345', '346', '301A', '352', '354', '356', '357', '358', '359', '361', '363', '355', '365', '353', '366', '455', '457', '459', '460', '468', '465', '469', '470', '471', '472', '473', '475', '477', '478', '480', '482', '483', '402', '404', '405', '411', '412', '414', '416', '417', '418', '419', '421', '422', '431', '434', '436', '438', '440', '441', '439', '437', '435', '432', '423', '420', '415', '413', '410', '406', '403', '481', '479', '476', '474', '468', '467', '466', '484', '1', '2', '3', '407', '408', '409', '426', '427', '428', '425', '424', '449', '448', '447', '446', '444', '443', '442', '445', '462', '461', '458', '456', '454', '453', '464', '401', '543', '545', '547', '550', '551', '552', '560', '561', '562', '563', '564', '565', '566', '559', '558', '557', '556', '555', '554', '553', '502', '503', '505', '510', '511', '513', '515', '520', '522', '524', '526', '527', '525', '523', '521', '519', '517', '516', '514', '512', '506', '504', '502', '508', '507', '509', '3', '2', '1', '534', '533', '531', '529', '528', '530', '532', '549', '548', '546', '537', '544', '542', '541', '539', '540', '538', '536', '535', '518']

while Num_R > count:
	Save_file="E:\College\Web GIS\CodeFiles-\GDB_example\GEOG391_CampusMap.gdb\{}".format("Merge_route"+str(count))                 #need to change file path for diffrent computers becauses of the diffrent file structure
	
	file='E:\\College\\Web GIS\\CodeFiles-\\GDB_example\\GEOG391_CampusMap.gdb\\{}\\{}'.format(Dataset_routes[num1],Route_L[num1])    #need to change file path for diffrent computers becauses of the diffrent file structure
	file1='E:\\College\\Web GIS\\CodeFiles-\\GDB_example\\GEOG391_CampusMap.gdb\\{}\\{}'.format(Dataset_routes[num2],Route_L[num2])    #need to change file path for diffrent computers becauses of the diffrent file structure
	file2='E:\\College\\Web GIS\\CodeFiles-\\GDB_example\\GEOG391_CampusMap.gdb\\{}\\{}'.format(Dataset_routes[num3],Route_L[num3])     #need to change file path for diffrent computers becauses of the diffrent file structure
	file3='E:\\College\\Web GIS\\CodeFiles-\\GDB_example\\GEOG391_CampusMap.gdb\\{}\\{}'.format(Dataset_routes[num4],Route_L[num4])      #need to change file path for diffrent computers becauses of the diffrent file structure
	file4='E:\\College\\Web GIS\\CodeFiles-\\GDB_example\\GEOG391_CampusMap.gdb\\{}\\{}'.format(Dataset_routes[num5],Route_L[num5])       #need to change file path for diffrent computers becauses of the diffrent file structure
	file5='E:\\College\\Web GIS\\CodeFiles-\\GDB_example\\GEOG391_CampusMap.gdb\\{}\\{}'.format(Dataset_routes[num6],Route_L[num6])        #need to change file path for diffrent computers becauses of the diffrent file structure
	
	arcpy.Merge_management([file,file1,file2,file3,file4,file5],Save_file)		
	count+=1
	
	num1+=6
	num2+=6
	num3+=6
	num4+=6
	num5+=6
	num6+=6
	
	
#MList=['115', '114', '113', '112', '111', '102', '121', '123', '125', '124', '120', '122', '119', '118', '110', '103', '104', '136B', '136', '136A', '129B', '133', '129', '129A', '131', '126', '126A', '128', '127', '130', '132', '105', '137', '139', '140', '140A', '143', '144', '146', '147', '100', '106', '106A', '116', '109', '108', '107', '148B', '149', '148', '148C', '145', '148A', '138', '142', '141', '135', '255', '256', '258', '259', '262', '266', '267', '268', '269', '270', '272', '273', '275', '276', '278', '280', '202', '204', '205', '211', '212', '215', '217', '218', '219', '220', '222', '224', '228', '229', '230', '231', '232', '234', '235', '236', '237', '233', '238', '239', '240', '241', '242', '226', '223', '221', '216', '213', '210', '206', '203', '281', '279', '277', '274', '271', '265', '264', '263', '207', '208', '209', '214', '246', '247', '250', '252', '254', '257', '251', '251A', '248', '249', '253', '254', '260', '1', '2', '3', '201A', '227', '360', '362', '364', '367', '368', '376', '377', '378', '379', '380', '381', '383', '384', '386', '387', '390', '391', '302', '304', '305', '311', '312', '314', '316', '317', '318', '319', '321', '322', '330', '332', '335', '337', '338', '339', '336', '334', '333', '331', '329', '323', '324', '320', '315', '313', '310', '306', '303', '392', '389', '388', '385', '382', '375', '374', '373', '372', '393', '370', '371', '1', '2', '3', '309', '307', '308', '326', '325', '327', '348', '349', '347', '334', '340', '341', '342', '343', '345', '346', '301A', '352', '354', '356', '357', '358', '359', '361', '363', '355', '365', '353', '366', '455', '457', '459', '460', '468', '465', '469', '470', '471', '472', '473', '475', '477', '478', '480', '482', '483', '402', '404', '405', '411', '412', '414', '416', '417', '418', '419', '421', '422', '431', '434', '436', '438', '440', '441', '439', '437', '435', '432', '423', '420', '415', '413', '410', '406', '403', '481', '479', '476', '474', '468', '467', '466', '484', '1', '2', '3', '407', '408', '409', '426', '427', '428', '425', '424', '449', '448', '447', '446', '444', '443', '442', '445', '462', '461', '458', '456', '454', '453', '464', '401', '543', '545', '547', '550', '551', '552', '560', '561', '562', '563', '564', '565', '566', '559', '558', '557', '556', '555', '554', '553', '502', '503', '505', '510', '511', '513', '515', '520', '522', '524', '526', '527', '525', '523', '521', '519', '517', '516', '514', '512', '506', '504', '502', '508', '507', '509', '3', '2', '1', '534', '533', '531', '529', '528', '530', '532', '549', '548', '546', '537', '544', '542', '541', '539', '540', '538', '536', '535', '518']