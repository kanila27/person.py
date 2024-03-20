import 'dart:io';

void main() {
  print('please enter a number');
  String? input = Stdin.readLineSync();
  int number = int.parse(input ?? '0');
  if (number > 10) {
    print('your number is greater than 10');
  } else if (number < 10) {
    print('your number is less than 10');
  } else {
    print('your number is equal to 10');
  }
}
