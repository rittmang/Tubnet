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
    client.invoke("calc", ip.value, subnet.value, (error, range_start,range_end) => {
    if(error) {
      console.error(error)
    } else {
      result1.textContent = range_start
      result2.textContent = range_end
    }
  })
})
ip.dispatchEvent(new Event('input'))