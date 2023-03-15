const hamburger = document.getElementById("hamburger")
const menu = document.getElementById("menu")
const b1 = document.getElementById("b-1")
const b2 = document.getElementById("b-2")
const b3 = document.getElementById("b-3")

hamburger.addEventListener("click",()=>{
    b1.classList.toggle("b-1")
    b2.classList.toggle("b-2")
    b3.classList.toggle("b-3")
    menu.classList.toggle("show")
})

const body = document.getElementById("body")
const header = document.getElementById("header")

body.onscroll = ()=>{
    header.style.padding = "0 0 1rem 0"
}