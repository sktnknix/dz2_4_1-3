# -*- coding: utf-8 -*-

import collections
import os
from utils import context_manager, logger_decorator, hash_generator


class Contact:
    instances = []

    @logger_decorator.path_to_logging(input('Enter file to save log: '))
    def __init__(self, firstname, lastname, tel, neo=False, **kwargs):
        self.firstname = firstname
        self.lastname = lastname
        self.tel = tel
        self.neo = neo
        self.kwargs = kwargs
        self.__class__.instances.append(self)

    def __str__(self):
        result = 'Имя: ' + self.firstname + '\n' + 'Фамилия: ' + self.lastname + '\n' + \
                'Телефон: ' + self.tel + '\n' + 'В избранных: ' + ('избранный' if self.neo else 'нет') + '\n' + \
                'Дополнительная информация: \n'
        add_result = ''
        for keys, values in self.kwargs.items():
            add_result += '\t'*2 + keys + ': ' + values + '\n'
        contact = result + add_result + 'Contact hash: \n'
        with open('__hash.tmp', 'w') as temp:
            temp.write(contact)
        for hashed in hash_generator.hash_strings('__hash.tmp'):
            contact += hashed
        os.remove('__hash.tmp')
        return contact


class PhoneBook:
    def __init__(self, fbname):
        self.fbname = fbname

    def print_contacts(self):
        if Contact.instances == []:
            print('Nothing to show ...')
        else:
            for ins in Contact.instances:
                print(ins)

    def is_add_parameters(self):
        add_list = []
        while 1:
            is_add = input('Some additional parameters ? (y/n)')
            if is_add == 'n':
                break
            elif is_add == 'y':
                addkey = input('Enter add parameter name: ')
                addvalue = input('Enter ' + addkey + ' value ')
                add_pare = {addkey: addvalue}
                add_list.append(add_pare)
                continue
            else:
                print('Enter y/n')
        return add_list

    def insert_contact(self):
        fstname = input('Firstname: ')
        lstname = input('Lastname: ')
        tlph = input('Tel: ')
        while 1:
            is_neo = input('Does person is Neo ? (True/False). To default = False, press Enter: ')
            if is_neo == '' or is_neo == 'False':
                neo = False
                break
            elif is_neo == 'True':
                neo = True
                break
            else:
                print('Only True/False')
        add_parameters = self.is_add_parameters()
        if add_parameters == []:
            fbook = Contact(fstname, lstname, tlph, neo)
        else:
            kwargs = dict(collections.ChainMap(*add_parameters))
            fbook = Contact(fstname, lstname, tlph, neo, **kwargs)

    def delete_contact_by_tel(self):
        while 1:
            tel_for_del = input('Enter tel for del contact: ')
            if tel_for_del != '':
                for ins in Contact.instances:
                    if getattr(ins, 'tel') == tel_for_del:
                        Contact.instances.remove(ins)
                        del ins
                        print('Success !')
                    else:
                        print('Contact with such tel not found ...')
                break
            else:
                print('Enter smth.')

    def find_neo_contacts(self):
        for ins in Contact.instances:
            if getattr(ins, 'neo') == True:
                print('Избранные: \n****\n')
                print(ins)
            else:
                print('Not Neo ...')

    def find_by_first_last_name(self):
        while 1:
            fstname = input('Enter firstname: ')
            lstname = input('Enter lastname: ')
            if fstname == '' or lstname == '':
                print('Enter smth.')
            else:
                for ins in Contact.instances:
                    if getattr(ins, 'firstname') == fstname and getattr(ins, 'lastname') == lstname:
                        print(ins)
                    else:
                        print('Nothing found ...')
                break


if __name__ == '__main__':
    with context_manager.TimeScore() as contacts_ts:
        phonebook = PhoneBook('work')
        while 1:
            inp = input('-------------------\nFor EXIT press 0\n1(insert contact); \n2(print all);\n'
                        '3(delete by tel);\n4(find Neo contacts);\n5(find by first and last names)\n'
                        '------------------- ==> ')
            if inp == '1':
                phonebook.insert_contact()
            elif inp == '2':
                phonebook.print_contacts()
            elif inp == '3':
                phonebook.delete_contact_by_tel()
            elif inp == '4':
                phonebook.find_neo_contacts()
            elif inp == '5':
                phonebook.find_by_first_last_name()
            elif inp == '0':
                break
            else:
                print('Enter only numbers 0 .. 5')
