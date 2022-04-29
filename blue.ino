void setup() {
  pinMode(6,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if(Serial.available()>0)
  {
    digitalWrite(6,Serial.read()=='1'? 1:0);
  }
}
