// websockets logic
var socket = io.connect("http://" + document.domain + ':' + location.port);

socket.on('connect', function () {
    socket.emit('connected');
    socket.emit("request");
});

function SocketDebugSend()
{
  console.log("sended debug");
  socket.emit("debug-send", {data: "xddd"});
};

socket.on('params', function (data) {
    console.log('data received + ');
    console.log(data);
});

socket.on("data", function (x) 
{
    console.log(x["temperature"] + ' ' + x["CPU"]);
    socket.emit("request");
});


function debugPrint(xdd)
{
    console.log("lmaooo" + xdd);
}