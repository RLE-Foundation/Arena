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
                    { data: 'Timestamp', className: 'dt-left' },
                    { data: 'Code', className: 'dt-left' }
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