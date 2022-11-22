function getInformation(id, publicKey) {
  const stripe = Stripe(publicKey);
  fetch("/buy/"+id)
      .then((response) => { return response.json()})
      .then((data) => {
        return stripe.redirectToCheckout({sessionId: data.sessionId})
          }
      )
}
