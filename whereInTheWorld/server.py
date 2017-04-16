#import os
import psycopg2
import psycopg2.extras

from flask import Flask, render_template, request
app = Flask(__name__)

#from lib.config import*
#from lib import postgresql_data as pg




def connectToDB():
    
    connectionString = 'dbname=world user=postgres password=Daniel21 host=localhost'
    print connectionString
    try:
        return psycopg2.connect(connectionString)
    except:
        print("Can't connect to DB")


@app.route('/search', methods = ['GET', 'POST'])
def query_db():
    
    var1 = "var1" #All three
    var2 = "var2" #Only Name
    var3 = "var3" #Name and Pop
    var4 = "var4" #Name and Code
    var5 = "var5" #Pop and Code
    var6 = "var6" #Only Pop
    var7 = "var7" #Only Code
    
    
    
    connection = connectToDB()
    cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    #Name, population, code
    if request.form.get('name') != None and request.form.get('population') != None and request.form.get('countrycode') != None:
    
        #First check if it's a country
        try:
            cur.execute("select name, code, population from country where name = \'%s\';" % (request.form['query']))
            #print(cur.fetchall())
            
            #If it is, grab the results
            try: 
                results = cur.fetchall()
                
                #return render_template('results.html', posts=results)#, var=var1)
                
            except:
                print("nothing, not a country")
        
            
        except:
            print("Not a country")
    
        #Check if it is a city
        if not results:
            #print("not a country, trying city with " + request.form['query'])
            try:
                
                cur.execute("select name, countrycode, population from city where name = \'%s\' ;" % (request.form['query']))
                print(cur.fetchall())
                #If it is, grab the results
                try: 
                    results = cur.fetchall()
                    #print(results + " city results")
                    #return render_template('results.html', posts=results)#, var=var1)
                    
                except:
                    print("nothing")
                
            except:
                print("Not a city")
            
            
        if not results:
            try:
                cur.execute("select name, countrycode, population from city where countrycode = \'%s\';" % (request.form['query']))
                
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var1)
                    
                except:
                    print("nothing")
                
            except:
                print("nothing")
        
        
        if not results:
            try:
                cur.execute("select name, code, population from country where code = \'%s\';" % (request.form['query']))
                
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var1)
                    
                except:
                    print("nothing")
                
            except:
                print("nothing")   
                
        if not results:
            try:
                cur.execute("select name, code, population from country where continent = \'%s\';" % (request.form['query']))
                
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var1)
                    
                except:
                    print("nothing")
                
                
            except:
                print("nothing")
            #If the Query was invalid
        if not results:
                
            try:    
                results = cur.fetchall()
            except:
                results = ""
            
            #Render in case it was an invalid query so we don't crash
            return render_template('results.html', posts=results, var=var1)
        

    # Only Name
    elif request.form.get('name') == 'Show Name' and request.form.get('population') != 'Show Population' and request.form.get('countrycode') != 'Show Country Code':
        
        print("only name")
        
        #First check if it's a country
        try:
            cur.execute("select name from country where name = \'%s\';" % (request.form['query']))
            print("Name")
            
            #If it is, grab the results
            try: 
                
                results = cur.fetchall()
               # return render_template('results.html', posts=results)#, var=var2)
                
            except:
                print("nothing")
        
            
        except:
            print("Not a country")
    
        if not results:
            try:
                cur.execute("select name from city where countrycode = \'%s\';" % (request.form['query']))
                
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var1)
                    
                except:
                    print("nothing")
                
            except:
                print("nothing")
        
        
        if not results:
            try:
                cur.execute("select name from country where code = \'%s\';" % (request.form['query']))
                
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var1)
                    
                except:
                    print("nothing")
                
            except:
                print("nothing")   
                
        if not results:
            try:
                cur.execute("select name from country where continent = \'%s\';" % (request.form['query']))
                
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var1)
                    
                except:
                    print("nothing")
                
                
            except:
                print("nothing")
    
        #Check if it is a city
        if not results: 
            try:
                
                cur.execute("select name from city where name = \'%s\' ;" % (request.form['query']))
                
                #If it is, grab the results
                try: 
                    results = cur.fetchall()
                   # return render_template('results.html', posts=results)#, var=var2)
                    
                except:
                    print("nothing")
                
            except:
                print("Not a city")
        
        
        #If the Query was invalid
        if not results:
            
            try:    
                results = cur.fetchall()
            except:
                results = ""
        
        #Render in case it was an invalid query so we don't crash
        return render_template('results.html', posts=results, var=var2)

    # Only Name and Population
    elif request.form.get('name') == 'Show Name' and request.form.get('population') == 'Show Population' and request.form.get('countrycode') != 'Show Country Code':
        
        #First check if it's a country
        try:
            cur.execute("select name, population from country where name = \'%s\';" % (request.form['query']))
            print("Name and Pop")
            
            #If it is, grab the results
            try: 
                results = cur.fetchall()
                #return render_template('results.html', posts=results)#, var=var3)
                
            except:
                print("nothing")
        
            
        except:
            print("Not a country")
    
        if not results:
            try:
                cur.execute("select name, population from city where countrycode = \'%s\';" % (request.form['query']))
                
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var1)
                    
                except:
                    print("nothing")
                
            except:
                print("nothing")
        
        
        if not results:
            try:
                cur.execute("select name, population from country where code = \'%s\';" % (request.form['query']))
                
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var1)
                    
                except:
                    print("nothing")
                
            except:
                print("nothing")   
                
        if not results:
            try:
                cur.execute("select name, population from country where continent = \'%s\';" % (request.form['query']))
                
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var1)
                    
                except:
                    print("nothing")
                
                
            except:
                print("nothing")
    
        #Check if it is a city
        if not results:
            
            try:
                
                cur.execute("select name, population from city where name = \'%s\' ;" % (request.form['query']))
                
                #If it is, grab the results
                try: 
                    results = cur.fetchall()
                  #  return render_template('results.html', posts=results)#, var=var3)
                    
                except:
                    print("nothing")
                
            except:
                print("Not a city")
        
        #If the Query was invalid
        if not results:
            
            try:    
                results = cur.fetchall()
            except:
                results = ""
        
        #Render in case it was an invalid query so we don't crash
        return render_template('results.html', posts=results, var=var3)

    # Only Name and Code
    elif request.form.get('name') == 'Show Name' and request.form.get('population')  != 'Show Population' and request.form.get('countrycode') == 'Show Country Code':
        
        #First check if it's a country
        try:
            cur.execute("select name, code from country where name = \'%s\';" % (request.form['query']))
            print("Name and Code")
            
            #If it is, grab the results
            try: 
                results = cur.fetchall()
                #return render_template('results.html', posts=results)#, var=var4)
                
            except:
                print("nothing")
        
            
        except:
            print("Not a country")
    
        if not results:
            try:
                cur.execute("select name, code from city where countrycode = \'%s\';" % (request.form['query']))
                
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var1)
                    
                except:
                    print("nothing")
                
            except:
                print("nothing")
        
        
        if not results:
            try:
                cur.execute("select name, code from country where code = \'%s\';" % (request.form['query']))
                
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var1)
                    
                except:
                    print("nothing")
                
            except:
                print("nothing")   
                
        if not results:
            try:
                cur.execute("select name, code from country where continent = \'%s\';" % (request.form['query']))
                
                
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var1)
                    
                except:
                    print("nothing")
                
            except:
                print("nothing")
    
        #Check if it is a city
        if not results:
            try:
                
                cur.execute("select name, countrycode from city where name = \'%s\' ;" % (request.form['query']))
                
                #If it is, grab the results
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var4)
                    
                except:
                    print("nothing")
                
            except:
                print("Not a city")
        
        #If the Query was invalid
        if not results:
            
            try:    
                results = cur.fetchall()
            except:
                results = ""
        
        #Render in case it was an invalid query so we don't crash
        return render_template('results.html', posts=results, var=var4)

    # Only Population and Code
    elif request.form.get('name') != 'Show Name' and  request.form.get('population') == 'Show Population' and request.form.get('countrycode') == 'Show Country Code' :
        
        #First check if it's a country
        try:
            cur.execute("select population, code from country where name = \'%s\';" % (request.form['query']))
            
            print("Pop and Code")
            
            #If it is, grab the results
            try: 
                results = cur.fetchall()
                #return render_template('results.html', posts=results)#, var=var5)
                
            except:
                print("nothing")
        
            
        except:
            print("Not a country")
    
        if not results:
            try:
                cur.execute("select population, code from city where countrycode = \'%s\';" % (request.form['query']))
                
                
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var1)
                    
                except:
                    print("nothing")
                
            except:
                print("nothing")
        
        
        if not results:
            try:
                cur.execute("select population, code from country where code = \'%s\';" % (request.form['query']))
                
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var1)
                    
                except:
                    print("nothing")
                
                
            except:
                print("nothing")   
                
        if not results:
            try:
                cur.execute("select population, code from country where continent = \'%s\';" % (request.form['query']))
                
                
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var1)
                    
                except:
                    print("nothing")
                
            except:
                print("nothing")
    
        #Check if it is a city
        if not results:
            try:
                
                cur.execute("select population, code from city where name = \'%s\' ;" % (request.form['query']))
                
                #If it is, grab the results
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var5)
                    
                except:
                    print("nothing")
                
            except:
                print("Not a city")
        
        #If the Query was invalid
        if not results:
            try:    
                results = cur.fetchall()
            except:
                results = ""
        
        #Render in case it was an invalid query so we don't crash
        return render_template('results.html', posts=results, var=var5)

    # Only Population
    elif request.form.get('name') != 'Show Name' and request.form.get('population') == 'Show Population' and request.form.get('countrycode') != 'Show Country Code':
        
        #First check if it's a country
        try:
            cur.execute("select population from country where name = \'%s\';" % (request.form['query']))

            #If it is, grab the results
            try: 
                results = cur.fetchall()
               # return render_template('results.html', posts=results)#, var=var6)
                
            except:
                print("nothing")
        
            
        except:
            print("Not a country")
    
        if not results:
            try:
                cur.execute("select population from city where countrycode = \'%s\';" % (request.form['query']))
                
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var1)
                    
                except:
                    print("nothing")
                
            except:
                print("nothing")
        
        
        if not results:
            try:
                cur.execute("select population from country where code = \'%s\';" % (request.form['query']))
                
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var1)
                    
                except:
                    print("nothing")
                
                
            except:
                print("nothing")   
                
        if not results:
            try:
                cur.execute("select population from country where continent = \'%s\';" % (request.form['query']))
             
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var1)
                    
                except:
                    print("nothing")
             
            except:
                print("nothing")
    
        #Check if it is a city
        if not results:
            try:
                
                cur.execute("select population from city where name = \'%s\' ;" % (request.form['query']))
                print("Pop only")
    
                #If it is, grab the results
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var6)
                    
                except:
                    print("nothing")
                
            except:
                print("Not a city")
            
            
        #If the Query was invalid
        if not results:
            try:    
                results = cur.fetchall()
            except:
                results = ""
        
        #Render in case it was an invalid query so we don't crash
        return render_template('results.html', posts=results, var=var6)

    # Only Code
    elif request.form.get('name') != 'Show Name' and  request.form.get('population')  != 'Show Population' and request.form.get('countrycode') == 'Show Country Code':
        
        #First check if it's a country
        try:
            cur.execute("select code from country where name = \'%s\';" % (request.form['query']))
            print("Code only")
            
            #If it is, grab the results
            try: 
                results = cur.fetchall()
                #return render_template('results.html', posts=results)#, var=var7)
                
            except:
                print("nothing")
        
            
        except:
            print("Not a country")
    
        if not results:
            try:
                cur.execute("select code from city where countrycode = \'%s\';" % (request.form['query']))
            
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var1)
                    
                except:
                    print("nothing")
            
            except:
                print("nothing")
        
        
        if not results:
            try:
                cur.execute("select code from country where code = \'%s\';" % (request.form['query']))
            
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var1)
                    
                except:
                    print("nothing")
            
            except:
                print("nothing")   
                
        if not results:
            try:
                cur.execute("select code from country where continent = \'%s\';" % (request.form['query']))
                
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var1)
                    
                except:
                    print("Non continent")
            
            except:
                print("nothing")
        
        #Check if it is a city
        if not results:
            try:
                
                cur.execute("select countrycode from city where name = \'%s\' ;" % (request.form['query']))
                
                #If it is, grab the results
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var7)
                    
                except:
                    print("nothing")
                
            except:
                print("Not a city")
        if not results:
            
            #If the Query was invalid
            try:    
                results = cur.fetchall()
            except:
                results = ""
        
        #Render in case it was an invalid query so we don't crash
        
        return render_template('results.html', posts=results, var=var7)

    
    #Just show everything by default if no boxes are checked
    else:
        
        print('mother fucker ' + request.form['query'])
       
        #First check if it's a country
        try:
            cur.execute("select name, code, population from country where name = \'%s\';" % (request.form['query']))
            
            
            #If it is, grab the results
            try: 
                results = cur.fetchall()
                #return render_template('results.html', posts=results)#, var=var1)
                
            except:
                print("nothing")
        
            
        except:
            print("Not a country")
    
        #Check if it is a city
        if not results:
            try:
                
                cur.execute("select name, countrycode, population from city where name = \'%s\' ;" % (request.form['query']))
                
                #If it is, grab the results
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var1)
                    
                except:
                    print("nothing")
                
            except:
                print("Not a city")
        
        if not results:
            try:
                cur.execute("select name, countrycode, population from city where countrycode = \'%s\';" % (request.form['query']))
                
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var1)
                    
                except:
                    print("nothing")
                
            except:
                print("nothing")
        
        
        if not results:
            try:
                cur.execute("select name, code, population from country where code = \'%s\';" % (request.form['query']))
            
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var1)
                    
                except:
                    print("nothing")
            
            except:
                print("nothing")   
                
        if not results:
            try:
                cur.execute("select name, code, population from country where continent = \'%s\';" % (request.form['query']))
                
                try: 
                    results = cur.fetchall()
                    #return render_template('results.html', posts=results)#, var=var1)
                    
                except:
                    print("nothing")
            
            
            except:
                print("nothing")
        
        if not results:
            #If the Query was invalid
            try:    
                results = cur.fetchall()
            except:
                results = ""
        
        #Render in case it was an invalid query so we don't crash
        return render_template('results.html', posts=results, var=var1)

@app.route('/')
def mainIndex():
	return render_template('index.html')



# start the server
if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=8080)