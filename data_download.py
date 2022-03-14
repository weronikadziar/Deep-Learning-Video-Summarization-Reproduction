# Reading an excel file using Python
import csv
 
######### Hi Krzysztof and Daniel, here's what you should do ##########
# Change the titles path to your local path of the:
# - video_name_train.csv file for TRAINIG data
# - video_name_test.csv file for TESTING data
# - video_name_val.csv file for VALIDATION data
# And that's it! The code will save a text file called set_urls.txt
urls = open(r"dataset\videos\query_videoURLs.csv","r", encoding="Latin-1")
titles = open(r"dataset\videos\video_name_test.csv","r", encoding="Latin-1")

urls_read = csv.reader(urls)
urls_list = []
all_titles_list = []
for row in urls_read:
    print('*' * 30)
    print(row[0])
    print(row[1])
    print('*' * 30)
    urls_list.append(row[1])
    all_titles_list.append(row[0])

urls_list = urls_list[1:]
all_titles_list = all_titles_list[1:]

titles_read = csv.reader(titles)
titles_list = []
for row in titles_read:
    titles_list.append(row[0])
    
titles_list = titles_list[1:]

set_urls = []
for i in range(190):
    if all_titles_list[i] in titles_list:
        set_urls.append(urls_list[i])
        
set_urls_txt = open("set_urls.txt", "w")
for element in set_urls:
    set_urls_txt.write(element + "\n")
set_urls_txt.close()

