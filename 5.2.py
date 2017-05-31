import urllib.request
import xml.etree.ElementTree as etree
from tkinter import *

def mmain():

    #서울공공데이터사용

    url = "http://openAPI.seoul.go.kr:8088/614d58696f7967303734694c686269/xml/PublicWiFiPlaceInfo/1/603/"



    data = urllib.request.urlopen(url).read()

    filename = "sample2.xml"
    f = open(filename, "wb") #다른 사람들의 예제처럼 "w"만 해서 했더니 에러가 발생
    f.write(data)
    f.close()

    #파싱하기
    tree = etree.parse(filename)
    root = tree.getroot()

    win = Tk()



    www = Canvas(win, width=500, height=500)
    www.pack()

    cc = '강남구'


    for a in root.findall('row'):
        if(a.findtext('GU_NM') == cc ):
             #L1 = Lable(win,a.findtext('GU_NM'))
            # L1.pack()
             print(a.findtext('GU_NM'))
             print(a.findtext('CATEGORY'))
             print(a.findtext('PLACE_NAME'))
             print(a.findtext('INSTL_DIV'))
             print('===============================')



   # win.mainloop()
#if __name__ == "__main__":
mmain()




