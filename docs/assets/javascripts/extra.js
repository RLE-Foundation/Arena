/**
 * Load JSON data and initialize DataTable
 * @param {string} jsonFilePath - Path to the JSON file
 * @param {string} tableId - ID of the table element
 */
function loadDataTable(jsonFilePath, tableId = 'data-table') {
    fetch(jsonFilePath)
        .then(response => response.json())
        .then(data => {
            $(`#${tableId}`).DataTable({
                data: data,
                columns: [
                    { data: 'Team ID', className: 'dt-left'  },
                    { data: 'Training Steps', className: 'dt-left' },
                    { data: 'Parameters', className: 'dt-left' },
                    { data: 'Score', className: 'dt-left' },
                    { data: 'Code', className: 'dt-left' },
                    { data: 'Timestamp', className: 'dt-left' },
                ]
            });
        })
        .catch(error => console.error('Error loading JSON:', error));
}

// Example usage
// $(document).ready(function() {
//     const jsonFilePath = 'data.json'; // Path to your JSON file
//     loadDataTable(jsonFilePath, 'data-table'); // Call the function
// });

function generateCards(containerSelector, cardData) {
    const cardContainer = document.querySelector(containerSelector);

    if (!cardContainer) {
        console.error(`Container not found: ${containerSelector}`);
        return;
    }

    cardData.forEach(data => {
        const card = document.createElement('a');
        card.className = 'env_card';
        card.href = data.link; 
        card.target = "_self"; 

        card.innerHTML = `
            <img src="${data.img}" alt="">
            <div class="card-content">
                <h2>${data.title}</h2>
                <p>${data.os}</p>
                <p>${data.as}</p>
            </div>
        `;

        cardContainer.appendChild(card);
    });
}