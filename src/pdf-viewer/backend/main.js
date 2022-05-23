window.addEventListener('pywebviewready', function() {
    
    console.log("pywebview is ready!")

    var book_content = pywebview.api.get_content(); // The API return a promise object
    // console.log(book_content);
    var read_zone = document.getElementsByClassName('read-zone');

    // If the promise object is fulfilled, it'll return the value to the function
    book_content.then(function(value) {
        for (var i = 0; i < value.length; i++) {
            read_zone[0].innerHTML += value[i];
        }
    });
})