
let socket = new WebSocket('ws://localhost:8000/ws/notification/')

socket.onmessage = function(event){
     var data = JSON.parse(event.data)
     console.log(data)
     document.querySelector('#app').innerText = data.message
}