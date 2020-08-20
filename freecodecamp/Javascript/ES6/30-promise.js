// You can specify the method which is called when a promise is resolved,
// with the `then` method which takes the value returned from `resolve` method
// as an argument.

const makeServerRequest = new Promise((resolve, reject) => {
  // responseFromServer is set to true to represent a successful response from a server
  let responseFromServer = true;
    
  if(responseFromServer) {
    resolve("We got the data");
  } else {  
    reject("Data not received");
  }
});

// This result comes from the argument given to the resolve method.
makeServerRequest.then(result => {
  console.log(result);
});
