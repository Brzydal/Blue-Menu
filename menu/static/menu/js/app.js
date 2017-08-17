
$(document).ready(function () {
$("#myTable").tablesorter()


let client = new coreapi.Client()
let schema = null
client.get("http://127.0.0.1:8000/cardsAPI/").then(function(data) {
    // Load a CoreJSON API schema.
    schema = data
    console.log('schema loaded')
    console.log(schema)
})



});
