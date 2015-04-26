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

version = 1 * 1000000 + 1 * 1000 + 0 * 1


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
    f.close()
    return respond

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', help='Cesta k odevzdavanym souborum, napriklad ./src')
    parser.add_argument('-l', '--login', help='Login do systemu')
    parser.add_argument('-p', '--password', help='Heslo do systemu')
    parser.add_argument('-a', '--app', help='Zarazeni v systemu [zdo, mpv, ...]')
    parser.add_argument('-t', '--task', help='Nazev odevzdavane ulohy')

    argv = parser.parse_args()

    submit(argv.app, argv.directory, argv.login, argv.password, argv.task)




