document.addEventListener('DOMContentLoaded', function() {
		const tableSelect = document.getElementById('tableSelect');
		if (tableSelect) {
				tableSelect.addEventListener('change', function() {
						const selectedTable = this.value;

						if (selectedTable === 'stock_items_categories') {
								window.location.href = '/categories/';
						} else if (selectedTable === 'stock_document_type') {
								window.location.href = '/doctype/';
						} else if (selectedTable === 'stock_items') {
								window.location.href = '/items/';
						} else if (selectedTable === 'stock_items_uom') {
								window.location.href = '/';
						}
				});
		}
});