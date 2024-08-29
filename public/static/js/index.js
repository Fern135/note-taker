
const fetchInterval = 1000;

function submitForm() {
    const title = document.getElementById('title').value;
    const content = document.getElementById('content').value;

    // Check if title has at least 200 characters
    if (title.length > 200) {
        alert('Title less than 200 characters.');
        return;
    }

    // Create the JSON object
    const data = {
        title: title,
        content: content
    };

    // Send the POST request
    fetch('/new/note/', { // Replace with your target URL
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return console.log(response.json());
    })
    .then(result => {
        alert('Success:', result);
    })
    .catch(error => {
        alert('Error:', error);
    });
}


function fetchAndRenderNotes() {
    fetch('/notes/all/')  // Replace with your actual endpoint URL
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('notes-container');
            container.innerHTML = '';  // Clear any existing content

            // Loop through each note and create a card
            data.forEach((note, index) => {
                // Create card structure
                const card = `
                    <div class="col-md-4 mb-3">
                        <div class="card text-center">
                            <div class="card-header">
                                <h3 id="note-title-render">${note["note-title"]}</h3>
                            </div>
                            <div class="card-body">
                                <h5 id="note-content-render">${note["note-content"]}</h5>
                            </div>
                            <div class="card-footer">
                                <h4 id="date-time-created">${note["created-at"]}</h4>
                            </div>
                        </div>
                    </div>
                `;
                container.innerHTML += card;  // Append the card to the container
            });
        })
    .catch(error => console.error('Error fetching data:', error));
}


document.addEventListener('DOMContentLoaded', () => {
    fetchAndRenderNotes(); // Initial fetch
    setInterval(fetchAndRenderNotes, fetchInterval);  // Refresh data every 5 seconds
});