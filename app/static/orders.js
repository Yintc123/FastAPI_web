import * as order from './order_module.js';
import * as url from './url_module.js';

let orders=null;

async function init(){
    // AJAX，拿取所有訂單資訊
    orders = await order.get_orders();
    // 將訂單資訊以 Table 的方式顯示
    add_order_to_table(orders);
}

// 將訂單資訊加入 Table
function add_order_to_table(orders){
    const table_orders = document.querySelector('#tbody_orders');

    for(let i=0;i<orders.length;i++){
        const tr = create_tr(orders[i]);
        table_orders.append(tr);
    }

    return table_orders;
}
// 建立 table 的列
function create_tr(order){
    const order_info = ["order_id", "customer_name", "product_name", "price", "amount", "total"];
    const tr_order = document.createElement('tr');
    tr_order.style.order = order.order_id;
    tr_order.className = "text-center";
    
    for(let i=0;i<order_info.length;i++){
        const td = create_td(order[order_info[i]]);
        if(order_info[i] == "order_id"){
            td.textContent = "";
            const a = create_a(order[order_info[i]]);
            td.append(a);
        }
        tr_order.append(td);
    }

    return tr_order;
}
// 建立列的單格並填入資料
function create_td(info){
    const td_info = document.createElement('td');
    td_info.textContent=info;
    return td_info;
}
// 建立超連結
function create_a(info){
    const a = document.createElement('a');
    a.href = url.url_mode['url_order_id'] + info;
    a.textContent = info;
    return a;
}

init();