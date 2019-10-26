const zerorpc = require("zerorpc")
let client = new zerorpc.Client()
client.connect("tcp://127.0.0.1:4242")
console.log("Renderer started")
client.on("error", function(error) {
    console.error("RPC client error:", error);
});

let ip = document.querySelector('#ip')
let subnet = document.querySelector('#subnet')
let result1 = document.querySelector('#start_results')
let result2 = document.querySelector('#end_results')
let booton = document.getElementById('booton')
console.log("Queries and elements found")
booton.addEventListener('click', () => {
    console.log("Event happening")
    client.invoke("calc", ip.value, subnet.value, (error, combined) => {
    if(error) {
      console.error(error)
    } else {
      
      //var res=combined.toString().split("+")//combined is a location object, needs a string conversion
      var all=combined.toString().split(",")
      var res1=all.slice(0,all.indexOf('+'))
      var res2=all.slice(all.indexOf('+')+1)
      //console.log(res)
      //result1.textContent = res[0] //combined is of type object. Either figure out how to split this, or interleave IPs
      //result2.textContent = res[1]
      // document.getElementById('start_results').reset()
      // document.getElementById('end_results').reset()
      
      var div1=document.getElementById('start_results')
      while(div1.firstChild){div1.removeChild(div1.firstChild);}
      var div2=document.getElementById('end_results')
      while(div2.firstChild){div2.removeChild(div2.firstChild);}
      
      document.getElementById('start_results').appendChild(makeUL(res1));
      document.getElementById('end_results').appendChild(makeUL(res2));
      //document.getElementById('end_results').appendChild(makeUL(res[1]));
    }
  })
  
})
function makeUL(array) {
  // Create the list element:
  var list = document.createElement('ul');
  list.setAttribute("class","list-unstyled row")
  // list.setAttribute("width","10%")
  //list.setAttribute("float","left")
  for(var i = 0; i < array.length; i++) {
      // Create the list item:
      var item = document.createElement('li');
      item.setAttribute("class","list-group-item col-12")
      item.setAttribute("float","left")
      // Set its contents:
      item.appendChild(document.createTextNode(array[i]));

      // Add it to the list:
      list.appendChild(item);
  }

  // Finally, return the constructed list:
  return list;
}
ip.dispatchEvent(new Event('input'))