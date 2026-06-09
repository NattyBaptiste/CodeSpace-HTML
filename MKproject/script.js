function addToCart(product, price){

    let cart = JSON.parse(localStorage.getItem("cart")) || [];

    cart.push({
        product: product,
        price: price
    });

    localStorage.setItem("cart", JSON.stringify(cart));

    alert(product + " added to cart!");
}

function displayCart(){

    let cart = JSON.parse(localStorage.getItem("cart")) || [];

    let output = "";
    let total = 0;

    cart.forEach(item => {

        output += `
        <p>
        ${item.product} - £${item.price}
        </p>
        `;

        total += item.price;
    });

    document.getElementById("cartItems").innerHTML = output;
    document.getElementById("total").innerHTML =
    "Total: £" + total;
}

function registerUser(){

    alert("Registration Successful");
}

function loginUser(){

    alert("Login Successful");
}