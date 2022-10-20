import * as order from './order_module.js';

console.log("hi orders")
let orders=null;

async function init(){
    orders = await order.get_orders();
    console.log(orders);
}

init();