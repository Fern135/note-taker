
const fetchInterval = 5000;
const emoji = ['😀', '😃', '😄', '😁', '😆', '😂', '☺️'];

function getRandomChoice(arr) {
    if (arr.length === 0) {
        throw new Error('Array is empty');
    }
    return arr[Math.floor(Math.random() * arr.length)];
}

function openCity(evt, cityName) {
    // Declare all variables
    var i, tabcontent, tablinks;
  
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}

function getDateTime() { 
    const date = new Date();
    const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    
    return `${monthNames[date.getMonth()]} / ${date.getDate()} / ${date.getFullYear()} - ${date.getHours() % 12 || 12}:${String(date.getMinutes()).padStart(2, '0')} ${date.getHours() < 12 ? 'am' : 'pm'}`;
}

function submitForm() {
    let title = document.getElementById('title').value;
    let content = document.getElementById('content').value;
    const date = new Date();

    if (title.trim() == '') {
        title = getDateTime();
    }

    if (title.length > 200) {
        alert('Title less than 200 characters.');
        return;
    }

    if (content.length <= 0){
        alert('Content cannot be empty.');
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
        console.error('Error:', error);
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
                                <h4 id="note-title-render" class="text-dark">${note["note-title"]}</h4>
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
    .catch(error => console.error('😭 Error fetching data:', error));
}

document.getElementById("defaultOpen").click();

document.addEventListener('keydown', function(event) {
    if (event.shiftKey && event.key === 'Enter') {
        submitForm();
    }
});

document.addEventListener('DOMContentLoaded', () => {
    fetchAndRenderNotes(); // Initial fetch
    setInterval(fetchAndRenderNotes, fetchInterval);
});

