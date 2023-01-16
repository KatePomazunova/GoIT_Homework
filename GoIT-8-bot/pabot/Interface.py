
#виведення карток з контактами користувача, нотатками, сторінка з інформацією про доступні команди

from abc import ABC, abstractmethod

class AllOutput(ABC):

    @abstractmethod
    def output(self, data):
        pass


class ContactsOutput(AllOutput): 
    
    def output(self):
        birthday_info = ''
        phones_info = [phone.value for phone in self.phones]
        email_info = ''
        
        if self.birthday:
            birthday_info = f' Birthday: {self.birthday.value}'
            
        if self.email:
            email_info = f' Email: {self.email.value}'
            
        return f'{self.name.value} : {", ".join(phones_info)}{birthday_info}{email_info}'


class NoteOutput(AllOutput):

    def output(self):
        tmp = [val for val in self.data.values()]
        return "".join(list(map(lambda x: str(x), tmp)))


class HelpOutput(AllOutput):
    
    def output(self):
        return '''Command to execute: 
>>> hello
>>> help - show commands list
>>> add contact - add new contact in storage Example: add contact "name (only letters without spaces)" "phone number (only digits without spaces)"
>>> add email - add email to the contact Example: add email "name" "email"
>>> add birthday - add birthday date to the contact Example: birthday name date(yyyy-mm-dd)
>>> change phone - change existing contact Example: change "exist contact name (only letters without spaces)" "new phone number (only digits without spaces)"
>>> change email - change contact`s email Example: change email "name" "new_email"
>>> phone - shows all users with given phone for search. Example: phone +380951234567
>>> days to birthday - show how much days left to the contact birthday Example: days to birthday name
>>> show all - show all existing contacts
>>> delete phone - remove entered phone from contact Example: delete phone "name (only letters without spaces)" "phone number (only digits without spaces)"
>>> delete contact - remove contact Example: delete "name (only letters without spaces)" 
>>> create note - creates a new note Example: create note "name (only letters without spaces)"
>>> remove note - deletes a note by name Example: remove note "name"
>>> describe note - adds description to a note Example: describe note "name" "description"
>>> remove description - deletes the description of a note 
>>> alter description - changes the description of a note, if it exists
>>> tag - add a tag to the note Example: tag "name" "tag"
>>> untag - deletes a tag from a note, if it exists Example: untag "name" "tag"
>>> search notes - searches all notes for a match, prints out all matching notes
>>> show notes - shows all recorded notes
>>> sort by tag - performs an alphabetical sorting of notes, based on matches in their tags
>>> sort directory - just what it says Example: sort directory D:\\stuff\\python_projects
>>> good bye/close/exit - bye bye\n
'''