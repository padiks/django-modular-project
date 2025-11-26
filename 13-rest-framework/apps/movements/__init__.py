'''
DROP TABLE IF EXISTS stock_movements;

CREATE TABLE "stock_movements" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "item_id" INTEGER NOT NULL,  -- Foreign Key to stock_items table
    "document_type_id" INTEGER NOT NULL,  -- Foreign Key to stock_document_type table
    "document_number" INTEGER NOT NULL,
    "document_reference" TEXT,
    "quantity" INTEGER NOT NULL,
    "status" INTEGER DEFAULT 1,
    "movement_date" DATETIME DEFAULT CURRENT_TIMESTAMP,
    "created_at" DATETIME DEFAULT CURRENT_TIMESTAMP,
    "updated_at" DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY("item_id") REFERENCES "stock_items"("id"),
    FOREIGN KEY("document_type_id") REFERENCES "stock_document_type"("id")
);

INSERT INTO stock_movements (
    item_id,
    document_type_id,
    document_number,
    document_reference,
    quantity,
    status,
    movement_date,
    created_at,
    updated_at
)
VALUES (
    1,  -- Assuming the item_id is 1 (you can change this based on your existing items)
    1,  -- Assuming the document_type_id is 1 (you can change this based on your document types)
    52341,  -- Example document number
    'DEMO',  -- Example reference
    1,  -- Quantity of 10 units
    1,  -- Status 1 (Active)
    '2025-11-22 18:00:00',  -- Example movement date (you can use the current timestamp or any date)
    '2025-11-22 18:00:00',  -- Created at
    '2025-11-22 18:00:00'  -- Updated at
);
'''
