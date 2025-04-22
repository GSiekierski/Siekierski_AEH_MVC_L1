Projekt: Zadanie 12 - Katalog kolekcji filmów

Spis treści
- Opis
- Funkcjonalności
- Instrukcja uruchomienia

Opis

Aplikacja stworzona w Django, umożliwiająca prowadzenie katalogu kolekcji filmów. 
Użytkownik może dodawać, edytować, usuwać oraz przeglądać filmy. 
Projekt realizuje wzorzec MVC:
- Model Movie (title, director, rating)
- View templates/*.html
- Controller views.py + urls.py

 Funkcjonalności

- Przeglądanie listy filmów
- Dodawanie nowego filmu z pomocą formularzu
- Edycja istniejącego filmu z pomocą formularzu
- Usuwanie filmu z potwierdzeniem
- Stylizacja interfejsu w CSS


Instrukcja uruchomienia

1. Sklonuj repozytorium i przejdź do katalogu z projektem:
   ```bash
   cd projekt/moviecatalog
2. Zainstaluj Django:
    ```bash
    pip install django
3. Wykonaj migracje bazy danych:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
4. Uruchom serwer:
    ```bash
    python manage.py runserver
5. Przejdź na przeglądarce do - http://127.0.0.1:8000/
