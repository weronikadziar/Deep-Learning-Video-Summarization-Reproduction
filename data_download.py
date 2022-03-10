# Reading an excel file using Python
import csv
 
# Give the location of the file
urls = open(r"C:\Users\Weronika\Documents\GitHub\DL_Reproducibility_Project\dataset\videos\query_videoURLs.csv","r", encoding="Latin-1")
titles_train = open(r"C:\Users\Weronika\Documents\GitHub\DL_Reproducibility_Project\dataset\videos\video_name_train.csv","r", encoding="Latin-1")

urls_read = csv.reader(urls)
urls_list = []
all_titles_list = []
for row in urls_read:
    urls_list.append(row[1])
    all_titles_list.append(row[0])

urls_list = urls_list[1:]
all_titles_list = all_titles_list[1:]

titles_train_read = csv.reader(titles_train)
titles_train_list = []
for row in titles_train_read:
    titles_train_list.append(row[0])
    
titles_train_list = titles_train_list[1:]

train_urls = []
for i in range(190):
    if all_titles_list[i] in titles_train_list:
        train_urls.append(urls_list[i])

practice_urls = train_urls[:2]        
practice_txt = open("practice.txt", "w")
for element in practice_urls:
    practice_txt.write(element + "\n")
practice_txt.close()
        
train_urls_txt = open("train_urls.txt", "w")
for element in train_urls:
    train_urls_txt.write(element + "\n")
train_urls_txt.close()

