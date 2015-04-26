#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
:platform: Unix, Windows
:synopsis: Klient Systému Automatické Kontroly (SAKo)

.. moduleauthor:: Petr Neduchal <neduchal@ntis.zcu.cz>

Závislosti
----------
* os
* os.path
* urllib
* glob

**Ukázka použití klienta**

Vytvořte si na disku slozku sako a do ni složku src.
Do složky sako nahrajte soubor SAKo.py.
Do složky src nahrajte soubory, které budete odevzdávat.

Následně ve složce sako vytvořte soubor submit.py.
Do něj pak vložte následující kód.


**Význam jednotlivých parametrů**

*"zdo"* - Aplikace, do které odevzdáváte (zdo/mpv

*"./src/"* - Relativní cesta ke složce s odevzdávanými soubory

*"login"* - Váš login do systému SAKo

*"heslo"* - Vaše heslo do systému SAKo

*"copy"* - Odevzdávaná úloha. Úloha copy pouze nahraje soubory na server.

**Samotný kód**

.. code-block:: python

    #! /usr/bin/python
    # -*- coding: utf-8 -*-
    import SAKo
    SAKo.submit("zdo", "./src/", "login", "heslo", "copy")

"""

# Imports
import os
import os.path
import urllib
import glob
import argparse
import pickle

version = 1 * 1000000 + 1 * 1000 + 0 * 1
path_to_script = os.path.dirname(os.path.abspath(__file__))


def submit(app, dir_name, login, passwd, task):
    """Funkce pro odevzdání úlohy na server.

       :param app: Aplikace do které je kód odevzdáván.
       :type app: str.

       :param dir_name:  Složka s odevzdávanými soubory.
       :type dir_name: str.
       :param login:  Login do systému SAKo.
       :type login: str.
       :param passwd:  Heslo do systému SAKo.
       :type passwd: str.
       :param task:  Název odevzdávané úlohy.
       :type task: str.

    """
    f = None
    url = 'http://147.228.124.51/' + app + '/'
    if dir_name[-1:] == '/':
        dir_name = dir_name[:-1]
    files = glob.glob(dir_name + '/*.*')
    data = dict(login=login, password=passwd, task=task, version=version)
    for i in range(len(files)):
        filename = files[i]
        print 'Oteviram soubor : ' + filename
        f = open(filename, 'rb')
        filebody = f.read()
        data['name' + str(i)] = filename
        data['file' + str(i)] = filebody
    print "Komunikace se serverem..."
    u = urllib.urlopen(url, urllib.urlencode(data))
    respond = u.read()
    if respond[0:9] == 'actualize':
        urllib.urlretrieve(respond[11:], os.path.abspath(__file__))
        print "Klient byl aktualizovan. Provedte novy pokus o odevzdani"
    else:
        print "Vysledek :"
        print respond
    if f is not None:
        f.close()
    return respond

def create_identification_file():
    """

    :return:
    """
    login = raw_input('Zadejte vase uzivatelske jmeno: ')
    password = raw_input('Zadejte vase heslo: ')
    app = raw_input('Vase zarazeni [zdo, mpv, ...]: ')

    f = open(path_to_script+'/identity.pck', 'wb')
    data = dict(login=login, password=password, app=app)
    pickle.dump(data, f)
    f.close()
    print 'Soubor', path_to_script+'/identity.pck', 'byl vytvoren'

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', help='Cesta k odevzdavanym souborum, napriklad ./src')
    parser.add_argument('-l', '--login', help='Login do systemu')
    parser.add_argument('-p', '--password', help='Heslo do systemu')
    parser.add_argument('-a', '--app', help='Zarazeni v systemu [zdo, mpv, ...]')
    parser.add_argument('-t', '--task', help='Nazev odevzdavane ulohy')
    parser.add_argument('-c', '--create', help='Vytvoreni identifikacniho souboru 0 ,1 2', default=0)

    argv = parser.parse_args()

    print argv.create
    if argv.create > 0:
        create_identification_file()

    if argv.create != 2:
        login = ''
        password = ''
        app = ''
        task = argv.task
        directory = argv.directory

        if os.path.isfile(path_to_script+'/identity.pck'):
            with open(path_to_script+'/identity.pck') as f:
                data = pickle.load(f)
                login = data['login']
                password = data['password']
                app = data['app']
        else:
            login = argv.login
            password = argv.password
            app = argv.app
        submit(app, directory, login, password, task)




