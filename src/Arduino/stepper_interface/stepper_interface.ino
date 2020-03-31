#include <AccelStepper.h>

const int stepsPerRevolution = 6400;
const double wheelCircumference = 8.66; // inches
const double maxLinearSpeed = 43.28; // inches / second
const double conversionToStepPerSecond = (1/wheelCircumference) * stepsPerRevolution; // converts from in/s to step/s

double leftSpeed = 0;
double rightSpeed = 0;

char side = 'l';


AccelStepper left(1, 3, 2); // pin 3 = step, pin 6 = direction
AccelStepper right(1, 12, 11); // pin 4 = step, pin 7 = direction

void setup() {
  right.setMaxSpeed(maxLinearSpeed * conversionToStepPerSecond);
  left.setMaxSpeed(maxLinearSpeed * conversionToStepPerSecond);
  right.setSpeed(0);
  left.setSpeed(0);
  Serial.begin(9600);
}

void loop() {
   static char buffer[32];
   static size_t pos;
   if (Serial.available()) {
      char c = Serial.read();
      if (c == 'l') {
        side = 'l';
      } else if (c == 'r') {
        side = 'r';
      } else if (c == '\n') {  // on end of line, parse the number
         buffer[pos] = '\0';
         double value = atof(buffer);
         if (side == 'l') {
          setWheelSpeed(value, rightSpeed);
         } else if (side == 'r') {
          setWheelSpeed(leftSpeed, value);
         }
         pos = 0;
      } else if (pos < sizeof buffer - 1) {  // otherwise, buffer it
         buffer[pos++] = c;
      }
   }
   right.runSpeed();
   left.runSpeed();
}

// inputs in inches/second
void setWheelSpeed(double tempLeftSpeed, double tempRightSpeed) {
  leftSpeed = tempLeftSpeed;
  rightSpeed = tempRightSpeed;
  left.setSpeed(leftSpeed * conversionToStepPerSecond);
  right.setSpeed(-rightSpeed * conversionToStepPerSecond);
}
