// A promise has three state, pending, fulfilled and rejected.

const makeServerRequest = new Promise((resolve, reject) => {
  // responseFromServer represents a response from a server
  let responseFromServer;
    
  if(responseFromServer) {
    // Indicate that the promise is resolved.
    resolve("We got the data");
  } else {  
    // Indicate that the promise is rejected.
    reject("Data not received");
  }
});
