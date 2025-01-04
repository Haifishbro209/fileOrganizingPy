import os
import shutil
from time import sleep
from PIL import Image

DirPath = "C:/Users/User/Downloads"
prevFiles = set(os.listdir(DirPath))

imgPath = r"C:\Users\User\Desktop\IMG"
vidPath = r"C:\Users\User\Desktop\VID"
ProgrammPath = r"C:\Users\User\Desktop\Programme"
gifPath = r"C:\Users\User\Desktop\IMG\GIF"
audPath = r"C:\Users\User\Desktop\AUD"

def move_file(file, target_dir):
    # Sicherstellen, dass der Zielordner existiert
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # Dateipfade definieren
    source = os.path.join(DirPath, file)
    target = os.path.join(target_dir, file)
    
    # Prüfen, ob die Datei im Zielordner bereits existiert
    if os.path.exists(target):
        base, ext = os.path.splitext(file)  # Dateiname und Erweiterung trennen
        target = os.path.join(target_dir, f"{base}_copy{ext}")
    
    # Datei verschieben
    shutil.move(source, target)
    print(f"Moved {file} to {target_dir} as {os.path.basename(target)}")


def Vid(file):
    move_file(file,vidPath)
    file_path = os.path.join(vidPath,file)
    name = file.rsplit('.', 1)[0]
    newFilePath = os.path.join(vidPath,f"{name}.mp4")
    os.rename(file_path,newFilePath)


def Aud(file):
    move_file(file,audPath)
    file_path = os.path.join(audPath,file)
    name = file.rsplit('.', 1)[0]
    newFilePath = os.path.join(audPath,f"{name}.mp3")
    os.rename(file_path,newFilePath)

def Img(file):
    move_file(file,imgPath)
    file_path = os.path.join(imgPath, file)
    print(file_path)  # Vollständigen Pfad erstellen
    with Image.open(file_path) as img:
        b, h = img.size
        b, h = str(b), str(h)
        name = file.rsplit('.', 1)[0]
        new_file_name = f"{b}x{h}__{name}.png"
        new_file_path = os.path.join(imgPath, new_file_name)
        img.save(new_file_path)
        print(f"Image saved as {new_file_path}")
    os.remove(file_path)

def Gif(file):
    move_file(file,gifPath)
    file_path = os.path.join(gifPath, file)
    print(file_path)  # Vollständigen Pfad erstellen
    with Image.open(file_path) as img:
        b, h = img.size
        b, h = str(b), str(h)
        new_file_name = f"{b}x{h}__{file}"
        new_file_path = os.path.join(gifPath, new_file_name)
        img.save(new_file_path)
        print(f"Image saved as {new_file_path}")
    os.remove(file_path)


def Prog(file):
    move_file(file,ProgrammPath)
    file_path = os.path.join(ProgrammPath,file)
    size = str(round(os.stat(file_path).st_size/(1024*1024)))
    newFile = f"{size}MB_{file}"
    newFilePath = os.path.join(ProgrammPath,newFile)
    os.rename(file_path,newFilePath)

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

