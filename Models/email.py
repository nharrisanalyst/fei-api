import time
from dataclasses import dataclass
from typing import Literal

@dataclass
class EmailForm:
    type:Literal['FindAnAgent', 'BuyHomeIns', 'BuyCarIns']
    name:str
    email:str
    message:str
    
    
    
class EmailBuilder:
    def __init__(self, EmailForm, Message):
        self.Message = Message 
        self.EmailForm = EmailForm
    
    def build(self, form):
        form = self.EmailForm(
                type = self.form['type'],
                email = self.form['email'].strip(),
                name =  self.form['name'].strip(),
                message= self.form['message'].strip(),
            )
        message = self.Message(
                subject=f'type: {form.type} from {form.name}',
                sender='reachoutatportal@gmail.com',
                recipients=['reachoutatportal@gmail.com'],
                date= int(time.time()),
                body = f' type: {form.type} name:{form.name} email: {form.email} message: {form.message}'
            )
        return message
    
    
class EmailService:
    def __init__(self, emailTransport):
        self.emailTransport = emailTransport

        def send(self,message):
            try:
                self.emailService.send(message)
            except Exception as e:
                return f"Failed to send email {e}", 500
            return 'Message was sent succesfully', 200
       