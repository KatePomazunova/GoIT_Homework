import re



contacts = {}  


def add(text):

    phone_number = re.findall(r"\d+", text)[-1]
    phone_name = re.findall(r"[a-z]+", text, flags=re.IGNORECASE)[1].title()
    contacts[phone_name] =  phone_number
    print("Number added. Something else?")


def change(text):
    
    phone_number = re.findall(r"\d+", text)[-1]
    phone_name = re.findall(r"[a-z]+", text, flags=re.IGNORECASE)[1].title()
    old_phone_number = contacts[phone_name] 
    contacts[phone_name] =  phone_number
    print(f"{phone_name}\'s number {old_phone_number} changed to {phone_number}. Something else?")


def end(text):

    print("Good bye!")
    

def hello(text):

    print("How can I help you?")


def input_error(funk):
      
    def inner(*args,**kwargs):  

        try:
            funk()
        except KeyError: 
            print("This name does not exist.")
            main()
        except IndexError:
            print("Did not receive a name or number.")
            main()
        except:
            print("Option entered incorrectly.")
            main()

    return inner


def phone(text):
    
    phone_name = re.findall(r"[a-z]+", text, flags=re.IGNORECASE)[1].title()
    print(contacts[phone_name])


def show_all(text):

    print(contacts)


@input_error
def main():

    start = True

    while start:

        access = False
        entered_text = input()
        
        for key in user_command.keys():
       
            if bool(re.search(key, entered_text, flags=re.IGNORECASE)):
                
                access = True
                user_command[key](entered_text)

                if key in ["exit","good bye","close"]:
                    start = False  
                break
      
        if not access:
            print("Option entered incorrectly...")
               
      

user_command = {
    "add": add,
    "change": change,
    "exit": end,
    "good bye": end,
    "close": end,
    "hello": hello,
    "phone": phone,
    "show all": show_all,
}


if __name__ == "__main__":
    main()


