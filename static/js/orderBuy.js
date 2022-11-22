function orderBuy(id, publicKey) {
    const stripe = Stripe(publicKey)
    fetch('buy')
        .then((sessionId) => sessionId.json())
        // .then((data) => console.log(data))
        .then((data) => {return stripe.redirectToCheckout({sessionId: data.sessionId})})
}