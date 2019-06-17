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
        const li = document.createElement('li');
        li.innerHTML = `Vote Recorded : ${data.selection}`;
        document.querySelector("#votes".append(li))
    } )    

})