// cwrap
let addModule = require('./example_3.js');
let add = addModule.cwrap('add', 'number', ['number','number']);
let hello = addModule.cwrap('hello', 'null', 'null');
let sayhi = addModule.cwrap('sayhi', 'string');
    addModule.onRuntimeInitialized = function() {
        console.log(add(1,2))
        console.log(hello())
        console.log(sayhi())
        
}