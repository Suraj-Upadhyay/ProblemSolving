// You can write anonymous functions this way ->
    // const myFunc = function() {
    //     const myVar = "value";
    //     return myVar;
    // }
// But es6 gives you another way to write anonymous functions.
    // const magic = () => {
    //     'use strict';
    //     return new Date();
    // }
// Now, if you just have a return statement in your function body.
// You can write like this.

const magic = () =>  new Date();

// NOTE:- the holding variables for anonymous functions should be const.
