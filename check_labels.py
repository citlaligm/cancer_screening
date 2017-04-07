import glob
import csv

image_names = []
file_name = "fixed_labels_v2.csv"
clean_output_file = "clean_log_train_3.csv"
type_image= "3"
#image_path = "train/Type_"+type_image+"/*.jpg"
image_path = "test/*.jpg"
#print(image_path)
for image in glob.glob(image_path):	
	image_name = image.split('/')[-1]
	image_names.append(image_name)
#print(image_names)


with open(file_name,'r') as file:
    datareader = csv.reader(file,delimiter=',')
    label_log = []
    #global type_image
    for row in datareader:
        image_name = row[0]
        type_img = row[2].split('_')[-1]
        #print(type_img)
        if type_img== type_image:
            #print(image_name)
            label_log.append(image_name)

#print(label_log)

image_found = []
image_not_found = []
for image_name in label_log :
    if image_name in image_names:
        image_found.append(image_name)
        
    else:
        image_not_found.append(image_name)
        

print("Images not found:", len(image_not_found))
print("Example image found:", len(image_found))

#print("Images found:", len(image_found))
# print(len(image_found), len(image_not_found), len(image_names), len(label_log))

with open(file_name,'r') as file, open (clean_output_file, 'w') as outfile:
    datareader = csv.reader(file,delimiter=',')
    datawriter = csv.writer(outfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    label_log = []
    for row in datareader:
        image_name = row[0].split('\\')[-1]
        print(image_name)
        if image_name in image_found:
              datawriter.writerow(row)
                
        # else:
        #     print('skip', image_name)