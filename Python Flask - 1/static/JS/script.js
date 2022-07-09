function activeURL(){
    var path = window.location.pathname;
        path = path.substring(1, path.length - 1);
    if(path !='/'){
        var links = document.getElementsByClassName('nav-link');
        for(var i = 0; i < links.length; i++){
            var text = links[i].innerText;
            if(path.toLowerCase() == text.toLowerCase()){
                links[i].classList.add('active');
            }else{
                links[i].classList.remove('active');
            }
        }
    }
}