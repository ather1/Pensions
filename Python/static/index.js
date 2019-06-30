document.addEventListener('DOMContentLoaded',()=>{

    //Connect to the socket
    var socket = io.connect(location.protocol+'//'+document.domain+'//' + document.port);

    //when web socket is connected
    socket.on('connect', ()=>{
        // each button should emit a 'submit vote' event 
        document.querySelectorAll('button').forEach(button => {
            button.onclick = () => {
                const selection = button.dataset.vote;
                socket.emit('submit vote',{'selection':selection});
            };
        });

    });

    socket.on('announce vote', data =>{
        document.querySelector("#yes").innerHTML = data.yes;
        document.querySelector("no").innerHTML=data.no;    
        document.querySelector("maybe").innerHTML= data.maybe
    } )    

})