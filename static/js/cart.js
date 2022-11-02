// var updateBtn = document.getElementsByClassName('update-cart')

// for (var i = 0; i < updateBtn.length; i++) {
//     updateBtn[i].addEventListener('click', function() {
//         var productId = this.dataset.product
//         var action = this.dataset.action
//         console.log('productId:', productId, 'action:', action)
//         console.log('User:', user)
//         if (user == 'AnonymousUser') {
//             console.log("User not authenticated")
//         } else {
//             updateUserOrder(productId, action)
//         }
//     })
// }

// function updateUserOrder(productId, action) {
//     console.log("user authenticated, sending data....")

//     var url = 'update_item/'
//     fetch(url, {
//             method: 'POST',
//             headers: {
//                 'Content-type': 'application/json',
//             },
//             body: JSON.stringify({ 'productId': productId, 'action': action })
//         })
//         .then((response) => {
//             return response.json();
//         })
//         .then((data) => {
//             console.log('Data:', data)
//         });
// }