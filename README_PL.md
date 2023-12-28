Program jest symulacją ruchu drogowego na skrzyżowaniu. Oto ogólne działanie:

1. **Inicjalizacja:**
   - Użytkownik podaje (lub losuje) parametry, takie jak czas trwania świateł zielonych dla ruchu prosto i skręcającego, oraz liczbę pojazdów.
   - Tworzone są obiekty sygnalizacji świetlnej (`TrafficLight`), dróg (`Road`) i wątków pojazdów (`Car`).


2. **Symulacja ruchu pojazdów:**
   - Dla każdego pojazdu tworzony jest wątek, który symuluje czas dojazdu do skrzyżowania i decyduje, czy pojazd porusza się prosto czy skręca.
   - Pojazdy wjeżdżają na drogi, akwirują semafory związane z ruchem drogowym, zwiększają liczniki pojazdów na drogach i opuszczają skrzyżowanie po pewnym czasie.

3. **Kontroler sygnalizacji świetlnej:**
   - W oddzielnym wątku działa kontroler sygnalizacji świetlnej, który w nieskończonej pętli zmienia światła zielone dla ruchu prosto i skręcającego.
   - Kontroler uwalnia i blokuje odpowiednie semafory, kontrolując tym samym, który kierunek ruchu ma obecnie zielone światło.

4. **Zakończenie symulacji:**
   - Pojazdy kończą swoje wątki.
   - Ustawiane jest zdarzenie informujące kontroler sygnalizacji świetlnej, że ruch drogowy powinien zostać zatrzymany.
   - Czekamy, aż kontroler zakończy swoją pracę.

Program skupia się na synchronizacji wątków i symulacji zmieniających się warunków ruchu drogowego na skrzyżowaniu. Zastosowanie semaforów i zdarzeń pozwala na kontrolowanie dostępu do współdzielonych zasobów i zapewnia bezpieczne warunki dla równoległego działania wątków. Zatrzymuje ruch drogowy i oczekuje na zakończenie wątku kontrolera sygnalizacji świetlnej.gólnie rzecz biorąc, program symuluje ruch samochodów na skrzyżowaniu, gdzie światła sygnalizacji zmieniają się cyklicznie, a samochody muszą czekać na zielone światło przed wjazdem na skrzyżowanie.


### Klasa `TrafficLight`:
- **Metoda `__init__(self)`**: Inicjalizuje obiekt sygnalizacji świetlnej. Tworzy semafory (`straight_semaphore` i `turn_semaphore`) oraz zdarzenie (`stop_flag`) do synchronizacji wątków.

- **Metoda `set_green_light(self, direction)`**: Ustawia zielone światło dla danego kierunku ruchu. Zwolnienie odpowiedniego semafora (zwężenie dla jednego kierunku ruchu i zwężenie dla drugiego) informuje o tym, który kierunek ma obecnie zielone światło.

- **Metoda `stop_traffic(self)`**: Ustawia zdarzenie `stop_flag`, co sygnalizuje, że ruch drogowy powinien zostać zatrzymany.

- **Metoda `should_stop_traffic(self)`**: Sprawdza, czy zdarzenie `stop_flag` jest ustawione, co oznacza, że ruch drogowy powinien zostać zatrzymany.

### Klasa `Road`:
- **Metoda `__init__(self, name, traffic_light)`**: Inicjalizuje obiekt drogi. Przyjmuje nazwę drogi i obiekt sygnalizacji świetlnej, z którym jest powiązana.

- **Metoda `enter_road(self, car, direction)`**: Obsługuje wjazd pojazdu na drogę. Akwizycja semafora związana z kierunkiem ruchu informuje, że pojazd może wejść na drogę. Licznik pojazdów na drodze jest zwiększany, a informacje są wydrukowywane na konsoli.

- **Metoda `exit_road(self, car)`**: Obsługuje wyjazd pojazdu z drogi. Pojazd spędza pewien czas na drodze (symulacja ruchu) przed opuszczeniem drogi. Licznik pojazdów na drodze jest aktualizowany, a informacje są wydrukowywane na konsoli.

### Klasa `Car`:
- **Atrybut `DIRECTIONS`**: Lista zawierająca dostępne kierunki ruchu.

- **Metoda `__init__(self, name, road)`**: Inicjalizuje obiekt pojazdu. Przyjmuje nazwę pojazdu i obiekt drogi, na której pojazd porusza się.

- **Metoda `run(self)`**: Metoda wątku, która symuluje działanie pojazdu. Pojazd czeka pewien czas (symulacja czasu dojazdu), a następnie wjeżdża na drogę i opuszcza ją.

### Funkcja `traffic_light_controller`:
- **Argumenty: `traffic_light`, `straight_duration`, `turn_duration`**: Funkcja kontrolera sygnalizacji świetlnej. W nieskończonej pętli zmienia światła na sygnalizacji, symulując ruch drogowy.

### Funkcja `user_interface`:
- Pobiera od użytkownika lub losuje wartości dla czasów trwania świateł i liczby pojazdów.
- Tworzy obiekt sygnalizacji świetlnej oraz dwie drogi (dla ruchu prosto i skręcającego).
- Tworzy wątek kontrolera sygnalizacji świetlnej.
- Tworzy i uruchamia wątki dla określonej liczby pojazdów.
- Oczekuje na zakończenie wątków pojazdów.
