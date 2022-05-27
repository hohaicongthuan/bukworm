window.addEventListener('pywebviewready', function() {
    
    console.log("pywebview is ready!");

    var tools = document.getElementsByClassName('tool-item');
    
    // tools[0] is the Open File button
    tools[0].addEventListener('click', function() {
        var file_path = pywebview.api.open_file();
        // console.log('File path is ', file_path);
        file_path.then(function(value) {
            // If user close the file dialog with no file selected, the return value is 'null'
            if (value != null) {
                // Get the file path, read the file content
                var book_content = pywebview.api.get_content(value[0]); // The API return a promise object
                console.log(book_content);
                var read_zone = document.getElementsByClassName('read-zone');
                var loading = document.getElementsByClassName('loading');

                // Show 'loading' notification
                loading[0].style.display = "block";

                // If the promise object is fulfilled, it'll return the value to the function
                book_content.then(function(value) {
                    // Clear possible content in read-zone
                    read_zone[0].innerHTML = ''

                    // Append new content to read-zone
                    if (Array.isArray(value)) {
                        for (var i = 0; i < value.length; i++) {
                            read_zone[0].innerHTML += value[i];
                        }
                    } else {
                        read_zone[0].innerHTML += value;
                    }

                    // Hid 'loading' notification
                    loading[0].style.display = "none";
                });
            }
        });
        
    });

    // tools[2] is the Exit button
    tools[2].addEventListener('click', function() {
        pywebview.api.exit();
    });

    // // tools[3] is the About button
    // tools[3].addEventListener('click', function() {
    //     pywebview.api.about();
    // });
})
