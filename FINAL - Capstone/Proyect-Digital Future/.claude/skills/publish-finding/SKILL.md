name: publish-finding
description: Publishes one completed finding to the Notion Findings Tracker database and creates a Notion page for it
When given a completed finding with: number, title, key statistic, 3-sentence interpretation, and priority (Alta/Media/Baja):
Use the Notion MCP to:
1. Create a new entry in the "Findings Tracker" database with fields: Titulo, Estadistica Clave, Alcance, Prioridad
2. Create a Notion page linked to that entry containing the details.
3. Confirm the Notion URL of the created page.