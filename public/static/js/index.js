
const fetchInterval = 5000;


function submitForm() {
    let title = document.getElementById('title').value;
    let content = document.getElementById('content').value;
    const date = new Date();

    if(title.trim() == '') {
        title = `${date.getDate()} / ${date.getDay()} / ${date.getFullYear()} - ${date.getHours()}:${date.getMinutes()}`;
    }

    if (title.length > 200) {
        alert('Title less than 200 characters.');
        return;
    }

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
        // console.log(response.json());
    })
    .then(result => {
        console.log('Success:', result);
    })
    .catch(error => {
        alert('Error:', error);
    });

    // title.value = "";
    // content.value = "";
}

function deleteById(id) {
    const url = `/notes/delete/${id}`; // URL defined in Step 1
    const fetchOptions = {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json'
      }
    };
  
    fetch(url, fetchOptions)
      .then(response => response.json())
      .then(data => {
        fetchAndRenderNotes();
        // console.log(data.result);
    })
    .catch(error => console.error(error));
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
                                <h3 id="note-title-render" class="text-dark">${note["note-title"]}</h3>
                            </div>
                            <div class="card-body">
                                <h5 id="note-content-render" class="text-dark">${note["note-content"]}</h5>
                            </div>
                            <div class="card-footer">
                                <h5 id="date-time-created" class="text-dark">${note["created-at"]}</h5>
                                <br>
                                <div class="btn-group">
                                    <button type="button" class="btn btn-danger" onclick="deleteById(${note["note-id"]});">
                                        Delete
                                    </button>
                                    <button type="button" class="btn btn-warning">
                                        Update
                                    </button>
                                    <button type="button" class="btn btn-success">
                                        Read
                                    </button>
                                </div>
                                <br>
                            </div>
                        </div>
                    </div>
                `;
                container.innerHTML += card;  // Append the card to the container
            });
        })
    .catch(error => console.error('Error fetching data:', error));
}


document.addEventListener('keydown', function(event) {
    if (event.shiftKey && event.key === 'Enter') {
        submitForm();
    }
});

document.addEventListener('DOMContentLoaded', () => {
    fetchAndRenderNotes(); // Initial fetch
    setInterval(fetchAndRenderNotes, fetchInterval);
});


// fetchAndRenderNotes();
// // setInterval(console.clear(), 10000); // clears console every 10 seconds. hopefully
// setInterval(fetchAndRenderNotes, fetchInterval);