//Write a function for reversing numbers in binary. For instance, the binary representation of 13 is 1101, and reversing it gives 1011, which corresponds to number 11.

//1 solution

function dec_bin(num) {

    //decNumber is a number that needs to convert
    let decNumber = 13;

    let binaryNumber = "";

    //To find a binary number I calculate the remainder of a quotient after division

    // 13/2 = 6(1)
    // 6/2 = 3(0)
    // 3/2 = 1(1)
    // 1/2=0(1)

    //1011

    while (decNumber != 0) {
        let rest = decNumber % 2;
        decNumber = (decNumber - rest) / 2;
        binaryNumber = rest + binaryNumber;
    }

    //reverse the resultat
    let reverseBinaryNumber = binaryNumber.split('').reverse().join('');
    //1101

    //convert to Integer number
    return parseInt(reverseBinaryNumber, 2);
    //11

}


console.log(dec_bin(13));




//2 solution 

function reversToBin(num) {
    return (num >>> 0).toString(2);
}

console.log(reversToBin(13).split('').reverse().join(''));

