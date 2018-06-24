from clint.textui import colored
from datetime import datetime

def welcome_message(message):
    return colored.yellow(f'''            
                                        
                      \`*-.                    
                       )  _`-.                 
                      .  : `. .                
                      : _   '  \               
                      ; *` _.   `*-._          
                      `-.-'          `-.       
                        ;       `       `.     
                        :.       .        \    
                        . \  .   :   .-'   .   
                        '  `+.;  ;  '      :   
                        :  '  |    ;       ;-. 
                        ; '   : :`-:     _.`* ;
                    .*' /  .*' ; .*`- +'  `*' 
                     `*-*   `*-*  `*-*'       \n\n''') + colored.red(message) + '\n'

def status_message(message):
    return '' + colored.green(message)

def users_list(users):
    return '' + colored.red(users)

def chat_message(message):
    return colored.blue(message)

def timestamp(ts):
    return colored.cyan(ts)

def username(name):
    return colored.magenta(name)

def format_message(message, user):
        return timestamp(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ") + \
               username(f'{user}: ') + \
               message.rstrip('\n')