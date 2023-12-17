const openmodal=document.getElementById("open");
const modal=document.getElementById("modal");
const cerrar=document.getElementById("cancelar");

openmodal.addEventListener("click" ,(e) =>{
    e.preventDefault();
    modal.showModal();
})

cerrar.addEventListener("click" ,(e) =>{
    e.preventDefault();
    modal.close();
})