"use strict";
/*global print, ice, Array*/


function queueMe(response) {
    print("Defined function called: " + response + "\n");
}

function onLoad() {
    print("onLoad start");
    print(new Array(30).join("="));

    ice.enqueue("named function", queueMe);

    ice.enqueue("anonymous function", function () {
        print("Ran anonymous function.");
    });

    ice.enqueue("anonymous function with data", function (reply) {
        print("Anonymous function with data passed: " + reply);
    });

    print(new Array(30).join("="));
    ice.processResponses();

    print("onLoad done");
    print(new Array(30).join("="));
}
