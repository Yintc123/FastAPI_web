console.log("hi")
import * as order from './order_module.js';

const submit_button=document.querySelector('#submit_button');

submit_button.addEventListener('click', ()=>{
    let name = document.querySelector('#name').value;
    let product = document.querySelector('#product').value;
    let price = document.querySelector('#price').value;
    let amount = document.querySelector('#amount').value;
    
    const order_info = [name, product, price, amount];
    check_inputed_value(order_info);

    order.create_order(name, product, price, amount).then(resp => {
        if (resp.ok){
            window.location = "/"
        }
    })
})

function check_inputed_value(data_info){
    for(let i=0;i<data_info.length;i++){
        if (!data_info[i]){
            console.log("hi123")
            const error_message = document.querySelector('#error_message');
            error_message.style.display = 'block';
            error_message.textContent = "Please fill out the form.";
            return "please fill all of columns.";
        } 
    }
}