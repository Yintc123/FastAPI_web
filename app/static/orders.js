import * as order from './order_module.js';

console.log("hi orders")
let orders=null;

async function init(){
    orders = await order.get_orders();
    console.log(orders);

    add_order_to_table(orders);
}

function add_order_to_table(orders){
    const table_orders = document.querySelector('#table_orders');

    for(let i=0;i<orders.length;i++){
        const tr = create_tr(orders[i]);
        table_orders.append(tr);
    }

    return table_orders;
}

function create_tr(order){
    const order_info = ["order_id", "customer_name", "product_name", "price", "amount", "total"];
    const tr_order = document.createElement('tr');
    tr_order.className = "text-center";
    
    for(let i=0;i<order_info.length;i++){
        const td = create_td(order[order_info[i]]);
        tr_order.append(td);
    }

    return tr_order
}

function create_td(info){
    const td_info = document.createElement('td');
    td_info.textContent=info;
    return td_info
}

init();