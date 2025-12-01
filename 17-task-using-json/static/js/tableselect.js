document.addEventListener('DOMContentLoaded', function() {
    const tableSelect = document.getElementById('tableSelect');

    if (tableSelect) {
        tableSelect.addEventListener('change', function() {
            const selectedTable = this.value;

            switch (selectedTable) {
                case 'stock_items_categories':
                    window.location.href = '/categories/';
                    break;
                case 'stock_document_type':
                    window.location.href = '/doctype/';
                    break;
                case 'stock_items':
                    window.location.href = '/items/';
                    break;
                case 'stock_items_uom':
                    window.location.href = '/uom/';
                    break;
                case 'stock_movements':
                    window.location.href = '/';
                    break;
            }
        });
    }
});

