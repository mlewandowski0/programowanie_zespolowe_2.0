# Raspi-Bot
This is the project created for UMK, called 'Programowanie Zespołowe 2.0', that encourage students of high schools to work on the project managed by the University. Our goal was to create a robot, which can be controlled from a web app and collect live stream video and data from sensors (such as carbon oxide level etc.).

To jest projekt stworzony na UMK o nazwie "Programowanie Zespołowe 2.0", którego celem była kilkumiesięczna praca nad projektem wybranym przez uczniów.
Naszym celem było stworzenie robota, który może być sterowany za pomocą aplikacji webowej, który ma widok z kamery na żywo oraz dostarcza informacji z zamonotowanych czujników (m.in. poziom tlenku węgla(II) itd.)

***
## Installation 
1. Download the newest (3.6.5) version of Python https://www.python.org/.
2. Download this repository (via Git client or just ZIP file from site).
3. Navigate to downloaded repository (by using the 'cd' command in terminal) and go to *web_app* folder.
4. In terminal type: 
```
pip install -r requirements.txt  [dunno if it works on Windows because of psutil]
```
5. Start the Python server by typing in:
```python
python app.py         # just run server 
python app.py --help  # show usage and flags 
```
6. In the web browser go to URL *localhost:5000*.

***
## Instalacja 
1. Pobierz najnowszą wersję (3.6.5) Python'a.
2. Pobierz to repozytorium (przez klienta Git'a albo jako plik ZIP przez stronę internetową).
3. Przejdź do katalogu głównego repozytorium (poprzez "cd" w terminalu), a następnie do *web_app*.
4. W terminalu wpisz tą komendę: 
```
pip install -r requirements.txt  [nie wiem czy to działa na Windowsie ze względu na psutil]
```
5. Uruchom serwer poprzez wpisanie:
```python
python app.py         # tylko uruchamia serwer, można dodać jakieś flagi 
python app.py --help  # pokaż użycie i flagi
```
6. W przeglądarce, idź do adresu *localhost:5000*. 
