// websockets logic

var sock = io.connect('http://' + document.domain + ':' + location.port);
sock.on('connect', function()
        {
          socket.emit('my event', {data: 'Imma connected !'});
        });

