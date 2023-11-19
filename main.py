from pytube import *

link = input("Ссылка на видео: ")
road = input("Вставьте путь до места куда вы хотите скачать видео: ")
quality = input("Введите качество High/Low: ")
output = YouTube(link)
if quality == "High":
    output.streams.get_highest_resolution().download(road)
elif quality == "Low":
    output.streams.get_lowest_resolution().download(road)
else:
    print("Некорректная операция!")


