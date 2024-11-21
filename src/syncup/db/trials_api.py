"""
Fetches data from the clinical trials API and saves
to disk.
"""

from    dotenv import load_dotenv
import  json
import  logging
import  os
import  requests

def get_study_data(api_server):
    """
    Pulls data from clinical trials API
    """

    logger.info(f"Pulling data from {api_server = }")
    response = requests.get(api_server)
    logger.info(f"Response: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        logger.info(f"{response.text = }")
        return None

def main(outpath, api_server):
    """
    Runs everything
    """

    logger.info(f"Running {os.path.basename(__file__)}")
    data = get_study_data(api_server)
    with open(outpath, 'w') as outfile:
        json.dump(data, outfile)
    logger.info(f"Done")
    

if __name__=="__main__":

    load_dotenv()

    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s | %(message)s"
    )
    logger = logging.getLogger(os.path.basename(__file__))

    api_server = os.getenv("API_SERVER")
    data_outpath = os.path.join(os.getenv("DATA_DIR"), "clinicaltrials_api_response.json")

    main(data_outpath, api_server)
    