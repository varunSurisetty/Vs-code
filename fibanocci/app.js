console.log('Hello World');
// program to generate fibonacci series up to n terms

// take input from the user
const number = 100
let n1 = 0, n2 = 1, nextTerm;


for (let i = 1; i <= 100; i++) {
    console.log(n1);
    nextTerm = n1 + n2;
    n1 = n2;
    n2 = nextTerm;
}
