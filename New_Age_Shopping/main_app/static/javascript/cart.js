
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

