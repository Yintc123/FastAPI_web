import * as url from './url_module.js';

// AJAX，根據訂單編號拿取訂單資訊
export async function get_order(order_id){
    let url_api_get_order = url.url_mode['url_api_order'] + '/' + order_id;
    return fetch(url_api_get_order).then(response => {
        return response.json();
    })
}
// AJAX，拿取所有訂單資訊
export async function get_orders(){
    const url_api_get_orders = url.url_mode['url_api_get_orders'];
    return fetch(url_api_get_orders).then(response => {
        return response.json();
    })
}
// AJAX，創建訂單（POST）
export async function create_order(name, item, price, amount){
    const url_api_create_order=url.url_mode['url_api_order'];
    let order_info=[name, item, price, amount];
    let order_titles=["name", "product_name", "price", "amount"];
    // 建立物件 FormData，將資訊以表單形式傳至 Server
    let form=new FormData()
    for(let i=0;i<order_info.length;i++){
        form.append(order_titles[i], order_info[i]);
    }
    return fetch(url_api_create_order, {
        method:'POST',
        body:form
    }).then(response => {
        return response.json()
    })
}
// AJAX，修改訂單資訊（PATCH）
export async function modify_order(name, item, price, amount, order_id){
    let url_api_modify_order = url.url_mode['url_api_order'] + '/' + order_id;
    let order_info = [name, item, price, amount];
    let order_titles=["name", "product_name", "price", "amount"];
    // 建立物件 FormData，將資訊以表單形式傳至 Server
    let form=new FormData()
    for(let i=0;i<order_info.length;i++){
        form.append(order_titles[i], order_info[i]);
    }
    return fetch(url_api_modify_order, {
        method:'PATCH',
        body:form
    }).then(response => {
        return response.json();
    })
}