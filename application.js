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
        print("!!!! RAN ME TO ANONYMOUSE");
    });

    ice.enqueue("anonymous function with data", function (reply) {
        print("Data passed: " + reply);
    });

    print(new Array(30).join("="));
    ice.processResponses();

    print("onLoad done");
    print(new Array(30).join("="));
}
