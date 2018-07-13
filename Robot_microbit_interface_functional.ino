
#define MPIN1B 5 // motor 1 pin B
#define MPIN1A 6 // motor 1 pin A
#define MPIN2A 9 // motor 2 pin A
#define MPIN2B 10 // motor 2 pin B
// SRF04 pin definitions
#define TRIGGER_PIN A2 // Arduino pin tied to trigger pin on the ultrasonic sensor.
#define ECHO_PIN A3 // Arduino pin tied to echo pin on the ultrasonic sensor.
#define MAX_DISTANCE 200 // Maximum distance we want to ping for (in centimeters).Maximum sensor distance is rated at 400 - 500cm.
#define REDPIN 1
#define GREENPIN 3
#define BLUEPIN 4
//NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); // NewPing setup of pins and maximum distance.
// Variables
int rSpeed = 150; // robot's max speed (used in Move() calculations)
//int TS1 = 75; // turn speed 1
//int FS = 75; // forward speed: the speed at which both motors turn at
// move function - we pass a speed for each wheel m1,m2 - as a percentage 0-100
void Move(int m1, int m2) {
  // for each motor, one pin is held low, the other pin is toggled - this is called sign-magnitude drive
  // the other drive method uses two pwm signals, anitphase to each other and is called locked antiphase
  if (m1 < 0) { // for reverse - not used
    analogWrite(MPIN1A, rSpeed * 1.15 * abs(m1) / 100);
    analogWrite(MPIN1B, 0);
  }
  else
  { // normal operation
    analogWrite(MPIN1A, 0);
    analogWrite(MPIN1B, rSpeed * 1.40 * m1 / 100); //controls speed of left motor increase multiplier to go more right/less left
  }
  if (m2 < 0) { // for reverse - not used
    analogWrite(MPIN2A, rSpeed * abs(m2) / 100);
    analogWrite(MPIN2B, 0);
  }
  else
  { // normal operation
    analogWrite(MPIN2A, 0);
    analogWrite(MPIN2B, rSpeed * m2 / 100);
  }
}
void Stop( int delayms) {
  RGBled(REDPIN, GREENPIN, BLUEPIN, 1, 0, 0); //RED
  Move(0, 0);
  delay(delayms);
}
void Forward(int delayms) {
  RGBled(REDPIN, GREENPIN, BLUEPIN, 0, 1, 0); //GREEN
  Move(-75, -75);
  delay(delayms);
  Move(0, 0);
}
void Reverse(int delayms) {
  RGBled(REDPIN, GREENPIN, BLUEPIN, 0, 0, 1); //BLUE
  Move(75, 75);
  delay(delayms);
  Move(0, 0);
}
void TurnRight(int delayms) {
  RGBled(REDPIN, GREENPIN, BLUEPIN, 1, 1, 0); //YELLOW
  Move(-75, 75);
  delay(delayms);
  Move(0, 0);
}
void TurnLeft(int delayms) {
  RGBled(REDPIN, GREENPIN, BLUEPIN, 0, 1, 1); //CYAN
  Move(75, -75);
  delay(delayms);
  Move(0, 0);
}
void RGBled(int redPin, int greenPin, int bluePin, int redValue, int greenValue, int blueValue) {
  // pinMode(redPin,OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  //digitalWrite(redPin, redValue);
  digitalWrite(greenPin, greenValue);
  digitalWrite(bluePin, blueValue);
}
void activeBuzzer(int pin, int duration_ms) {
  pinMode(pin, OUTPUT);
  digitalWrite(pin, HIGH);
  delay(duration_ms);
  digitalWrite(pin, LOW);
}
void passiveBuzzer(int pin, int duration_ms) {
  pinMode(pin, OUTPUT);
  digitalWrite(pin, HIGH);
  delay(duration_ms);
  digitalWrite(pin, LOW);
}
// Setup - runs once
void setup() {
  Serial.begin(115200); // serial for serial port
  pinMode(MPIN1B, OUTPUT); // set motor pin as output
  pinMode(MPIN1A, OUTPUT); // set motor pin as output
  pinMode(MPIN2A, OUTPUT); // set motor pin as output
  pinMode(MPIN2B, OUTPUT); // set motor pin as output
  digitalWrite(A4, HIGH);
  digitalWrite(A5, HIGH);
  digitalWrite(7, HIGH);
  Stop(2000);
  activeBuzzer(11, 500);
}

// main loop - runs infinetly

void loop () {

  // put your main code here, to run repeatedly: // you chose our variables based on base 2 (binary code)
  int pos1 = digitalRead(A4); // read the pin, if the pin is 5 volts we get a 1; if the pin is ground, we get a 0
  int pos2 = digitalRead(A5);
  int pos4 = digitalRead(7); //we can't use A7 or A6 as they are special- they are anlog input only so the can only read analog
  int command = pos1 | (pos2 << 1) | (pos4 << 2); //This is our logic(Taking 3 variable and making them into one variable)
  //the pipe command is called a bitwise "or" and the << is a bit shift i.e. shift once<<1 (pushes things over) & is our bitwise & 

  
  switch (command) {
    //we'll use a switchcase ( it's a compound if statement)
    case 0: //Whenever command is o it will follow whatever code
      Stop (0);
      break; // means stop and kicks it out of switch and runs whatever is after this
    case 1: //Whenever command is o it will follow whatever code
      Forward(625); //this is about 10 inches on my kitchen floor - KJM
      // time forward  = desired distance/speec (about 0.016 inches/ms)
      // if you modify this then make sure to add sleep time on the micro:bit
      break;
    case 2:
      Reverse(500);
      break;
    case 3:
      TurnLeft(500);
      break;
    case 4:
      TurnRight(375);
      break;
    case 5:
      activeBuzzer(12, 1); // 12 is the pin number on the pcb( printed circuit board) and 1 is millisecond
      break;
    case 6:
      break;
    case 7:
      break;
  } //END switch

  command = 0; //Set command to stop until we receive the next command
}
