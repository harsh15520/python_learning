import re
class phone_book:
    @staticmethod
    def main_menu(data:dict[str,str]):
        print('1.) view complete phone book')
        print('2.) add/update contact')
        print('3.) look up for specific contact')
        print('4.) delete a contact')
        print('5.) exit')
    @staticmethod
    def view_data(data:dict[str,str]):
        if not data:
            print('--phone book is empty--')
        else:
            for person,phone in data.items():
                print(f'{person}:{phone}')
        return ''
    @staticmethod
    def adding_data(data:dict[str,str]):
        person=input('enter name of person').strip()
        phone=input('enter phone number').strip()
        format=re.findall(r'^[6-9]\d{9}$|^[6-9]\d{2}[\s-]?\d{3}[\s-]?\d{4}$',phone)
        if not format:
            return '-wrong phone number format ***-****'
        clean_phone=phone.replace(" ",'').replace('-','')
        if person in data.keys():
            print(f'{person} already present')
            data.update({person: clean_phone})
        else:
            data[person]=clean_phone
        return f'{person}:{clean_phone} added/updated'
    @staticmethod
    def lookup(data:dict[str,str]):
        person=input('enter name of person')
        if person in data.keys():
            return (f'{person}:{data[person]}')
        else:
            return (f'{person} not in phone book')
    @staticmethod
    def remove_contact(data:dict[str,str]):
        person=input('enter name of person')
        data.pop(person,None)
        return (f'{person} is removed')
contact_book={}
while(True):
    menu=phone_book.main_menu(contact_book)
    choice=int(input('enter your choice'))
    if choice==1:
        complete_book=phone_book.view_data(contact_book)
        print(complete_book)
    elif(choice==2):
        updating_data=phone_book.adding_data(contact_book)
        print(updating_data)
    elif(choice==3):
        contact_finder=phone_book.lookup(contact_book)
        print(contact_finder)
    elif(choice==4):
        data_removal=phone_book.remove_contact(contact_book)
        print(data_removal)
    elif(choice==5):
        print('--thankyou--')
        break
    else:
        print('wrong choice')
