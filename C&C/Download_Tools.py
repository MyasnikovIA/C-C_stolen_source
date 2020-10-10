import requests as req
import os

# https://www.adityaravishankar.com/projects/games/command-and-conquer/images/bullets/120mm-sprite-sheet.png

# URL корневой путь 
urlSrc = 'https://www.adityaravishankar.com/projects/games/command-and-conquer/'



# локальный корневой путь к расположению файлов скаченого
# dirDst = "F:\\AppServ\\var\\www\\ExtJS\\Tut_003\\"
# dirDst = __file__[:__file__.rfind("\\")]+"\\"

dirDst = __file__[:__file__.rfind("/")]


def LoadInet(url):
    if len(url) == 0:
        return
    smolPath = url[len(urlSrc):]
    if url[-1:] == "/":
        return

    FileName = f"{dirDst}/{smolPath}".replace('/', '\\')
    print(FileName)
    # dirFileName = FileName[:FileName.rfind("/")].replace('/', '\\')
    # dirFileName = FileName[:FileName.rfind("/")].replace('/', '\\')
    dirFileName = FileName[:FileName.rfind("\\",2)]
    if not os.path.exists(dirFileName):
        os.makedirs(dirFileName)
    if not os.path.exists(FileName):
        r = req.get(url)
        open(FileName, 'wb').write(r.content)

"""
f = open('text.txt')
for line in f:
    if 'fetch("' in line:
        loadUrl=line[7:-5]
        if urlSrc not in loadUrl:
            continue
        LoadInet(loadUrl)
print("ok")
exit(1)

"""



def LoadLocalUrl(url):

    if len(url) == 0:
        return
    smolPath = url[len(urlSrc):]
    if url[-1:] == "/":
        return

    FileName = f"{dirDst}/{smolPath}".replace('/', '\\')
    print(FileName)
    # dirFileName = FileName[:FileName.rfind("/")].replace('/', '\\')
    # dirFileName = FileName[:FileName.rfind("/")].replace('/', '\\')
    dirFileName = FileName[:FileName.rfind("\\",2)]
    if not os.path.exists(dirFileName):
        os.makedirs(dirFileName)
    if not os.path.exists(FileName):
        r = req.get(url)
        open(FileName, 'wb').write(r.content)

url = "http://127.0.0.1:9090/del/command-and-conquer-inet/videos/nod/nod2.webm"
url = "https://www.adityaravishankar.com/projects/games/command-and-conquer/videos/nod/nod2.webm"
LoadInet(url)


