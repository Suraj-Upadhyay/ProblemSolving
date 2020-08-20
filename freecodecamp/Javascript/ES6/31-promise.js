// Handle a rejected promise with the catch method.

const makeServerRequest = new Promise((resolve, reject) => {
  // responseFromServer is set to false to represent an unsuccessful response from a server
  let responseFromServer = false;
    
  if(responseFromServer) {
    resolve("We got the data");
  } else {  
    reject("Data not received");
  }
});

makeServerRequest.then(result => {
  console.log(result);
});

// The error parameter comes from the argument given to reject method.
makeServerRequest.catch(error => {
  console.log(error);
});

