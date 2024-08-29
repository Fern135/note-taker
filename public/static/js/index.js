// const textarea = document.getElementById('content');

// // Function to auto-expand textarea width and height
// function autoExpand() {
//     // Save the current scroll position
//     const scrollTop = textarea.scrollTop;

//     // Reset height and width to auto to allow shrinking
//     textarea.style.height = 'auto';
//     // textarea.style.width = 'auto';

//     // Adjust the height and width dynamically based on the scroll size
//     textarea.style.height = textarea.scrollHeight + 'px'; // Expands based on height of content
//     // textarea.style.width = Math.min(textarea.scrollWidth, window.innerWidth - 20) + 'px'; // Expands based on width of content, limits to viewport width minus some padding

//     // Restore the scroll position
//     textarea.scrollTop = scrollTop;
// }

// // Event listener to call autoExpand on input event
// textarea.addEventListener('input', autoExpand);

// // Initial call to set size based on content when page loads
// autoExpand();