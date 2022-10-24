const domain_name = 'orders.yin888.info'

const url={
    "dev":{
        "url_order_id":"http://127.0.0.1:6060/?order_id=",
        "url_api_order":"http://127.0.0.1:6060/api/order",
        "url_api_get_orders":"http://127.0.0.1:6060/api/orders",
    },
    "prod":{
        "url_order_id":"https://" + domain_name +"/?order_id=",
        "url_api_order":"https://" + domain_name +"/api/order",
        "url_api_get_orders":"https://" + domain_name +"/api/orders",
    }
}
// 生產模式
const env="prod";
// 開發模式
// const env="dev";

export const url_mode=url[env];
export default url_mode;