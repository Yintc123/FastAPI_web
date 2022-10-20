import * as url from './url_module.js';

console.log("hi modify order")

const submit_button=document.querySelector('#submit_button');

submit_button.addEventListener('click', async ()=>{
    const input_order_id = document.querySelector('#order_id').value;
    window.location = url.url_mode['url_order_id'] + input_order_id;
})