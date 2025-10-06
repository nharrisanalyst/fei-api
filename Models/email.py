import time
from dataclasses import dataclass
from typing import Literal

@dataclass
class EmailForm:
    type:Literal['FindAnAgent', 'BuyHomeIns', 'BuyCarIns']
    name:str
    email:str
    message:str
    
    
class Email:
    def __init__(self, *, emailService, form, Message, EmailForm=EmailForm ):
        self.form = form 
        self.emailServices = emailService
        self.Message = Message 
        self.EmailForm = EmailForm
        
        self._make_form()
        self._make_message()
        
        def _make_form(self):
            self._form = self.EmailForm(
                type = self.form['type'],
                email = self.form['email'].strip(),
                name =  self.form['name'].strip(),
                message= self.form['message'].strip(),
            )
        
        def _make_message(self):
            self._message = self.Message(
                subject=f'type: {self._form.type} from {self._form.name}',
                sender='reachoutatportal@gmail.com',
                recipients=['reachoutatportal@gmail.com'],
                date= int(time.time()),
                body = f' type: {self._form.type} name:{self._form.name} email: {self._form.email} message: {self._form.message}'
            )
            
        def send(self):
            self.emailService.send(self._message)