console.log("hi")
import * as order from './order_module.js';

let submit_button=document.querySelector('#submit_button');

submit_button.addEventListener('click', ()=>{
    let name = document.querySelector('#name').value;
    let product = document.querySelector('#product').value;
    let price = document.querySelector('#price').value;
    let amount = document.querySelector('#amount').value;
    order.create_order(name, product, price, amount).then(resp => {
        console.log(resp);
        return;
    })
})