// fetch("/config/")
// .then((result) => { return result.json(); })
// .then((data) => {
//   // Initialize Stripe.js
//   //   console.log('success', data.publicKey)
//   const stripe = Stripe(data.publicKey);
//
//   // Event handler
//   document.querySelector("#submitBtn").addEventListener("click", () => {
//     // Get Checkout Session ID
//     fetch("/create-checkout-session/")
//     .then((result) => { return result.json(); })
//     .then((data) => {
//       console.log(data);
//       // Redirect to Stripe Checkout
//       return stripe.redirectToCheckout({sessionId: data.sessionId})
//     })
//     .then((res) => {
//       console.log(res);
//     });
//   });
// });
function getInformation(id, publicKey) {
  // console.log('information', id, publicKey)
  const stripe = Stripe(publicKey);
  fetch("/buy/"+id)
      // .then((response) => {console.log('id', response)})
      .then((response) => { return response.json()})
      .then((data) => {
        // console.log('data', data, data.sessionId)
        return stripe.redirectToCheckout({sessionId: data.sessionId})
          }
      )
};