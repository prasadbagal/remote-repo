$(document).ready(function() {
    var dt_table = $('.datatable').dataTable({
        language: dt_language,  // global variable defined in html
        order: [[ 0, "desc" ]],
        lengthMenu: [[25, 50, 100, 200], [25, 50, 100, 200]],
        columnDefs: [
            {orderable: true,
             searchable: true,
             className: "center",
             targets: [0, 1, 2, 3]
            },
            {
                data: 'first',
                targets: [0]
            },
            {
                data: 'last',
                targets: [1]
            },
            {
                data: 'mid',
                targets: [2]
            },
            {
                data: 'passw',
                targets: [3]
            },
        ],
        searching: true,
        processing: true,
        serverSide: true,
        stateSave: true,
        ajax: TESTMODEL_LIST_JSON_URL
    });
});