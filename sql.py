from psycopg2.sql import SQL, Identifier


SQL(" ").join([SQL("SELECT * FROM"), Identifier("table")])
