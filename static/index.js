$(document).ready(function(){
    var socket = io.connect("http://localhost:5000");

    socket.on('message',function(data){
        $('#messages').append($('<p>').text(data));
    });
    
    $('#sendBtn').on("click",function(){
        var message = username + ":" + $('#message').val()
        socket.emit("message",message);
        $("#message").val("");
    });


})