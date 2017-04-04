import glob
import csv

image_names = []
file_name = "fixed_labels_v2.csv"
type_= "1"
image_path = "train/Type_"+type_+"/*"

for image in glob.glob(image_path):	
	image_name = image.split('/')[-1]
	image_names.append(image_name)
#print(image_names)


with open(file_name,'r') as file:
    datareader = csv.reader(file,delimiter=',')
    label_log = []
    for row in datareader:
        image_name = row[0].split('\\')[-1]
        label_log.append(image_name)

#print(image_name)

image_found = []
image_not_found = []
for image_name in label_log :
    if image_name in image_names:
        image_found.append(image_name)
        
    else:
        image_not_found.append(image_name)
        
print("Images not found:", len(image_not_found))
print("Images found:", len(image_found))


# #print(len(image_found), len(image_not_found), len(image_names))

# with open('label_log.csv','r') as file, open ('clean_log.csv', 'w', newline='') as outfile:
#     datareader = csv.reader(file,delimiter=',')
#     datawriter = csv.writer(outfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     label_log = []
#     for row in datareader:
#         image_name = row[0].split('\\')[-1]
#         image_name = image_name.split('.')[0]
#         if image_name not in image_not_found:
#               datawriter.writerow(row)
                
#         else:
#             print('skip', image_name)