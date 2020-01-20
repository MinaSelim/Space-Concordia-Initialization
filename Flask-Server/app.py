from flask import Flask
import serial

app = Flask(__name__)

ser = serial.Serial("COM4")

@app.route('/')
def index():
   return (
      """<h1>Hello To the Ardunio manipulation app</h1>
         <a href="/on">ON   </a> <a  href="/off"> OFF</a>
      """
      )
      

@app.route('/on')
def indexOn():
   ser.write(b'1')
   return (
      """<h1>Hello To the Ardunio manipulation app</h1>
         <a href="/on">ON   </a> <a  href="/off"> OFF</a>
      """
      )

@app.route('/off')
def indexOff():
   ser.write(b'0')
   return (
      """<h1>Hello To the Ardunio manipulation app</h1>
         <a href="/on">ON   </a> <a  href="/off"> OFF</a>
      """
      )