# First Minimal Application of flask

from flask import Flask   # Import the Flask Class

# creating an instance of Flask class

app = Flask(__name__)  #__name__ : this is the name of your application's package or module.
                            # which tells flask where to look for resources such as templates or static files.

@app.route('/')     # We will use route() decorator to tell flask which url should trigger our function
                    # we use decorator to add some extra code as additional functionality to the application
def hello_world():
    return "<h1> Hello World! </h1>"

if __name__ == '__main__':
    app.run(debug=True, port=8080)   # by default, it runs on 5000 port number    # first activate the env and then run this app using :
                                                                                           #  py app.py
                                                                                  # TO RUN THIS APP without specifying the above lines:
                                                                                     #  py -m flask run