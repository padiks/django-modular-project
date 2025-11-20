CREATE TABLE stock_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    category_id INTEGER,                  -- foreign key to categories
    uom_id INTEGER,                       -- foreign key to units of measure
    status INTEGER DEFAULT 1,             -- 1 = active, 0 = inactive
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES stock_items_categories(id),
    FOREIGN KEY (uom_id) REFERENCES stock_items_uom(id)
)