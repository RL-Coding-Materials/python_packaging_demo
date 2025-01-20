# Demo dystrybuowalnego projektu

Projekt dostarcza prostego programu o nazwie `greet`. Po jego uruchomieniu wyświetla napis `demoapp.library is greeting you!` w kolorze czerwonym.

Projekt ma zależności w postaci pakeitu `colroama`.

Ale... projekt nie jest kompletny. Twoim zadaniem jest uzupełnienie go o brakujace elementy.

## Początek

1. Pobierz repozytorium:
   ```bash
   git clone ...
   ```

1. Stwórz środowisko wirtualne i je aktywuj:
   ```bash
   virtualenv venv_demo
   . venv_demo/bin/activate
   ```

1. Zainstaluj projekt:
   ```bash
   cd demoapp
   pip install .
   ```

1. Uruchom program, wynik powinien być taki (lub bardzo podobny) jak na poniżej:
   ```bash
   greet
   ```
   ```
   Traceback (most recent call last):
     File "/tmp/venv/bin/greet", line 5, in <module>
       from demoapp.executable import main
     File "/tmp/venv/lib/python3.13/site-packages/demoapp/executable.py", line 1, in <module> 
       from .library import foo
     File "/tmp/venv/lib/python3.13/site-packages/demoapp/library.py", line 1, in <module>
       from colorama import Fore, Back, Style
   ModuleNotFoundError: No module named 'colorama'
   ```

1. Zobaczmy informacje o projekcie:
   ```bash
   pip show demoapp
   ```
   ```
   Name: demoapp
   Version: 0.0.1
   Summary: 
   Home-page: 
   Author: 
   Author-email: 
   License: 
   Location: /tmp/venv/lib/python3.13/site-packages
   Requires:
   Required-by:
   ```

## Zadanie

1. Na początek dodaj odpowiedni `.gitignore` aby odizolować wszystkie pliki tymczasowe powstające w trakcie procesu rozwoju, budowania i instalowania projektu: https://github.com/github/gitignore/blob/main/Python.gitignore
Pobież plik i dodaj do repozytorium.

1. Proces instalacji stworzył skrypt o nazwie `greet`, którego nie ma w źródłach projektu. Sprawdź zawartość tego skryptu. Najpierw znajdz ścieżkę do tego pliku poleceniem `which greet`, a potem podejrzyj kod tego pliku.

1. Zadbaj, aby pakiet podczas instalacji instalował również zależność `colorama`. Wtedy polecenie `greet` wykona się bez problemów.

1. Uzupełnij informacje o autorze swoimi danymi, dla przykładu:
   ```
   Name: demoapp
   Version: 0.0.1
   Summary: Short app to demonstrate redistrutable projects.
   Home-page: https://www.example.com
   Author: Awesome Programer
   Author-email: awesome@example.com
   License: MIT
   Location: /tmp/venv/lib/python3.13/site-packages
   Requires: colorama
   Required-by:
   ```

1. Uzupełnij `pyproject.toml` o wsparcie dla `pytest`, aby mogly się uruchamiać poleceniem `python -m pytest` lub po prostu `pytest`.

   Przydatne linki:
   - https://docs.pytest.org/en/stable/reference/customize.html
   - https://docs.pytest.org/en/stable/reference/reference.html?highlight=pythonpath#confval-pythonpath
   - https://docs.pytest.org/en/stable/explanation/goodpractices.html

1. Dodaj wsparcie dla `tox`. Wykorzystaj plik `tox.ini` z poprzednich zajeć, ale włącz go w `pyproject.toml`:
   - https://tox.wiki/en/latest/config.html

1. Dodaj te pakiety: `pytest`, `tox` (może również lintery `pylint`, `flake8` i formater `black`) jako opcjonalne zależności  typu development (nie są potrzebne do uruchomienia - czyli również do instalacji, ale do pracowania nad projektem).

1. Przenieś tę wiedzę na swój projekt zaliczeniowy. Być może będziesz musiał dostosować strukturę swojego projektu. Rozważ aby zastosować jeden z dwóch modeli `src-layout` lub `flat-layout`: https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/#src-layout-vs-flat-layout. Sprawdz, który layout jest użyty w tym prostym projekcie.

## Przydatne linki:
- https://setuptools.pypa.io/en/latest/userguide/index.html
- https://packaging.python.org/en/latest/
- https://packaging.python.org/en/latest/tutorials/packaging-projects/
