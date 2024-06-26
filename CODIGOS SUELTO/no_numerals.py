text = 'i need 2 pumkins and 3 apples'

for i in text:
    match i:
        case '1':
            text = text.replace('1', 'one')
        case '2':
            text = text.replace('2', 'two')
        case '3':
            text = text.replace('3', 'three')
        case '4':
            text = text.replace('4', 'four')
        case '5':
            text = text.replace('5', 'five')
        case '6':
            text = text.replace('6', 'six')
        case '7':
            text = text.replace('7', 'seven')
        case '8':
            text = text.replace('8', 'eight')
        case '9':
            text = text.replace('9', 'nine')