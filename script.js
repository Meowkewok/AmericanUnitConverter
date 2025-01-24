const input = document.createElement('input');
const dropdown = document.createElement('select');
const toBox = document.createElement('output');
toBox.textContent = 'to ';
const dropdown2 = document.createElement('select');
const output = document.createElement('output');
let disnum

document.body.appendChild(input);
document.body.appendChild(dropdown);
document.body.appendChild(toBox);
document.body.appendChild(dropdown2);
document.body.appendChild(output);
dropdown.appendChild(new Option('Meters'));
dropdown.appendChild(new Option('Centimeters'));
dropdown.appendChild(new Option('Milimeters'));
dropdown.appendChild(new Option('Bananas'));
dropdown.appendChild(new Option('Cadillac Escalades'));
dropdown.appendChild(new Option('Ford F-150s'));
dropdown.appendChild(new Option('(American) Football Field'))
dropdown2.appendChild(new Option('Meters'));
dropdown2.appendChild(new Option('Centimeters'));
dropdown2.appendChild(new Option('Milimeters'));
dropdown2.appendChild(new Option('Bananas'));
dropdown2.appendChild(new Option('Cadillac Escalades'));
dropdown2.appendChild(new Option('Ford F-150s'));
dropdown2.appendChild(new Option('(American) Football Field'))

const escalade = 5052;
const f150 = 5884;
const banana = 178;
const fballf = 109728;

setInterval(convert, 100)

function convert() {
    if (dropdown.value == 'Meters') {
        if (dropdown2.value == 'Cadillac Escalades') {
            disnum = input.value * 1000 / escalade;
        }
        else if (dropdown2.value == 'Ford F-150s') {
            disnum = input.value * 1000 / f150;
        }
        else if (dropdown2.value == 'Bananas') {
            disnum = input.value * 1000 / banana;
        } 
        else if (dropdown2.value == 'Meters') {
            disnum = input.value;
        }
        else if (dropdown2.value == 'Centimeters') {
        disnum = input.value * 100;
        }
        else if (dropdown2.value == 'Milimeters') {
            disnum = input.value * 1000;
        }
        else if (dropdown2.value == '(American) Football Field') {
            disnum = input.value * 1000 / fballf;            
        }
    }
    else if (dropdown.value == 'Centimeters') {
        if (dropdown2.value == 'Cadillac Escalades') {
            disnum = input.value * 10 / escalade;
        }
        else if (dropdown2.value == 'Ford F-150s') {
            disnum = input.value * 10 / f150;
        }
        else if (dropdown2.value  == 'Bananas') {
            disnum = input.value * 10 / banana;
        }
        else if (dropdown2.value == 'Meters') {
            disnum = input.value / 100;
        }
        else if (dropdown2.value == 'Centimeters') {
            disnum = input.value;
        }
        else if (dropdown2.value == 'Milimeters') {
            disnum = input.value * 10;
        }
        else if (dropdown2.value == '(American) Football Field') {
            disnum = input.value * 10 / fballf;            
        }
    }
    else if (dropdown.value == 'Milimeters') {
        if (dropdown2.value == 'Cadillac Escalades') {
            disnum = input.value / escalade;
        }
        else if (dropdown2.value == 'Ford F-150s') {
            disnum = input.value / f150;
        }
        else if (dropdown2.value == 'Bananas') {
            disnum = input.value / banana;
        }
        else if (dropdown2.value == 'Meters') {
            disnum = input.value * 1000;
        }
        else if (dropdown2.value == 'Centimeters') {
            disnum = input.value * 10;
        }
        else if (dropdown2.value == 'Milimeters') {
            disnum = input.value;
        }
        else if (dropdown2.value == '(American) Football Field') {
            disnum = input.value / fballf;            
        }
    }
    else if (dropdown.value == 'Cadillac Escalades') {
        if (dropdown2.value == 'Cadillac Escalades') {
            disnum = input.value;
        }
        else if (dropdown2.value == 'Ford F-150s') {
            disnum = input.value * escalade / f150;
        }
        else if (dropdown2.value == 'Bananas') {
            disnum = input.value * escalade / banana;
        } 
        else if (dropdown2.value == 'Meters') {
            disnum = input.value * escalade / 1000;
        }
        else if (dropdown2.value == 'Centimeters') {
            disnum = input.value * escalade / 10;
        }
        else if (dropdown2.value == 'Milimeters') {
            disnum = input.value * escalade;
        }
        else if (dropdown2.value == '(American) Football Field') {
            disnum = input.value * escalade / fballf;            
        }
    }
    else if (dropdown.value == 'Ford F-150s') {
        if (dropdown2.value == 'Cadillac Escalades') {
            disnum = input.value * f150 / escalade;
        }
        else if (dropdown2.value == 'Ford F-150s') {
            disnum == input.value;
        }
        else if (dropdown2.value == 'Bananas') {
            disnum = input.value * f150 / banana;
        } 
        else if (dropdown2.value == 'Meters') {
            disnum = input.value * f150 / 1000;
        }
        else if (dropdown2.value == 'Centimeters') {
            disnum = input.value * f150 / 10;
        }
        else if (dropdown2.value == 'Milimeters') {
            disnum = input.value * f150
        }
        else if (dropdown2.value == '(American) Football Field') {
            disnum = input.value * f150 / fballf;            
        }
    }
    else if (dropdown.value == 'Bananas') {
        if (dropdown2.value == 'Cadillac Escalades') {
            disnum = input.value * banana / escalade;
        }
        else if (dropdown2.value == 'Ford F-150s') {
            disnum = input.value * banana / f150;
        }
        else if (dropdown2.value == 'Bananas') {
            disnum = input.value;
        } 
        else if (dropdown2.value == 'Meters') {
            disnum = input.value * banana / 1000;
        }
        else if (dropdown2.value == 'Centimeters') {
            disnum = input.value * banana / 10;
        }
        else if (dropdown2.value == 'Milimeters') {
            disnum = input.value * banana;
        }
        else if (dropdown2.value == '(American) Football Field') {
            disnum = input.value * banana / fballf;            
        }
    }
    else if (dropdown.value == '(American) Football Field') {
        if (dropdown2.value == 'Cadillac Escalades') {
            disnum = input.value * fballf / escalade;
        }
        else if (dropdown2.value == 'Ford F-150s') {
            disnum = input.value * fballf / f150;
        }
        else if (dropdown2.value == 'Bananas') {
            disnum = input.value * fballf / banana;
        } 
        else if (dropdown2.value == 'Meters') {
            disnum = input.value * fballf / 1000;
        }
        else if (dropdown2.value == 'Centimeters') {
            disnum = input.value * fballf / 10;
        }
        else if (dropdown2.value == 'Milimeters') {
            disnum = input.value * fballf;
        }
        else if (dropdown2.value == '(American) Football Field') {
            disnum = input.value;
        }
    }
    output.textContent = disnum
}