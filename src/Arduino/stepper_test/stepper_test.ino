#include <AccelStepper.h>

const int stepsPerRevolution = 6400;
const double wheelCircumference = 8.66; // inches
const double maxLinearSpeed = 43.28; // inches / second
const double conversionToStepPerSecond = (1/wheelCircumference) * stepsPerRevolution; // converts from in/s to step/s

double leftSpeed = 0;
double rightSpeed = 0;


AccelStepper right(1, 3, 2); // pin 3 = step, pin 6 = direction
AccelStepper left(1, 12, 11); // pin 4 = step, pin 7 = direction

void setup() {
  right.setMaxSpeed(maxLinearSpeed * conversionToStepPerSecond);
  left.setMaxSpeed(maxLinearSpeed * conversionToStepPerSecond);
  right.setSpeed(0);
  left.setSpeed(0);
  setWheelSpeed(-20, 20);
}

void loop() {  
   right.runSpeed();
   left.runSpeed();
}

// inputs in inches/second
void setWheelSpeed(double tempLeftSpeed, double tempRightSpeed) {
  leftSpeed = tempLeftSpeed;
  rightSpeed = tempRightSpeed;
  left.setSpeed(-leftSpeed * conversionToStepPerSecond);
  right.setSpeed(rightSpeed * conversionToStepPerSecond);
}
