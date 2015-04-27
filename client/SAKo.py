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


def submit(p_app, p_dir_name, p_login, p_passwd, p_task):
    """
        Funkce pro odevzdání úlohy na server.

        :param p_app: Aplikace do které je kód odevzdáván.
        :type p_app: str.

        :param p_dir_name:  Složka s odevzdávanými soubory.
        :type p_dir_name: str.
        :param p_login:  Login do systému SAKo.
        :type p_login: str.
        :param p_passwd:  Heslo do systému SAKo.
        :type p_passwd: str.
        :param p_task:  Název odevzdávané úlohy.
        :type p_task: str.


    """
    p_f = None
    url = 'http://147.228.124.51/' + p_app + '/'
    if p_dir_name[-1:] == '/':
        p_dir_name = p_dir_name[:-1]
    files = glob.glob(p_dir_name + '/*.*')
    p_data = dict(login=p_login, password=p_passwd,
                  task=p_task, version=version)
    for i in range(len(files)):
        filename = files[i]
        print 'Oteviram soubor : ' + filename
        p_f = open(filename, 'rb')
        file_data = p_f.read()
        p_data['name' + str(i)] = filename
        p_data['file' + str(i)] = file_data
    print 'Komunikace se serverem...'
    u = urllib.urlopen(url, urllib.urlencode(p_data))
    respond = u.read()
    if respond[0:9] == 'actualize':
        urllib.urlretrieve(respond[11:], os.path.abspath(__file__))
        print 'Klient byl aktualizovan. Provedte novy pokus o odevzdani'
    else:
        print "Vysledek :"
        print respond
    if p_f is not None:
        p_f.close()
    return respond


def create_identification_file(identity):
    """
        Interaktivni vytvoreni identifikacniho souboru
    """
    p_login = raw_input('Zadejte vase uzivatelske jmeno: ')
    p_password = raw_input('Zadejte vase heslo: ')
    p_app = raw_input('Vase zarazeni [zdo, mpv, ...]: ')

    try:
        p_f = open(path_to_script + '/' + identity + '.pck', 'wb')
        p_data = dict(login=p_login, password=p_password, app=p_app)
        pickle.dump(p_data, p_f, pickle.HIGHEST_PROTOCOL)
        p_f.close()
    except IOError as e:
        print 'I/O error ({0}): {1}'.format(e.errno, e.strerror)
        return 0
    print 'Soubor', path_to_script + '/identity.pck', 'byl vytvoren'
    return 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory',
                        help='Cesta k odevzdavanym souborum [./src]')
    parser.add_argument('-l', '--login',
                        help='Login do systemu')
    parser.add_argument('-p', '--password',
                        help='Heslo do systemu')
    parser.add_argument('-a', '--app',
                        help='Zarazeni v systemu [zdo, mpv, ...]')
    parser.add_argument('-t', '--task',
                        help='Nazev odevzdavane ulohy')
    parser.add_argument('-c', '--create',
                        help='Vytvoreni identifikacniho souboru [only|yes]',
                        default='none')
    parser.add_argument('-i', '--identity', help='Soubor s identitou',
                        default='identity.pck')

    argv = parser.parse_args()

    if argv.create != 'none':
        create_identification_file(argv.identity)

    if argv.create != 'only':
        task = argv.task
        directory = argv.directory

        if os.path.isfile(path_to_script + '/' + argv.identity + '.pck'):
            with open(path_to_script + '/' + argv.identity + '.pck', 'rb') as f:
                data = pickle.load(f)
                login = data['login']
                password = data['password']
                app = data['app']
        else:
            login = argv.login
            password = argv.password
            app = argv.app
        submit(app, directory, login, password, task)
