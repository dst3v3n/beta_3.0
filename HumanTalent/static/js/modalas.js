const openas=document.getElementById("openas");
const modalas=document.getElementById("modalas");
const cerraras=document.getElementById("cancelaras");

openas.addEventListener("click" ,(e) =>{
    e.preventDefault();
    modalas.showModal();
})

cerraras.addEventListener("click" ,(e) =>{
    e.preventDefault();
    modalas.close();
})