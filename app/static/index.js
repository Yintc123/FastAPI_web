console.log("hi")
import * as order from './order_module.js';

let submit_button=document.querySelector('#submit_button');

submit_button.addEventListener('click', ()=>{
    let name = document.querySelector('#name').value;
    console.log(name);
    order.create_order("tom", "apple", "15", "3").then(resp => {
        console.log(resp);
    })
})