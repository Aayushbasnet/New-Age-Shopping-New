
console.log("Cart here")

var updateBtns = document.getElementsByClassName("update-cart")

for (var i =0; i<updateBtns.length; i++)
{
    updateBtns[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action)

        console.log('USER:', user)
        if(user == "AnonymousUser")
        {
            addCookieItem(productId, action)
        }
        else
        {
            updateUserOrder(productId, action)
        }
    }) 

}

function addCookieItem(productId, action){

}

function updateUserOrder(productId, action)
{
    console.log("User logged in and sending data")

    var url = '/update_item/'

    //sending post data to backend
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action':action})

    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        location.reload()
        console.log('Data:',data)
    })
}



//Increase and decrease cart
// const increaseProductQuantity = (product) => {
//     const productId = $(product).parents('.product').get(0).id
//     const price = $.grep(productsInCart, el => { return el.id == productId })[0].get_total;
  
//     $.each(storageData, (i, el) => {
//       if (el.id == productId) {
//         el.itemsNumber += 1
//         $(product).siblings('.quantity').val(el.itemsNumber);
//         $(`#${productId}`).find('.price').html(`$${(price * el.itemsNumber).toFixed(2)}`);
//         $(`#${productId}-dropdown`).find('.price').html(`$${(price * el.itemsNumber).toFixed(2)}`);
//       }
//     });
  
//     updateCart();
//   }
  
//   const subtractProductQuantity = (product) => {
//     const productId = $(product).parents('.product').get(0).id
//     const price = $.grep(productsInCart, el => { return el.id == productId })[0].price;
//     let itemsInCart = $.grep(productsInCart, el => { return el.id == productId })[0].itemsNumber;
  
//     if (itemsInCart > 0 ) {
//       storageData.map( el => {
//         if (el.id == productId) {
//           el.itemsNumber -= 1
//           $(product).siblings('.quantity').val(el.itemsNumber)
//           $(`#${productId}`).find('.price').html(`$${(price * el.itemsNumber).toFixed(2)}`);
//           $(`#${productId}-dropdown`).find('.price').html(`$${(price * el.itemsNumber).toFixed(2)}`);
//         }
//       });
  
//       updateCart();
//     };
//   }
  
//   const removeProduct = (product) => {
//     const productId = $(product).parents('.product').get(0).id
  
//     storageData = $.grep(storageData, (el, i) => {
//       return el.id != productId
//     });
  
//     updateCart();
//     updateProductList();
//   }