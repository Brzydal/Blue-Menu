
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

//var ProperListRender = React.createClass({displayName: "ProperListRender",
//render: function() {
//  return (
//    React.createElement("ul", null,
//      this.props.list.map(function(listValue){
//        return React.createElement("li", null, listValue);
//      })
//    )
//  )
//}
//});
//React.render(React.createElement(ProperListRender, {list: [1,2,3,4,5]}), document.getElementById('proper-list-render1'));
//React.render(React.createElement(ProperListRender, {list: [1,2,3,4,5,6,7,8,9,10]}), document.getElementById('proper-list-render2'));


});
