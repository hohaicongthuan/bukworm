window.addEventListener("pywebviewready", function()
{
    console.log("pywebview is ready!");

    // Return true if provided element is visible on the viewport
    function isVisible(el)
    {
        let rect = el.getBoundingClientRect();
        let viewportWidth = window.innerWidth || document.documentElement.clientWidth;
        let viewportHeight = window.innerHeight || document.documentElement.clientHeight;
        return (
            rect.top >= -2000 && rect.top <= viewportHeight + 2000
        );
    }

    let read_zone = document.getElementsByClassName("read-zone")[0];
    read_zone.addEventListener("scroll", function()
    {
        let pages = document.getElementsByClassName("page");
        for (let i = 0; i < pages.length; i++)
        {
            if (pages[i].getAttribute("data-booktype") == "pdf") {
                if (isVisible(pages[i]) && pages[i].innerHTML == "")
                {
                    let page_img = pywebview.api.load_page(pages[i].getAttribute("data-filepath"), pages[i].getAttribute("id"));
                    page_img.then(function(value)
                    {
                        pages[i].innerHTML = value;
                    });
                }
                // else
                // {
                //     pages[i].innerHTML = "";
                // }
            } 
        }
    });

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
