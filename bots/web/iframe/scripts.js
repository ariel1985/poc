// This function will create and append the floating image, the box, and an iframe
function createRoZChat() {
    // chat button
    var img = document.createElement('img');
    img.src = 'https://steady-tarsier-ea3724.netlify.app/images/chaticon.png'; // Replace with your image URL
    img.style.position = 'fixed';
    img.style.bottom = '3vw'; // Padding from bottom, using viewport width
    img.style.right = '4rem'; // Padding from right, using viewport width
    img.style.width = '5rem'; // Width relative to the width of the viewport
    img.style.height = 'auto'; // Maintain aspect ratio
    img.style.zIndex = '1000'; // Ensure it stays on top of other elements

    // Create the box
    var box = document.createElement('div');
    box.style.position = 'fixed';
    box.style.bottom = 'calc(9rem)'; // Position above the image
    box.style.right = '4rem';
    box.style.backgroundColor = 'white'; // Set the background color
    box.style.color = 'black'; // Set the text color
    box.style.border = '1px solid black'; // Add a border
    box.style.borderRadius = '10px';
    box.style.zIndex = '999'; // Ensure it appears below the floating image if they overlap
    box.style.display = 'none'; // Start with the box hidden
    box.style.justifyContent = 'center'; // Center horizontally
    box.style.alignItems = 'center'; // Center vertically
    box.style.display = 'none';
    // box.textContent = 'Box Content'; // Add some text to the box

    // Create the 'X' button
    var closeButton = document.createElement('div');
    closeButton.textContent = 'X'; // Text for the close button
    closeButton.style.position = 'absolute';
    closeButton.style.top = '0';
    closeButton.style.left = '0';
    closeButton.style.padding = '10px';
    closeButton.style.cursor = 'pointer'; // Change the mouse pointer on hover
    closeButton.style.fontSize = '1vw'; // Relative font size
    closeButton.style.zIndex = '1001'; // Ensure it's above the box

    // Append the close button to the box
    box.appendChild(closeButton);

    // width: 95%;
    // height: calc(100% - 2.5rem);
    // border: none;
    // display: block;
    // bottom: 0;
    // position: absolute;

    // Create an iframe to embed Google
    var iframe = document.createElement('iframe');
    // iframe.src = 'https://main--steady-tarsier-ea3724.netlify.app/#/';
    iframe.src = 'localhost:9000/#/'
    iframe.style.width = '95%'; // Take the full width of the box
    iframe.style.height = 'calc(100% - 2.5rem)'; // Take the full height of the box minus the height of the close button
    iframe.style.border = 'none'; // Optional: remove the border of the iframe
    iframe.style.display = 'block'; // Ensure the iframe is displayed as a block element within the box
    iframe.style.bottom = '0';
    iframe.style.position = 'absolute';

    // Append the iframe to the box
    box.appendChild(iframe);

    // Function to update the box size based on the screen width
    function updateBoxSize() {
        if (window.innerWidth <= 768) { // 768px is a common breakpoint for mobile devices
            box.style.width = '100vw'; // Full width
            box.style.height = '100vh'; // Full height
            box.style.top = '0'; // Align to the top of the viewport
            box.style.right = '0'; // Align to the right of the viewport
            box.style.bottom = 'auto'; // Disable the bottom property
        } else {
            box.style.width = '20rem'; // Set a fixed width for desktop
            box.style.height = '50vh'; // Set a fixed height for desktop
            box.style.top = 'auto';
            box.style.bottom = '9rem';
            box.style.right = '4rem';
        }
    }

    // Initial box size update
    updateBoxSize();

    // Update box size on window resize
    window.addEventListener('resize', updateBoxSize);

    // Add click event listener to the image to toggle the box visibility
    img.addEventListener('click', function () {
        box.style.display = box.style.display === 'none' ? 'flex' : 'none';
    });

    // Add click event listener to the close button to hide the box
    closeButton.addEventListener('click', function () {
        box.style.display = 'none';
    });

    // Append the box and the image to the body
    document.body.appendChild(box);
    document.body.appendChild(img);
}

// Call the function to activate the components as soon as the page loads
window.onload = createRoZChat;
