from waitress import serve
    
from database.wsgi import application
    
if __name__ == '__main__':
    serve(application)