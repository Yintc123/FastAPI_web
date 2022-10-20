import * as url from './url_module.js';

export async function get_order(order_id){
    console.log("get an order");
    let url_api_get_order = url.url_mode['url_api_get_order'] + order_id;
    return fetch(url_api_get_order).then(response => {
        return response.json();
    })
}

export async function get_orders(){
    console.log("get all orders");
    const url_api_get_orders = url.url_mode['url_api_get_orders'];
    return fetch(url_api_get_orders).then(response => {
        return response.json();
    })
}

export async function create_order(name, item, price, amount){
    const url_api_create_order=url.url_mode['url_api_create_order'];
    let order_info=[name, item, price, amount];
    let order_titles=["name", "product_name", "price", "amount"];
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

export async function modify_order(name, item, price, amount, order_id){
    console.log("modify");
    let url_api_modify_order = url.url_mode['url_api_modify_order'] + order_id;
    let order_info = [name, item, price, amount];
    let order_titles=["name", "product_name", "price", "amount"];
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