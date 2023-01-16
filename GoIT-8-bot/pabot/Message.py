from abc import abstractmethod, ABC
from Interface import HelpOutput

# у цьомі классі зібрані усі меседжі які будуть виводитися користувачу при роботі з командами

class Message(ABC):
    
    @abstractmethod
    def get_message():
        pass
    
    
    

class HelpMessage(Message):
    
    @staticmethod
    def get_message():
        return HelpOutput.output()

class GreetingMessage(Message):
        
    @staticmethod
    def get_message():
        return 'How can I help you?'
    
class StopMessage(Message):
    
    @staticmethod
    def get_message():
        return 'Good bye!'
    
class AddContactMessage(Message):
    
    @staticmethod
    def get_message(name):
        return f'contact {name} was added'

class ChangeContacPhonetMessage(Message):
    
    @staticmethod
    def get_message(name):
        return f'contact {name} was updated'   
     
class DeletePhoneMessage(Message):
    
    @staticmethod
    def get_message(flag, name, phone):
        if flag:
            return f'Phone {phone} for {name} contact deleted.'
        return f'{name} contact does not have this number'
    
class DeleteContactMessage(Message):
    
    @staticmethod
    def get_message(name):
        return f'Contact {name} was deleted' 
    
class AddContactBirthdayMessage(Message):
    
    @staticmethod
    def get_message(name, birthday):
        return f'For {name} you add Birthday {birthday}' 
    
class AddContactEmaiMessage(Message):
    
    @staticmethod
    def get_message(name, email):
        return f'For {name} you add email {email}'    
    
class DaysToBirthdayMessage(Message):
    
    @staticmethod
    def get_message(name, days):
        return f'{days} left for the contact birthday {name}'


class BirthdaysAfterDaysMessage(Message):

    @staticmethod
    def get_message(result: list):
        if not result:
            print('No birthdays for this days')
        return '\n'.join(result)

class ValueErrorMessage(Message):

    @staticmethod
    def get_message():
        return print('The number of days must be a numeric value')
