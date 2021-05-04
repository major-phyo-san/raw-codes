Event = require('events');
orderShipped = new Event();
sendShippmentNoti = function (product) {
// product = product;
setImmediate(function(product){
    console.log('inside asynchronous notifier, notify shippment of ' + product + ' products');
});
console.log('shipped ' + product + ' products');
};

orderShipped.on('shipped', sendShippmentNoti);

orderShipped.emit('shipped', 'clothing');