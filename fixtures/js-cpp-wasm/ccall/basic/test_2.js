// ccall
let addModule = require('./example_2.js');
    addModule.onRuntimeInitialized = function() {
        console.log(addModule.ccall('add', 'number', ['number','number'], [1,2]));
        console.log(addModule.ccall('hello'));
        console.log(addModule.ccall('sayhi', 'string'));
}