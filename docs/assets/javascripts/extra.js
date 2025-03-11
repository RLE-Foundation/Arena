/**
 * Load JSON data and initialize DataTable
 * @param {string} jsonFilePath - Path to the JSON file
 * @param {string} tableId - ID of the table element
 */
function loadDataTable(jsonFilePath, version, environment, tableId = 'data-table') {
    fetch(jsonFilePath)
        .then(response => response.json())
        .then(data => {
            const versionData = data[version];
            if (!versionData) {
                console.error(`Version "${version}" not found in JSON file.`);
                return;
            }

            const environmentData = versionData[environment];
            if (!environmentData) {
                console.error(`Environment "${environment}" not found for version "${version}".`);
                return;
            }

            const table = $(`#${tableId}`).DataTable({
                data: environmentData,
                columns: [
                    { data: 'Team', className: 'dt-left'  },
                    { data: 'Name', className: 'dt-left'  },
                    { data: 'Version', className: 'dt-left'  },
                    { data: 'Training Steps', className: 'dt-left' },
                    { data: 'Parameters', className: 'dt-left' },
                    { data: 'Mean', className: 'dt-left' },
                    { 
                        data: 'Code', 
                        className: 'dt-left',
                        render: function(data) {
                            // 将 Code 转换为超链接
                            return `<a href="${data}" target="_blank">Link</a>`;
                        }
                    },
                    { data: 'Date', className: 'dt-left' },
                ],
                order: [[5, 'desc']],
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