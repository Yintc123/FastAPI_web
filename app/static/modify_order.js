import * as url from './url_module.js';
import * as order from './order_module.js';

console.log("hi modify order")

const submit_button=document.querySelector('#submit_button');

submit_button.addEventListener('click', async ()=>{
    const input_order_id = document.querySelector('#order_id').value;
    const order_info = await order.get_order(input_order_id);

    console.log(order_info)
    if(!order_info || order_info.detail){
        alert("There's no this order, order_id = " + input_order_id + " .");
        return;
    }
    window.location = url.url_mode['url_order_id'] + input_order_id;
})