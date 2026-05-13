# get.py
import os
import logging
import redivis

logger = logging.getLogger(__name__)

REDIVIS_API_TOKEN = os.environ["REDIVIS_API_TOKEN"]

if not REDIVIS_API_TOKEN:
    raise RuntimeError("Missing REDIVIS_API_TOKEN environment variable.")

def get():
    
    logger.info('Getting notebooks from Redivis...')
    username = "opierce"
    workflow_name = "gva_time_series:x57m"
    notebook_name = "updates:mefy"
    
    notebook = redivis.notebook(f"{username}.{workflow_name}.{notebook_name}")
    
    logger.info(f'Running {notebook_name} notebook...')
    notebook.run(wait_for_finish=True)  # Wait for the notebook to finish running
    logger.info(f'Running {notebook_name} notebook finished.')
    # Wordpress triggers here or in Redivis notebook itself.
