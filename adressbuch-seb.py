import mysql.connector
import configparser

#Config laden
config = configparser.ConfigParser()
config.read('db_config.ini')

def create_connection():
    connection = mysql.connector.connect(
            host=config['mysql']['host'],
            user=config['mysql']['user'],
            password=config['mysql']['password'],
            database=config['mysql']['database'])
    if connection.is_connected():
        return connection
    else:
        print("Fehler")

conn = create_connection()
if conn:
    print("Verbindung erfolgreich!")
    conn.close()
else:
    print("Fehlgeschlagen")

def main_menu():
    while True:
        print("1. Kontakt hinzufügen\n2. Kontakte anzeigen\n3. Kontakt aktualisieren\n4. Kontakt löschen\n5. Beenden")
        choice = input("Gib eine Zahl ein: ")
        try:
            if choice == '1':
                add_contact()
            elif choice == '2':
                show_contacts()
            elif choice == '3':
                update_contacts()
            elif choice == '4':
                del_contact()
            elif choice == '5':
                quit()
        except ValueError:
            print("Falsche Eingabe!")

def add_contact():
    con = create_connection()
    cursor = con.cursor()

    name = input("Gib den Namen ein: ")
    phone = input("Telefonnummer: ")
    email = input("Email: ")
    adresse = input("Adresse: ")

    cursor.execute("INSERT INTO contacts (name, phone, email, adresse) VALUES (%s, %s, %s, %s)", (name, phone                  , email, adresse))
    con.commit()
    cursor.close()
    con.close()

def show_contacts():
    con = create_connection()
    cursor = con.cursor()

    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    for contact in contacts:
        print(contact)
    con.close()
    cursor.close()

def update_contacts():
    con = create_connection()
    cursor = con.cursor()

    search = input("Gib den Namen ein: ")
    cursor.execute("SELECT * FROM contacts WHERE name = %s", (search,))
    found_name = cursor.fetchone()
    accept = input(f"Ist das {found_name[1]} der richtige Name? j/n: ").lower()
    if accept == 'j':
        neuer_name = input("Neuer Name: ")
        neue_nummer = input("Neue Nummer: ")
        neue_email = input("Neue Email: ")
        neue_adresse = input("Neue Adresse: ")

        cursor.execute('UPDATE contacts SET name = %s, phone = %s, email = %s, adresse = %s WHERE name = %s', (neuer_name, neue_nummer, neue_email, neue_adresse, found_name[1]))
        con.commit()
        con.close()
    else:
        update_contacts()

def del_contact():
    con = create_connection()
    cursor = con.cursor()

    search = input("Gib den Namen ein: ")
    cursor.execute("SELECT * FROM contacts WHERE name = %s", (search,))
    found_name = cursor.fetchone()
    accept = input(f"Ist das {found_name[1]} der richtige Kontakt? j/n: ").lower()
    if accept == 'j':
        cursor.execute("DELETE FROM contacts WHERE name = %s", (found_name[1],))
        con.commit()
        con.close()
        cursor.close()
    else:
        del_contacts()


if __name__ == '__main__':
    main_menu()
    