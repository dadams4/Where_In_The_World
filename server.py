import os
import uuid
from cassandra.cluster import Cluster

from cassandra.auth import PlainTextAuthProvider

from flask import Flask, render_template, request, session

from flask_socketio import SocketIO, emit

app = Flask(__name__)

app.secret_key = os.urandom(24).encode('hex')

socketio = SocketIO(app)

users = {}

#Where the results of the queries are displayed to the user
@socketio.on('displayactors1')
def on_displayactors(result):
    
    print("made it to displayactors1")
    
    tmp = {'title': result['title']}
    
    emit('displayactors1', tmp)
    
    

@socketio.on('displayactors2')
def on_displayactors2(result):
    
    
    tmp = {'name': result['name']}
   
    emit('displayactors2', tmp)

@socketio.on('displaymovies')
def on_displaymoves(result):
    
    tmp = {'title': result['title'], 'score': result['score'], 'votes': result['votes'], 'yr': result['yr']}
    
    emit('displaymovies', tmp)
    
#Where the queries are handled
@socketio.on('search')
def on_search(query):
    
    print("In search")

    auth_provider = PlainTextAuthProvider(
    
    username = 'manager', password='123')
    
    cluster = Cluster(auth_provider=auth_provider)

    session = cluster.connect('rudiment')
    
    print(query)
    
    #query_actor_string = "select title from actors where name = \'%s\';" % query
    #print(query_actor_string)
    
    rows = ''
    rows2 = ''
    
    """ Variables to hold query results """
    
    # Result from querying an actor name
    actorResults = False
    
    #Results from querying a movie name 
    movieResults = False
    
    
    #First try searching for movies an actor was in
    try: 
        rows = session.execute("select title from actors where name = \'%s\';" % query)

    except:
        print("not an actor")
        
    actorResults = True
    
    #Otherwise we are searching a movie title    
    if not rows:
    
        actorResults = False
    
        try:
            rows = session.execute("select title, score, votes, yr from movies where title = \'%s\' limit 1;" % query)
        except:
            print("not a movie")
            
        if rows:
            
            movieResults = True;
           
            try:
                rows2 = session.execute("select name from actors where title = \'%s\';" % query)
            except:
                print("this should never print")

    if actorResults:
        
        for i in range(1,2):
        
            divider = {'title': '--------Movie Title--------'}
            emit('displayactors1', divider)
        
        for row in rows:
            
            
            tmp = {'title': row.title}
            
            print(tmp)
            
            emit('displayactors1', tmp)
    
    elif movieResults:
        
        for i in range(1,2):
            divider = {'title': '-Title-',  'score': '-Score-', 'votes': '-Votes-', 'yr': '-Year-'}
            emit('displaymovies', divider)
            
        for row in rows:
            
            
            
            tmp = {'title': row.title, 'score': row.score, 'votes': row.votes, 'yr': row.yr}
            
            print(tmp)
            
            emit('displaymovies', tmp)
          
        for i in range(1,2): 
            
            divider = {'name': '--------Actors--------'}
            emit('displayactors2', divider)
           
                
        for row in rows2:
            
            
            tmp = {'name': row.name}
            
            print(tmp)
            
            emit('displayactors2', tmp)
    else:
        print("Nothing sport")
    

  
@app.route('/')
def mainIndex():
	return render_template('index.html')

# start the server
if __name__ == '__main__':
   # app.debug=True
    #app.run(host='0.0.0.0', port=8080)
    
    socketio.run(app, host=os.getenv('IP', '0.0.0.0'), port =int(os.getenv('PORT', 8080)), debug=True)
