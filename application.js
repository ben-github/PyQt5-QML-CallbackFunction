function queueMe(response)
{
    console.log('Enqueued Function Called: ' + response + "\n");
}

function onLoad()
{
    console.log("onLoad start==================")

	ice.enqueue('#version 1', 1, queueMe);
    console.log("     =========================")
	ice.processResponses();

    console.log("onLoad done==================")
}
