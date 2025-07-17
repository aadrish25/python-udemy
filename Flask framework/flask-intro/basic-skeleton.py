# flask is a web framework used to implement end to end web applications using python
from flask import Flask

app=Flask(__name__)  # we are creating an instance of Flask class, and this will be acting as my WSGI(Web Server Gateway Interface), and it will interact with the web server itself


if __name__=="__main__": # this is the entry point of any .py application, code inside this if block will be executed only if the file is run as a main file, and not as a module
    
    # and we can run our flask app using this 'app.run()'
    app.run()