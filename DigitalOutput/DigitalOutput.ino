const short LED = LED_BUILTIN;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
}

void flushReadBuffer()
{
  if(Serial.peek() != -1)
  {
    Serial.read();
  }
}

// the loop function runs over and over again forever
void loop() {
    while(!Serial.available());
   
    if(Serial.peek()!= -1)
    {
      char input = Serial.read();
      Serial.read();
      
      if(input == '0'){
        Serial.println("Turning Off LED");
        digitalWrite(LED, LOW);
      }
       else if( input == '1') {
        Serial.println("Turning ON LED");
        digitalWrite(LED, HIGH);
      }
      else {
        if(input != '\n')
        {
          Serial.print(input);
          Serial.println(" is not a valid input");
          Serial.println("1 to turn on LED, 0 to turn off LED");
        }

      }
    }
    flushReadBuffer();
}
