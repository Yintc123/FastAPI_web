console.log("hi")
import * as order from './order_module.js';

const submit_button=document.querySelector('#submit_button');
const button_modify = document.querySelector('#button_modify');
let order_id = null;

async function init(){
    const url_current = document.URL;

    show_button(is_query_string_existed(url_current));

    if(is_query_string_existed(url_current)){
        order_id = url_current.split("=")[1];
        const order_info = await order.get_order(order_id);
        if(!order_info){
            window.location = '/';
        }
        fill_out_form(order_info);
    }
}

submit_button.addEventListener('click', ()=>{
    let name = document.querySelector('#customer_name').value;
    let product = document.querySelector('#product_name').value;
    let price = document.querySelector('#price').value;
    let amount = document.querySelector('#amount').value;
    
    const order_info = [name, product, price, amount];
    check_inputed_value(order_info);

    order.create_order(name, product, price, amount).then(resp => {
        if (!resp.ok || resp.detail){
            show_error();
            return;
        }
        window.location = "/"
    })
})

button_modify.addEventListener('click', async ()=>{
    let name = document.querySelector('#customer_name').value;
    let product = document.querySelector('#product_name').value;
    let price = document.querySelector('#price').value;
    let amount = document.querySelector('#amount').value;

    order.modify_order(name, product, price, amount, order_id).then(resp => {
        if(resp.ok){
            alert("modify the order successfully.")
        }
    })
})

function check_inputed_value(data_info){
    for(let i=0;i<data_info.length;i++){
        if (!data_info[i]){
            show_error();
            return "please fill all of columns.";
        } 
    }
}

function show_error(){
    const error_message = document.querySelector('#error_message');
    error_message.style.display = 'block';
    error_message.textContent = "Please fill out the form or fill in the correct values.";
}

function is_query_string_existed(url){
    let splited_url = url.split("?");
    if(splited_url.length != 1){
        return true;
    }
    return false;
}

function show_button(is_query_string_existed){
    if(is_query_string_existed==true){
        submit_button.style.display = "none";
        return;
    }
    button_modify.style.display = "none";
    return;
}

function fill_out_form(order_info){
    let form_titles = ["customer_name", "product_name", "amount", "price"];

    for(let i=0;i<form_titles.length;i++){
        let form_info = document.querySelector('#'+form_titles[i]);
        form_info.value = order_info[form_titles[i]];
    }
}

init();