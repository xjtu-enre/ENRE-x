// 直接调用
let addModule = require('./example_1.js');
    addModule.onRuntimeInitialized = function() {
        console.log(addModule._add(5,6))
        console.log(addModule._hello());
        console.log(addModule._sayhi());
}
