// Assignment

// Build a basic arithmetic calculator without a frontend

// The calculator should be able to perform basic operations like Addition, Subtraction, Multiplication, & Division

var number1 = window.prompt("Enter your first number: ");
var number2 = window.prompt("Enter your second number: ");

number1 = Number(number1);
number2 = Number(number2);

// addition operation

alert('The result of the addition operation is ' + (number1 + number2));

// subtraction operation

if (number1 > number2){
    alert('The result of the subtraction operation is ' + (number1 - number2));
}

else{
    alert('Your first number must be greater than the second number to have an answer');
}

// multiplication operation

alert('The result of the multiplication operation is ' + (number1 * number2));

// division operation

if (number1 > number2){
    alert('The result of the division operation is ' + (number1 / number2));
}

else{
    alert('Your first number must be greater than the second number to have an answer');
}