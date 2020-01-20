from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
   return (
      """<h1>Hello To the Ardunio manipulation app</h1>
         <a href="/on">ON   </a> <a  href="/off"> OFF</a>
      """
      )
      

@app.route('/on')
def indexOn():
   return (
      """<h1>Hello To the Ardunio manipulation app</h1>
         <a href="/on">ON   </a> <a  href="/off"> OFF</a>
      """
      )

@app.route('/off')
def indexOff():
   return (
      """<h1>Hello To the Ardunio manipulation app</h1>
         <a href="/on">ON   </a> <a  href="/off"> OFF</a>
      """
      )