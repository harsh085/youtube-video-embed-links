from selenium import webdriver

import pyautogui as p,time




def ex(k):
    roll=w.find_element_by_id("youtube-url")    
    roll.clear()
    roll.send_keys(k)
    time.sleep(2)
    w.execute_script('createYouTubeEmbed();')
    l = w.find_element_by_tag_name("textarea").text
    return(l)
           
        
w = webdriver.Chrome(executable_path='chromedriver.exe')
#w.maximize_window()
plink=p.prompt("Enter playlist link: ")
w.get(plink)
h = []
elems = w.find_elements_by_xpath("//a[@id='thumbnail' and @href]")
for elem in elems:
    h.append(elem.get_attribute("href"))
  
file2 = open("MyFile1.txt","w")  

w.get("http://embedresponsively.com/")

"""
roll=w.find_element_by_id("youtube-url")    
roll.clear()
roll.send_keys(h[0])
time.sleep(10)
"""

for i in range(1,len(h)):
    l = ex(h[i])
    file2.write(" \" ")
    file2.write(str(i))
    file2.write(" \" => \" ")
    file2.write(l)
    file2.write(" \", ")
    file2.write("\n\n")


file2.close()

w.close()
