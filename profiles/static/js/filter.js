let teamTableBody = null;
let teamTableBodyRows = null;
let filterInput = null;
let debug = true;

function dbgPrint(msg) {
    if (debug) {
        console.log('debug: ' + msg);
    }
}

function applyAllFilters() {
    // Reset
    $('#team-table-body tr').filter(function () {
        $(this).toggle(true);
    });

    // Apply Text Filter
    $('#team-table-body tr').filter(function () {
        //category from row
        row = $(this)[0];
        var not_already_hidden = !($(this).css('display') == 'none');
        var contains_filter = Array.from(row.cells).some((col) => {
            return col.textContent.toLowerCase().includes(
                filterInput.value.toLowerCase()
            );
        });
        $(this).toggle(contains_filter && not_already_hidden);
    }); 
}

// On change of Keyword Filter box
function handleInput(event) {
    applyAllFilters();
}

$(document).ready(function () {
    // On click of a tag
    $('button[name=profile_tag]').click(function () {
        current_button = $(this)[0];
        filterInput.value = current_button.textContent;
        applyAllFilters();
    })
});

window.onload = function () {
    dbgPrint('filter.js loaded!');

    teamTableBody = document.getElementById('team-table-body');
    dbgPrint('teamTableBody:' + teamTableBody);
    teamTableBodyRows = Array.from(teamTableBody.rows);
    dbgPrint('teamTableBodyRows:' + teamTableBodyRows);

    filterInput = document.getElementById('filter-input');
    dbgPrint('filterInput: ' + filterInput);
    filterInput.addEventListener("keyup", handleInput);

    applyAllFilters();
}
