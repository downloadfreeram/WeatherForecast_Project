# Jak uruchomić stronę lokalnie (Windows)
W pierwszym kroku przy użyciu wiersza poleceń należy utworzyć nowe środowisko wirtualne w folderze głownym przy użyciu komendy 
```
py -m venv <nazwa środowiska>
```
Następnie nasze środowisko uruchamiamy przy pomocy komendy
```
<nazwa środowiska>\Scripts\activate.bat
```
Teraz potrzebujemy zainstalować za pomocą instalatora pip dwa moduły:
- Django
- requests
które są niezbędne do działania strony, i pobieramy je za pomocą komendy
```
pip install django

pip install requests

```
Po zainstalowaniu modułów musimy uruchomić serwer komendą
```
manage.py runserver
```
Teraz wpisując w wyszukiwarkę adres 127.0.0.1:8000, otworzymy stronę. Aby przerwać działanie serwera wykonujemy kombinacje klawiszy CTRL + C

Przy każdorazowym otworzeniu wiersza poleceń musimy uruchomić nasze wirtualne środowisko oraz uruchomić serwer
