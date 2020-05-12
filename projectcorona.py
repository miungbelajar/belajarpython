#belajar kelas python
import requests
from bs4 import BeautifulSoup
country=input("MASUKAN NAMA NEGARA:")
url="https://www.worldometers.info/coronavirus/country/{}/".format(country)
r=requests.get(url)
s=BeautifulSoup(r.text,"html.parser")
data=s.find_all("div",class_="maincounter-number")
print("""
             *     ,MMM8&&&.            *
                  MMMM88&&&&&    .
                 MMMM88&&&&&&&
     *           MMM88&&&&&&&&
                 MMM88&&&&&&&&
                 'MMM88&&&&&&'
                   'MMM8&&&'      *    
           /\/|_      __/\\
          /    -\    /-   ~\  .              '
          \    = Y =T_ =   /
           )==*(`     `) ~ \
          /     \     /     \
          |     |     ) ~   (
         /       \   /     ~ \
         \       /   \~     ~/
  _/\_/\__ _/_/\_/\__~__/_/\_/\_/\_/\_/\__/\_
  |  |  |  | ) ) |  |  | ((  |  |  |  |  |  |
  |  |  |  |( (  |  |  |  \\ |  |  |  |  |  |
  |  |  |  | )_) |  |  |  |))|  |  |  |  |  |
  |  |  |  |  |  |  |  |  (/ |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  """)
print("JUMLAH KASUS : ",data[0].text.strip())
print("JUMLAH KEMATIAN : ",data[1].text.strip())
print("JUMLAH KESEMBUHAN : ",data[2].text.strip())
print("""
----------------------------------------SELALU JAGA KEBSEHATAN DAN KEBERSIHAN HOOMAN----------------------------------------
              
                      \`*-.                    
                       )  _`-.                 
                      .  : `. .                
                      : _   '  \               
                      ; *` _.   `*-._          
                      `-.-'          `-.       
                        ;       `       `.     
                        :.       .        \    
                        . \  .   :   .-'   .   
                        '  `+.;  ;  '      :   
                        :  '  |    ;       ;-. 
                        ; '   : :`-:     _.`* ;
               		 .*' /  .*' ; .*`- +'  `*' 
                  	`*-*   `*-*  `*-*'     
----------TETAP TINGGAL DIRUMAH BIAR MIUNG YANG KELUAR MALAM MINGGUAN----------
""")
