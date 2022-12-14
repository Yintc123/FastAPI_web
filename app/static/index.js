import * as order from './order_module.js';

const submit_button=document.querySelector('#submit_button');
const button_modify = document.querySelector('#button_modify');
let order_id = null;

async function init(){
    const url_current = document.URL;

    // 根據有無 query string 顯示不同按鈕，有 query string 顯示修改訂單按鈕；無 query string 顯示新增訂單按鈕
    show_button(is_query_string_existed(url_current));

    // 網址是否有帶 query string
    if(is_query_string_existed(url_current)){
        // 訂單編號為 = 後的值
        order_id = url_current.split("=")[1];
        // AJAX，拿取訂單資訊
        const order_info = await order.get_order(order_id);
        // 如果無訂單資訊
        if(!order_info){
            // 返回首頁
            window.location = '/';
        }
        // 有訂單資訊，將其填入表單
        fill_out_form(order_info);
    }
}

submit_button.addEventListener('click', ()=>{
    let name = document.querySelector('#customer_name').value;
    let product = document.querySelector('#product_name').value;
    let price = document.querySelector('#price').value;
    let amount = document.querySelector('#amount').value;
    
    const order_info = [name, product, price, amount];
    // 檢查訂單資訊是否皆填寫
    check_inputed_value(order_info);
    // AJAX，將創建訂單的請求傳至 Server
    order.create_order(name, product, price, amount).then(resp => {
        // 當回應並非 ok 或是有 detail
        if (!resp.ok || resp.detail){
            // 顯示錯誤訊息
            show_error();
            return;
        }
        // 創建完訂單返回首頁
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

// 檢查表單的輸入資訊
function check_inputed_value(data_info){
    for(let i=0;i<data_info.length;i++){
        if (!data_info[i]){
            show_error();
            return "please fill all of columns.";
        } 
    }
}

// 顯示錯誤訊息
function show_error(){
    const error_message = document.querySelector('#error_message');
    error_message.style.display = 'block';
    error_message.textContent = "Please fill out the form or fill in the correct values.";
}

// 檢查是否有 query string
function is_query_string_existed(url){
    let splited_url = url.split("?");
    if(splited_url.length != 1){
        return true;
    }
    return false;
}

// 根據有無 query string 顯示不同按鈕，有 query string 顯示修改訂單按鈕；無 query string 顯示新增訂單按鈕
function show_button(is_query_string_existed){
    if(is_query_string_existed==true){
        submit_button.style.display = "none";
        return;
    }
    button_modify.style.display = "none";
    return;
}

// 填寫訂單資訊
function fill_out_form(order_info){
    let form_titles = ["customer_name", "product_name", "amount", "price"];

    for(let i=0;i<form_titles.length;i++){
        let form_info = document.querySelector('#'+form_titles[i]);
        form_info.value = order_info[form_titles[i]];
    }
}

init();