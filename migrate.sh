#!/bin/bash

# Database credentials
DB_NAME="rasabot"
DB_USER="root"
DB_PASSWORD="" # Default MySQL password is empty
MIGRATIONS_DIR="./migrations"

# Log start
echo "Starting database migrations for $DB_NAME..."

# Loop through each SQL file in the migrations directory
for FILE in "$MIGRATIONS_DIR"/*.sql; do
    if [ -f "$FILE" ]; then
        echo "Migrating: $FILE"
        mysql -u "$DB_USER" -p"$DB_PASSWORD" "$DB_NAME" < "$FILE"
        if [ $? -eq 0 ]; then
            echo "Migration successful: $FILE"
        else
            echo "Migration failed: $FILE"
            exit 1
        fi
    else
        echo "No migration files found in $MIGRATIONS_DIR."
    fi
done

# Log completion
echo "All migrations completed successfully!"
