let funModule = (() => {
    return {
      isCuteMixin : function(obj) {
        obj.isCute = function() {
          return true;
        };
      },
      singMixin : function(obj) {
        obj.sing = function() {
          console.log("Singing to an awesome tune");
        };
      }
    }
})()

// You can use the above module created to share common behavior of objects
// efficiently, i.e. without creating two isCuteMixin and singMixin functions
