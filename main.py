import os
import shutil
from time import sleep
from PIL import Image

DirPath = "C:/Users/User/Downloads"
prevFiles = set(os.listdir(DirPath))

imgPath = r"C\Users\User\Desktop\IMG"
vidPath = r""
ProgrammPath = r""
gifPath = r""

def move_file(file, target_dir):
    # Sicherstellen, dass der Zielordner existiert
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # Dateipfade definieren
    source = os.path.join(DirPath, file)
    target = os.path.join(target_dir, file)
    
    # Datei verschieben
    shutil.move(source, target)
    print(f"Moved {file} to {target_dir}")

def Vid(file):
    print()

def Aud(file):
    print()

def Img(file):
    move_file(file,imgPath)
    file_path = os.path.join(imgPath, file)  # Vollständigen Pfad erstellen
    with Image.open(file_path) as img:
        b, h = img.size
        b, h = str(b), str(h)
        name = file.rsplit('.', 1)[0]
        new_file_name = f"{b}x{h}|{name}.png"
        new_file_path = os.path.join(imgPath, new_file_name)
        img.save(new_file_path)
        print(f"Image saved as {new_file_path}")

def Gif(file):
    move_file(file,r"C:\Users\User\Desktop\VID\GIF")
def Prog(file):
    move_file(file,r"C:\Users\User\Desktop\Programme")

def newItems(files):
    print("new Items in Download Directory found")
    print(files)
    for file in files:
        file = file.lower()
        index = file.rfind('.')
        file_type = file[index + 1:]
        match file_type:
            case "mp4" | "mov" | "avi" | "wmv" | "mkv":
                Vid(file)
            case "mp3" | "wav":
                Aud(file)
            case "jpg" | "jpeg" | "png" | "webp" | "bmp" :
                Img(file)
            case "gif":
                Gif(file)
            case "exe" | "msi":
                Prog(file)
            
while True:
    sleep(1)
    files = set(os.listdir(DirPath))
    newFiles = files - prevFiles
    if newFiles:
        newItems(newFiles)
    prevFiles = files

