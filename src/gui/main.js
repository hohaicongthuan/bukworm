window.addEventListener("pywebviewready", function()
{
    console.log("pywebview is ready!");

    let tools = document.getElementsByClassName("tool-item");
    
    // tools[0] is the Open File button
    tools[0].addEventListener("click", function()
    {
        pywebview.api.open_file();
        // var open_file = pywebview.api.open_file();
        // var loading = document.getElementsByClassName("loading");
        // loading[0].style.display = "block"; // Show loading notification
        // open_file.then(function(value)
        // {
        //     if (value != 0) {
        //         alert("Cannot open file.");
        //     }
        //     loading[0].style.display = "none"; // Hide "loading" notification
        // });
    });

    // tools[2] is the Exit button
    tools[2].addEventListener("click", function()
    {
        pywebview.api.exit();
    });

    // // tools[3] is the About button
    // tools[3].addEventListener("click", function() {
    //     pywebview.api.about();
    // });
})
