// This function will create and append the floating image
function createRoZChat() {
    var img = document.createElement('img');
    img.src = 'chatgpt4chaticon-modified.png'; // Replace with your image URL
    img.style.position = 'fixed';
    img.style.bottom = '3vw'; // Padding from bottom, using viewport width
    img.style.right = '4vw'; // Padding from right, using viewport width
    img.style.width = '5vw'; // Width relative to the width of the viewport
    img.style.height = 'auto'; // Maintain aspect ratio
    img.style.zIndex = '1000'; // Ensure it stays on top of other elements
  
    // Add click event listener to the image
    img.addEventListener('click', function() {
      // Create the box
      var box = document.createElement('div');
      box.style.position = 'fixed';
      box.style.bottom = 'calc(3vw + 5vw)'; // Position above the image
      box.style.right = '4vw';
      box.style.backgroundColor = 'white'; // Set the background color
      box.style.color = 'black'; // Set the text color
      box.style.border = '1px solid black'; // Add a border
      box.style.zIndex = '999'; // Ensure it appears below the floating image if they overlap
      box.style.display = 'flex'; // To center the text inside the box
      box.style.justifyContent = 'center'; // Center horizontally
      box.style.alignItems = 'center'; // Center vertically
      box.textContent = 'Box Content'; // Add some text to the box
  
      // Check if the site is being accessed on mobile
      if (window.innerWidth <= 768) { // 768px is a common breakpoint for mobile devices
        box.style.width = '100vw'; // Full width
        box.style.height = '100vh'; // Full height
        box.style.top = '0'; // Align to the top of the viewport
        box.style.right = '0'; // Align to the right of the viewport
        box.style.bottom = 'auto'; // Disable the bottom property
      } else {
        // Desktop styles
        box.style.width = '50vw'; // Half of the viewport width
        box.style.height = '50vh'; // Half of the viewport height
      }
  
      // Append the box to the body
      document.body.appendChild(box);
    });
  
    document.body.appendChild(img);
  }
  
  // Call the function to activate the floating image as soon as the page loads
  window.onload = createRoZChat;
  