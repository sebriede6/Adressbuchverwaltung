# Adressbuchverwaltung

##
# Kontakte-Verwaltungssystem

Dieses Python-Skript ermöglicht die Verwaltung von Kontakten in einer MySQL-Datenbank. Es bietet Funktionen zum Hinzufügen, Anzeigen, Aktualisieren und Löschen von Kontakten.

## Voraussetzungen

- Python 3.x
- MySQL-Datenbank
- Die Pakete `mysql-connector-python` und `configparser`

## Installation

1. **Python installieren**:
   - Stelle sicher, dass Python 3.x auf deinem System installiert ist. Du kannst Python von [python.org](https://www.python.org/downloads/) herunterladen.

2. **Benötigte Pakete installieren**:
   - Installiere die benötigten Pakete mit pip:

   ```bash
   pip install mysql-connector-python
   ```

3. **Datenbank einrichten**:
   - Stelle sicher, dass eine MySQL-Datenbank eingerichtet ist, und erstelle eine Tabelle namens `contacts` mit den folgenden Spalten:

   ```sql
   CREATE TABLE contacts (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255) NOT NULL,
       phone VARCHAR(50),
       email VARCHAR(100),
       adresse VARCHAR(255)
   );
   ```

4. **Konfigurationsdatei erstellen**:
   - Erstelle eine Datei namens `db_config.ini` im gleichen Verzeichnis wie das Skript und füge die folgenden Konfigurationen hinzu:

   ```ini
   [mysql]
   host = IP_ADRESSE_DEINER_DB_VM
   user = DEIN_BENUTZERNAME
   password = DEIN_PASSWORT
   database = DEIN_DATABASENAME
   ```

   Ersetze die Platzhalterwerte durch die tatsächlichen Verbindungsinformationen deiner MySQL-Datenbank.

## Ausführung

Um das Skript auszuführen, navigiere zu dem Verzeichnis, in dem sich die Skriptdatei befindet, und führe den folgenden Befehl aus:

```bash
python dein_skript_name.py
```

## Benutzung

Nach dem Start des Skripts wird ein Menü angezeigt, das folgende Optionen bietet:

1. **Kontakt hinzufügen**: Ermöglicht das Hinzufügen eines neuen Kontakts.
2. **Kontakte anzeigen**: Zeigt alle gespeicherten Kontakte an.
3. **Kontakt aktualisieren**: Ermöglicht das Aktualisieren eines bestehenden Kontakts.
4. **Kontakt löschen**: Ermöglicht das Löschen eines Kontakts.
5. **Beenden**: Schließt das Skript.

Folge den Anweisungen im Menü, um die gewünschten Aktionen auszuführen.

## Fehlerbehebung

- **Verbindungsfehler**: Stelle sicher, dass die MySQL-Datenbank läuft und dass die Verbindungsdetails in der `db_config.ini` korrekt sind.
- **Tabellen- oder Spaltenfehler**: Vergewissere dich, dass die Tabelle `contacts` mit den richtigen Spalten in der Datenbank existiert.
