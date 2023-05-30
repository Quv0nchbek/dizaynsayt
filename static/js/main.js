let search = document.querySelector('.search-box');

document.querySelector('#search-icon').onclick = ()=>{
        search.classList.toggle('active');  
        navbar.classList.reomve('active'); 
}

let navbar = document.querySelector('.navbar');

document.querySelector('#menu-icon').onclick = ()=>{
        navbar.classList.toggle('active'); 
        search.classList.reomve('active');   
}

window.onscroll = () => {
        navbar.classList.reomve('active');
        search.classList.reomve('active');

}




let header = document.querySelector('header');

window.addEventListener('scroll' , () => {
        header.classList.toggle('shadow', window.scrollY > 0);
}


)